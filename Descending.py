# input list from user

marks= [int(i) for i in input('Enter marks:').split()]
print(marks)
new=[]
while marks:
    maximum=marks[0]


    for i in marks:

        #temp=marks[0]
        if i>maximum:
            maximum=i

    new.append(maximum)
    marks.remove(maximum)
print('Descending order is :' new)