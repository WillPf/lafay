import PySimpleGUI as sg

S6 = 6 # nombre de series
S4 = 4 # nombre de series
S3 = 3 # nombre de series

niv4 = [
    [sg.Text("B", s=5, background_color="#99b19c")] + [sg.Input(k=f"B{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("A6", s=5, background_color="#99b19c")] + [sg.Input(k=f"A6{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("A2", s=5, background_color="#99b19c")] + [sg.Input(k=f"A2{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("I3", s=5, background_color="#99b19c")] + [sg.Input(k=f"I3{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("E2G", s=5, background_color="#99b19c")] + [sg.Input(k=f"E2G{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("E2D", s=5, background_color="#99b19c")] + [sg.Input(k=f"E2D{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("F", s=5, background_color="#99b19c")] + [sg.Input(k=f"F{i + 1}", s=5, background_color="#d7d1c9") for i in range(S4)],
    [sg.Text("G", s=5, background_color="#99b19c")] + [sg.Input(k=f"G{i + 1}", s=5, background_color="#d7d1c9") for i in range(S6)],
    [sg.Text("K3", s=5, background_color="#99b19c")] + [sg.Input(k=f"K3{i + 1}", s=5, background_color="#d7d1c9") for i in range(S3)],
]