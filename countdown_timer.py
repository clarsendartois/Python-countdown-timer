import tkinter as tk
import customtkinter as ctk
import time
from playsound import playsound

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

font_style_clock = ("ds-digital", 180)
font_style_text1_3 = ("Bookman Old Style", 60, "bold")
font_style_text2_4 = ("Bookman Old Style", 30)
font_style_timer = ("ds-digital", 80)
font_style_set_timer = ("Bookman Old Style", 25, "bold")


fg_color_clock = "#000000"
bg_fg_color = "#2b2b2b"
clock_color = "#00FF00"
timer_color = "#f97583"
text1_3_color = "#FFFFFF"
text2_4_color = "#a9a9a9"

text_text1 = "You don't have any timers"
text_text2 = 'Please, select "+" below to add a new timer.'
text_text3 = "Set your timer (24 hours)."
text_text4 = 'After, select "Set Timer!".'


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
        self.frame_display_default = self.create_frame_display_default()
        self.label_default = self.create_label_default()

        # self.hrs = tk.StringVar()
        # self.mins = tk.StringVar()
        # self.sec = tk.StringVar()

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

    def create_frame_display_default(self):
        frame_display_default = ctk.CTkFrame(self.main_frame, width=580,
                                             height=200, corner_radius=10, bg_color=bg_fg_color, fg_color=fg_color_clock)
        frame_display_default.place(relx=0.5, rely=0.5, x=-290, y=-30)
        return frame_display_default

    def create_label_default(self):
        photo1 = tk.PhotoImage(file=".\img\\timer.png")
        button = ctk.CTkButton(self.frame_display_default, text="",
                               image=photo1, border_width=0, width=10, bg_color=fg_color_clock, fg_color=fg_color_clock)
        button.place(relx=0.5, rely=0.5, x=-40, y=-95)

        text1 = tk.Label(self.frame_display_default, text=text_text1, font=font_style_text1_3,
                         background=fg_color_clock, foreground=text1_3_color)
        text1.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        text2 = tk.Label(self.frame_display_default, text=text_text2, font=font_style_text2_4,
                         background=fg_color_clock, foreground=text1_3_color)
        text2.place(relx=0.5, rely=0.5, x=-430, y=50)

        photo2 = tk.PhotoImage(file=".\img\\add.png")
        button = ctk.CTkButton(self.frame_display_default, text="", image=photo2, border_width=0, width=10,
                               bg_color=fg_color_clock, fg_color=fg_color_clock, command=self.create_timer)
        button.place(relx=0.5, rely=0.5, x=-20, y=55)

    def create_timer(self):
        global hrs, mins, sec
        frame_display_alarm = ctk.CTkFrame(self.main_frame, width=580,
                                           height=200, corner_radius=10, bg_color=bg_fg_color, fg_color=fg_color_clock)
        frame_display_alarm.place(relx=0.5, rely=0.5, x=-290, y=-30)

        text3 = tk.Label(self.main_frame, text=text_text3, font=font_style_text1_3,
                         background=fg_color_clock, foreground=text1_3_color)
        text3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        text4 = tk.Label(self.main_frame, text=text_text4, font=font_style_text2_4,
                         background=fg_color_clock, foreground=text2_4_color)
        text4.place(relx=0.5, rely=0.5, x=-220, y=50)

        text5 = tk.Label(self.main_frame, text=":", font=font_style_timer,
                         background=fg_color_clock, foreground=timer_color)
        text5.place(relx=0.5, rely=0.5, x=-400, y=120)

        text6 = tk.Label(self.main_frame, text=":", font=font_style_timer,
                         background=fg_color_clock, foreground=timer_color)
        text6.place(relx=0.5, rely=0.5, x=-200, y=120)

        hrs = tk.StringVar()
        hrs = tk.Entry(self.main_frame, width=2, font=font_style_timer,
                       foreground=timer_color, borderwidth=10)
        hrs.place(relx=0.5, rely=0.5, x=-550, y=120)

        mins = tk.StringVar()
        mins = tk.Entry(self.main_frame, width=2, font=font_style_timer,
                        foreground=timer_color, borderwidth=10)
        mins.place(relx=0.5, rely=0.5, x=-350, y=120)

        sec = tk.StringVar()
        sec = tk.Entry(self.main_frame, width=2, font=font_style_timer,
                       foreground=timer_color, borderwidth=10)
        sec.place(relx=0.5, rely=0.5, x=-150, y=120)

        button = ctk.CTkButton(self.main_frame, text="Set Timer!", font=font_style_set_timer,
                               text_color=timer_color, border_width=2, width=10)
        button.place(relx=0.5, rely=0.5, x=60, y=75)
        button.bind("<Button-1>", self.timer_begin)

        return frame_display_alarm

    # def create_timer(self):
    #     times = int(hrs.get())*3600 + int(mins.get())*60 + int(sec.get())
    #     while times > -1:
    #         minute, second = (times // 60, times % 60)

    #         hour = 0
    #         if minute > 60:

    #             hour, minute = (minute // 60, minute % 60)

    #         sec.set(second)
    #         mins.set(minute)
    #         hrs.set(hour)

    #         self.window.update()
    #         time.sleep(1)

    #         if (times == 0):
    #             playsound('./mp3/Loud_Alarm_Clock_Buzzer.mp3')
    #             sec.set('00')
    #             mins.set('00')
    #             hrs.set('00')
    #         times -= 1

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    countdown_timer = CountdownTimer()
    countdown_timer.run()
