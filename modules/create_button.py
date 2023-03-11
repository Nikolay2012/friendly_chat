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
        
button = My_Button(text= "Chat", master= m_app.app.MENU_FRAME)
button2 = My_Button(text="Contacts", master= m_app.app.MENU_FRAME)
button3 = My_Button(text= "Settings", master= m_app.app.MENU_FRAME)

button_y = button.HEIGHT // 2 + 10
button.place(x= m_app.app.MENU_FRAME._current_width // 2, y = button_y, anchor= ctk.CENTER)
button2.place(x= m_app.app.MENU_FRAME._current_width // 2, y = button_y + button.HEIGHT + 5, anchor = ctk.CENTER)
button3.place(x= m_app.app.MENU_FRAME._current_width // 2, y = button_y + 10 + button.HEIGHT * 2, anchor= ctk.CENTER)