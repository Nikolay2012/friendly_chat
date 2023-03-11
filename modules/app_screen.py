import customtkinter
# створюємо клас App 
class App(customtkinter.CTk):
    def __init__(self, app_width, app_height):
        super().__init__()
        # задаємо властивості, що зберігають розміри екрану додатку
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        # задаємо властивості, що зберігають розміри екрану комп'ютера
        self.PC_SCREEN_WIDTH = self.winfo_screenwidth()
        self.PC_SCREEN_HEIGHT = self.winfo_screenheight()
        # встановлюємо розмір додатку та його розташування на екрані комп'ютера
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        # задаємо назву вікну додатку
        self.title("Головне вікно додатку")
        self.resizable(False, False)
        self.MENU_FRAME = self.make_menu_frame()
        self.CHAT_FRAME = self.make_chat_frame()
        self.INPUT_FRAME = self.make_input_frame()
        self.DATA_FRAME = self.make_data_frame()

    def make_menu_frame(self):
        frame = customtkinter.CTkFrame(
            master= self, 
            width= 120,
            height= self.APP_HEIGHT - 20,
            # fg_color = "lightgray",
            border_width = 3,
            border_color = "lightblue",
            corner_radius = 10
        )
        frame.grid(row = 0, column= 0, padx= 5, pady = 10)
        return frame
    
    def make_chat_frame(self):
        frame = customtkinter.CTkFrame(
            master= self,
            width= 150,
            height= self.APP_HEIGHT - 20,
            border_width = 3,
            border_color = "lightblue",
            corner_radius = 10
        )
        frame.grid(row = 0, column= 1, padx= 0, pady = 10)
        return frame
    
    def make_input_frame(self):
        frame = customtkinter.CTkFrame(
            master= self,
            width= self.APP_WIDTH - self.MENU_FRAME._current_width - self.CHAT_FRAME._current_width - 20,
            height= 100,
            border_width = 3,
            border_color = "lightblue",
            corner_radius = 10
        )
        frame.grid(row = 0, column= 2, padx= 5, pady = 10, sticky = customtkinter.S)
        return frame
    
    def make_data_frame(self):
        frame = customtkinter.CTkFrame(
            master= self,
            width= self.APP_WIDTH - self.MENU_FRAME._current_width - self.CHAT_FRAME._current_width - 20,
            height= 570,
            border_width = 3,
            border_color = "lightblue",
            corner_radius = 10
        )
        frame.grid(row = 0, column= 2, padx= 5, pady = 10, sticky = customtkinter.N)
        return frame

# створюємо об'єкт від класу App
app = App(app_width= 800, app_height = 700)
