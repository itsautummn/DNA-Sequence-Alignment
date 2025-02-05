# CS325 Homework 2 Implementation
Private git repo for our second homework implementation project in analysis of algorithms

## HOW TO USE
### Options:
The program has optional parameters when run:
- `-c <cost_file>` will use the provided file as the cost matrix for calculations. Defaults to "imp2cost.txt" if not specified
- `-i <input_file>` will use the provided file as the input for the sequences. Defaults to "imp2input.txt" if not specified
- `-o <output_file>` will use the provided file as the output. Defaults to "imp2output.txt" if not specified

### Run with Provided Input:
To run the program with the provided input file, run the command `python seq_align.py`. This will use the default file names "imp2input.txt" and "imp2cost.txt" and create a file named "imp2output.txt". 

To ensure that this output is correct, run the command `python check_cost.py`. This will use the default file names "imp2output.txt" and "imp2cost.txt" and create a file named "cost_check_results.txt", detailing all the checks and whether or not they were passed.

### Run with Random Input:
To run the program with a random input file, run the command `python input_gen.py <size of desired input>`. This will create a file named "imp2input-\<size of desired input\>.txt".

To run the "seq_align.py" file with this new input file, run the command `python seq_align.py -i imp2input-<size of desired input>.txt`. Continue from the Provided Input section above.

For example, if one wanted to use a file size of 1000, the steps they would take are:
1. Run `python input_gen.py 1000`
3. Run `python seq_align.py -i imp2input-1000.txt`
4. Run `python check_cost.py`
