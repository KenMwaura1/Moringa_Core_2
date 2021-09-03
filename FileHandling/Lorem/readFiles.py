text_file = "test.txt"


def read_file(txt_file):
    """
    Function that reads a text file and returns the data from the text file.
    :param txt_file:
    :return: data from the text file
    """
    with open(txt_file, "r") as handle:
        return handle.read()
