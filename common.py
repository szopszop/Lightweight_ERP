""" Common module
implement commonly used functions here
"""

import random, string
import ui
ID = 0


def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    l1 = [random.choice(string.digits) for _ in range(2)]
    l2 = [random.choice(string.ascii_uppercase) for _ in range(2)]
    l3 = [random.choice(string.ascii_lowercase) for _ in range(2)]
    l4 = [';',';']
    while ';' in l4:
        l4 = [random.choice(string.punctuation) for _ in range(2)]

    password_list = l1 + l2 + l3 + l4

    random.shuffle(password_list)
    generated =  "".join(password_list)

    for line in table:
        if generated  == line[ID]:
            generated = generate_random(table)
            continue

    return generated


def add_item(table, title_list):
    new_line = []
    id_ = generate_random(table)
    for line in table:
        if id_ == line[ID]:
            id_ = generate_random(table)
            continue
    new_line.append(id_)
    for title in title_list[1:]:
        user_input = ui.get_inputs(["Please enter: "], title)
        new_line.append(''.join(user_input))
    table.append(new_line)

    return table


def remove_item(table, id_):
    id_ = ''.join(id_)
    line_counter = 0
    for line in table:
        if id_ == line[ID]:
            del table[line_counter]
            break
        line_counter += 1

    return table


def update_item(table, title_list, id_):
    new_line = []
    id_ = ''.join(id_)
    new_line.append(id_)
    line_counter = 0
    for line in table:
        if id_ == line[ID]:
            index_to_update = line_counter
            del table[index_to_update]
            for title in title_list[1:]:
                user_input = ui.get_inputs(["Please enter: "], title)
                new_line.append(''.join(user_input))
            if index_to_update <= len(table):
                table.append(new_line)
            else:
                table[index_to_update] = new_line
            break
        line_counter += 1

    return table

