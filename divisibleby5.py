#ask the user to input a list

n = input('Enter nos: ').split()

x= [int(i) for i in n]
print(x,end='')

for i in x:
    if i%5==0:
        print('nos which are divisoble by 5 are',i)
    