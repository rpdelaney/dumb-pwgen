import sys

import click

from .pwgen import search


@click.command(
    no_args_is_help=True,
)
@click.version_option()
@click.option(
    "--min_length",
    type=click.IntRange(min=1, max=512),
    help="The length of the password.",
)
@click.option(
    "--min_uppercase",
    type=int,
    default=0,
    help="The minimum number of uppercase characters.",
)
@click.option(
    "--min_lowercase",
    type=int,
    default=0,
    help="The minimum number of lowercase characters.",
)
@click.option(
    "--min_digits",
    type=int,
    default=0,
    help="The minimum number of digit characters.",
)
@click.option(
    "--min_specials",
    type=int,
    default=0,
    help="The minimum number of special characters.",
)
@click.option(
    "--blocklist",
    type=str,
    default="""'";""",
    show_default=True,
    help="Characters that may not be in the password.",
)
@click.option(
    "--allow-repeating/--reject-repeating",
    help="Allow or reject repeating characters in the password.",
    default=False,
    show_default=True,
)
def cli(
    min_length: int,
    min_uppercase: int,
    min_lowercase: int,
    min_digits: int,
    min_specials: int,
    blocklist: str,
    allow_repeating: bool,
) -> int:
    try_password = search(
        min_length,
        min_uppercase,
        min_lowercase,
        min_digits,
        min_specials,
        blocklist,
        allow_repeating,
    )

    try:
        print(try_password)
    except ValueError as ve:
        print(ve)
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(cli())
