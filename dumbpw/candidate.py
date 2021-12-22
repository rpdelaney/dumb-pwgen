import string
from typing import Iterator


class Candidate:
    def __init__(self, password: str) -> None:
        self._password = password

    def _count_string_type(self, haystack: str) -> int:
        """Return a count of how many characters in the password are part of
        the haystack."""
        return sum(1 for char in self._password if char in haystack)

    @property
    def digits(self) -> int:
        return self._count_string_type(string.digits)

    @property
    def specials(self) -> int:
        return self._count_string_type(string.punctuation)

    @property
    def uppers(self) -> int:
        return self._count_string_type(string.ascii_uppercase)

    @property
    def lowers(self) -> int:
        return self._count_string_type(string.ascii_lowercase)

    @property
    def has_duplicates(self) -> bool:
        return (
            any(self._password.count(c) != 1 for c in self._password)
            if len(self._password)
            else False
        )

    @property
    def has_repeating(self) -> bool:
        for index in range(1, len(self._password)):
            if self._password[index] == self._password[index - 1]:
                return True
        else:
            return False

    def __len__(self) -> int:
        return len(self._password)

    def __str__(self) -> str:
        return self._password

    def __iter__(self) -> Iterator[str]:
        return iter(self._password)

    def __getitem__(self, item: int) -> str:
        return self._password[item]
