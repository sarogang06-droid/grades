# Write calculate_grade(marks: list[int]) -> str for 5
# subject marks (0-100). Raise ValueError for wrong
# count or out-of-range marks, TypeError for non-
# integers. Grade by average: O >= 90, A >= 80,
# B >= 70, C >= 60, else F. 

def calculate_grade(marks: list[int]) -> str:
    if not isinstance(marks, list):
        raise TypeError("Input must be a list")

    if len(marks) != 5:
        raise ValueError("Exactly 5 marks are required")

    for mark in marks:
        if not isinstance(mark, int):
            raise TypeError("All marks must be integers")
        if not 0 <= mark <= 100:
            raise ValueError("Marks must be between 0 and 100")

    average = sum(marks) / 5

    if average >= 90:
        return "O"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "F"



















