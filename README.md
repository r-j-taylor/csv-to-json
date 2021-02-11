# csv-to-json
A repository containing a program that converts files from CSV format to JSON format. The input files are expected to be an orders file, containing order IDs and order names, and a dependency file, containing parent and child IDs. Example files are included under the `tests` directory.

This program can be run by entering `python3 csvToJSON.py [orders file] [dependency file] [output file]`. Alternatively, the example test file can be run by entering `python3 csvToJSONTests.py`, which will run through all example files included in the `tests` directory.