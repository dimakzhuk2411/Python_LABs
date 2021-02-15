Vstr = str(input('Введите текст\n')).lower()
buf = []
for i in Vstr:
    if Vstr.count(i) == 1:
        buf.append(i)
print(' '.join(buf))
