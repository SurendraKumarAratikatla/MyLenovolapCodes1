def keywordarg(**kwargs):
    for key, value in kwargs.items():
        print(key +":"+ value)

keywordarg(arg1 = 'argument1',arg2 = 'argument2', arg3= 'argument3')
