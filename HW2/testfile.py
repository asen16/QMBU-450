# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 06:06:43 2020

@author: anils
"""
import whodatascrapping
import unittest

csvfilea='dataa.csv'
csvfileb='datab.csv'
csvfilec='datac.csv'
csvfiled='datad.csv'
url1="https://apps.who.int/gho/athena/data/GHO/R_excise_proportion,R_excise_type,R_excise_uniform_varied,R_excise_specific_reliance,R_excise_min_specific,R_excise_retail_price_base,R_afford_gdp,R_afford_less,R_afford_tax_auto_adjust,R_afford_price_dispersion,R_admin_tax_stamps,R_admin_duty_free_limited,R_admin_duty_free_allowance.html?profile=ztable&filter=COUNTRY:*;REGION:*"
url2= "https://apps.who.int/gho/athena/data/GHO/R_Curr_mp,R_Price_mp_estimate,R_Price_mp_ppp,R_Price_mp_usd,R_Curr_average,R_Price_average_curr,R_Price_average_ppp,R_Price_average_usd.html?profile=ztable&filter=COUNTRY:*;REGION:*"
url3="https://apps.who.int/gho/athena/data/GHO/M_Est_tob_curr,M_Est_tob_daily,M_Est_cig_curr,M_Est_cig_daily.html?profile=ztable&filter=COUNTRY:*;SEX:*"
url4="https://apps.who.int/gho/athena/data/GHO/PC_sfe_compliance,P1_compliance,P2_compliance,P3_compliance,P4_compliance,P5_compliance,P6_compliance,P7_compliance,P8_compliance.html?profile=ztable&filter=COUNTRY:*;REGION:*"
statement1="Tax structure: Excise tax proportion of price"
statement2="Average -  cigarette price in international dollars"
statement3="Daily cigarette smoking, age-standardised"
statement4="Compliance with regulations on smoke-free environments (national legislation)"
year="2012"

csvfilea='employee_fileaa.csv'
urla= "https://apps.who.int/gho/athena/data/GHO/R_Sp_excise_average,R_Ad_val_average,R_imp_duty_average,R_VAT_average,R_Other_average,R_total_tax_average.html?profile=ztable&filter=COUNTRY:*;REGION:*"

class datascrapTest(unittest.TestCase):
    def whodatascrap(self):
        self.whodatascrapping.whodata.whodtscr1(url1,csvfilea,statement1,year)
        self.whodatascrapping.whodata.whodtscr2(url2,csvfileb,statement2,year)
        self.whodatascrapping.whodata.whodtscr3(url3,csvfilec,statement3)
        self.whodatascrapping.whodata.whodtscr4(url4,csvfiled,statement4,year)

    def test_who_data_unif(self):
        self.whodatascrapping.whodata.dataunif(csvfilea,csvfileb,csvfilec,csvfiled)
    
    def test_regres(self,datapackage,valuey,valuex):
        self.whodatascrapping.regres("totaldate.csv","VALUE3","VALUE1")
        self.whodatascrapping.regres("totaldate.csv","VALUE4","VALUE1")
        self.whodatascrapping.regres("totaldate.csv","VALUE2","VALUE4")
        self.whodatascrapping.regres("totaldate.csv","VALUE2","VALUE3")
    
        
