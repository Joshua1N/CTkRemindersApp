from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = customtkinter.CTk()
app.geometry("900x750")
app.title("Reminders")


class RemindersApp:
    def __init__(self):
        self.active = False
        self.font1 = "Helvetica 92"
        self.font2 = "Helvetica 48"
        self.font3 = "Helvetica 32"
        self.font4 = "Helvetica 22"
        self.font5 = "Helvetica 16"

        self.dark = "#212325"
        self.light_dark = "#2a2d2e"
        self.white = "#FFFFFF"
        self.blue = "#226da5"

        self.widgets()

        self.i = -1

    def widgets(self):
        self.main_frame = customtkinter.CTkFrame(master=app, width=880, height=730)
        self.main_frame.pack(fill="both", expand=True)
        self.button = customtkinter.CTkButton(master=app, text="Add Item", text_color=self.white,
                                              text_font=self.font5, width=200, height=50, command=self.add_item)
        self.button.place(relx=0.5, rely=0.92, anchor="center")

    def add_item(self):
        self.input = input("...")
        self.i += 1
        self.t = self.i
        self.item_frame = customtkinter.CTkFrame(self.main_frame, width=850, height=100)
        self.item_frame.pack(pady=10, anchor="center")

        self.label = customtkinter.CTkLabel(self.item_frame, text=self.input,
                                            text_font=self.font4)
        self.label.place(relx=0.4, rely=0.5, anchor="center")

        self.radio = customtkinter.CTkRadioButton(self.item_frame, text=f"{self.i}", width=50, height=50,
                                                  command=self.remove_item)
        self.radio.place(relx=0.9, rely=0.5, anchor="center")

    def remove_item(self):
        print(self.radio.winfo_parent())
        self.main_frame.winfo_children()[self.i].destroy()
        print(f"destroyed frame {self.i}")
        self.i -= 1


RemindersApp()
app.mainloop()
