import requests

id = input("Enter employee id :")
resp = requests.get(f"http://localhost:8000/hr/rest/employees/{id}")
if resp.status_code == 200:
    emp = resp.json()
    print(emp['name'], emp['desg'], emp['salary'])
else:
    print("Sorry! Employee not found!")
