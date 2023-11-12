#!/usr/bin/env python3

class CashRegister:

  def __init__(self,discount = 0):
    self.discount = discount
    self.items = []
    self.total = 0
    recent_price = 0
    recent_quantity = 0
  
  def add_item(self,item,price,quantity=1):
    self.quantity = 0
    for i in range(quantity):
      self.total += price
      self.quantity += 1
      self.items.append(item)
      self.recent_price = price
  
  def apply_discount(self):
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      self.total -= self.total * (self.discount/100)
      print("After the discount, the total comes to $800.")
  
  def void_last_transaction(self):
    for n in range(self.quantity):
      self.items.pop()
      self.total -= self.recent_price


  
    
      
