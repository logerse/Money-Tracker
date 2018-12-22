#!/usr/bin/env python3

#---

import DataEdit
import subprocess

#---

DATE = subprocess.check_output("date +%d.%m.%y", shell = True).decode("latin1").strip()

#---

def new_Expense(count, reason = None):
    #----
    All_Money = get_All_money()
    All_Money -= int(count)
    #----
    DataEdit.set_field(date = DATE, money = count, reason = reason, all_money = All_Money, type = "Expense")

def new_Income(count, reason = None):
    #----
    All_Money = get_All_money()
    All_Money += int(count)
    #----
    DataEdit.set_field(date = DATE, money = count, reason = reason, all_money = All_Money, type = "Income")

def get_All_money():
    All_Money = DataEdit.get_field("all_money")
    if not All_Money:
        All_Money = 0
    else:
        All_Money = int(All_Money[-1])
    return All_Money
