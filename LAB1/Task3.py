print('Please, type number of your card')
num = str(input())
if len(num) !=16:
    print('Недопустимое количество символов')
    exit()
else:
    hidden = num[:4]+' '+'****'+' '+'****'+' '+num[-4:]
    print(hidden)
