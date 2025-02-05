# CS325 Homework 2 Implementation
Private git repo for our second homework implementation project in analysis of algorithms

## HOW TO USE
### Provided Input:
To run the program with the provided input file, run the command `python seq_align.py`. This will use the default file names "imp2input.txt" and "imp2cost.txt" and create a file named "imp2output.txt". 

To ensure that this output is correct, run the command `python check_cost.py`. This will use the default file names "imp2output.txt" and "imp2cost.txt" and create a file named "cost_check_results.txt", detailing all the checks and whether or not they were passed.

### Random Input:
To run the program with a random input file, run the command `python input_gen.py <size of desired input>`. This will create a file named "imp2output-\<size of desired input\>.txt".

To run the "seq_align.py" file with this new input file, change the text "imp2input.txt" on line 22 to "imp2input-\<size of desired input\>.txt" and run the file as described in the Provided Input section above.
