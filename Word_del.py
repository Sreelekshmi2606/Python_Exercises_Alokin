name= input('Enter your name: ')
dele= input('Which word you want to delete? ')
new_name=''
for i in name:
    if i==dele:
        pass
    else:
        new_name=new_name+i
print('Your new name is ',new_name)

