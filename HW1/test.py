# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:13:55 2020

@author: anils
"""
import HW1AnılSen

a=HW1AnılSen.Stock(100,"S1")
b=HW1AnılSen.Stock(200,"S2")
c=HW1AnılSen.MutualFund("MF1")
d=HW1AnılSen.MutualFund("MF2")
e=HW1AnılSen.Bond("B1")
f=HW1AnılSen.Bond("B2")
HW1AnılSen.Bond.bondlist()
HW1AnılSen.MutualFund.mutualfundlist()
HW1AnılSen.Stock.stocklist()
    
portfolio=HW1AnılSen.Portfolio()
portfolio.addCash(100)
#portfolio.withdrawCash(200)
#We dont have enough money
portfolio.addCash(200)
portfolio.withdrawCash(100)
portfolio.addCash(20000000000000)
#portfolio.history()
#portfolio.buyStock(200,a)
#We dont have enough stock
portfolio.buyStock(1000,a)
portfolio.buyStock(1,b)
portfolio.buyStock(59,b)
#print(portfolio)
#portfolio.buyStock(1000,a)
#we dont have enough stock
portfolio.sellStock("S1",10)
portfolio.buyBond(1000,f)
portfolio.buyMutualFund(12,c)
portfolio.buyBond(1000,e)
portfolio.buyMutualFund(220,d)
portfolio.sellMutualFund("MF1",10)
portfolio.sellBond("B1",200)
portfolio.buyBond(12,e)
portfolio.sellMutualFund("MF2",100)
print(portfolio)
portfolio.history()