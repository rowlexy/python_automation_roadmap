def employee_filter(employees, **filter):
    employee_data = []
    for records in employees:
        match = True
        for key, value in filter.items():
            if records.get(key) != value:
                match = False
                break
        if match:
            employee_data.append(records)
    return employee_data
                
def filterEmployeeTest(employee_test, **test_result):
    employee_results = []
    for data in employee_test:
        match = True
        for key, value in test_result.items():
            if key.endswith('_lte'):
                field = key.replace('_lte', '')
                if float(data.get(field, 0)) > float(value):
                    # .get(field, 0) tries to fetch the value for "Age" from the record. 
                    # If it doesn’t exist, it defaults to 0
                    match = False
                    break
            elif key.endswith('_gte'):
                field = key.replace('_gte', '')
                if float(data.get(field, 0)) < float(value):
                    match = False
                    break
            elif key.endswith('_lt'):
                field = key.replace('_lt', '')
                if float(data.get(field, 0)) >= float(value):
                    match = False
                    break
            elif key.endswith('_gt'):
                field = key.replace('_gt', '')
                if float(data.get(field, 0)) <= float(value):
                    match = False
                    break
            else:
                if data.get(key) != value:
                    match = False
                    break
        if match:
            employee_results.append(data)
    return employee_results

def healthQuestMedicalsFilter(medicals, **kwargs):
    returned_results = []
    for data in medicals:
        match = True
        for key, value in kwargs.items():
            # for keys with values less than or equal to
            if key.endswith('_lte'):
                field = key.replace('_lte', '')
                if float(data.get(field, 0)) > float(value):
                    # Avoids errors and falls back to zero if the field is missing
                    match = False
                    break
            elif '_gte' in key:
                field = key.replace('_gte', '')
                if float(data.get(field, 0)) < float(value):
                    match = False
                    break
            elif '_lt' in key:
                field = key.replace('_lt', '')
                if float(data.get(field, 0)) >= float(value):
                    match = False
                    break
            elif '_gt' in key:
                field = key.replace('_gt', '')
                if float(data.get(field, 0)) <= float(value):
                    match = False
                    break
            else:
                if data.get(key) != value:
                    match = False
                    break
        if match:
            returned_results.append(data)
    return returned_results 
                