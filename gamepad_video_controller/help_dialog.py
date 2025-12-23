import threading
import tkinter as tk
from tkinter import ttk


def _show():
    root = tk.Tk()
    root.title("Gamepad Video Controller – Keybinds")
    root.resizable(False, False)

    text = """
Media Controls
A        → Play / Pause
B        → Fullscreen toggle
X        → Mute / Unmute
Y        → Toggle captions

D-Pad ←  → Seek backward
D-Pad →  → Seek forward
D-Pad ↑  → Volume up
D-Pad ↓  → Volume down

Browser / Window
L1       → Next browser tab
R1       → Previous browser tab
R3       → Reload current tab
R2*      → Switch window

Scrolling
Left Stick → Scroll (vertical / horizontal)

System
L2 (hold) → Enable / Disable controller*

* Behavior may change once custom mappings are added.
"""

    frame = ttk.Frame(root, padding=12)
    frame.pack(fill="both", expand=True)

    label = ttk.Label(frame, text=text, justify="left")
    label.pack(fill="both", expand=True)

    btn = ttk.Button(frame, text="OK", command=root.destroy)
    btn.pack(pady=(10, 0))

    root.mainloop()


def show_keybinds():
    # Run Tk in its own thread so it doesn't fight pystray
    threading.Thread(target=_show, daemon=True).start()
