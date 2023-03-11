import customtkinter as ctk
import modules.app_screen as m_app
import modules.create_font as m_font
import modules.input_data as m_input

button_width = 70
button_height = 50 

def write_text():
    text_lable = ctk.CTkLabel(
        master= m_app.app,
        text = m_input.text.get(),
        width= 200,
        height= 50,
        font = m_font.font_size,
        text_color= "orange"
    )
    text_lable.place(x= m_app.app.APP_WIDTH // 2, y = m_app.app.APP_HEIGHT // 2, anchor = ctk.CENTER)
    m_input.input_data.delete(0, ctk.END)

button_input = ctk.CTkButton(
    master= m_app.app.INPUT_FRAME,
    width= button_width,
    height= button_height,
    fg_color= "darkorange",
    font= m_font.font_size,
    text= "->",
    command= write_text
)
button_input.place(
    x = m_app.app.INPUT_FRAME._current_width // 2 + m_input.input_width // 1.5 - 65, 
    y = m_app.app.INPUT_FRAME._current_height // 2, 
    anchor = ctk.CENTER
)