from build_system import build_system


def test_build_system():
    package_deps = [
        ("A", []),
        ("B", []),
        ("C", ["A", "B"]),
        ("D", ["B"]),
        ("E", ["C"]),
        ("F", ["E", "D"]),
        ("G", ["F"]),
        ("H", ["E"])
    ]
    res = build_system(package_deps)
    assert res in [
        ["A", "B", "C", "D", "E", "F", "G", "H"],
        ["A", "B", "D", "C", "E", "F", "G", "H"],
        ["B", "A", "C", "D", "E", "F", "G", "H"],
        ['A', 'B', 'C', 'E', 'D', 'F', 'G', 'H'],
        ['B', 'D', 'A', 'C', 'E', 'F', 'G', 'H'],
    ]
