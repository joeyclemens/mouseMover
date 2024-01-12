import tkinter as tk
import time
import pyautogui
import ctypes

root = tk.Tk()
root.title("Mouse Mover")
root.iconbitmap('mouse_icon.ico')
root.geometry("300x200")

count = 0
interval = 30
is_running = False

status = tk.Label(text="Stopped", fg="red")
status.pack()

label = tk.Label(text="Interval (seconds)")
label.pack()

entry = tk.Entry(width=20)
entry.insert(0, "30")
entry.pack()

def start_moving():
    global is_running
    if not is_running:
        is_running = True
        status.config(text="Running...", fg="green")
        check_move_mouse()

def stop_moving():
    global is_running
    is_running = False
    status.config(text="Stopped", fg="red")
    toggle_num_lock()  # Turn on Num Lock when stopping

def toggle_num_lock():
    ctypes.windll.user32.keybd_event(0x90, 0, 0, 0)  # Press Num Lock key
    ctypes.windll.user32.keybd_event(0x90, 0, 2, 0)  # Release Num Lock key

def check_move_mouse():
    if is_running:
        global count
        global interval

        interval = int(entry.get())
        x, y = pyautogui.position()

        pyautogui.move(-10, 0)
        count += 1
        print(f"Moved: {count} times")

        toggle_num_lock()

        pyautogui.moveTo(x, y)
        root.after(interval * 1000, check_move_mouse)

# Call check_move_mouse once to make it work initially
check_move_mouse()

start_btn = tk.Button(text="Start", command=start_moving)
start_btn.pack()

stop_btn = tk.Button(text="Stop", command=stop_moving)
stop_btn.pack()

root.mainloop()
