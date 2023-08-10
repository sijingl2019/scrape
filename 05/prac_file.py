import json
import csv

str = '''
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}, {
    "name": " 王伟 ",
    "gender": " 男 ",
    "birthday": "1992-10-18"
}]
'''
print(type(str))
data = json.loads(str)
print(data)
print(type(data))

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))

# with open('data.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['id', 'name', 'age'])
#     writer.writerow(['10001', 'Mike', 20])
#     writer.writerow(['10002', 'Bob', 22])
#     writer.writerow(['10003', 'Jordan', 21])

with open('data.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'id': '10001', 'name': 'Mike', 'age': 20})
    writer.writerow({'id': '10002', 'name': 'Bob', 'age': 22})
    writer.writerow({'id': '10003', 'name': 'Jordan', 'age': 21})

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
