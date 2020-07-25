# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 03:32:43 2020

@author: rilha
"""

import requests

bcaVA = "https://www.static-src.com/siva/asset//07_2020/2-BankDeals-BCAVA.jpg"
bcaKlik = "https://www.static-src.com/siva/asset//07_2020/3-BankDeals-BCAKP.jpg"
briDebit = "https://www.static-src.com/siva/asset//07_2020/5-BankDeals-BRI.jpg"
mandiriKredit = "https://www.static-src.com/siva/asset//07_2020/12-BankDeals-MDR.jpg"


for url in [bcaVA,briDebit,briDebit,mandiriKredit]:
    r = requests.get(url)
    if r.status_code == 200:
        print("Voucher {nama voucher} Aktif")
    elif r.status_code == 404:
        print("Voucher Belum Aktif")
    else:
        print("Link error")
        
