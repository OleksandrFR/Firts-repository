from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import declarative_base
from datetime import datetime
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import Table
from sqlalchemy.orm import Mapped, relationship

import tkinter as tk
from tkinter import messagebox
Base = declarative_base()

associate_table = Table(
    "check_products",
    Base.metadata,
    Column("check_id", ForeignKey("Check.id")),
    Column("product_id", ForeignKey("product.id"))
)

class Check(Base):
    __tablename__='Check'
    id=Column(Integer, primary_key=True)
    time=Column(DateTime(), default=datetime.now)
    items = relationship('Product', secondary=associate_table)
    amount=Column(Integer, nullable=False)
class Product(Base):
    __tablename__='product'
    id=Column(Integer,primary_key=True)
    title=Column(String(100), nullable=False)
    price=Column(Integer, nullable=False)
    barcode=Column(String(100), nullable=False)
    count=Column(String, nullable=False)
    guarantee=Column(String, nullable=False)

engine = create_engine(r'sqlite:///C:\Users\student\Documents\Mitrjo\db.sqlite', echo=True)
Base.metadata.create_all(engine)
class ProductWindow:

    def __init__(self)-> None:
        self.root=tk.Tk()
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
       
        self.root.resizable(width=False, height=False)
        self.root.mainloop()


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


class CheckWindow:

    def __init__(self)-> None:
        self.root = tk.Tk()
        self.root.resizable(width=False, height=False)
        clicked=tk.StringVar()
        clicked.set('click me')
        l = self.fetch_products()
        l2 = [i.title for i in l]
        products=tk.OptionMenu(self.root, clicked, *l2)
        products.pack()
        self.root.mainloop()

    def fetch_products(self):
        with Session(engine) as session:
            resultProducts = session.execute(select(Product))
            
            return resultProducts.scalars().all()




class Window:
    root =tk.Tk()
    def __init__(self) -> None:

        self.button_open_create_product_dialog = tk.Button(text='Відкрити вікно створення товару', command=self.open_product_window)
        self.button_open_create_check_dialog = tk.Button(text='Відкрити вікно створення чеку', command=self.open_check_window)

        self.button_open_create_check_dialog.grid(row=0, column=0)
        self.button_open_create_product_dialog.grid(row=0, column=1)

        #self.root.geometry("800x500")


        self.root.resizable(width=False, height=False)
        self.root.mainloop()
    def open_product_window(self):
        p=ProductWindow()
    def open_check_window(self):
        cw = CheckWindow()
    






window = Window()