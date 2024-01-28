import tkinter as tk
from CommonWindows import BaseWindow, BaseSubWindow
from tkinter import messagebox
from db_api import Session, engine
from db_api import Product ,  Check
class ProductWindow(BaseSubWindow):



    def create_UI(self):
        self.titleUI = tk.Entry(self.root)
        self.priceUI = tk.Entry(self.root)
        self.barcodeUI = tk.Entry(self.root)
        self.countUI = tk.Entry(self.root)
        self.guarantee = tk.Entry(self.root)
        self.submit = tk.Button(self.root, text ='Підтвердити', command=self.submit_product)
        self.labelBarcode = tk.Label(self.root, text='Штрихкод')
        self.labelTitle = tk.Label(self.root, text='Назва')
        self.labelPrice = tk.Label(self.root, text='Ціна')
        self.selfLabelCount = tk.Label(self.root, text='Кількість')
        self.labelGuarantee = tk.Label(self.root, text='Гарантія')

    def __init__(self, parent)-> None:
          super().__init__(parent, 'Додати Товар')

   
    def setup_layout(self):
            self.labelTitle.grid(row=0, column=0)
            self.titleUI.grid(row=0, column=1)
            self.labelPrice.grid(row=1, column=0)
            self.priceUI.grid(row=1, column=1)
            self.labelBarcode.grid(row=2, column=0)
            self.barcodeUI.grid(row=2, column=1)
            self.selfLabelCount.grid(row=3, column=0)
            self.countUI.grid(row=3, column=1)
            self.labelGuarantee.grid(row=4, column=0)
            self.guarantee.grid(row=5, column=1)
            self.submit.grid(row=5, column=1, columnspan=2)
        

    def submit_product(self):
        count=0
        price=0
        guarantee = 0
        try:
          count = int(self.countUI.get())
          price = float(self.priceUI.get())
          guarantee = int(self.guarantee.get())
          if count <1 or price <=0 or guarantee <1: 
              raise ValueError()
        except ValueError:
            tk.messagebox.showwarning('Помилка','Кількість,ціна та гарантія мають бути цілим числом')
            return
        if self.barcodeUI.get() == '':
            tk.messagebox.showwarning('Помилка', 'Штрихкод не може бути пустим')
        if self.titleUI.get() == '':
              tk.messagebox.showwarning('Помилка', 'Назва не може бути пустою')     
        product = Product(title = self.titleUI.get(),
                          price=price,
                          barcode=self.barcodeUI.get(),
                          count=count,
                          guarantee=guarantee)
        with Session(engine) as session:
            session.add(product)
            session.commit()
            self.root.destroy()
            messagebox.showinfo('Успіх', 'Товар додано')

