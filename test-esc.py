# вариант 4


RED = '\u001b[41m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
BLACK='\u001b[30m'
BLUE = '\u001b[44m'


print("Задание 1. Флаг Польши:")
for i in range(6):
    if i<3:
        print(f"{WHITE}{' '*20}{END}")
    else:
        print(f"{RED}{' '*20}{END}")


print("Задание 2. Повторяющийся узор")
length=100
width=7
d=1
for i in range(width):
    if i%2==0:
        print("\n",f"{WHITE}{' '*length}{END}")
    else:
        if d==1:
            for j in range(length//12):
                print(f"{' '*10}{WHITE}{'  '}{END}",end='')
            d=2
        else:
            for q in range(length//12):
                print(f"{' '*5}{WHITE}{'  '}{END}{' '*5}",end='')
            d=1


print("Задание 3. График функции y=x**0.5")
x=9
y=9
if __name__ == "__main__":
    for i in range(y):
         if (y-i)**2  <= x:
             print(y-i, ' '*(((y-i)**2)*2-2),'*')
         else:
             print(y-i)
print('  ',*list(x for x in range(1,x+1)))


print("Задание 4. Диаграмма")
import math
f=[x[:-1] for x in open('sequence.txt').readlines()]
sr1=sr2=c=0
for i in f:
    x=float(i)
    c+=1
    if c<=125:
        sr1+=abs(x)
    else:
        sr2+=abs(x)
sr1,sr2=sr1/125,sr2/125
per1=math.ceil(sr1/(sr1+sr2)*100)
per2=100-per1
print("Первые 125 чисел")
print(per1,f'{RED}{' '*per1}{END}')
print("Последние 125 чисел")
print(per2,f'{BLUE}{' '*per2}{END}')

