import PySimpleGUI as sg
from pyperclip import copy


def rm(txt):
    txt = txt.replace("... ", "", 1)
    txt = txt.replace(">>> ", "", 1)
    return txt


def stripper(txt):
    lines = txt.splitlines()
    lines = [rm(l) for l in lines]
    return "\n\r".join(lines)


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
