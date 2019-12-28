import requests

name = input("Enter name :")
desg = input("Enter desg : ")
salary = input("Enter salary : ")

data = {'name': name, 'desg':desg, 'salary': salary}

resp = requests.post("http://localhost:8000/hr/rest/employees/", data)
if resp.status_code == 200:
    print("Employee added successfully!")
else:
    print("Sorry! Could not add Employee!")
