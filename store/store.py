""" Store module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * title (string): Title of the game
    * manufacturer (string)
    * price (number): Price in dollars
    * in_stock (number)
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common
import os
from pathlib import Path

file_name = 'games.csv'

def start_module():

    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """
    print('Store manager')

    print(' (1) Show table')
    print(' (2) Add new record')
    print(' (3) Remove record')
    print(' (4) Update record')
    print(' (5) Show how many kinds of records are available of each manufacturer')
    print(' (6) Show the average amount of games in stock of a given manufacturer')
    print(' (0) Back to main menu')
    user_input = input(': ')

    table = data_manager.get_table_from_file(str(Path(__file__).parent.absolute())+ '\\'+ file_name)
    manufacturer = table[3]
    id_ = 'nic' #TODO

    if user_input == '1':
        show_table(table)
    if user_input == 2:
        add(table)
    if user_input == 3:
        remove(table, id_)
    if user_input == 4:
        update(table, id_)
    if user_input == 5:
        get_counts_by_manufacturers(table)
    if user_input == 6:
        get_average_by_manufacturer(table, manufacturer)
    if user_input == 0:
        ui.print_menu()
    # your code


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    path = (str(Path(__file__).parent.absolute()) + '\\' + file_name)
    table = data_manager.get_table_from_file(path)
    print(table)



def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    # your code

    return table


def remove(table, id_):
    """
    Remove a record with a given id from the table.

    Args:
        table (list): table to remove a record from
        id_ (str): id of a record to be removed

    Returns:
        list: Table without specified record.
    """

    # your code

    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table: list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    # your code

    return table


# special functions:
# ------------------

def get_counts_by_manufacturers(table):
    """
    Question: How many different kinds of game are available of each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
         dict: A dictionary with this structure: { [manufacturer] : [count] }
    """

    # your code


def get_average_by_manufacturer(table, manufacturer):
    """
    Question: What is the average amount of games in stock of a given manufacturer?

    Args:
        table (list): data table to work on
        manufacturer (str): Name of manufacturer

    Returns:
         number
    """

    # your code
