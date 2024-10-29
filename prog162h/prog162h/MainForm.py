import System.Drawing
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
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(180, 25)
        self._label1.TabIndex = 0
        self._label1.Text = "Guests:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(12, 47)
        self._label2.Name = "label2"
        self._label2.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label2.Size = System.Drawing.Size(180, 25)
        self._label2.TabIndex = 1
        self._label2.Text = "Chairs:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(211, 6)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 2
        self._textBox1.Text = "0"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(211, 47)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 31)
        self._textBox2.TabIndex = 3
        self._textBox2.Text = "0"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._label3.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(13, 90)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(298, 204)
        self._label3.TabIndex = 4
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 297)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(298, 54)
        self._button1.TabIndex = 5
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(12, 357)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(298, 54)
        self._button2.TabIndex = 6
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(13, 417)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(298, 54)
        self._button3.TabIndex = 7
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(326, 489)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog162h"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        guests = int(self._textBox1.Text)
        chairs = int(self._textBox2.Text)
        working = guests
        self._label3.Text = "Guests: " + str(guests) + "\nChairs: " + str(chairs)
        for num in range(0, (chairs -1)):
            guests -= 1
            working *= guests
        guests = int(self._textBox1.Text)
        self._label3.Text = "Guests: " + str(guests) + "\nChairs: " + str(chairs)  + "\nPermutations: " + str(working) + "\nStanding Guests: " + str(guests-chairs)
        
            
            

    def MainFormLoad(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._label3.Text = ""
        self._textBox1.Text = "0"
        self._textBox2.Text = "0"
        

    def Button3Click(self, sender, e):
        Application.Exit()