names = ["bread","milk","jom"]
persons = ["John","Charlie","Tom"]

for person, name in zip(persons,names):
    #print(person +" likes "+ name)
    print(f'{person} likes {name}')