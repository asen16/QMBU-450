import random
import datetime
class Stock(object):
    stocks={}
    def __init__(self,stockprice,stocksymbol):
        self.stockprice=stockprice
        self.stocksymbol=stocksymbol
        self.stocks.update({self.stocksymbol : self.stockprice})
    def stocklist():
        return "Stocks==>"+str(Stock.stocks)
    def __str__(self):
        return "Selected Stock,Name: '"+str(self.stocksymbol)+"' ;Price: "+str(self.stockprice)+" $"

class MutualFund(object):
    funds=[]
    def __init__(self,mutualfundsymbol):
        self.mutualfundsymbol=mutualfundsymbol
        self.funds.append(self.mutualfundsymbol)
    def mutualfundlist():
        return "Mutual Funds==>"+str(MutualFund.funds)
    def __str__(self):
        return "Selected Fund,Name: '"+str(self.mutualfundsymbol)+"'"
    
class Bond(object):
    bonds=[]
    def __init__(self,bondsymbol):
        self.bondsymbol=bondsymbol
        self.bonds.append(self.bondsymbol)
    def bondlist():
        return "Bonds==>"+str(Bond.bonds)
    def __str__(self):
        return "Selected Bond,Name: '"+str(self.bondsymbol)+"'"

class Portfolio(object):
        portbondlist={}
        portstocklist={}
        portmutualfundlist={}
        def __init__(self,cashstock=0):
            self.cashstock=cashstock
            self.stocklist=Stock.stocklist()
            self.mutualfundlist=MutualFund.mutualfundlist()
            self.bondlist=Bond.bondlist()
            self.histor=[]
            
        def addCash(self,cash):
            self.cash=cash
            if type(cash) is not int:
                raise KeyError("Cash should be integer")
            if cash<0:
                raise KeyError("Cash should be positive")
            self.cashstock=self.cashstock+self.cash
            self.histor.append(str(datetime.date.today())+": Cash deposited:"+str(cash)+" $")
            return self.cashstock
        def withdrawCash(self,cashout):
            self.cashout=cashout
            if type(cashout) is not int:
                raise KeyError("Cashout should be integer")
            if cashout<0:
                raise KeyError("Cash should be positive")
            if self.cashstock>=cashout:
                self.cashstock=self.cashstock-self.cashout
                self.histor.append(str(datetime.date.today())+": Cash taken into Account:"+str(cashout)+" $")
            else:
                raise ValueError("You don't have enough money")
        def buyStock(self,stockquan,value):
            self.stockquantity=stockquan
            if type(stockquan) is not int:
                raise KeyError("Quantity should be integer")
            if type(value.stockprice) is not int:
                raise KeyError("Stockprice should be integer")
            if type(value.stocksymbol) is not str:
                raise KeyError("Stocksymbol should be string")
            if stockquan<0:
                raise KeyError("Stockquan should be positive")
            if value.stockprice<0:
                raise KeyError("Stockprice should be positive")
            if self.cashstock>=value.stockprice*stockquan:
                self.cashstock=self.cashstock-value.stockprice*stockquan
                self.histor.append(str(datetime.date.today())+" : #"+str(stockquan)+" "+value.stocksymbol+" stock was bought by "+str(value.stockprice*stockquan)+" $")
                if value.stocksymbol in self.portstocklist.keys():
                    newdeger=self.stockquantity
                    self.portstocklist[value.stocksymbol]+=newdeger
                    self.portstocklist.update({value.stocksymbol : self.portstocklist[value.stocksymbol]})
                else:
                    self.portstocklist.update({value.stocksymbol : self.stockquantity})
            else:
                raise ValueError("You don't have enough money")
        def buyMutualFund(self,mutualfundquan,value):
            self.stockquantity=mutualfundquan
            if type(mutualfundquan) is not int:
                raise KeyError("Quantity should be integer")
            if type(value.mutualfundsymbol) is not str:
                raise KeyError("Mutualfundsymbol should be string")
            if mutualfundquan<0:
                raise KeyError("Mutualfundquan should be positive")
            if self.cashstock>=1*mutualfundquan:
                self.histor.append(str(datetime.date.today())+" : #"+str(mutualfundquan)+" "+value.mutualfundsymbol+" mutual fund was bought by "+str(1*mutualfundquan)+" $")
                self.cashstock=self.cashstock-1*mutualfundquan
                if value.mutualfundsymbol in self.portmutualfundlist.keys():
                    newdeger=self.stockquantity
                    self.portmutualfundlist[value.mutualfundsymbol]+=newdeger
                    self.portmutualfundlist.update({value.mutualfundsymbol : self.portmutualfundlist[value.mutualfundsymbol]})
                else:
                    self.portmutualfundlist.update({value.mutualfundsymbol : self.stockquantity})
            else:
                raise ValueError("You don't have enough money")
        def buyBond(self,bondquan,value):
            self.stockquantity=bondquan
            if type(bondquan) is not int:
                raise KeyError("Quantity should be integer")
            if type(value.bondsymbol) is not str:
                raise KeyError("Bondsymbol should be string")
            if bondquan<0:
                raise KeyError("Bondquan should be positive")
            if self.cashstock>=1*bondquan:
                self.histor.append(str(datetime.date.today())+" : #"+str(bondquan)+" "+value.bondsymbol+" bond was bought by "+str(1*bondquan)+" $")
                self.cashstock=self.cashstock-1*bondquan
                if value.bondsymbol in self.portbondlist.keys():
                    newdeger=self.stockquantity
                    self.portbondlist[value.bondsymbol]+=newdeger
                    self.portbondlist.update({value.bondsymbol : self.portbondlist[value.bondsymbol]})
                else:
                    self.portbondlist.update({value.bondsymbol : self.stockquantity})
            else:
                raise ValueError("You don't have enough money")
        def sellStock(self,stocksymbol,stockquan):
            self.stockquantity=stockquan
            if type(stockquan) is not int:
                raise KeyError("Quantity should be integer")
            if type(stocksymbol) is not str:
                raise KeyError("Stocksymbol should be string")
            if stockquan<0:
                raise KeyError("Stockquan should be positive")
            if stocksymbol  not in self.portstocklist:
                raise ValueError("Stocksymbol is not in the list")
            if self.portstocklist[stocksymbol]>=stockquan:
                revenue=round(Stock.stocks[stocksymbol]*random.uniform(0.5,1.5)*stockquan,2)
                self.histor.append(str(datetime.date.today())+" : #"+str(stockquan)+" "+stocksymbol+" stock was sold by "+str(revenue)+" $")
                self.portstocklist[stocksymbol]-=stockquan
                self.cashstock+=revenue
            else:
                raise ValueError("You don't have enough stock")
        def sellMutualFund(self,mutualfundsymbol,mutualfundquan):
            self.mutualquantity=mutualfundquan
            if type(mutualfundquan) is not int:
                raise KeyError("Quantity should be integer")
            if type(mutualfundsymbol) is not str:
                raise KeyError("Mutualfundsymbol should be string")
            if mutualfundquan<0:
                raise KeyError("Mutualfundquan should be positive")
            if mutualfundsymbol  not in self.portmutualfundlist:
                raise ValueError("Mutualfundsymbol is not in the list")
            if self.portmutualfundlist[mutualfundsymbol]>=self.mutualquantity:
                    revenue=round(random.uniform(0.9,1.2)*self.mutualquantity,2)
                    self.histor.append(str(datetime.date.today())+" : #"+str(mutualfundquan)+" "+mutualfundsymbol+" mutual fund was sold by "+str(revenue)+" $")
                    self.portmutualfundlist[mutualfundsymbol]-=self.mutualquantity
                    revenue=random.uniform(0.9,1.2)*self.mutualquantity
                    self.cashstock+=revenue
            else:
                raise ValueError("You don't have enough mutual fund")
        def sellBond(self,bondsymbol,bondquan):
            self.bondquantity=bondquan
            if type(bondquan) is not int:
                raise KeyError("Quantity should be integer")
            if type(bondsymbol) is not str:
                raise KeyError("Bondsymbol should be string")
            if bondquan<0:
                raise KeyError("Bondquan should be positive")
            if bondsymbol  not in self.portbondlist:
                raise ValueError("Bondsymbol is not in the list")
            if self.portbondlist[bondsymbol]>=self.bondquantity:
                revenue=round(random.uniform(0.9,1.2)*self.bondquantity,2)
                self.histor.append(str(datetime.date.today())+" : #"+str(bondquan)+" "+bondsymbol+"bond was sold by "+str(revenue)+" $")
                self.portbondlist[bondsymbol]-=self.bondquantity
                revenue=random.uniform(0.9,1.2)*self.bondquantity
                self.cashstock+=revenue
            else:
                raise ValueError("You don't have enough bond")
        def history(self):
            print("History of Your Transaction")
            for i in self.histor:print(i+"\n")
            print("Cash Balance: "+str(self.cashstock)+ " $"+"\n"+"---------------------------------------------")
        def __str__(self):
            return ("My Portfolio:"+"\n"+"Cash:"+str(self.cashstock)+"$"+"\n"+"Stock List: "+str(self.portstocklist)+"\n"+"Mutual Fund List: "+str(self.portmutualfundlist)+"\n"+"Bond List: "+str(self.portbondlist)+"\n"+"-----------------------------------------------")

        
