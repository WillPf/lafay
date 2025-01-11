import PySimpleGUI as sg
from datetime import datetime
from niveaux import *

today = datetime.now().strftime("%a %d/%m/%Y")

sg.theme('LightGreen7')
# sg.theme_previewer()

layout = [[sg.Text(today, k="date"), sg.Push(), sg.Text(0, k="clock", font=("_", 20, "bold"), s=3), sg.Button("25 sec"), sg.Button("3 min"), sg.Push(), sg.Text("LAFAY")],
    [sg.Push(), sg.Text("Niveau: "), sg.Combo([2, 3, 4, 5, 6, 7, 8], k="NIV")],
    niv4,
    [sg.Button("Save"), sg.Push(), sg.Exit()],
    [sg.Push(), sg.Text("©Willy J. CS50P Final Project 2025", font=("Roboto", 8), text_color="#ffffff")]]