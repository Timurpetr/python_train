import customtkinter as ctk

ctk.set_default_color_theme("blue")
ctk.set_appearance_mode("dark")


app = ctk.CTk()
app.title("Modal Window")
app.geometry("480x300")

label = ctk.CTkLabel(app, text="Greetings", font=("Arial", 18, "bold"))
label.pack(pady=20)

app.mainloop()
