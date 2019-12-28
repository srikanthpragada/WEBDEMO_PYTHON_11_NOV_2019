import requests

id = input("Enter employee id :")
resp = requests.delete(f"http://localhost:8000/hr/rest/employees/{id}")
if resp.status_code == 204:
    print("Employee was deleted successfully!")
else:
    print("Sorry! Employee not found!")
