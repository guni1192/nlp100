sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

words = sentence.split(" ")
index = [1, 5, 6, 7, 8, 9, 15, 16, 19]

for i, word in enumerate(words):
    if i in index:
        print(word[:1:])
    else:
        print(word[:2:])
