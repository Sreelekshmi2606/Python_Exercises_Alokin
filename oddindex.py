#Take input from user
n = [int(i) for i in input('Enter the elements: ').split()]
print(n)
for i in range(len(n)+1):
    if i%2!=0:
        print('Elems at odd positions are',n[i])
         