# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 20:11:40 2015

@author: Administrator
"""

import wx

class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="example",pos=(200,200),size=(1000,800))
        panel=wx.Panel(self)
        text1=wx.TextCtrl(panel,value="hello world!",size=(1000,800))
        
if __name__=='__main__':
    app=wx.App()
    frame=Frame1(None)
    frame.Show(True)
    
    app.MainLoop()

#######################################    
import matplotlib.pyplot as plt
import numpy as np

plt.figure(1, figsize=(6,6))

labels=['asd','faf','aaaaa','fsdf','sdf','sfdf','asd','asdads']
quants=[10,3,5,6,3,2,3,1]

def explode(label, target='aaaaa'):
    if label == target: return 0.1
    else: return 0
expl = map(explode,labels)
    
colors  = ["pink","coral","yellow","orange"]

plt.pie(quants, explode=expl, colors=colors, labels=labels, autopct='%1.2f%%',pctdistance=0.8, shadow=True)
plt.title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})

plt.show()

#########################################
import matplotlib.pyplot as plt
import numpy as np

labels=['asd','faf','aaaaa','fsdf','sdf','sfdf','asd','asdads','asdads','asdads']
quants=[10,3,5,6,3,2,3,1,4,5]
width = 0.4
ind = np.linspace(0.5,9.5,10)
# make a square figure
fig = plt.figure(1, figsize=(12,6))
ax1=fig.add_subplot(1,1,1)
#ax1.hist(randn(100), bins=20, color='k', alpha=0.3)
#ax2.scatter(np.arange(30), np.arange(30) + 3 * randn(30))
# Bar Plot
ax1.bar(ind-width/2,quants,width,color='r')
# Set the ticks on x-axis
ax.set_xticks(ind)
ax.set_xticklabels(labels)
# labels
ax.set_xlabel('Country')
ax.set_ylabel('GDP (Billion US dollar)')
# title
ax.set_title('Top 10 GDP Countries', bbox={'facecolor':'0.8', 'pad':5})
plt.show()
