def occurance(text):
    count = dict()
    words = text.split()

    for word in words:
        if word in count>3:
            count[word] += 1
        else:
            count[word] = 1

    return count

print( occurance('hello hai hello box key gate gate hello hai key.'))