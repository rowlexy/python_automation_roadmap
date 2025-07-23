# Unmarried frequent travelers between ages of 20 and 40
from helper import healthQuestMedicalsFilter
import csv

with open('Health Quest Medicals - EmployeeData.csv') as healthQuest:
    reader = csv.DictReader(healthQuest)
    medicals = list(reader)
    final_output = healthQuestMedicalsFilter(medicals, Age_gte=20, Age_lte=40, BusinessTravel='Travel_Frequently', MaritalStatus='Single')
    print(final_output)
    
# Transfer the result into an excel file

with open('Filtered_Health_Quest_Employees.csv', 'w', newline='') as healthQuestOutput:
    writer = csv.DictWriter(healthQuestOutput, fieldnames=final_output[0].keys())
    writer.writeheader()
    writer.writerows(final_output)