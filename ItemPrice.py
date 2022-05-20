items= int(input('How many items you need? '))
if items <10:
    cost= 12*items
    print('Cost is', cost)
elif items>=10 and items<=100:
    cost= 10* items
    print('Cost is', cost)
else:
    cost= 7* items
    print('Cost is', cost)
    