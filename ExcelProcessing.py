# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 20:10:06 2015

@author: Administrator
"""

import xlrd
from pandas import DataFrame
import pandas as pd
from datetime import datetime
from datetime import date
import time
import wx
import matplotlib.pyplot as plt
import numpy as np

def set_ch():
    from pylab import mpl
    mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题


class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,None,title=u"考勤表",pos=(200,200),size=(1000,800))
                
        self.CreateStatusBar()
        menuBar = wx.MenuBar()
        filemenu= wx.Menu()
        menuBar.Append(filemenu,"&File")
        menuAbout = filemenu.Append(wx.ID_ABOUT, "&About"," Information about this program")
        filemenu.AppendSeparator()
        menuQuit = filemenu.Append(wx.ID_EXIT,"&Quit"," Terminate the program")
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnQuit, menuQuit)
        self.SetMenuBar(menuBar)
        
        panel=wx.Panel(self)
        
        self.list = wx.ListCtrl(panel, wx.NewId(), style=wx.LC_REPORT)
        self.list.InsertColumn(0,u'学工号')
        self.list.InsertColumn(1,u'姓名')
        self.list.InsertColumn(2,u'性别')
        self.list.InsertColumn(3,u'门')  
        self.list.InsertColumn(4,u'进出标志')  
        self.list.InsertColumn(5,u'发生时间')  
        self.list.InsertColumn(6,u'部门')  
        self.list.InsertColumn(7,u'身份')  

        pos = self.list.InsertStringItem(0,"--")
        self.list.SetStringItem(pos,1,"loading...")
        self.list.SetStringItem(pos,2,"--")
        self.list.SetStringItem(pos,3,"--")
        self.list.SetStringItem(pos,4,"--")
        self.list.SetStringItem(pos,5,"--")
        self.list.SetStringItem(pos,6,"--")
        self.list.SetStringItem(pos,7,"--")
#        self.Bind(wx.EVT_LIST_ITEM_ACTIVATED, self.OnClick, self.list)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.list, -1, wx.ALL | wx.EXPAND, 10)
        
        panel.SetSizerAndFit(vsizer)        
        panel.Layout()        
        
#        self.option_list = [u'学工号',u'姓名',u'性别',u'门',u'进出标志',u'发生时间',u'部门',u'身份']      
    def setData(self,CSdata):
        self.list.ClearAll()
        self.list.InsertColumn(0,u'学工号')
        self.list.InsertColumn(1,u'姓名')
        self.list.InsertColumn(2,u'性别')
        self.list.InsertColumn(3,u'门')  
        self.list.InsertColumn(4,u'进出标志')  
        self.list.InsertColumn(5,u'发生时间')  
        self.list.InsertColumn(6,u'部门')  
        self.list.InsertColumn(7,u'身份')
        self.list.SetColumnWidth(0, 120)
        self.list.SetColumnWidth(1, 60)
        self.list.SetColumnWidth(2, 40)
        self.list.SetColumnWidth(3, 120)
        self.list.SetColumnWidth(4, 80)
        self.list.SetColumnWidth(5, 130)
        self.list.SetColumnWidth(6, 270)
        self.list.SetColumnWidth(7, 130)
        pos = 0
        for row in CSdata.index:
            pos = self.list.InsertStringItem(pos+1,str(CSdata.ix[row,u'学工号']))
            self.list.SetStringItem(pos,1,str(CSdata.ix[row,u'姓名']))
            self.list.SetStringItem(pos,2,str(CSdata.ix[row,u'性别']))
            self.list.SetStringItem(pos,3,str(CSdata.ix[row,u'门']))
            self.list.SetStringItem(pos,4,str(CSdata.ix[row,u'进出标志']))
            self.list.SetStringItem(pos,5,str(CSdata.ix[row,u'发生时间']))
            self.list.SetStringItem(pos,6,str(CSdata.ix[row,u'部门']))
            self.list.SetStringItem(pos,7,str(CSdata.ix[row,u'身份']))     
            if (pos % 2 == 0):
                self.list.SetItemBackgroundColour(pos, (134, 225, 249))
        self.FitInside()
        pass
        
    def OnAbout(self, event):
        dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
        dlg.ShowModal()
        dlg.Destroy()

    def OnQuit(self, event):
        self.Close()
        self.Destroy()    

def DataLoading():
    xlsxfile=xlrd.open_workbook(r'D:\2015.xlsx')
    try:
        mysheet = xlsxfile.sheet_by_name(u'2015sheet')
        print("%d rows, %d cols"%(mysheet.nrows, mysheet.ncols))
    except  Exception,e:
        print str(e)
    a=mysheet.col_values(0)
    b=mysheet.col_values(1)
    c=mysheet.col_values(2)
    d=mysheet.col_values(3)
    e=mysheet.col_values(4)
    f=mysheet.col_values(5)
    g=mysheet.col_values(6)
    h=mysheet.col_values(7)
    a.pop(0)
    b.pop(0)
    c.pop(0)
    d.pop(0)
    e.pop(0)
    f.pop(0)
    g.pop(0)
    h.pop(0)
    data=pd.DataFrame({u'学工号':a,u'姓名':b,u'性别':c,u'门':d,u'进出标志':e,u'发生时间':f,u'部门':g,u'身份':h})
    return data

def DataFormalization(data):
    for row in range(len(data.index)):
        if type(data.ix[row,u'学工号'])==float:
            data.ix[row,u'学工号']=long(data.ix[row,u'学工号'])       
#        print type(data.ix[row,u'学工号'])
        x = data.ix[row,u'发生时间']#1447900333)#42277.9608449)
        data.ix[row,u'发生时间'] = xlrd.xldate.xldate_as_datetime(x, 0)
        #print time.strftime('%Y-%m-%d %H:%M:%S',a),time.strftime('%Y-%m-%d %H:%M:%S',b)
        #data.ix[row,u'发生时间']=time.strftime('%Y/%m/%d %H:%M:%S',x) 
    return data
    
def GetCSers(data):
    CSdata=data[data[u'部门'] == u'教职工/计算机科学与工程学院']
    return CSdata

def PieChart(CSdata):
    grouped = CSdata.groupby(u'姓名').size()
    plt.figure(1, figsize=(12,12))
    labels=grouped.index
    quants=grouped.values
    
    def explode(label, target=u'贺小箭'):
        if label == target: return 0.1
        else: return 0
    expl = map(explode,labels)    
    colors  = ["pink","coral","yellow","orange"]
    plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.2f%%',pctdistance=0.8, shadow=True)
    plt.title('打卡次数比例', bbox={'facecolor':'0.8', 'pad':5})

    plt.show()    
    
def BarChart(CSdata):
    grouped = CSdata.groupby(u'姓名').size()
    fig=plt.figure(1, figsize=(12,6))
    labels=grouped.index
    quants=grouped.values 
    width = 0.8
    ind = np.linspace(10,90,len(grouped.index))
    ax=fig.add_subplot(1,1,1)
    ax.bar(ind-width/2,quants,width,color='r')
    ax.set_ylim(bottom=0, top=100)
    ax.set_xticks(ind+0.1)
    ax.set_xticklabels(labels,rotation='vertical')
    ax.set_xlabel(u'姓名')
    ax.set_ylabel(u'次数')
    # title
    ax.set_title(u'打卡次数统计', bbox={'facecolor':'0.8', 'pad':5})
    plt.show()
    
if __name__ == '__main__':
    set_ch()
        
    data=DataLoading()
    data=DataFormalization(data)
    CSdata=GetCSers(data)    

    BarChart(CSdata)
#    PieChart(CSdata)

#    app=wx.App()
#    frame=Frame1(None)
#    frame.Show(True)   
#    frame.setData(CSdata)
#    app.MainLoop()
#    del app
