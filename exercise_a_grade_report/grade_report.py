students = {
    "S001": 78, "S002": 55, "S003": None,
    "S004": 91, "S005": "63", "S006": 82
}

def class_report(data):
    marks = []
    skipped_count = 0

    for student_id, mark in data.items():
        if mark is None:
            skipped_count += 1
            print(student_id, "skipped: missing mark")
            continue

        try:
            mark = int(mark)
            marks.append(mark)

        except ValueError:
            skipped_count += 1
            print(student_id, "skipped: mark is not a valid number")

    # marks = list(data.values())

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Skipped records:", skipped_count)

    # print(len(marks))

class_report(students)