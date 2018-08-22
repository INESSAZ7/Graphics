import numpy as np

def vozvrat_znach_x_from_file():
    with open("File_with_znach.txt",'r') as file:
        x1 = file.readline()
        x1 = x1.split()
        x1 = list(map(float, x1))
        x = np.array(x1)
    return x

def vozvrat_znach_y_from_file():
        with open("File_with_znach.txt", 'r') as file:
            y1 = file.readline()
            y1 = file.readline()
            y1 = y1.split()
            y1 = list(map(float, y1))
            y = np.array(y1)
        return y


def vozvrat_znach_xerr_from_file():
    with open("File_with_pogreshnosti.txt", 'r') as file:
        xerr1 = file.readline()
        xerr1 = xerr1.split()
        xerr1 = np.array(xerr1)
        xerr = list(map(float,xerr1))

    return xerr


def vozvrat_znach_yerr_from_file():
    with open("File_with_pogreshnosti.txt", 'r') as file:
        yerr1 = file.readline()
        yerr1 = file.readline()
        yerr1 = yerr1.split()
        yerr1 = np.array(yerr1)
        yerr = list(map(float, yerr1))
    return yerr

def text_ox_file():
    with open("File_with_text.txt", 'r') as file:
        str = file.readline()
    return str



