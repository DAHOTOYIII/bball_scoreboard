from typing import Optional, Tuple, Union
import customtkinter as ctk
from tkinter import messagebox
import tkinter as tk
import time
import toml


config = {}
#Getting configurations
with open('settings.toml', 'r') as f:
    config = toml.load(f)


#Setting appearance of the GUI
ctk.set_appearance_mode("Dark")  
ctk.set_default_color_theme("blue")

appWidth, appHeight = 600, 700

#timer variables
#TODO create a GUI that can modify these values dynamically
minutes = config['timer']['minutes']
seconds = config['timer']['seconds']

#Scoreboar App GUI declarations and Grid Layout
class ScoreBoard(ctk.CTk):
    def __init__(self, fg_color: str | Tuple[str, str] | None = None, **kwargs):
        super().__init__(fg_color, **kwargs)
        
        #Windows Form Dimensions
        self.geometry("1920x1080")
        self.grid_columnconfigure((0, 3), weight=1)
        
        #Timer Label
        self.sbtitle = ctk.CTkLabel(self,
                                text="SCOREBOARD TIMER", 
                                font=("Helvetica", 32))
        self.sbtitle.grid(row=0, 
                          column=1, 
                          padx=20, 
                          pady=20, 
                          sticky="ew", 
                          columnspan=2)
        
        #Timer variables
        self.scoreboard_frame = ctk.CTkFrame(self)
        self.scoreboard_frame.grid(row=1, 
                                   column=2, 
                                   padx=10, 
                                   pady=(10, 0),
                                   sticky="ew")
        self.total_seconds = minutes * 60 + seconds
        self.paused = False
        
        
        self.teamonename_frame = ctk.CTkFrame(self)
        self.teamonename_frame.grid(row=1, 
                                   column=0, 
                                   padx=10, 
                                   pady=(10, 0))
        
        self.firstteam = ctk.CTkLabel(self.teamonename_frame,
                                text="Wolfpack", 
                                font=("Arial Black", 84),
                                text_color = ("#ffffff"))
        self.firstteam.grid(row=1, 
                          column=0, 
                          padx=40, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=1)
        
        self.timerLabel = ctk.CTkLabel(self.scoreboard_frame,
                                text="12:00", 
                                font=("Bahnschrift SemiCondensed", 150),
                                text_color = ("#d6494f"))
        self.timerLabel.grid(row=1, 
                          column=1, 
                          padx=40, 
                          pady=20, 
                          sticky="ew", 
                          columnspan=1)
        
        
        self.teamonetwo_frame = ctk.CTkFrame(self)
        self.teamonetwo_frame.grid(row=1, 
                                   column=3, 
                                   padx=10, 
                                   pady=(10, 0))
        self.secondteam = ctk.CTkLabel(self.teamonetwo_frame,
                                text="BallDogs", 
                                font=("Arial Black", 84),
                                text_color = ("#ffffff"))
        self.secondteam.grid(row=1, 
                          column=3, 
                          padx=40, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=1)
        
        self.scorefirst_frame = ctk.CTkFrame(self)
        self.scorefirst_frame.grid(row=2, column=3, padx=10, pady=(10, 0),
                                 sticky="")
        self.firstteamscore = ctk.CTkLabel(self.scorefirst_frame,
                                text="24", 
                                font=("Arial Black", 300),
                                text_color = ("#ffa743"))
        self.firstteamscore.grid(row=2, 
                          column=0, 
                          padx=40, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=1)
        
        
        self.sbtitle = ctk.CTkLabel(self,
                                text="→", 
                                text_color = ("#1466ff"),
                                font=("Helvetica", 230))
        self.sbtitle.grid(row=2, 
                          column=1, 
                          padx=20, 
                          pady=20, 
                          sticky="ew", 
                          columnspan=2)
        
        self.scoresecond_frame = ctk.CTkFrame(self)
        self.scoresecond_frame.grid(row=2, column=0, padx=10, pady=(10, 0),
                                 sticky="")
        
        self.secondteamscore = ctk.CTkLabel(self.scoresecond_frame,
                                text="50", 
                                font=("Arial Black", 300),
                                text_color = ("#ffa743"))
        self.secondteamscore.grid(row=2, 
                          column=3, 
                          padx=40, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=1)
        
        self.sbtitle = ctk.CTkLabel(self,
                                text="PERIOD", 
                                font=("Helvetica", 32))
        self.sbtitle.grid(row=4, 
                          column=1, 
                          padx=20, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=2)
        
        self.sbtitle = ctk.CTkLabel(self,
                                text="3", 
                                font=("Arial Black", 100),
                                text_color = ("#ffa743"))
        self.sbtitle.grid(row=5, 
                          column=1, 
                          padx=20, 
                          pady=10, 
                          sticky="nsew", 
                          columnspan=2)
        
        self.sbtitle = ctk.CTkLabel(self,
                                text="FOULS", 
                                font=("Helvetica", 32))
        self.sbtitle.grid(row=4, 
                          column=0, 
                          padx=20, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=1)
        
        self.sbtitle = ctk.CTkLabel(self,
                                text="4", 
                                font=("Helvetica", 85))
        self.sbtitle.grid(row=5, 
                          column=0, 
                          padx=20, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=1)
        self.sbtitle = ctk.CTkLabel(self,
                                text="FOULS", 
                                font=("Helvetica", 32))
        self.sbtitle.grid(row=4, 
                          column=3, 
                          padx=20, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=2)
        
        
        self.sbtitle = ctk.CTkLabel(self,
                                text="4", 
                                font=("Helvetica", 85))
        self.sbtitle.grid(row=5, 
                          column=3, 
                          padx=20, 
                          pady=20, 
                          sticky="nsew", 
                          columnspan=2)
        self.paused = True
        self.update_timer()
        self.mainloop()

    def update_timer(self):
        mins, secs = divmod(self.total_seconds, 60)
        timer_text = f"{mins:02d}:{secs:02d}"
        self.timerLabel.configure(text=timer_text)

        if self.total_seconds > 0 and not self.paused:
            self.total_seconds -= 1
            self.after(1000, self.update_timer)
        elif self.total_seconds == 0:
            messagebox.showinfo("Countdown Timer", "Time's up!")

    def start_timer(self):
        self.paused = False
        self.start_button.configure(state=ctk.DISABLED)
        self.pause_button.configure(state=ctk.NORMAL)
        self.reset_button.configure(state=ctk.NORMAL)

    def pause_timer(self):
        self.paused = True
        self.start_button.configure(state=ctk.NORMAL)
        self.pause_button.configure(state=ctk.DISABLED)

    def reset_timer(self):
        self.total_seconds = 0
        self.start_button.configure(state=ctk.NORMAL)
        self.pause_button.configure(state=ctk.DISABLED)
        self.reset_button.configure(state=ctk.DISABLED)
        self.update_timer()
       
 
 
 
 #utilities
def countdown_timer(minutes, seconds):
    total_seconds = minutes * 60 + seconds

    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        print(f"Time remaining: {mins:02d}:{secs:02d}")
        time.sleep(1)  # Pause for 1 second
        total_seconds -= 1
    print("Time's up!")       


if __name__ == "__main__":
    app = ScoreBoard()
    app.mainloop()