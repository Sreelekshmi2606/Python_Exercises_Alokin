from audioop import avg


marks = input("Input some comma seprated numbers : ")
list1 = marks.split(",")
list1=list(list1)
n=len(list1)
temp=0
print(list1)
print('maximum mark is : ',max(list1))
print('minimum mark is : ',min(list1))
for i in marks:
    if i>100:
        print('Mark exceeded 100')