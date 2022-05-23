scores = [int(i) for i in input("Input score : ").split()]

n=len(scores)

print(scores)
print('maximum score is : ',max(scores))
print('minimum score is : ',min(scores))

for i in scores:
    if i>100:
        print('USer put a score greater than 100 is :',i)
    print(i)
        