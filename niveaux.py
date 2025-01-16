import PySimpleGUI as sg

S6 = 6 # nombre de series
S4 = 4 # nombre de series
S3 = 3 # nombre de series

exo_style = {"s": 5, "background_color": "#99b19c", "text_color": "#ffffff", "border_width": 0}
serie_style = {"s": 5, "background_color": "#d7d1c9", "justification": "c"}

niv4 = [
    [sg.Input("B", **exo_style)] + [sg.Input(k=f"B{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("A6", **exo_style)] + [sg.Input(k=f"A6{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("A2", **exo_style)] + [sg.Input(k=f"A2{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("I3", **exo_style)] + [sg.Input(k=f"I3{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("E2G", **exo_style)] + [sg.Input(k=f"E2G{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("E2D", **exo_style)] + [sg.Input(k=f"E2D{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("F", **exo_style)] + [sg.Input(k=f"F{i + 1}", **serie_style) for i in range(S4)],
    [sg.Input("G", **exo_style)] + [sg.Input(k=f"G{i + 1}", **serie_style) for i in range(S6)],
    [sg.Input("K3", **exo_style)] + [sg.Input(k=f"K3{i + 1}", **serie_style) for i in range(S3)],
]