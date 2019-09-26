import pytest

from lies_on_path import lies_on_path


@pytest.mark.parametrize(
    "soruce, dest, graph, expected",
    [
        (
            "1",
            "5",
            [
                ("1", "2", 1),
                ("2", "3", 1),
                ("3", "4", 1),
                ("4", "5", 1),
                ("5", "1", 3),
                ("1", "3", 2),
                ("5", "3", 1),
            ],
            [True, True, False, False, True, True, True]
        ),
        (
            "1",
            "5",
            [
                ("1", "2", 1),
                ("2", "3", 1),
                ("3", "5", 1),
                ("1", "4", 1),
                ("4", "5", 2),
                ("3", "4", 2),
                ("2", "4", 4),
            ],
            [True, True, True, True, True, False, False]
        ),
        (
            "1",
            "4",
            [
                ("1", "2", 1),
                ("1", "3", 1),
                ("1", "4", 1),
                ("2", "3", 1),
                ("2", "4", 1),
            ],
            [False, False, True, False, False]
        )
    ]
)
def test_lies_on_path(soruce, dest, graph, expected):
    res = lies_on_path(soruce, dest, graph)
    assert res == expected
