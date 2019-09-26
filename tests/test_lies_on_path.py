import pytest

from lies_on_path import lies_on_path


@pytest.mark.parametrize(
    "paths, expected",
    [
        ([7,1,5,3,6,4], 5),
        ([10, 7, 5, 8, 11, 9], 6),
        ([7,6,4,3,1], 0),
        ([1, 0], 0),
        ([1], 0),
        ([], 0),
    ]
)
def test_lies_on_path(paths, expected):
    res = lies_on_path(paths)
    assert res == expected
