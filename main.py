import customtkinter as ctk

from labels.text import create_labels


window = ctk.CTk()

window.geometry("800x600")

window.title("The Filther")

create_labels(window)

window.mainloop()

