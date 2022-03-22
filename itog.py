ch = int(input(f'На какой процент вы кладёте деньги?'))
summa = int(input(f'Какая сумма?'))
time = int(input(f'На сколько лет вы хотите положить деньги?'))
itog = []

for i in range(time):
             summa = summa / 100 * ch + summa
             itog.append(summa)
    
print(summa)
            
            
