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

        except (ValueError, TypeError):
            skipped_count += 1
            print(student_id, "skipped: mark is not a valid number")
            continue

        if mark < 0 or mark > 100:
            raise ValueError(student_id + " has an invalid mark. Between 0 - 100.")
        
        marks.append(mark)


    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)
    print("Skipped records:", skipped_count)

class_report(students)