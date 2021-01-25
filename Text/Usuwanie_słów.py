
def main():

    infile = "17th-century philosophy.txt"
    outfile = "17th-century philosophy_corrected.txt"

    delete_list = [" is ", " and ", " or "]
    with open(infile) as fin, open(outfile, "w+") as fout:
        for line in fin:
            for word in delete_list:
                line = line.replace(word, " ")
            fout.write(line)

if __name__ == "__main__":
    main()


