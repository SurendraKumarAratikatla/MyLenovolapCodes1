names = ['chiru','nag','venky','mahesh','allu']
movies = ['tagoor','king','seenu','okkadu','arya']

for index, name in enumerate(names):
    movie = movies[index]
    print(f'{name} movie is: {movie}')

# by using zip list method we can simplify it

for name, movie in zip(names, movies):
    print(f'{name} movie is: {movie}')

# by using zip we can zip 'n' number of list or dictionaries or tuples or sets
