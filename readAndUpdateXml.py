import xml.dom.minidom as xl

def main():
    doc=xl.parse("navigator.xml")
    print(doc.nodeName)
    print(doc.firstChild.tagName)


if __name__ == "__main__":
    main()