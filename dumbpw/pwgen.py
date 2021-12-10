import secrets

import deal

from .charspace import Charspace


@deal.has("random")
@deal.pure
@deal.raises()
@deal.pre(
    validator=lambda charspace, pass_length: pass_length > 0,
    message="pass_length must be greater than zero.",
    exception=ValueError,
)
@deal.pre(
    validator=lambda charspace, pass_length: pass_length <= 512,
    message="pass_length cannot be greater than 512.",
    exception=ValueError,
)
@deal.pre(
    validator=lambda charspace, pass_length: len(charspace.charset) > 0,
    message="charset must have positive len.",
    exception=ValueError,
)
@deal.ensure(
    lambda charspace, pass_length, result: len(result) == pass_length,
    message="function return value len must equal requested pass_length.",
)
@deal.ensure(
    lambda charspace, pass_length, result: all(
        char in "".join(charspace.charset) for char in result
    ),
    message="function return value must be "
    "composed of characters in the charspace",
)
def generate(charspace: Charspace, pass_length: int) -> str:
    """Return a cryptographically secure password of length pass_length using
    characters only from the given charspace. Max pass_length is 512."""
    return "".join(
        secrets.choice(charspace.charset) for i in range(pass_length)
    )
