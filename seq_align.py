import sys
import csv
import string

"""
Steps:
    1. Import all necessary files into proper data sets
"""
def sequence_alignment(first: string, second: string):
    # Set up all variables
    costMatrix = []

    # Import all necessary files into proper data sets
    with open("imp2cost.txt", "r") as fcost:
        csvCost = csv.reader(fcost)
        for line in csvCost:
            costMatrix.append(line)
    finput = open("imp2input.txt", "r")
    x = finput.readline()
    print(f"Length 1 = {len(x.split(",")[0])}\nLength 2 = {len(x.split(",")[1])}")
    minDist, distMatrix = edit_dist(x.split(",")[0], x.split(",")[1], costMatrix)
    print(f"minDist = {minDist}")
    for line in distMatrix:
        print(line)


def edit_dist(first: string, second: string, costMatrix: list[list]):
    print(f"second[59] {second[59]}")
    lenFirst = len(first)
    lenSecond = len(second) - 1

    # Set up the 2D lists for later use (why is this so hard)
    print(lenSecond)
    maxLen = max(lenFirst, lenSecond)
    ptr = [[None] * maxLen] * maxLen
    ptr[0][0] = 0

    distMatrix = []
    for i in range(lenFirst):
        distMatrix.append([i])
        for j in range(1, lenSecond):
            distMatrix[i].append(j)
    
    for i in range(1, lenFirst):
        print(f"Outer {i}")
        for j in range(1, lenSecond):
            print(f"Index {j}")
            distMatrix[i][j] = min(
                distMatrix[i - 1][j] + 1,
                distMatrix[i][j - 1] + 1,
                distMatrix[i - 1][j - 1] + diff(first[i], second[j], costMatrix)
            )
            match distMatrix[i][j]:
                case 1:
                    ptr[i][j] = ptr[i - 1][j]
                case 2:
                    ptr[i][j] = ptr[i][j - 1]
                case 3:
                    ptr[i][j] = ptr[i - 1][j - 1]
    
    return distMatrix[lenFirst- 1][lenSecond - 1], distMatrix


def diff(a, b, costMatrix) -> int:
    fi = 0
    si = 0
    for i in range(len(costMatrix)):
        if costMatrix[i][0] == a:
            fi = i
            break
    for j in range(len(costMatrix)):
        if costMatrix[0][j] == b:
            si = j
            break
    return int(costMatrix[fi][si])


def backtrace():
    pass
    

if __name__ == "__main__":
    sequence_alignment("foo", "bar")
