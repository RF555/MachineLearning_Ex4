import pandas as pd


def read(name):
    with open(name) as file_in:
        lines = []
        for line in file_in:
            line = line.replace("\n", "")
            line = line.split(" ")
            lines.append(line)
        return lines


def dfFromSquares(file_path):
    with open(file_path) as file_in:
        lines = []
        for line in file_in:
            line = line.replace("\n", "")
            line = line.split(" ")
            lines.append(line)
        return pd.DataFrame(lines, columns=["x", "y", "label"])
