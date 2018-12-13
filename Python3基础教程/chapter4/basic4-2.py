d = dict(name='wangbo', age=30)
print(d)
print(len(d))
print(d['age'])
del d['age']
print(d)
print('name' in d)
x = [None] * 43
x[42] = 'Foo'
print(x)
x = {}
x[42] = 'Foo'
print(x)
phonebook = {'Beth': '9102', 'Alice': '2341', 'Cecil': 3258}
print("Cecil's number is {Cecil:#>10.3f}.".format_map(phonebook))
template = '''<html>
    <head><title>{title}</title></head>
    <body>
    <h1>{title}</h1>
    <p>{text}</p>
    </body>'''
data = {'title': 'My Home Page', 'text': 'welcome to my home page'}
print(template.format_map(data))

