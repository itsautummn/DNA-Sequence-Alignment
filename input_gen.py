import sys
import random

def generate(size: int):
    with open(f"imp2input-{size}.txt", "w") as fo:
        choices = ["A", "T", "G", "C"]

        for i in range(10):
            # Pick a random length for each string, totaling to size 'size'
            # The length will be at least a third of the size, so that we don't get strings that are 1 and 499 often

            for j in range(size // 2):
                fo.write(random.choice(choices))
            fo.write(",")
            for k in range(size // 2):
                fo.write(random.choice(choices))
            fo.write("\n")
    fo.close()

def main(argv):
    try:
        size = int(argv)
        generate(size)
    except:
        raise TypeError("Only integers allowed")

if __name__ == "__main__":
    main(sys.argv[1])
