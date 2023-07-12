import customtkinter as ctk
import toml

from scoreboard import ScoreBoard


config = {}
#Getting configurations
with open('pc_scoreboard/settings.toml', 'r') as f:
    config = toml.load(f)
    
#Setting appearance of the GUI
ctk.set_default_color_theme(config['custom_theme']['path'])


if __name__ == "__main__":
    app = ScoreBoard()
    app.mainloop