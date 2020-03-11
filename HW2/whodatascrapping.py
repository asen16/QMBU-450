# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 17:32:51 2020

@author: anils
"""

from bs4 import BeautifulSoup
import requests
import csv
import numpy as np
import linearregres
class whodata(object):
    def whodtscr1(url,csvfile,statement,year):
        
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        
        table = soup.findAll("tr")[1:]
        a=[]
        i=0
        fields=["GHO","PUBLISHSTATE","REGION","COUNTRY","DISPLAYVALUE","NUMERICVALUE","LOW RANGE","HIGH RANGE","Comment"]
        with open(csvfile, mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=fields,lineterminator='\n')
            writer.writeheader()
            loyee_writer = csv.writer(f,lineterminator='\n')
            for rows in table:
                c=1+i
                c=[]
                cells = rows.findAll("td")
                if len(rows) > 0:
                    if cells[0].find(text = True)==statement:
                        c.append(cells[0].find(text = True))
                        c.append(cells[1].find(text = True))
                        c.append(cells[2].find(text = True))
                        c.append(cells[3].find(text = True))
                        c.append(cells[4].find(text = True))
                        c.append(cells[5].find(text = True))
                        c.append(cells[6].find(text = True))
                        c.append(cells[7].find(text = True))
                        loyee_writer.writerow(c)
                        a.append(c)
    def whodtscr2(url,csvfile,statement,year):
        
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        
        table = soup.findAll("tr")[1:]
        a=[]
        i=0
        fields=["GHO","PUBLISHSTATE","YEAR","REGION","COUNTRY","DISPLAYVALUE","NUMERICVALUE","LOW RANGE","HIGH RANGE","Comment"]
        with open(csvfile, mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=fields,lineterminator='\n')
            writer.writeheader()
            loyee_writer = csv.writer(f,lineterminator='\n')
            for rows in table:
                c=1+i
                c=[]
                cells = rows.findAll("td")
                if len(rows) > 0:
                    if cells[0].find(text = True)==statement:
                        if cells[2].find(text = True)==year:
                            c.append(cells[0].find(text = True))
                            c.append(cells[1].find(text = True))
                            c.append(cells[2].find(text = True))
                            c.append(cells[3].find(text = True))
                            c.append(cells[4].find(text = True))
                            c.append(cells[5].find(text = True))
                            c.append(cells[6].find(text = True))
                            c.append(cells[7].find(text = True))
                            loyee_writer.writerow(c)
                            a.append(c)
    def whodtscr3(url,csvfile,statement):
        
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        
        table = soup.findAll("tr")[1:]
        a=[]
        i=0
        fields=["GHO","PUBLISHSTATE","YEAR","REGION","COUNTRY","SEX","NUMERICVALUE","LOW RANGE","HIGH RANGE","Comment"]
        with open(csvfile, mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=fields,lineterminator='\n')
            writer.writeheader()
            loyee_writer = csv.writer(f,lineterminator='\n')
            for rows in table:
                c=1+i
                c=[]
                cells = rows.findAll("td")
                if len(rows) > 0:
                    if cells[5].find(text = True)=="Both sexes":
                        if cells[0].find(text = True)==statement:
                            c.append(cells[0].find(text = True))
                            c.append(cells[1].find(text = True))
                            c.append(cells[2].find(text = True))
                            c.append(cells[3].find(text = True))
                            c.append(cells[4].find(text = True))
                            c.append(cells[5].find(text = True))
                            c.append(cells[6].find(text = True))
                            c.append(cells[7].find(text = True))
                            loyee_writer.writerow(c)
                            a.append(c)
    def whodtscr4(url,csvfile,statement,year):
        
        r = requests.get(url)
        soup = BeautifulSoup(r.text,"html.parser")
        
        table = soup.findAll("tr")[1:]
        a=[]
        i=0
        fields=["GHO","PUBLISHSTATE","YEAR","REGION","COUNTRY","DISPLAYVALUE","NUMERICVALUE","LOW RANGE","HIGH RANGE","Comment"]
        with open(csvfile, mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=fields,lineterminator='\n')
            writer.writeheader()
            loyee_writer = csv.writer(f,lineterminator='\n')
            for rows in table:
                c=1+i
                c=[]
                cells = rows.findAll("td")
                if len(rows) > 0:
                    if cells[0].find(text = True)==statement:
                        if cells[2].find(text = True)==year:
                            c.append(cells[0].find(text = True))
                            c.append(cells[1].find(text = True))
                            c.append(cells[2].find(text = True))
                            c.append(cells[3].find(text = True))
                            c.append(cells[4].find(text = True))
                            c.append(cells[5].find(text = True))
                            c.append(cells[6].find(text = True))
                            c.append(cells[7].find(text = True))
                            loyee_writer.writerow(c)
                            a.append(c)
    def dataunif(csvfilea,csvfileb,csvfilec,csvfiled):
        first1=[]
        second1=[]
        forth1=[]
        first2=[]
        second2=[]
        third2=[]
        forth2=[]
        first3=[]
        second3=[]
        forth3=[]
        first4=[]
        second4=[]
        forth4=[]
        with open(csvfilea, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                first1.append(row['COUNTRY'])
                second1.append(row['NUMERICVALUE'])
                forth1.append(row['GHO'])
        with open(csvfileb, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                first2.append(row['COUNTRY'])
                second2.append(row['NUMERICVALUE'])
                third2.append(row['YEAR'])
                forth2.append(row['GHO'])
        with open(csvfilec, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                first3.append(row['COUNTRY'])
                second3.append(row['NUMERICVALUE'])
                forth3.append(row['GHO'])
            print(first3,second3)
        with open(csvfiled, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                first4.append(row['COUNTRY'])
                second4.append(row['NUMERICVALUE'])
                forth4.append(row['GHO'])
            print(first4,second4)
        counter=0
        newsecond2=[]
        newthird2=[]
        newforth2=[]
        for i in first1:
            counter=0
            for a in first2:
                if a==i:
                    newsecond2.append(second2[counter])
                    newthird2.append(third2[counter])
                    newforth2.append(forth2[counter])
                else:
                    counter+=1
        print(newsecond2,newthird2,newforth2)
        newsecond3=[]
        newforth3=[]
        for i in first1:
            counter=0
            for a in first3:
                if a==i:
                    newsecond3.append(second3[counter])
                    newforth3.append(forth3[counter])
                else:
                    counter+=1
        print(newsecond3,newforth3)
        
        newsecond4=[]
        newforth4=[]
        for i in first1:
            counter=0
            for a in first4:
                if a==i:
                    newsecond4.append(second4[counter])
                    newforth4.append(forth4[counter])
                else:
                    counter+=1
              
    
        fields=["COUNTRY","YEAR","GHO","VALUE1","GHO","VALUE2","GHO","VALUE3","GHO","VALUE4"]
        with open("totaldate.csv", mode='w') as f:
            writer = csv.DictWriter(f,fieldnames=fields,lineterminator='\n')
            writer.writeheader()
            x_writer = csv.writer(f,lineterminator='\n')
            a=0
            for i in first1:
                if second1[a]==0 or second1[a]=="" or second1[a]=="Not available" or newsecond2[a]==0 or newsecond2[a]=="" or newsecond2[a]=="Not available" or newsecond3[a]==0 or newsecond3[a]=="" or newsecond3[a]=="Not available" or newsecond4[a]==0 or newsecond4[a]=="" or newsecond4[a]=="Not available":
                    a+=1
                    pass
                else:
                    c=[]
                    c.append(first1[a])
                    c.append(newthird2[a])
                    c.append(forth1[a])
                    c.append(second1[a])
                    c.append(newforth2[a])
                    c.append(newsecond2[a])
                    c.append(newforth3[a])
                    c.append(newsecond3[a])
                    print(newsecond3[a])
                    c.append(newforth4[a])
                    c.append(newsecond4[a])
                    x_writer.writerow(c)
                    a+=1
    def regres(datapackage,valuey,valuex):
        return linearregres.linearregression(datapackage,valuey,valuex)
    

    

   
