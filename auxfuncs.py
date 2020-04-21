"""
Auxiliary functions for demo Flask application.
"""

import pathlib


def load_ingredients():
    """Returns a list of possible ingredients from a file"""

    ingredients = []

    rootdir = pathlib.Path('.').parent  # rootdir of the app
    datadir = rootdir / 'data-files'

    csvpath = datadir / 'ingredients.csv'
    try:
        with csvpath.open('rt') as csvfile:
            _ = csvfile.readline()  # skip header line
            for line in csvfile:
                name, item_type, cost = line.split(',')

                # We store in a dictionary to make it easier
                # to access from the templates.
                itemdict = {
                    'name': name,
                    'type': item_type,
                    'cost': cost
                }
                
                ingredients.append(itemdict)
            
    except FileNotFoundError:
        raise Exception('File not found!!')

    return ingredients