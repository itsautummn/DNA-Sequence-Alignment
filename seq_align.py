import sys
import csv
import string


def sequence_alignment():
    # Import all necessary files into proper data sets
    costMatrix = []
    with open("imp2cost.txt", "r") as fcost:
        csvCost = csv.reader(fcost)
        for line in csvCost:
            costMatrix.append(line)
    finput = open("imp2input.txt", "r")

    # Perform the edit distance calculations
    for x in finput:
        minDist, bt = edit_dist(x.split(",")[0], x.split(",")[1], costMatrix)
        first, second = backtrace(bt, x.split(",")[0], x.split(",")[1])
        print(f"{first},{second}:{minDist}")

    # # Perform the edit distance calculations
    # x = finput.readline()
    # minDist, bt = edit_dist(x.split(",")[0], x.split(",")[1], costMatrix)
    # first, second = backtrace(bt, x.split(",")[0], x.split(",")[1])
    # print(f"{first},{second}:{minDist}")


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
    # ptr = []
    # for i in range(lenFirst):
    #     ptr.append([i])
    #     for j in range(1, lenSecond):
    #         ptr[i].append(j)
    # ptr = []

    # Fill in the 2D distMatrix list and the 2D ptr list
    # Largely similar to the psuedocode provided in lecture
    for i in range(1, lenFirst):
        for j in range(1, lenSecond):
            distMatrix[i][j] = min(
                distMatrix[i - 1][j] + 1,
                distMatrix[i][j - 1] + 1,
                distMatrix[i - 1][j - 1] + diff(first[i], second[j], costMatrix)
            )
            # ptr.append(distMatrix[i][j])
            # # if distMatrix[i][j] == distMatrix[i - 1][j] + 1:
            # #     ptr[i][j] = ptr[i - 1][j]
            # # elif distMatrix[i][j] == distMatrix[i][j - 1] + 1:
            # #     ptr[i][j] = ptr[i][j - 1]
            # # else:
            # #     ptr[i][j] = ptr[i - 1][j - 1]

    return distMatrix[lenFirst- 1][lenSecond - 1], distMatrix


def diff(a, b, costMatrix) -> int:
    # Very crude and inefficient way of finding the cost of two characters via the cost matrix
    x = 0
    y = 0

    for i in range(len(costMatrix)):
        if costMatrix[i][0] == a:
            x = i
            break

    for j in range(len(costMatrix)):
        if costMatrix[0][j] == b:
            y = j
            break

    return int(costMatrix[x][y])


def backtrace(bt, first, second): # Not implemented yet
    lenFirst = len(bt)
    lenSecond = len(bt[0])

    lenAligned = max(lenFirst, lenSecond)

    # Indecies
    i = lenFirst - 1
    j = lenSecond - 1

    alignedFirst = ""
    alignedSec = ""
    while i > 0 and j > 0:
        next = min(
            bt[i - 1][j],
            bt[i][j - 1],
            bt[i - 1][j - 1]
        )
        if next == bt[i - 1][j]:
            alignedFirst = first[i] + alignedFirst
            alignedSec = "-" + alignedSec
            i -= 1
        elif next == bt[i][j - 1]:
            alignedFirst = "-" + alignedFirst
            alignedSec = second[j] + alignedSec
            j -= 1
        else:
            alignedFirst = first[i] + alignedFirst
            alignedSec = second[j] + alignedSec
            i -= 1
            j -= 1
    
    while i > 0:
        alignedFirst = first[i] + alignedFirst
        alignedSec = "-" + alignedSec
        i -= 1
    while j > 0:
        alignedFirst = "-" + alignedFirst
        alignedSecond = second[j] + alignedSec
        j -= 1
    
    return alignedFirst, alignedSec

if __name__ == "__main__":
    sequence_alignment()
