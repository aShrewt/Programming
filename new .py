import time

start = time.time()

string = 'abc xyz'
string = string.upper()

a = []

for x in string:
    if 65 <=ord(x) <=90:
        x = ord(x) + 2
        if x > 90:
            x -= 26
        x = chr(x)
    a.append(x)

print(''.join(a))

end = time.time()

print(end - start)