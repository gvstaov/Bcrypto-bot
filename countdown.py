import time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import winsound

def countdown(t):
    while t >= 0 and timer_running.get():
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timer)
        root.update()
        time.sleep(1)
        t -= 1

    if timer_running.get() and t == -1:
        messagebox.showinfo("Timer", "Timer completed!")
        play_sound()

def play_sound():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)

def timer_function():
    t = int(time_entry.get())
    timer_running.set(True)
    countdown(t)
    timer_running.set(False)

def update_stopwatch(start_time, target_time):
    if stopwatch_running.get():
        elapsed_time = int(time.time() - start_time)
        mins, secs = divmod(elapsed_time, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        time_label.config(text=timer)
        root.update()

        if elapsed_time >= target_time:
            messagebox.showinfo("Stopwatch", "Stopwatch completed!")
            play_sound()
            stopwatch_running.set(False)
        else:
            root.after(1000, update_stopwatch, start_time, target_time)

def start_stopwatch():
    t = int(time_entry.get())
    start_time = time.time()
    stopwatch_running.set(True)
    update_stopwatch(start_time, t)

def stop_stopwatch():
    stopwatch_running.set(False)

def reset_timer():
    time_label.config(text="00:00")
    timer_running.set(False)

def save_records():
    filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if filename:
        with open(filename, "w") as file:
            file.write(time_label.cget("text") + "\n")

root = tk.Tk()
root.title("Timer and Stopwatch")

stopwatch_running = tk.BooleanVar()
stopwatch_running.set(False)

timer_running = tk.BooleanVar()
timer_running.set(False)

time_label = tk.Label(root, text="00:00", font=("Helvetica", 48))
time_label.pack(pady=20)

time_entry = tk.Entry(root, font=("Helvetica", 24))
time_entry.pack(pady=10)
time_entry.insert(0, "60")

timer_button = tk.Button(root, text="Start Timer", font=("Helvetica", 14), command=timer_function)
timer_button.pack(pady=10)

stopwatch_button = tk.Button(root, text="Start Stopwatch", font=("Helvetica", 14), command=start_stopwatch)
stopwatch_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Stopwatch", font=("Helvetica", 14), command=stop_stopwatch)
stop_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset", font=("Helvetica", 14), command=reset_timer)
reset_button.pack(pady=10)

save_button = tk.Button(root, text="Save Records", font=("Helvetica", 14), command=save_records)
save_button.pack(pady=10)

root.mainloop()
