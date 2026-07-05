students = {
    "S001": 78, "S002": 55, "S003": None,
    "S004": 91, "S005": "63", "S006": 82
}
def class_report(data):
    marks = []

    for mark in data.values():
        if mark is not None:
            mark = int(mark)
            marks.append(mark)

    # marks = list(data.values())

    total = sum(marks)
    average = total / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print("Average:", average)
    print("Highest:", highest)
    print("Lowest:", lowest)

    # print(len(marks))

class_report(students)