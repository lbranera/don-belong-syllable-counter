def get_doc(filename):
    file = open(filename)
    doc = [line.strip().split(" ") for line in file.readlines()]
    file.close()

    return doc