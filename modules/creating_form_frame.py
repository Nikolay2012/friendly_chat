import customtkinter
import modules.app_screen as m_app

name_font = customtkinter.CTkFont(family = "TimesNewRoman", size = 25, weight= "bold" )
text_font = customtkinter.CTkFont(family = "Arial", size = 12)

class Message_Frame(customtkinter.CTkFrame):
    def __init__(self, width, height, master, border_width, fg_color, bg_color, border_color, **kwargs):
        customtkinter.CTkFrame.__init__(self, master = master, border_width = border_width, fg_color = fg_color, bg_color = bg_color, width = width, height = height, border_color = border_color, **kwargs)

        self.NAME_LABEL = self.message_name_label("Ринат", "black", "transparent")
        self.TEXT_LABEL = self.message_text_label("Танцует лучше всех", "black", "transparent")
        self.NAME_LABEL.place(x = 7, y = 7 )
        self.TEXT_LABEL.place(x = 7, y = 50)

    def message_name_label(self, text, text_color, fg_color):
        return customtkinter.CTkLabel(
            master = self,
            text = text,
            font = name_font,
            text_color = text_color,
            fg_color = fg_color,
            bg_color = "transparent"    
        ) 
    def message_text_label(self, text, text_color, fg_color):
        return customtkinter.CTkLabel(
            master = self,
            text = text,
            font = text_font,
            text_color = text_color,
            fg_color = fg_color,
            bg_color = "transparent"
        )
    
message_first_user = Message_Frame(
    width = 250,
    height = 100,
    master = m_app.app.DATA_FRAME,
    border_width = 2,
    fg_color = "Moccasin",
    bg_color = "transparent",
    border_color = "orange"
)
message_first_user.place(x = 10, y = 10, anchor = customtkinter.NW)

message_second_user = Message_Frame(
    width = 250,
    height = 100,
    master = m_app.app.DATA_FRAME,
    border_width = 2,
    fg_color = "Khaki",
    bg_color = "transparent",
    border_color = "orange"
)
message_second_user.place(x = m_app.app.DATA_FRAME._current_width - 10, y = 120, anchor = customtkinter.NE)