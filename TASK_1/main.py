import tkinter as tk
from tkinter import ttk
from forex_python.converter import CurrencyRates

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        # Entry for amount
        amount_label = ttk.Label(root, text="Amount:")
        amount_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        amount_entry = ttk.Entry(root, textvariable=self.amount_var)
        amount_entry.grid(row=0, column=1, padx=10, pady=10)

        # Dropdown for "from" currency
        from_currency_label = ttk.Label(root, text="From Currency:")
        from_currency_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        from_currency_combobox = ttk.Combobox(root, textvariable=self.from_currency_var)
        from_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
        from_currency_combobox['values'] = self.get_currency_list()
        from_currency_combobox.set('USD')

        # Dropdown for "to" currency
        to_currency_label = ttk.Label(root, text="To Currency:")
        to_currency_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        to_currency_combobox = ttk.Combobox(root, textvariable=self.to_currency_var)
        to_currency_combobox.grid(row=2, column=1, padx=10, pady=10)
        to_currency_combobox['values'] = self.get_currency_list()
        to_currency_combobox.set('EUR')

        # Result label
        result_label = ttk.Label(root, text="Result:")
        result_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.result_var = tk.StringVar()
        result_entry = ttk.Entry(root, textvariable=self.result_var, state="readonly")
        result_entry.grid(row=3, column=1, padx=10, pady=10)

        # Convert button
        convert_button = ttk.Button(root, text="Convert", command=self.convert_currency)
        convert_button.grid(row=4, column=0, columnspan=2, pady=20)

    def get_currency_list(self):
        c = CurrencyRates()
        currencies = c.get_rates('USD')
        return list(currencies.keys())

    def convert_currency(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get()
        to_currency = self.to_currency_var.get()

        try:
            c = CurrencyRates()
            rate = c.get_rate(from_currency, to_currency)
            result = round(amount * rate, 2)
            self.result_var.set(f"{amount} {from_currency} = {result} {to_currency}")
        except Exception as e:
            self.result_var.set("Error: " + str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
