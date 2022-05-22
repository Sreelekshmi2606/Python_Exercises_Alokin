def ana(string_1,string_2):
    if sorted(string_1)==sorted(string_2):
        print('They are anagrams')
    else:
        print('They are not anagrams')
string_1='below'
string_2='elbow'
ana(string_1,string_2)