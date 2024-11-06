﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.Font = System.Drawing.Font("MS UI Gothic", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 29
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(422, 468)
        self._listBox1.TabIndex = 0
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.OliveDrab
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.ActiveCaption
        self._button1.Location = System.Drawing.Point(440, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(194, 93)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.OliveDrab
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.ActiveCaption
        self._button2.Location = System.Drawing.Point(440, 198)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(194, 93)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.OliveDrab
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.ActiveCaption
        self._button3.Location = System.Drawing.Point(440, 391)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(194, 93)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(644, 495)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122b"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        header = "Hours of Work \t Pay"
        self._listBox1.Items.Add(header)
        hours = 0
        pay = 0
        
        for num in range (0, 40):
            hours =  hours + 1
            pay = hours * 4
            line = str(hours) + "\t\t" + str(pay)
            self._listBox1.Items.Add(line)
            
        

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()