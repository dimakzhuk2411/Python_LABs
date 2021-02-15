num = float(input())
if num <0:
    print("Отрицательное значение!!!")
    exit()
else:
    num1 = int(num)
    num2 = (num - num1)*100
    num2 = int(num2)
print (num1, "рублей", num2, "копеек")