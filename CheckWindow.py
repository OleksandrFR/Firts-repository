from db_api import Session, engine
from tkinter import messagebox
import tkinter as tk
from sqlalchemy import select
from db_api import Product ,  Check
from CommonWindows import BaseWindow, BaseSubWindow
class CheckWindow(BaseSubWindow):

    def __init__(self, parent)-> None:
      super().__init__(parent, 'Створити Чек')

    def setup_window(self):
        self.fill_product_list()
        self.selected=list()
        self.totalAmount=0

    def fetch_products(self):
        with Session(engine) as session:
            resultProducts = session.execute(select(Product))
            
            return resultProducts.scalars().all()
    def submit_check(self):
        if not self.totalAmount is None and not self.totalAmount==0:
         with Session(engine) as session:
            check = Check(amount=self.totalAmount, items=self.selected)
            session.add(check)
            session.commit()
            self.destroy_window()
            messagebox.showinfo('Успіхів', 'Чек Створено')
        else:
            messagebox.showwarning('Помилка', 'Чек не може бути пустим')
    def create_ui(self):
         self.selected_products = tk.Listbox(self.root)
         self.labelProduct = tk.Label(self.root, text='Виберіть Товар')
         self.labelAmount = tk.Label(self.root, text='Сума чека')
         self.amountEntry = tk.Label(self.root)
         self.buttonSubmit = tk.Button(self.root, text='Створити', command=self.submit_check)
         self.products=tk.Listbox(self.root)
         self.button_add_product_to_cart = tk.Button(self.root, text='Додати товар', command=self.add_product_to_cart)
         self.button_remove_from_cart=tk.Button(self.root, text='Видалити Товар', command=self.remove_from_cart)
         
    def setup_layout(self):
         self.buttonSubmit.grid(row=3, column=0, columnspan=2)
         self.labelProduct.grid(row=0, column=0)
         self.products.grid(row=0, column=1, rowspan=2)
         self.labelAmount.grid(row=2, column=0)
         self.amountEntry.grid(row=2, column=1)
         self.selected_products.grid(row=0, column=2, rowspan=3)
         self.button_add_product_to_cart.grid(row=1, column=0)
         self.button_remove_from_cart.grid(row=2, column=2)
    def fill_product_list(self):
         self.l = self.fetch_products()
         for i in range(len(self.l)):
            self.products.insert(i, self.l[i].title)
    def add_product_to_cart(self):
        l = self.products.curselection()
        for i in l:
            self.selected.append(self.l[i])
            self.update_cart_view()
            

    def update_cart_view(self):
        self.totalAmount=0
        self.selected_products.delete(0, tk.END)
        for i in range(len(self.selected)):
            self.selected_products.insert(i, self.selected[i].title)
            self.totalAmount+=self.selected[i].price
            
        self.amountEntry.config(text=self.totalAmount)

    def remove_from_cart(self):
        for i in self.selected_products.curselection():
            del self.selected[i]
            self.update_cart_view()