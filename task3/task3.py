import sys
import json

tests = open(sys.argv[1]).read()
values = open(sys.argv[2]).read()

dataTests = json.loads(tests)
dataValues = json.loads(values)

newValues = {}
for i in dataValues['values']:
    newValues[i['id']] = i['value']

def setValue(i):
    if 'values' in i:
        if 'value' in i:
            i['value'] = newValues.get(i['id'])
        for j in i['values']:
            setValue(j)
    else:
        i['value'] = newValues.get(i['id'])

for i in dataTests['tests']:
    setValue(i)

res = []
def result(i):
    if 'values' in i:
        res.append(i)
        for j in i['values']:
            result(j)
    else:
        res.append(i)

for i in dataTests['tests']:
    result(i)

with open('report.json', 'w') as write_file:
    for i in dataTests['tests']:
        json.dump(i, write_file)