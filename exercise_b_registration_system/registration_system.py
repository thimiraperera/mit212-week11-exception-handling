class InvalidMarkError(Exception):
    pass

students = {
    "S001": 78,
    "S002": 55,
    "S003": None,
    "S004": 91,
    "S005": 63,
    "S006": 82
}

def set_mark(student_id, mark):
    mark = int(mark)

    if mark < 0 or mark > 100:
        raise InvalidMarkError("Mark must be between 0 and 100")

    students[student_id] = mark

set_mark("S007", 75)
print(students)