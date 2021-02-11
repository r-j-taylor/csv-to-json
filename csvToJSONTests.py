import sys
import os
from csvToJSON import process_csv_file
from classes import FormatException

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

print("\nBeginning tests!")

# ---------- Test #1 ----------
# Opening necessary files
try:
    good_orders_file = open(os.path.join(
        __location__, 'tests/good_orders.txt'))
except:
    print("Could not open good_orders.txt")
    sys.exit()

try:
    good_dependencies_file = open(os.path.join(
        __location__, 'tests/good_dependencies.txt'))
except:
    print("Could not open good_dependencies.txt")
    sys.exit()

try:
    output_file = open(os.path.join(
        __location__, 'tests/good_output.json'), 'w')
except:
    print("Could not open good_output.json")
    sys.exit()

# Running test for success
print("\nExpecting to succeed:")
print("---------------------------------------------------------------")
try:
    process_csv_file(good_orders_file, good_dependencies_file, output_file)
except FormatException as exception:
    print(exception.message)
print("---------------------------------------------------------------")


# ---------- Test #2 ----------
# Opening necessary files
try:
    bad_orders_file = open(os.path.join(__location__, 'tests/bad_orders.txt'))
except:
    print("Could not open bad_orders.txt")
    sys.exit()

try:
    good_dependencies_file = open(os.path.join(
        __location__, 'tests/good_dependencies.txt'))
except:
    print("Could not open good_dependencies.txt")
    sys.exit()

try:
    output_file = open(os.path.join(
        __location__, 'tests/bad_output.json'), 'w')
except:
    print("Could not open bad_output.json")
    sys.exit()

# Running test for improperly formatted orders file
print("\nExpecting to fail due to orders:")
print("---------------------------------------------------------------")
try:
    process_csv_file(bad_orders_file, good_dependencies_file, output_file)
except FormatException as exception:
    print(exception.message)
print("---------------------------------------------------------------")

# ---------- Test #3 ----------
# Opening necessary files
try:
    good_orders_file = open(os.path.join(
        __location__, 'tests/good_orders.txt'))
except:
    print("Could not open good_orders.txt")
    sys.exit()

try:
    bad_dependencies_file = open(os.path.join(
        __location__, 'tests/bad_dependencies.txt'))
except:
    print("Could not open bad_dependencies.txt")
    sys.exit()

try:
    output_file = open(os.path.join(
        __location__, 'tests/bad_output.json'), 'w')
except:
    print("Could not open bad_output.json")
    sys.exit()

# Running test for improperly formatted orders file
print("\nExpecting to fail due to dependencies:")
print("---------------------------------------------------------------")
try:
    process_csv_file(good_orders_file, bad_dependencies_file, output_file)
except FormatException as exception:
    print(exception.message)
print("---------------------------------------------------------------")
