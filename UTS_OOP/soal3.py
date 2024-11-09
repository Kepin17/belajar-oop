from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

class Tagihan(ABC):
    def __init__(self, id, amount, due_date, discount=0.0, description=""):
        self.id = id
        self.amount = amount
        self.due_date = due_date
        self.status = "unpaid"
        self.discount = discount
        self.description = description

    @abstractmethod
    def calculate_total(self):
        pass

    def apply_discount(self, discount_rate):
        self.discount = discount_rate

    def mark_as_paid(self):
        self.status = "paid"

    def show_invoice(self):
        return f"""
        Invoice Olyzano Bills
        ID: {self.id}
        Amount: {self.amount}
        Due Date: {self.due_date}
        Status: {self.status}
        """   

class TagihanListrik(Tagihan):
    def __init__(self, id, due_date, unit_consumed, unit_rate=0.15):
        super().__init__(id, amount=0, due_date=due_date, description="Tagihan Listrik")
        self.unit_consumed = unit_consumed
        self.unit_rate = unit_rate

    def calculate_total(self):
        return (self.unit_consumed * self.unit_rate) * (1 - self.discount)

class TagihanAir(Tagihan):
    def __init__(self, id, due_date, water_used, water_rate=0.05):
        super().__init__(id, amount=0, due_date=due_date, description="Tagihan Air")
        self.water_used = water_used
        self.water_rate = water_rate

    def calculate_total(self):
        return (self.water_used * self.water_rate) * (1 - self.discount)

class TagihanInternet(Tagihan):
    def __init__(self, id, due_date, data_used, data_rate=0.1):
        super().__init__(id, amount=0, due_date=due_date, description="Tagihan Internet")
        self.data_used = data_used
        self.data_rate = data_rate

    def calculate_total(self):
        return (self.data_used * self.data_rate) * (1 - self.discount)

class User:
    def __init__(self, user_id, username, email):
        self.user_id = user_id
        self.username = username
        self.email = email
        self.account_balance = 0
        self.payment_history = []

    def top_up_dana(self, amount):
        self.account_balance += amount

    def make_payment(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return True
        else:
            print("Not enough balance, please top up your balance!")
            return False

    def view_payment_history(self):
        return [receipt.details() for receipt in self.payment_history]

class Receipt:
    def __init__(self, receipt_id, user_id, bill_id, total_paid):
        self.receipt_id = receipt_id
        self.user_id = user_id
        self.bill_id = bill_id
        self.payment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.total_paid = total_paid

    def details(self):
        return f"""
        Receipt ID : {self.receipt_id}
        User ID : {self.user_id}
        Bill ID : {self.bill_id}
        Payment Date : {self.payment_date}
        Total Paid : {self.total_paid}
        """

class SistemPembayaranTagihan:
    def __init__(self):
        self.bills = []
        self.users = []
        self.receipts = []

    def add_user(self, user):
        self.users.append(user)

    def add_bill(self, bill):
        self.bills.append(bill)

    def process_payment(self, user, bill):
        total_amount = bill.calculate_total()
        if user.make_payment(total_amount):
            bill.mark_as_paid()
            receipt = Receipt(receipt_id=f"REC{len(self.receipts) + 1}", user_id=user.user_id, bill_id=bill.id, total_paid=total_amount)
            user.payment_history.append(receipt)
            self.receipts.append(receipt)
            print(f"Payment successful for Bill ID {bill.id} by User ID {user.user_id}")
        else:
            print("Payment failed, please top up your balance!")  

    def generate_receipt(self, user, bill):
        for receipt in user.payment_history:
            if receipt.bill_id == bill.id:
                return receipt.details()
        return "No receipt found!"    

system = SistemPembayaranTagihan()
user1 = User(user_id="U001", username="Alice", email="alice@example.com")
user1.top_up_dana(100.0)
system.add_user(user1)

bill1 = TagihanListrik(id="B001", due_date="2024-12-01", unit_consumed=100)
bill2 = TagihanAir(id="B002", due_date="2024-12-01", water_used=200)
system.add_bill(bill1)
system.add_bill(bill2)

system.process_payment(user1, bill1)  
print(system.generate_receipt(user1, bill1))  

system.process_payment(user1, bill2)  
print(system.generate_receipt(user1, bill2)) 
