def get_doc(filename):
    file = open(f"./input/{filename}")
    doc = [line.strip().split(" ") for line in file.readlines()]
    file.close()

    return doc