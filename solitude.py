import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
import time
import os

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.past_seconds = 0
        self.timespan = 0
        self["bg"] = '#242424'
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        font = tkFont.Font(family="monospace", size=22)
        
        self.set_time_label = tk.Label(self)
        self.set_time_label["text"] = "Timespan (min):"
        self.set_time_label["font"] = font
        self.set_time_label["bg"] = '#242424'
        self.set_time_label["fg"] = '#2a94b7'
        self.set_time_label.pack(pady=5)

        self.set_time_entry = tk.Entry(self)
        self.set_time_entry["font"] = font
        self.set_time_entry["bg"] = '#f4f4f4'
        self.set_time_entry["fg"] = '#2a94b7'
        self.set_time_entry.pack(padx=10, pady=10)

        self.set_time_btn = tk.Button(self)
        self.set_time_btn["font"] = font
        self.set_time_btn["command"] = self.start_timer
        self.set_time_btn["text"] = "Start"
        self.set_time_btn["width"] = 15
        self.set_time_btn["fg"] = '#2a94b7'
        self.set_time_btn["bg"] = '#242424'
        self.set_time_btn.pack(pady=10)

        self.timer = tk.Label(self)
        self.timer["text"] = "00:00"
        self.timer["font"] = font
        self.timer["bg"] = '#242424'
        self.timer['fg'] = '#2a94b7'
        self.timer.pack(pady=5)

    def start_timer(self):
        try:
            timespan = int(self.set_time_entry.get())
            if timespan > 0:
                print("Fire")
                os.system('netsh interface set interface "Wi-Fi" DISABLED')
                self.clear_timer()
                self.timespan = timespan
                self.master.after(1000, self.run_timer)
        except:
            self.clear_timer()
    
    def run_timer(self):
        if self.past_seconds <= (self.timespan*60):
            self.show_timer()
            self.past_seconds += 1
            self.master.after(1000, self.run_timer)
        else: 
            print("Acabou")
            os.system('netsh interface set interface "Wi-Fi" ENABLED')
            messagebox.showinfo("Timeout!", "Time is over!")

    def show_timer(self):
        sec_left = (self.timespan * 60) - self.past_seconds
        min_left = sec_left//60

        time = "{}:{}".format( self.format_time(min_left), self.format_time((sec_left - (min_left*60))) )
        self.timer["text"] = time

    def clear_timer(self):
        self.past_seconds = 0
        self.timespan = 0
        self.timer["text"] = "00:00"
    
    def format_time(self, t):
        t = str(t)
        if len(t) == 1:
            return "0{}".format(t)
        return t

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Solitude")
    app = App(master=root)
    app.mainloop()