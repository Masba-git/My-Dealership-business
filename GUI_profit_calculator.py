import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Define product details
products = {
    "B.Coffee": {"buying_price": 360},
    "B.Red": {"buying_price": 240},
    "C.Milk": {"buying_price": 330},
    "C.Red": {"buying_price": 230},
    "C.Coffee": {"buying_price": 350},
}

class ProfitCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profit Calculator")
        self.total_profit = 0

        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        title_label = tk.Label(self.root, text="Profit Calculator", font=("Arial", 16))
        title_label.grid(row=0, column=0, columnspan=2, pady=10)

        # Product Dropdown
        tk.Label(self.root, text="Select Product:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.product_var = tk.StringVar()
        self.product_dropdown = ttk.Combobox(
            self.root, textvariable=self.product_var, values=list(products.keys()), state="readonly"
        )
        self.product_dropdown.grid(row=1, column=1, padx=10, pady=5)

        # Quantity Entry
        tk.Label(self.root, text="Quantity:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.quantity_entry = tk.Entry(self.root)
        self.quantity_entry.grid(row=2, column=1, padx=10, pady=5)

        # Selling Price Entry
        tk.Label(self.root, text="Selling Price:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.selling_price_entry = tk.Entry(self.root)
        self.selling_price_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add Button
        add_button = tk.Button(self.root, text="Add Product", command=self.add_product)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Profit Display
        self.profit_label = tk.Label(self.root, text="Total Profit: 0.00", font=("Arial", 14))
        self.profit_label.grid(row=5, column=0, columnspan=2, pady=10)

    def add_product(self):
        # Get user input
        product_name = self.product_var.get()
        quantity = self.quantity_entry.get()
        selling_price = self.selling_price_entry.get()

        # Validate input
        if not product_name:
            messagebox.showerror("Input Error", "Please select a product.")
            return
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Input Error", "Please enter a valid positive quantity.")
            return
        if not selling_price.replace('.', '', 1).isdigit() or float(selling_price) <= 0:
            messagebox.showerror("Input Error", "Please enter a valid positive selling price.")
            return

        # Calculate profit
        quantity = int(quantity)
        selling_price = float(selling_price)
        buying_price = products[product_name]["buying_price"]
        profit = (selling_price - buying_price) * quantity
        self.total_profit += profit

        # Update profit display
        self.profit_label.config(text=f"Total Profit: {self.total_profit:.2f}")

        # Reset inputs
        self.product_var.set("")
        self.quantity_entry.delete(0, tk.END)
        self.selling_price_entry.delete(0, tk.END)

# Run the GUI application
if __name__ == "__main__":
    root = tk.Tk()
    app = ProfitCalculatorApp(root)
    root.mainloop()
