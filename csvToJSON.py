# Written by Ryan Taylor for Hatchways assessment

import sys
import json
from classes import Order, OrderEncoder, FormatException

# A function to set up a dictionary of the given orders
def create_order_dictionary(orders_file):
    line_number = 0
    orders_dict = {}
    
    for line in orders_file:
        line_number += 1
        pieces = line.split(",")
        
        if len(pieces) != 2:
            raise FormatException(line_number, orders_file.name, line)
        elif pieces[0] != "id":
            try:
                id = int(pieces[0])
                name = pieces[1]
                if name[-1] == "\n":
                    name = name[:-1]
                orders_dict[id] = Order(id, name)
            except:
                raise FormatException(line_number, orders_file.name, line)
    
    return orders_dict

# A function to add dependents to orders while keeping track of independent orders
def create_dependent_list(dependencies_file, orders_dict):
    
    independent_order_ids = set()
    for key in orders_dict.keys():
        independent_order_ids.add(key)

    line_number = 0
    for line in dependencies_file:
        line_number += 1
        pieces = line.split(",")
        
        if len(pieces) != 2:
            raise FormatException(line_number, dependencies_file.name, line)
        elif pieces[0] != "id":
            try:
                id = int(pieces[0])
                child_id = int(pieces[1])
                orders_dict[id].dependencies.append(orders_dict[child_id])
                if child_id in independent_order_ids:
                    independent_order_ids.remove(child_id)
            except:
                raise FormatException(line_number, dependencies_file.name, line)
    
    return orders_dict, independent_order_ids


# The main processing function
def process_csv_file(orders_file, dependencies_file, output_file):
    orders_dict = create_order_dictionary(orders_file)
    orders_dict, independent_order_ids = create_dependent_list(dependencies_file, orders_dict)

    # Create and save list of independent orders
    independent_orders = []
    for order_id in independent_order_ids:
        independent_orders.append(orders_dict[order_id])

    output_file.write(json.dumps(
        {"orders": independent_orders}, cls=OrderEncoder, indent=2))

    print("\nSuccess! Written to \"" + output_file.name + "\".\n")

# ------- Begin processing -------
def main():

    # Check for proper usage
    if len(sys.argv) != 4:
        print(
            "\n\tUsage:\n\t  csvToJson.py {path-to-orders-file} {path-to-dependencies-file} {path-to-output-file}\n")
        sys.exit()

    # Open all given files
    path_to_orders_file = sys.argv[1]
    path_to_dependencies_file = sys.argv[2]
    path_to_output_file = sys.argv[3]

    try:
        given_orders_file = open(path_to_orders_file, "r")
    except:
        print("Could not open ", path_to_orders_file)
        sys.exit()

    try:
        given_dependencies_file = open(path_to_dependencies_file, "r")
    except:
        print("Could not open ", path_to_dependencies_file)
        sys.exit()

    try:
        given_output_file = open(path_to_output_file, "w")
    except:
        print("Could not open ", path_to_output_file)
        sys.exit()

    try:
        process_csv_file(given_orders_file, given_dependencies_file, given_output_file)
    except FormatException as exception:
        print(exception.message)

    given_orders_file.close()
    given_dependencies_file.close()
    given_output_file.close()

if __name__=="__main__":
    main()
