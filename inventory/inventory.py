""" Inventory module

Data table structure:
    * id (string): Unique and random generated identifier
        at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letters)
    * name (string): Name of item
    * manufacturer (string)
    * purchase_year (number): Year of purchase
    * durability (number): Years it can be used
"""

# everything you'll need is imported:
# User interface module
import ui
# data manager module
import data_manager
# common module
import common


ID = 0
NAME = 1
MANUFACTURER = 2
PURCHASE_YEAR = 3
DURABILITY = 4
title_list = ["Id", "Name", "Manufacturer", "Purchase year", "Durability"]


def start_module():
    """
    Starts this module and displays its menu.
     * User can access default special features from here.
     * User can go back to main menu from here.

    Returns:
        None
    """

    file_name = "inventory/inventory.csv"
    table = data_manager.get_table_from_file(file_name)

    options = ["Display a table",
               "Add new record",
               "Remove record",
               "Update record",
               "Show items that have not exceeded their durability yet",
               "Show the average durability times for each manufacturer"]

    while True:
        try:
            ui.print_menu("Store Manager", options, "Back to main menu")
            inputs = ui.get_inputs(["Please enter a number: "], "")
            option = inputs[0]
            if option == "1":
                show_table(table)
                continue
            elif option == "2":
                add(table)
                data_manager.write_table_to_file(file_name, table)
                continue
            elif option == "3":
                remove(table, id_=ui.get_inputs(["Please enter: "], title_list[ID]))
                data_manager.write_table_to_file(file_name, table)
                continue
            elif option == "4":
                update(table, id_=ui.get_inputs(["Please enter: "], title_list[ID]))
                data_manager.write_table_to_file(file_name, table)
                continue
            elif option == "5":
                get_available_items(table, year=int(ui.get_inputs(["Please enter: "], title_list[PURCHASE_YEAR])[0]))
                continue
            elif option == "6":
                get_average_durability_by_manufacturers(table)
                continue
            elif option == "0":
                break
            else:
                raise KeyError("There is no such option.")
        except KeyError as err:
            ui.print_error_message(str(err))


def show_table(table):
    """
    Display a table

    Args:
        table (list): list of lists to be displayed.

    Returns:
        None
    """

    ui.print_table(table, title_list)


def add(table):
    """
    Asks user for input and adds it into the table.

    Args:
        table (list): table to add new record to

    Returns:
        list: Table with a new record
    """

    table = common.add_item(table, title_list)
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

    table = common.remove_item(table, id_)
    return table


def update(table, id_):
    """
    Updates specified record in the table. Ask users for new data.

    Args:
        table (list): list in which record should be updated
        id_ (str): id of a record to update

    Returns:
        list: table with updated record
    """

    table = common.update_item(table, title_list, id_)
    return table


# special functions:
# ------------------

def get_available_items(table, year):
    """
    Question: Which items have not exceeded their durability yet (in a given year)?

    Args:
        table (list): data table to work on
        year (number)

    Returns:
        list: list of lists (the inner list contains the whole row with their actual data types)
    """

    durability_not_exceeded = list()
    for line in table:
        purchase_year = int(line[PURCHASE_YEAR])
        durability = int(line[DURABILITY])
        if (year - purchase_year) < durability:
            durability_not_exceeded.append(line)
    for value in durability_not_exceeded:
        value[PURCHASE_YEAR] = int(value[PURCHASE_YEAR])
        value[DURABILITY] = int(value[DURABILITY])

    label = 'Items with not exceeded durability'
    ui.print_result(durability_not_exceeded, label)
    return durability_not_exceeded


def get_average_durability_by_manufacturers(table):
    """
    Question: What are the average durability times for each manufacturer?

    Args:
        table (list): data table to work on

    Returns:
        dict: a dictionary with this structure: { [manufacturer] : [avg] }
    """

    manufacturers = set()
    manufacturers_count = dict()
    durability_list = list()
    sum_of_durability = 0
    avg_durability = 0
    for line in table:
        manufacturers.add(line[MANUFACTURER])
        durability_list.append(line[DURABILITY])
    for manufacturer in manufacturers:
        durability_list = list()
        sum_of_durability = 0
        for line in table:
            if manufacturer == line[MANUFACTURER]:
                durability_list.append(line[DURABILITY])
        for durability in durability_list:
            sum_of_durability += int(durability)
        avg_durability = sum_of_durability / len(durability_list)
        manufacturers_count[manufacturer] = avg_durability

    label = 'Average durability times for each manufacturer'
    ui.print_result(manufacturers_count, label)
    return manufacturers_count
