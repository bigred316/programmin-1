﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.CadetBlue
        self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label1.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(25, 35)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(187, 43)
        self._label1.TabIndex = 0
        self._label1.Text = "Speed Limit:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.CadetBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.FlatStyle = System.Windows.Forms.FlatStyle.Popup
        self._label2.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(25, 127)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(224, 43)
        self._label2.TabIndex = 1
        self._label2.Text = "Vehicle Speed:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(218, 35)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(191, 43)
        self._textBox1.TabIndex = 2
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(255, 127)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(191, 43)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.SpringGreen
        self._label3.Font = System.Drawing.Font("MS PGothic", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlDarkDark
        self._label3.Location = System.Drawing.Point(25, 211)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(579, 206)
        self._label3.TabIndex = 4
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(475, 3)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(156, 48)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(475, 57)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(156, 48)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(475, 111)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(156, 48)
        self._button3.TabIndex = 7
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Teal
        self.ClientSize = System.Drawing.Size(643, 437)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Ticket Calculator"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        lim = float(self._textBox1.Text)
        spd = float(self._textBox2.Text)
        fine = 20.00 + ((spd - lim) * 5.00)
        self._label3.Text = "Your fine is $" + str(fine)

    def Button2Click(self, sender, e):
        self._label3.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()