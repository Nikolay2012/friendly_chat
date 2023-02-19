import customtkinter as ctk
import modules.app_screen as m_app
import tkinter

class My_Button(ctk.CTkButton):
    def __init__(self, text, master, width = 100, height = 70, border_width = 5, corner_radius= 5, **kwargs):
        super().__init__(
            master = master, 
            width = width, 
            height = height, 
            border_width = border_width, 
            text = text,
            corner_radius = corner_radius, 
            **kwargs
        )
        self.WIDTH = width
        self.HEIGHT = height
        
button = My_Button(text= "Chat", master= m_app.app)
button2 = My_Button(text="Contacts", master= m_app.app)
button3 = My_Button(text= "Settings", master= m_app.app)

button.place(x= button.WIDTH // 2, y = button.HEIGHT // 2, anchor= ctk.CENTER)
button2.place(x= button.WIDTH // 2, y = button.HEIGHT // 2 + button.HEIGHT, anchor = ctk.CENTER)
button3.place(x= button.WIDTH // 2, y = button.HEIGHT // 2 + button.HEIGHT * 2, anchor= ctk.CENTER)