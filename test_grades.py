import pytest

from grades import calculate_grade


@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        ([100, 90, 90, 90, 80], "O"),
        ([90, 90, 90, 90, 90], "O"),
        ([90, 90, 90, 90, 89], "A"),
        ([100, 100, 80, 80, 80], "A"),
        ([80, 80, 80, 80, 80], "A"),
        ([80, 80, 80, 80, 79], "B"),
        ([100, 70, 70, 70, 70], "B"),
        ([70, 70, 70, 70, 70], "B"),
        ([70, 70, 70, 70, 69], "C"),
        ([100, 60, 60, 60, 60], "C"),
        ([60, 60, 60, 60, 60], "C"),
        ([60, 60, 60, 60, 59], "F"),
        ([59, 59, 59, 59, 59], "F"),
        ([0, 0, 0, 0, 0], "F"),
        ([100, 100, 100, 100, 100], "O"),
    ],
)
def test_calculate_grade_for_each_grade(marks, expected):
    assert calculate_grade(marks) == expected


@pytest.mark.parametrize(
    ("marks", "exception"),
    [
        ("90,90,90,90,90", TypeError),
        ((90, 90, 90, 90, 90), TypeError),
        ([], ValueError),
        ([90, 90, 90, 90], ValueError),
        ([90, 90, 90, 90, 90, 90], ValueError),
        ([-1, 90, 90, 90, 90], ValueError),
        ([101, 90, 90, 90, 90], ValueError),
        ([90, 90, 90, 90, 90.5], TypeError),
        ([90, 90, 90, 90, "90"], TypeError),
        ([True, 90, 90, 90, 90], TypeError),
        ([False, 90, 90, 90, 90], TypeError),
    ],
)
def test_calculate_grade_rejects_invalid_inputs(marks, exception):
    with pytest.raises(exception):
        calculate_grade(marks)  
