import tkinter as tk # importing  Library
from tkinter import messagebox # displaying messages in GUI(Graphical User Interface)

class ATM:
    def __init__(self, master):
        self.master = master
        master.title("ATM Interface")
        # Dictionary to store card information: {PIN: balance}
        self.cards = {} # card pin information saved in this dictionary
        self.current_pin = None

        self.label = tk.Label(master, text="Welcome to the SBI ATM")
        self.label.pack()

        self.register_button = tk.Button(master, text="Register New Card", command=self.register_card)
        self.register_button.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def register_card(self):
        self.clear_window()

        self.label = tk.Label(self.master, text="Register New Card")
        self.label.pack()

        self.pin_label = tk.Label(self.master, text="Enter a new PIN:")
        self.pin_label.pack()

        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.pack()

        self.balance_label = tk.Label(self.master, text="Enter initial balance:")
        self.balance_label.pack()

        self.balance_entry = tk.Entry(self.master)
        self.balance_entry.pack()

        self.register_button = tk.Button(self.master, text="Register", command=self.process_registration)
        self.register_button.pack()

        self.back_button = tk.Button(self.master, text="Back to Main Menu", command=self.show_main_menu)
        self.back_button.pack()

    def process_registration(self):
        new_pin = self.pin_entry.get()
        try:
            initial_balance = float(self.balance_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid balance. Please enter a numeric value.")
            return

        if new_pin in self.cards:
            messagebox.showerror("Error", "PIN already exists. Please choose a different PIN.")
        elif len(new_pin) < 4:
            messagebox.showerror("Error", "PIN must be at least 4 digits.")
        else:
            self.cards[new_pin] = initial_balance
            messagebox.showinfo("Success", f"Card registered successfully! Initial balance: ₹{initial_balance}")
            self.show_main_menu()

    def login(self):
        self.clear_window()

        self.label = tk.Label(self.master, text="Login to Your Account")
        self.label.pack()

        self.pin_label = tk.Label(self.master, text="Enter your PIN:")
        self.pin_label.pack()

        self.pin_entry = tk.Entry(self.master, show="*")
        self.pin_entry.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.check_pin)
        self.login_button.pack()

        self.back_button = tk.Button(self.master, text="Back to Main Menu", command=self.show_main_menu)
        self.back_button.pack()

    def check_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin in self.cards:
            self.current_pin = entered_pin
            self.show_menu()
        else:
            messagebox.showerror("Error", "Invalid PIN. Please try again.")

    def show_menu(self):
        self.clear_window()

        self.label = tk.Label(self.master, text="ATM Menu")
        self.label.pack()

        self.balance_button = tk.Button(self.master, text="Check Balance", command=self.check_balance)
        self.balance_button.pack()

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

        self.logout_button = tk.Button(self.master, text="Logout", command=self.logout)
        self.logout_button.pack()

    def check_balance(self):
        balance = self.cards[self.current_pin]
        messagebox.showinfo("Balance", f"Your balance is: ₹{balance}")

    def deposit(self):
        self.clear_window()

        self.label = tk.Label(self.master, text="Deposit Money")
        self.label.pack()

        self.amount_label = tk.Label(self.master, text="Enter amount to deposit:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack()

        self.deposit_button = tk.Button(self.master, text="Deposit", command=self.process_deposit)
        self.deposit_button.pack()

        self.back_button = tk.Button(self.master, text="Back to Menu", command=self.show_menu)
        self.back_button.pack()

    def process_deposit(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
            return

        self.cards[self.current_pin] += amount
        messagebox.showinfo("Success", f"You have deposited ₹{amount}. New balance: ₹{self.cards[self.current_pin]}")
        self.show_menu()

    def withdraw(self):
        self.clear_window()

        self.label = tk.Label(self.master, text="Withdraw Money")
        self.label.pack()

        self.amount_label = tk.Label(self.master, text="Enter amount to withdraw:")
        self.amount_label.pack()

        self.amount_entry = tk.Entry(self.master)
        self.amount_entry.pack()

        self.withdraw_button = tk.Button(self.master, text="Withdraw", command=self.process_withdraw)
        self.withdraw_button.pack()

        self.back_button = tk.Button(self.master, text="Back to Menu", command=self.show_menu)
        self.back_button.pack()

    def process_withdraw(self):
        try:
            amount = float(self.amount_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid amount. Please enter a numeric value.")
            return

        if amount > self.cards[self.current_pin]:
            messagebox.showerror("Error", "Insufficient funds.")
        else:
            self.cards[self.current_pin] -= amount
            messagebox.showinfo("Success", f"You have withdrawn ₹{amount}. New balance: ₹{self.cards[self.current_pin]}")
        self.show_menu()

    def logout(self):
        self.current_pin = None
        self.show_main_menu()

    def clear_window(self):
        for widget in self.master.winfo_children():
            widget.destroy()

    def show_main_menu(self):
        self.clear_window()

        self.label = tk.Label(self.master, text="Welcome to the ATM")
        self.label.pack()

        self.register_button = tk.Button(self.master, text="Register New Card", command=self.register_card)
        self.register_button.pack()

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack()


if __name__ == "__main__": #script runs when it executed directly.
    root = tk.Tk()
    atm = ATM(root)
    root.mainloop()
