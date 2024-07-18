first = input ('Введите число :')
second = input ('Введите число :')
third = input ('Введите число :')
if first == second   and first == third :
    print(3)
elif first == second and first != third and second != third :
    print(2)
elif first != second and first != third and second == third :
    print(2)
elif first != second and first == third and second != third :
    print(2)
elif first != second and first != third and second != third :
    print(0)
