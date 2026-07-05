class InvalidMarkError(Exception):
    pass

class DuplicateStudentError(Exception):
    pass

students = {
    "S001": 78,
    "S002": 55,
    "S003": None,
    "S004": 91,
    "S005": 63,
    "S006": 82
}

def set_mark(student_id, mark, overwrite=False):
    mark = int(mark)

    if mark < 0 or mark > 100:
        raise InvalidMarkError("Mark must be between 0 and 100")

    if student_id in students and overwrite == False:
        raise DuplicateStudentError("Student ID already exists")

    students[student_id] = mark

set_mark("S001", 80, overwrite=True)

print(students)