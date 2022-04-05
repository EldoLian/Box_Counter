#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 00:57:36 2022

@author: lian
"""

# *****正式编码*****

import tkinter
from tkinter import *
from tkinter import messagebox
import pandas as pd

cata_list = ["1.01","1.02","1.03","1.04","1,05","1.06", \
   "2.01","2.02","2.03","2.04","2.05","2.06","2.07","2.08","2.09","2.10","2.11","2.12","2.13","2.14","2.15","2.16", \
   "2.17","2.18", \
   "3.01","3.02","3.03","3.04","3.05","3.06","3.07","3.08","3.09","3.10","3.11","3.12","3.13","3.14","3.15","3.16", \
   "3.17","3.18","3.19","3.20", \
   "4.01","4.02","4.03","4.04","4.05","4.06","4.07","4.08","4.09","4.10","4.11","4.12","4.13","4.14","4.15","4.16", \
   "4.17", \
   "5.01","5.02","5.03","5.04","5.05", \
   "6.01","6.02", \
   "7.01","11.01","11.06","11.07","11.08","11.09"]
stor_time_list = ['Y','C','D']
result1 = 'none'

# 事件函数

def query():
    cata = var1.get()
    year = entry2.get()
    time = var3.get()
    if cata == "" or year == "" or time == "":
        messagebox.showinfo('提示',"数据填写不全！")
    else:
        # messagebox.showinfo('提示',"执行查询成功！")
        box_counter_csv = pd.read_csv("box_counter.csv")
        for i in range(len(box_counter_csv)):
            if str(box_counter_csv['cata'][i])==cata and str(box_counter_csv['year'][i])==year \
            and str(box_counter_csv['stor_time'][i])==time:
                # messagebox.showinfo('提示',"找到目标行！")
                result1=box_counter_csv['latest_boxN'][i]
                # text1.insert(INSERT, result1)
                mess1="查询成功，"+cata+"-"+year+"-"+time+"当前最大盒号是："+ str(result1)
                messagebox.showinfo('提示',mess1)
                break
            else:
                if i==len(box_counter_csv)-1:
                    mess2="未找到记录，"+cata+"-"+year+"-"+time+"当前最大盒号是：0"
                    messagebox.showinfo('提示',mess2)
            
def renew():
    cata = var1.get()
    year = entry2.get()
    time = var3.get()
    added = entry1.get()
    if cata == "" or year == "" or time == "" or added=="":
        messagebox.showinfo('提示',"数据填写不全！")
    else:
        if added.isdigit() is True and year.isdigit() is True:
            if int(year)>1900 and int(year)<2030:
                new_value = 0
                box_counter_csv = pd.read_csv("box_counter.csv")
                for i in range(len(box_counter_csv)):
                    if str(box_counter_csv['cata'][i])==cata and str(box_counter_csv['year'][i])==year \
                    and str(box_counter_csv['stor_time'][i])==time:
                        #用户确认后修改
                        messB1=messagebox.askquestion('提示',"确认将"+cata+"-"+year+"-"+time+"的最大盒号增加"+added+"吗？")
                        if messB1 == "yes":
                            result1=box_counter_csv['latest_boxN'][i]
                            added = int(added)
                            result1 = int(result1)
                            new_value = result1 + added
                            box_counter_csv.loc[i,'latest_boxN']=new_value
                            box_counter_csv.to_csv('box_counter.csv',index=False)
                            box_counter_csv = pd.read_csv("box_counter.csv")
                            if box_counter_csv.loc[i,'latest_boxN']==new_value:
                                print('写入成功A')
                                mess2="增加盒号成功，"+cata+"-"+year+"-"+time+"当前最大盒号是："+ str(new_value) \
                                +"——更新前为："+str(result1)
                                messagebox.showinfo('提示',mess2)
                                break
                        else:
                            break
                    else:
                        if i==len(box_counter_csv)-1:
                            added=int(added)
                            add_value = [cata,year,time,added]
                            add_row = pd.DataFrame([add_value],columns=['cata','year','stor_time','latest_boxN'])
                            box_counter_csv = box_counter_csv.append(add_row, ignore_index=True)
                            print(box_counter_csv)
                            box_counter_csv.to_csv('box_counter.csv',index=False)
                            box_counter_csv = pd.read_csv("box_counter.csv")
                            if box_counter_csv.loc[i+1,'latest_boxN']==added:
                                print('写入成功B')
                                mess3="增加盒号成功，"+cata+"-"+year+"-"+time+"当前最大盒号是："+ str(added) \
                                +"——更新前为：0"
                                messagebox.showinfo('提示',mess3)
            else:
                messagebox.showinfo('提示',"年度应在1900-2030之间，请检查！")
        else:
            messagebox.showinfo('提示',"仅限输入数值，请检查输入框！")
        
            
            



# GUI
root = tkinter.Tk()
root.title('Box Counter')
root.geometry('500x300')
frm1 = tkinter.Frame(root)
frm1.pack()
# 分类下拉列表
var1 = tkinter.StringVar()
list_cata = tkinter.OptionMenu(root,var1,*cata_list)
list_cata.pack()

#年度输入框
entry2 = Entry(root)
entry2.pack()


# 保管期限下拉列表
var3 = tkinter.StringVar()
list_time_list = tkinter.OptionMenu(root,var3,*stor_time_list)
list_time_list.pack()

button_query = tkinter.Button(root,text='查询',command=query)
button_query.pack()

entry1 = Entry(root)
entry1.pack()



button_renew = tkinter.Button(root,text='刷新盒号',command=renew)
button_renew.pack()

root.mainloop()



