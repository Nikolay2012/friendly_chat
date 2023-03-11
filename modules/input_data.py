import customtkinter as ctk
import modules.app_screen as m_app
import modules.create_font as m_font

input_width = 410
input_height = 50

text = ctk.StringVar()

input_data = ctk.CTkEntry(
    master= m_app.app.INPUT_FRAME, 
    width= input_width,
    height= input_height,
    fg_color= "white",
    border_width= 3,
    border_color= "orange",
    text_color= "black",
    font= m_font.font_size,
    textvariable= text
)
input_data.place(x = m_app.app.INPUT_FRAME._current_width // 2 - 35, y = m_app.app.INPUT_FRAME._current_height // 2, anchor = ctk.CENTER)

