import tkinter as tk
from CheckWindow import CheckWindow
from PlotsWindow import PlotsWindow
from PoductWindow import ProductWindow
class Window:
    root =tk.Tk()
    def create_ui(self):
        self.button_open_create_product_dialog = tk.Button(text='Відкрити вікно створення товара', command=self.open_product_window)
        self.button_open_plots = tk.Button(text='Відкрити вікно графіків',command=self.open_plots_window)
        
        self.button_open_create_product_dialog = tk.Button(text='Відкрити вікно створення товару', command=self.open_product_window)
        self.button_open_create_check_dialog = tk.Button(text='Відкрити вікно створення чеку', command=self.open_check_window)

    def __init__(self) -> None:
        super().__init__()
       
    
   
        

        #self.root.geometry("800x500")
     
        self.root.mainloop()
    def __init__(self) ->None:
        super().__init__()
        self.create_ui()
        self.setup_layout()
        self.root.mainloop()

    def open_product_window(self):
        p=ProductWindow(self.root)
    def open_check_window(self):
        cw = CheckWindow(self.root)


    def  open_plots_window(self):
        pw = PlotsWindow(self.root)
    
    def setup_layout(self):
        self.button_open_create_check_dialog.grid(row=0, column=0)
        self.button_open_create_product_dialog.grid(row=0, column=1)
        self.root.resizable(width=False, height=False)
        self.button_open_plots.grid(row= 1, column= 0)



window = Window()