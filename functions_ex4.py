def word (string):
    if (len(string) < 8):
        return "False"
    else:
        return "True"

print(word("giraffe"))
print(word("fantastic"))
print(word("bitmaker"))
print(word("lion"))