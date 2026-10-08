import pytest

from grades import calculate_grade


@pytest.mark.parametrize(
    ("marks", "expected"),
    [
        ([90, 90, 90, 90, 90], "O"),
        ([80, 80, 80, 80, 80], "A"),
        ([70, 70, 70, 70, 70], "B"),
        ([60, 60, 60, 60, 60], "C"),
        ([59, 59, 59, 59, 59], "F"),
    ],
)
def test_calculate_grade_for_each_grade(marks, expected):
    assert calculate_grade(marks) == expected


@pytest.mark.parametrize(
    ("marks", "exception"),
    [
        ((90, 90, 90, 90, 90), TypeError),
        ([90, 90, 90, 90], ValueError),
        ([90, 90, 90, 90, 90, 90], ValueError),
        ([-1, 90, 90, 90, 90], ValueError),
        ([101, 90, 90, 90, 90], ValueError),
        ([90, 90, 90, 90, 90.5], TypeError),
        ([90, 90, 90, 90, "90"], TypeError),
    ],
)
def test_calculate_grade_rejects_invalid_inputs(marks, exception):
    with pytest.raises(exception):
        calculate_grade(marks)
