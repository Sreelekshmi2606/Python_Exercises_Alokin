marks = [int(i) for i in input("Input some comma seprated numbers : ").split()]

n=len(marks)
temp=0
print(marks)
print('maximum mark is : ',max(marks))
print('minimum mark is : ',min(marks))
for i in marks:
    if i>100:
        print('Mark exceeded 100')
    else:
        print('Correct insertion')
        