f = open("./input/day2.txt", "r")

reports = []

for line in f:
    splitted_input = line.strip().split(" ")
    reports.append(list(map(int, splitted_input)))

def is_safe(report):
    # Check if the report is either all increasing or all decreasing
    increasing = all(report[i] < report[i + 1] for i in range(len(report) - 1))
    decreasing = all(report[i] > report[i + 1] for i in range(len(report) - 1))
    
    # Check if adjacent levels differ by at least 1 and at most 3
    adjacent_diff_valid = all(1 <= abs(report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))
    
    return (increasing or decreasing) and adjacent_diff_valid

def can_be_safe_by_removing_one(report):
    for i in range(len(report)):
        # Create a new report without the i-th level
        new_report = report[:i] + report[i + 1:]
        if is_safe(new_report):
            return True
    return False

def count_safe_reports(reports):
    safe_count = 0
    for report in reports:
        if is_safe(report) or can_be_safe_by_removing_one(report):
            safe_count += 1
    return safe_count

print(count_safe_reports(reports))