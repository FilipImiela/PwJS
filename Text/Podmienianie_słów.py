
def main():

    infile = "Radio in the United States.txt"
    outfile = "Radio in the United States_corrected.txt"

    dict = {" is ": " jest ", " on ": " na ", " or ": " albo "}
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in dict:
                line = line.replace(word, dict[word])
            fout.write(line)


if __name__ == "__main__":
    main()