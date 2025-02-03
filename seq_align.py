import sys
import csv
import string

"""
Steps:
    1. Import all necessary files into proper data sets
"""
def sequence_alignment(first: string, second: string):
    # Set up all variables
    costMatrix = [[]]

    # Import all necessary files into proper data sets
    with open("imp2cost.txt", "r") as fcost:
        csvCost = csv.reader(fcost)
        for line in csvCost:
            costMatrix.append(line)
    finput = open("imp2input.txt", "r")
    for x in finput:
        edit_dist(x.split(",")[0], x.split(",")[1], costMatrix)
    print(costMatrix)


def edit_dist(first: string, second: string, costMatrix: list[list]):
    # Set up the 2D lists for later use (why is this so hard)
    minLen = min(len(first), len(second))
    distMatrix = [[None] * minLen] * minLen
    distMatrix[0][0] = 0
    ptr = [[None] * minLen] * minLen
    ptr[0][0] = 0

    for i in range(1, len(first)):
        distMatrix[i][0] = i
        ptr[i][0] = ptr[i - 1][0]
    for j in range(1, len(second)):
        distMatrix[0][j] = j
        ptr[0][j] = ptr[0][j - 1]
    
    for i in range(1, len(first)):
        for j in range(1, len(second)):
            distMatrix[i][j] = min(
                distMatrix[i - 1][j] + 1,
                distMatrix[i][j - 1] + 1,
                distMatrix[i - 1][j - 1] + diff(first[i], second[j])
            )
            match distMatrix[i][j]:
                case 1:
                    ptr[i][j] = ptr[i - 1][j]
                case 2:
                    ptr[i][j] = ptr[i][j - 1]
                case 3:
                    ptr[i][j] = ptr[i - 1][j - 1]
    
    return distMatrix[len(first)][len(second)], ptr


def diff(a, b) -> int:
    if a == b:
        return 0
    if a != b:
        return 1


def backtrace():
    pass
    

if __name__ == "__main__":
    sequence_alignment("foo", "bar")
