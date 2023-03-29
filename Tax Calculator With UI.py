#Mason Williams
#11/21/2021
#This program creates a GUI for a tax calculator program


import tkinter
from tkinter import *

class TaxCalc:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("Tax Calculator")
        self.main_window.geometry("250x125")

        self.line1_frame = tkinter.Frame(self.main_window)
        self.line2_frame = tkinter.Frame(self.main_window)
        self.line3_frame = tkinter.Frame(self.main_window)
        self.line4_frame = tkinter.Frame(self.main_window)
        self.line5_frame = tkinter.Frame(self.main_window)

        self.prompt_label = tkinter.Label(self.line1_frame, text="Total Purchase: $")
        self.total_purchase = tkinter.Entry(self.line1_frame, width=10)

        self.prompt_label2 = tkinter.Label(self.line2_frame, text='Tax Rate: %')
        self.tax_rate = tkinter.Entry(self.line2_frame, width=10)

        self.tax_value = tkinter.StringVar()
        self.tax_label = tkinter.Label(self.line3_frame, text='Sales Tax: $')
        self.tax_result_label = tkinter.Label(self.line3_frame, textvariable=self.tax_value)
        self.tax_value.set('0.00')   #for some reason, this is not appearing

        self.total_value = tkinter.StringVar()
        self.total_label = tkinter.Label(self.line4_frame, text='Amount Due: $')
        self.total_result_label = tkinter.Label(self.line4_frame, textvariable=self.total_value)
        self.total_value.set('0.00')


        self.calc_button = tkinter.Button(self.line5_frame, text="Calculate", command=self.get_tax_message)
        self.quit_button = tkinter.Button(self.line5_frame, text='Quit', command=self.main_window.destroy)

        self.tax_value.set('')

        self.line1_frame.pack()
        self.line2_frame.pack()
        self.line3_frame.pack()
        self.line4_frame.pack()
        self.line5_frame.pack()
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='right')
        self.prompt_label.pack(side='left')
        self.total_purchase.pack(side='left')
        self.prompt_label2.pack(side='left')
        self.tax_rate.pack(side='left')
        self.tax_label.pack(side='left')
        self.tax_result_label.pack(side='right')
        self.total_label.pack(side='left')
        self.total_result_label.pack(side='right')


        tkinter.mainloop()



    def get_tax_message(self):
        try:
            purchase_amount = float(self.total_purchase.get())
            tax = (float(self.tax_rate.get()))/100
            tax_total = purchase_amount * tax
            total_amount = tax_total + purchase_amount
            self.tax_value.set(f'{tax_total:.2f}')
            self.total_value.set(f'{total_amount:.2f}')
        except ValueError:
            self.tax_value.set('Error')
            self.total_value.set('Error')






tax_calc = TaxCalc()
