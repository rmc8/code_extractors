import re

import PySimpleGUI as sg
from pyperclip import copy


def rm(txt):
    if txt == "...":
        return " " * 4
    return re.sub(r"[\.|>]{3}\s?", "", txt, 1)


def stripper(txt):
    lines = txt.splitlines()
    lines = [rm(l) for l in lines]
    return "\r\n".join(lines)


def gui():
    sg.theme("Black")
    layout = [
        [sg.T("Please enter the code listed in the interpreter.")],
        [sg.Multiline(size=(48, 8), key="code")],
        [sg.Submit("Copy")],
    ]

    window = sg.Window("Code Extractors", grab_anywhere=False).Layout(layout)
    while True:
        event, val = window.Read()
        if event in (None, ):
            break
        elif event == "Copy":
            code = stripper(val["code"])
            copy(code)
            window["code"].update("")
    window.Close()


def main():
    gui()


if __name__ == "__main__":
    main()
