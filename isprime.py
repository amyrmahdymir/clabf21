n = int(input('enter the number: '))
flg = True
for i in range(2, n):
    if(n % i == 0):
        print('Not Prime')
        flg = False
        break

print(flg)
