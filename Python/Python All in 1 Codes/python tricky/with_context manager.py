# f = open('text.txt','r')
# file_content = f.read()
# f.close()
# words = len(file_content)
# print(words)

# instead of doing all this using context manager we can simply it by using with statement
# by using context manager avoid to close every time to close files in files concept

with open('text.txt','r') as f:
    file_content = f.read()
words = len(file_content)
print(words)