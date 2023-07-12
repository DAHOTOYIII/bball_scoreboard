import customtkinter as ctk
import toml

from scoreboard import ScoreBoard

#Setting appearance of the GUI
ctk.set_default_color_theme("pc_scoreboard/ctk-theme/custom_theme.json")


if __name__ == "__main__":
    app = ScoreBoard()
    app.mainloop