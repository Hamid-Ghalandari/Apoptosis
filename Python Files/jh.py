dict1 = {
    "student1": {"name": "javad",
                 "age": 23},
    "student2": {"name": "maryam",
                 "age": 33
                 },
    "student3": {"name": "amir",
                 "age": 44,
                 }
}
if dict1["student1"]["age"] > dict1["student2"]["age"]:
    if dict1["student1"]["age"] > dict1["student3"]["age"]:
        print(dict1["student1"]["name"])
if dict1["student2"]["age"] > dict1["student1"]["age"]:
    if dict1["student2"]["age"] > dict1["student3"]["age"]:
        print(dict1["student2"]["name"])
if dict1["student3"]["age"] > dict1["student1"]["age"]:
    if dict1["student3"]["age"] > dict1["student2"]["age"]:
        print(dict1["student3"]["name"])
