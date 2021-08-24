text = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
size = 4

l_s = len(text)/size
l = []

for i in range(0, len(text), size):
    print(size+i)
    # l.append(text[i:i+size])

print(l)
