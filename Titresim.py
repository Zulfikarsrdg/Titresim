import tkinter as tk
import ctypes
import os

def vibrate_device(duration):
    if os.name == 'nt':  #Windows
        ctypes.windll.kernel32.Beep(1000, int(duration * 1000))
    elif os.name == 'posix':  #Linux
        os.system(f"xdotool keydown XF86Launch1; sleep {duration}; xdotool keyup XF86Launch1")
    elif os.name == 'darwin':  # MacOS
        os.system(f"osascript -e 'tell application \"System Events\" to key code 20'")

def start_vibration():
    duration = float(entry.get())
    vibrate_device(duration)

root = tk.Tk()
root.title("Cihaz Titreşimi")
root.geometry("300x150")

label = tk.Label(root, text="Titreşim Süresi (saniye):")
label.pack(pady=10)

entry = tk.Entry(root, width=10)
entry.pack()

button = tk.Button(root, text="Titret", command=start_vibration)
button.pack(pady=10)

root.mainloop()
