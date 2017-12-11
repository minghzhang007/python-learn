import json

data = {
    'no': 1,
    'name': 'Runoob',
    'url': 'http://www.runoob.com'
}

json_str = json.dumps(data)
print("Python的原始数据：", repr(data))
print("Json对象：", json_str)

data2 = json.loads(json_str)
print("data2['name']", data2['name'])
print("data2['url']", data2['url'])

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('data.json', 'r') as f:
    data_file = json.load(f)
    print("从文件中加载：", data_file)
