import csv


def print_csv():
    with open('Song_file.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

    file.close()


def add_content(row_content):
    with open('Song_file.csv', "r", newline='') as file:
        reader = list(csv.reader(file))
        reader.insert(len(reader), row_content)

    with open('Song_file.csv', "w", newline='') as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            writer.writerow(line)

    file.close()
    outfile.close()


def delete_content(song):
    lines = list()
    with open('Song_file.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            lines.append(row)
            for field in row:
                if field == song:
                    lines.remove(row)
    with open('Song_file.csv', 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(lines)

    file.close()
    outfile.close()


def main():
    while 1:
        print("(0) Show")
        print("(1) Add Song")
        print("(2) Delete song")
        print("(3) Exit")
        code = int(input("Choose operation: "))
        if code == 0:
            print_csv()
        elif code == 1:
            song = input("Enter song name: ")
            artist = input("Enter artist: ")
            album = input("Enter album: ")
            year = input("Enter year: ")
            row_contents = [song, artist, album, year]
            add_content(row_contents)
        elif code == 2:
            song = input("Enter song name to be deleted: ")
            delete_content(song)

        elif code == 3:
            quit()
        else:
            quit()


if __name__ == "__main__":

    main()
