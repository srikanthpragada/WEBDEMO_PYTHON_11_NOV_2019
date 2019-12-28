import requests

resp = requests.get("http://localhost:8000/hr/rest/employees/")
if resp.status_code == 200:
    employees = resp.json()
    for emp in employees:
         print(emp['id'], emp['name'])
else:
    print("Sorry! Could not get details of employees!")
