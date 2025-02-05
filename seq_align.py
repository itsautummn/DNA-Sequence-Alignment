import csv
import string

# Global dictionary for accessing the cost matrix easier
cdx = {
    "*": 0,
    "-": 1,
    "A": 2,
    "T": 3,
    "G": 4,
    "C": 5
}


def sequence_alignment():
    # Import all necessary files into proper data sets
    cm = []
    with open("imp2cost.txt", "r") as fcost:
        csvCost = csv.reader(fcost)
        for line in csvCost:
            cm.append(line)
    finput = open("imp2input.txt", "r")

    # Perform the edit distance calculations
    with open("imp2output.txt", "w") as fo:
        for x in finput:
            a = x.split(",")[0]
            b = x.split(",")[1][:-1] # Remove the newline character

            md, bt = edit_dist(a, b, cm)
            f, s = backtrace(bt, a, b)

            fo.write(f"{f},{s}:{md}\n")


"""
Steps:
    1.  The base cases are the first x and y axis lines, which both start
        at (0, 0) and "increment" up `i` and `j` based on a) the previous 
        cell `i - 1` or `j - 1` and b) the cost of the current character 
        in x based on the given cost matrix. 

    2.  The unknown cases (all cells from i = `1..n` and j = `1..m`) are
        found by taking the minimum of the three cells to the right, below, 
        and diagonal of the current cell + the cost of the character. 
        For example: cell `[i][j]` is equal to 
           `min([i - 1][j] + diff(i - 1, "-"), 
                [i][j - 1] + diff("-", j - 1),
                [i - 1][j - 1] + diff(i - 1, j - 1))
"""
def edit_dist(f: string, s: string, cm: list[list]) -> (int, list[list]): # type: ignore
    # Set up the 2D distance matrix
    dm = [["F" for i in range(len(s) + 1)] for j in range(len(f) + 1)]
    dm[0][0] = int(cm[cdx["-"]][cdx["-"]])

    for i in range(1, len(f) + 1):
        dm[i][0] = dm[i - 1][0] + int(cm[cdx[f[i - 1]]][cdx["-"]])
    for j in range(1, len(s) + 1):
        dm[0][j] = dm[0][j - 1] + int(cm[cdx["-"]][cdx[s[j - 1]]])

    for i in range(1, len(f) + 1):
        for j in range(1, len(s) + 1):
            dm[i][j] = min(dm[i - 1][j] + int(cm[cdx[f[i - 1]]][cdx["-"]]),
                           dm[i][j - 1] + int(cm[cdx["-"]][cdx[s[j - 1]]]),
                           dm[i - 1][j - 1] + int(cm[cdx[f[i - 1]]][cdx[s[j - 1]]]))

    return dm[len(f)][len(s)], dm


def backtrace(bt, f, s):
    # Indecies
    i = len(f) - 1
    j = len(s) - 1

    # Aligned strings
    fa = ""
    sa = ""

    # Backtrace by finding the minimum from the top right corner to the bottom left
    # Note that in the actual implemenation, the top right corner is actually the bottom right, and the bottom left is actually the top left, this is just how it is with 2D matrices
    while i >= 0 and j >= 0:
        # The next direction is the minimum of all directions
        n = min(bt[i - 1][j],
                bt[i][j - 1], 
                bt[i - 1][j - 1])

        if n == bt[i - 1][j]:   # If next is left
            fa = f[i] + fa
            sa = "-" + sa
            i -= 1
        elif n == bt[i][j - 1]: # If next is down
            fa = "-" + fa
            sa = s[j] + sa
            j -= 1
        else:                   # If next is diagonal
            fa = f[i] + fa
            sa = s[j] + sa
            i -= 1
            j -= 1
    
    # Clean up any left over characters
    while i >= 0:
        fa = f[i] + fa
        sa = "-" + sa
        i -= 1
    while j >= 0:
        fa = "-" + fa
        sa = s[j] + sa
        j -= 1

    return fa, sa


if __name__ == "__main__":
    sequence_alignment()
