db = {
    '唐僧' : {
        'phone': '1001',
        'addr': '东土大唐',
    },
    '孙悟空': {
        'phone': '1002',
        'addr': '东胜花果山水帘洞',
    },
    '猪八戒': {
        'phone': '1003',
        'addr': '高老庄',
    },
    '沙悟净': {
        'phone': '1004',
        'addr': '流沙河',
    }
}

labels = {
    'addr': '地址',
    'phone': '电话',
}

name = input('请输入被查询者姓名：')
query = input('查询电话(p)还是地址(a)？')
key = query
if query == 'p' : key = 'phone'
if query == 'a' : key = 'addr'

person = db.get(name, {})
label = labels.get(key, key)
res = person.get(key, '不存在')
response = '{}的{}:{}'.format(name, label, res)
print(response)