"""A module to take a list and turn it into a table"""
import argparse
import ipaddress
import os
import sys
import numpy as np

def create_matrix(input_list, columns):
    """Create a matrix out of the given list"""
    sys.stdout.write("Creating table...")
    sys.stdout.flush()
    # Sort by IP Address or the normal string sort
    if input_list[0].count(".") == 3:
        sorted_list = sorted(input_list, key = ipaddress.IPv4Network)
    else:
        sorted_list = sorted(input_list)

    # Fill the list with blanks to get enough values for matrix
    for _ in range(0, columns - len(input_list) % columns):
        sorted_list.append("")
    matrix = np.array(sorted_list).reshape(-1, columns)
    sys.stdout.write("Done!\n")
    return matrix

def create_output(matrix, filename, file_format):
    """Output the findings in the specified format"""
    if file_format != 'csv':
        print(f"[-] Error: Only supported output format is CSV: {file_format}")
        sys.exit(1)
    np.savetxt(filename, matrix, delimiter=",", fmt='%s')
    print(f"[+] Successfully wrote table to {filename}!")

def create_list(input_list):
    """Construct the list of items to turn into a table. File and string inputs supported"""
    if os.path.isfile(input_list):
        with open(input_list, 'r', encoding='UTF-8') as ifile:
            return [line.rstrip() for line in ifile]
    return input_list.split(',')

def main():
    """Create a table out of a list of items"""

    # Parse required arguments to generate the list of targets and output configurations
    parser = argparse.ArgumentParser(
        description='Turn the inputted list into a table with the specified columns.')
    parser.add_argument('--filename', required=True, help="The output filename")
    parser.add_argument('--inputList', required=True, help='The list to turn into a table.')
    parser.add_argument('--cols', required=True, type=int,
                        help='The number of columns in the output table.')
    parser.add_argument('--format', default='csv',
                        help='The output format to display and save results in, defaults to csv.')

    args = parser.parse_args()
    output_filename = args.filename
    output_format = args.format
    input_list = create_list(args.inputList)
    columns = args.cols

    # Retrieve the header for each target
    matrix = create_matrix(input_list, columns)

    # Output the results to the desired format
    create_output(matrix, output_filename, output_format)


if __name__ == "__main__":
    main()
