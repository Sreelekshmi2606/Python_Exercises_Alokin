list1=['name','age','place']
list2=['Sreelu',27,'Alappuzha']
res = {list1[i]: list2[i] for i in range(len(list1))}
print('New mapped  dict is ',res)