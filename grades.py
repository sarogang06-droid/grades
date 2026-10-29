# Write calculate_grade(marks: list[int]) -> str for 5
# subject marks (0-100). Raise ValueError for wrong
# count or out-of-range marks, TypeError for non-
# integers. Grade by average: O >= 90, A >= 80,
# B >= 70, C >= 60, else F.
def calculate_grade(marks: list[int]) -> str:
    if not isinstance(marks, list):
        raise TypeError("Input must be a list")

    if len(marks) != 5:
        raise ValueError("Input must contain exactly 5 marks")

    for mark in marks:
        if not isinstance(mark, int) or isinstance(mark, bool):
            raise TypeError("All marks must be integers")
        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100")

    total: int = sum(marks)

    if total >= 90 * len(marks):
        return "O"
    elif total >= 80 * len(marks):
        return "A"
    elif total >= 70 * len(marks):
        return "B"
    elif total >= 60 * len(marks):
        return "C"
    else:
        return "F"

if __name__ == "__main__":
    sample_marks: list[list[int]] = [
        [90, 90, 90, 90, 90],
        [80, 80, 80, 80, 80],
        [70, 70, 70, 70, 70],
        [60, 60, 60, 60, 60],
        [59, 59, 59, 59, 59],
    ]

    for marks in sample_marks:
        print(f"{marks} -> {calculate_grade(marks)}")










#  

















