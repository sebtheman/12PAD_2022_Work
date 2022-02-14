a = 1
b = 2
print(a,b)

a, b = 1, 2
print(a, b)

x = 10
y = 5
x, y = y, x
print(x)
print(y)

a = 10
print(id(10))
print(id(a))

print(type(10))
print(type(10.5))
print(type(True))
print(type(False))
print("Hello World", "has a type", type("Hello World"))
print('Hello World', 'has a type', type('Hello World'))
print('word', 'has a type', type('word'))
print('a', 'has a type', type('a'))
print('@', 'has a type', type('@'))
print(23, 'has a type', type(23))
print('23', 'has a type', type('23'))
a = "23"
print(a, 'has a type', type(a))
b = 23
print(b, 'has a type', type(b))

n = int(input("Enter a number: "))
for i in range(1, n+1):
    print(i, end='\nLets learn Python\n')

name = " you me "
print(name.strip())
print(name.lstrip())
print(name.rstrip())
print(len(name))
print(name)
name = name.lstrip()
print(len(name))
print(name)
name = name.rstrip()
print(len(name))
print(name)
name = name.title()
print(len(name))
print(name)