def Generate():
    print('Welcome to the Band Name Generator!');
    print('==========');
    cityName = input('What\'s the name of the city you grow up in?\n');
    petName = input('What\'s your pet\'s name?\n');
    print(f'\nYour band name could be: {cityName.capitalize()} {petName.capitalize()}')

Generate()