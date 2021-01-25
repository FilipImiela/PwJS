import xml.dom.minidom as dom


def main():

    doc = dom.parse("Note.xml")

    print("First child tagname: " + doc.firstChild.tagName)

    # adding new task
    new = doc.createElement("body")
    new.setAttribute("name", "Don't forget to buy milk")
    doc.firstChild.appendChild(new)

    # changing name to "Maria"
    doc.getElementsByTagName("to")[0].childNodes[0].nodeValue = "Maria"

    with open("ChangedNote.xml", "x") as file:
        file.write(doc.toxml())
        file.close()


if __name__ == "__main__":
    main()
