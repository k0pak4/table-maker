# table-maker
 Make tables from lists for easy reporting

## Installation
All required libraries are covered in the Python3 standard lib, so cloning this repository should suffice.
    
## Usage

### Required Arguments

#### filename
The output filename for the resulting data.

#### columns
The amount of columns to create the table with. Extra blank values will fill any additional needed space.

#### inputList
The input list to become a table. Can either be a comma separated list or file with one item per line.

### Optional Arguments

#### format
Supported formats are `csv`. Defaults to `csv`.

## Example Usage
`python3 table_maker.py --filename test.csv --cols 4 --inputList 10.100.150.0/24,10.100.161.0/24,172.1.40.0/24,172.16.95.0/24,10.200.150.0/24,10.200.161.0/24,10.200.183.0/24,10.100.10.0/24,10.100.17.0/24`

## Contributing    
Contributions for the following features (or others!) are welcome through pull requests:

### Future Features
- Add support for more output file types (e.g. .doc, .xls)