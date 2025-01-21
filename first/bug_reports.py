
list_bug_report = []
list_bug_report.append("critical_bug_report")
list_bug_report.append("block_bug_report")
list_bug_report.append("major_bug_report")
list_bug_report.append("mid_bug_report")
list_bug_report.append("minor_bug_report")
list_bug_report.remove("critical_bug_report")
del list_bug_report[0]
list_bug_report.sort()
print(list(sorted(list_bug_report)))