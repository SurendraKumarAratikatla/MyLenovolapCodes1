f = open('text.txt', 'r')
file_content = f.read()
print(file_content)
f.close()

words = file_content.split(',')
word_length = len(words)
print(word_length)


# by using context manager (using with statement here) we can avoid to close file every time, this context manager will take care to close the file

with open('text.txt','r') as f:
    file_content1 = f.read()

print(file_content1)