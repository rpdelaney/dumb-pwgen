import sys

import click
import deal

deal.activate()

from .constants import MAX_PASSWORD_LENGTH
from .exceptions import DumbValueError
from .pwgen import search


@click.command(
    no_args_is_help=True,
)
@click.version_option()
@click.option(
    "--min-uppercase",
    type=int,
    default=0,
    help="The minimum number of uppercase characters.",
)
@click.option(
    "--min-lowercase",
    type=int,
    default=0,
    help="The minimum number of lowercase characters.",
)
@click.option(
    "--min-digits",
    type=int,
    default=0,
    help="The minimum number of digit characters.",
)
@click.option(
    "--min-specials",
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
@click.argument(
    "length",
    type=click.IntRange(min=1, max=MAX_PASSWORD_LENGTH),
)
def cli(
    length: int,
    min_uppercase: int,
    min_lowercase: int,
    min_digits: int,
    min_specials: int,
    blocklist: str,
    allow_repeating: bool,
) -> int:
    try:
        try_password = search(
            length=length,
            min_uppercase=min_uppercase,
            min_lowercase=min_lowercase,
            min_digits=min_digits,
            min_specials=min_specials,
            blocklist=blocklist,
            allow_repeating=allow_repeating,
        )
    except DumbValueError as ve:
        print(ve)
        return 1

    print(try_password)

    return 0


if __name__ == "__main__":
    sys.exit(cli())
