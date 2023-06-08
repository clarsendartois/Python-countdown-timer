import tkinter as tk
import customtkinter as ctk
import time
from playsound import playsound

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_clock = ("ds-digital", 180)


fg_color_clock = "#000000"
bg_fg_color = "#2b2b2b"
clock_color = "#00FF00"


class CountdownTimer:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.geometry("600x360+0+0")
        self.window.resizable(0, 0)
        self.window.iconbitmap("./img/countdown_icon.ico")
        self.window.title("CLARSEN: Countdown Timer")

        self.main_frame = self.create_main_frame()
        self.frame_clock = self.create_frame_clock()
        self.label_clock = self.create_label_clock()
        self.time = self.create_time()

    def create_main_frame(self):
        main_frame = ctk.CTkFrame(
            self.window, width=590, height=350, corner_radius=10, fg_color=bg_fg_color)
        main_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_frame_clock(self):
        frame_clock = ctk.CTkFrame(self.main_frame, width=580,
                                   height=130, corner_radius=10, bg_color=bg_fg_color, fg_color=fg_color_clock)
        frame_clock.place(relx=0.5, rely=0.5, x=-290, y=-170)
        return frame_clock

    def create_label_clock(self):
        global clock
        clock = tk.Label(self.frame_clock, font=font_style_clock,
                         background=fg_color_clock, foreground=clock_color)
        clock.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    def create_time(self):
        string = time.strftime("%H:%M:%S %p")
        clock.configure(text=string)
        clock.after(1000, self.create_time)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    countdown_timer = CountdownTimer()
    countdown_timer.run()
