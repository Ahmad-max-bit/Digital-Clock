import tkinter as tk
from time import strftime

# Main Window

root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x250")
root.resizable(False, False)
root.configure(bg="#0f172a")

clock_frame = tk.Frame(  # Clock Frame
    root, bg="#1e293b", bd=0, highlightthickness=0
)
clock_frame.place(relx=0.5, rely=0.5, anchor="center", width=360, height=200)

title_label = tk.Label(  # Title
    clock_frame,
    text="DIGITAL CLOCK",
    font=("Segoe UI", 14, "bold"),
    bg="#1e293b",
    fg="#94a3b8",
)
title_label.pack(pady=(25, 5))

time_label = tk.Label(  # Time
    clock_frame, font=("Consolas", 58, "bold"), bg="#1e293b", fg="#38bdf8"
)
time_label.pack()  # AM / PM + Date

info_label = tk.Label(clock_frame, font=("Segoe UI", 16), bg="#1e293b", fg="#cbd5e1")
info_label.pack(pady=(5, 20))


def update_clock():
    current_time = strftime("%H:%M:%S")
    current_date = strftime("%A, %d %B %Y")
    period = strftime("%p")
    time_label.config(text=current_time)
    info_label.config(text=f"{period}   •   {current_date}")

    root.after(1000, update_clock)


update_clock()  # Start clock

root.mainloop()  # Run application
