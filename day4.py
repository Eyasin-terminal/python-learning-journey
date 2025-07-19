"""🧠 Scenario: You’re sending student data to a web server and getting it back
✅ Practice Task:
Create a dict (Python object).

Convert it to JSON (as a string).

Convert that JSON string back to a dict.

Access some values."""

import json
#dict
student = {
    "name": "Ayesha",
    "ID": 23456,
    "Course": ["math","English"],
    "grades": {
        "math": 90,
        "English": 80
    }
}

#convert dict to json
student_json= json.dumps(student)
print(student_json)
    