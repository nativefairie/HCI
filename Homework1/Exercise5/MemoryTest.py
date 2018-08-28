import time
import random
import re
import wx

class MemoryTest(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Memory', size=(400, 200))
        self.panel = wx.Panel(self)
        self.panel.BackgroundColour = "white"
       
        
        box0 = wx.SingleChoiceDialog(None, "Select type", "Display words or numbers:", ['Words', 'Numbers'])
        if box0.ShowModal() == wx.ID_OK:
            self.objectsOrNumbers = box0.GetStringSelection()

        self.inputLabel = ""
        self.answerLabel = ""
        self.fileName = ""
        
        if self.objectsOrNumbers == 'Words':
            self.fileName = "Words.txt"
            self.inputLabel = "Insert the number of words:"
            self.answerLabel = "Write the words:"

        if self.objectsOrNumbers == 'Numbers':
            self.fileName = "Numbers.txt"
            self.inputLabel = "Insert the number of numbers!"
            self.answerLabel = "Write the numbers:"

        file = open(self.fileName, 'r')
        objects = file.read().lower()
        self.all_objects = re.split('\W+', objects)
        
        
        box1 = wx.TextEntryDialog(None, self.inputLabel, "Number")
        if box1.ShowModal() == wx.ID_OK:
            self.objects = box1.GetValue()
        
        box2 = wx.TextEntryDialog(None, "Chose the amount of time:", "Time")
        if box2.ShowModal() == wx.ID_OK:
            self.sec = box2.GetValue()
            
        box3 = wx.SingleChoiceDialog(None, "Select display direction:", "Display direction", ['Horizontal', 'Vertical'])
        if box3.ShowModal() == wx.ID_OK:
            self.type = box3.GetStringSelection()
            
        
        self.selected_objects = []
        for i in range(int(self.objects)):
            self.selected_objects.append(random.choice(self.all_objects))
           
           
   
        self.panel.Bind(wx.EVT_PAINT, self.draw)
            
    
    def draw(self, event):
        self.dc = wx.PaintDC(self.panel) 
        self.dc.Clear()
        self.dc.SetPen(wx.Pen("BLACK", 1))
        
        if self.type == 'Horizontal':
            self.dc.DrawText(', '.join(self.selected_objects), 10, 10)
            time.sleep(float(self.sec))
            self.dc.Clear() 
            del self.dc      
        
            answer_box1 = wx.TextEntryDialog(None, self.answerLabel, "Response")
            if answer_box1.ShowModal() == wx.ID_OK:
                input1 = answer_box1.GetValue()
            
            answer1 = re.split('\W+', input1)
            match = 0
            order = 0
            for i, word1 in enumerate(self.selected_objects):
                if word1.lower() in answer1:
                    match += 1
            
            if match == len(self.selected_objects):
                order = 1
                for i, word in enumerate(self.selected_objects):
                    if self.selected_objects[i] != answer1[i]:
                        order = 0
            print (match)
            print (order)
            
            if match == len(self.selected_objects) and order == 0:
                output1 = wx.MessageDialog(None, "You remenbered everything!", "Nice!", wx.OK)
                ans1 = output1.ShowModal()
                
            if match == len(self.selected_objects) and order == 1:
                output2 = wx.MessageDialog(None, "You remembered everything in order!", "Good job!", wx.OK)
                ans2 = output2.ShowModal()
                
            if match != len(self.selected_objects):
                output3 = wx.MessageDialog(None, "You didn`t remember everything.", "Loser!", wx.OK)
                ans3 = output3.ShowModal()
            
        if self.type == 'Vertical':
            gap = 0
            for word in self.selected_objects: 
                self.dc.DrawText(word, 10, 10 + gap)
                gap += 15
            time.sleep(float(self.sec))
            self.dc.Clear() 
            del self.dc
            
                
            answer_box1 = wx.TextEntryDialog(None, "Insert the words you remember:", "Response")
            if answer_box1.ShowModal() == wx.ID_OK:
                input1 = answer_box1.GetValue()
            
            answer1 = re.split('\W+', input1)
            match = 0
            order = 0
            for i, word1 in enumerate(self.selected_objects):
                if word1.lower() in answer1:
                    match += 1
            
            if match == len(self.selected_objects):
                order = 1
                for i, word in enumerate(self.selected_objects):
                    if self.selected_objects[i] != answer1[i]:
                        order = 0
            print (match)
            print (order)
            
            if match == len(self.selected_objects) and order == 0:
                output1 = wx.MessageDialog(None, "You remenbered!", "Nice!", wx.OK)
                ans1 = output1.ShowModal()

            if match == len(self.selected_objects) and order == 1:
                output2 = wx.MessageDialog(None, "You remembered them in order", "Good job!", wx.OK)
                ans2 = output2.ShowModal()

            if match != len(self.selected_objects):
                output3 = wx.MessageDialog(None, "You didn`t remember them all.", "Try again!", wx.OK)
                ans3 = output3.ShowModal()
                
if __name__ == '__main__':
    App = wx.App()
    frame = MemoryTest(parent=None, id=-1)
    frame.Show()
    App.MainLoop()    
    
    
    
    