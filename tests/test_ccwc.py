import pytest
from ccwc.utils import process
from . import get_fixture_path
from argparse import Namespace


@pytest.mark.parametrize(
    "filename, expected",
    [
        ("empty.txt", [0, 0, 0]),
        ("single-char.txt", [1, 1, 1]),
        ("multilines.txt", [3, 16, 128]),
        ("big-content.txt", [7188, 58163, 335191]),
    ],
)
def test_process_files(filename, expected):
    full_path = get_fixture_path(filename)

    with open(full_path) as stream:
        assert process(stream, Namespace(count=1, lines=1, words=1)) == expected
