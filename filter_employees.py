import send2trash, csv
from helper import employee_filter

with open('Employee.csv') as employee_file:
    reader = csv.DictReader(employee_file)
    employees = list(reader)
    # print(employees)
    final_data = employee_filter(employees, BusinessTravel = "Travel_Frequently", MaritalStatus = "Single", OverTime = "No", JobSatisfaction = "4")
    # print(final_data)
with open('employee_data.csv', 'w', newline='') as employee_data:
    writer = csv.DictWriter(employee_data, fieldnames=final_data[0].keys())
    writer.writeheader()
    writer.writerows(final_data)