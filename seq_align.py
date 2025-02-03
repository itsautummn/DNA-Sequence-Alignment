import sys
import csv
import string


def sequence_alignment(first: string, second: string):
    # Import all necessary files into proper data sets
    costMatrix = []
    with open("imp2cost.txt", "r") as fcost:
        csvCost = csv.reader(fcost)
        for line in csvCost:
            costMatrix.append(line)
    finput = open("imp2input.txt", "r")
    x = finput.readline()

    # Perform the edit distance calculations
    minDist, distMatrix = edit_dist(x.split(",")[0], x.split(",")[1], costMatrix)

    # Print statements
    print(f"minDist = {minDist}")
    # for line in distMatrix:
    #     print(line)


def edit_dist(first: string, second: string, costMatrix: list[list]):
    # This caused us so much headache to figure out
    # The second string includes a newline character, so the length is altered because of it
    # Fixed it by doing the below:
    lenFirst = len(first)
    lenSecond = len(second) - 1

    # Set up the 2D distMatrix list
    distMatrix = []
    for i in range(lenFirst):
        distMatrix.append([i])
        for j in range(1, lenSecond):
            distMatrix[i].append(j)
    
    # Set up the 2D ptr list
    ptr = []
    for i in range(lenFirst):
        ptr.append([None])
        for j in range(1, lenSecond):
            ptr[i].append(None)

    # Fill in the 2D distMatrix list and the 2D ptr list
    # Largely similar to the psuedocode provided in lecture
    for i in range(1, lenFirst):
        for j in range(1, lenSecond):
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
    # Very crude and inefficient way of finding the cost of two characters via the cost matrix
    x, y = 0

    for i in range(len(costMatrix)):
        if costMatrix[i][0] == a:
            x = i
            break

    for j in range(len(costMatrix)):
        if costMatrix[0][j] == b:
            y = j
            break

    return int(costMatrix[x][y])


def backtrace(): # Not implemented yet
    pass
    

if __name__ == "__main__":
    sequence_alignment("foo", "bar")
