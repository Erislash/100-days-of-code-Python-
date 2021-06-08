from turtle import Turtle, Screen
import prettytable

# ricki = Turtle()
#
# myScreen = Screen()
# ricki.shape("turtle")
#
# myScreen.exitonclick()

from prettytable import  PrettyTable

table = PrettyTable()
print(table)

table.add_column('Pokemon', ['Pikachu', 'Bulldoze', 'Charmander', 'Pycharmander'])
print(table)
table.add_column('Type', ['Lightning', 'Water', 'Pyro', 'Pyro++'])
print(table)

