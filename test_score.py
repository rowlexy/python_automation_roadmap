from helper import filterEmployeeTest
import csv

with open('Employee_test.csv') as employee_test:
    reader = csv.DictReader(employee_test)
    employee_test = list(reader)
    training_score = filterEmployeeTest(employee_test, avg_training_score_gt=79)
    # print(employee_test)

with open('test_results.csv', 'w', newline='') as test_score:
    writer = csv.DictWriter(test_score, fieldnames=training_score[0].keys())
    writer.writeheader()
    writer.writerows(training_score)