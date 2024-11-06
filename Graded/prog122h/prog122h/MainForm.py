import System.Drawing
import System.Windows.Forms
import math

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
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(225, 13)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(675, 485)
        self._listBox1.TabIndex = 0
        self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(4, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(215, 126)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(4, 192)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(215, 126)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(3, 371)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(215, 126)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self.ClientSize = System.Drawing.Size(930, 510)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading= "Number\t\tSquare\t\tSquare Root\t\tCube\t\tFourth Root"
        
        self._listBox1.Items.Add(heading)
        x = float()
        xsquare = float(0)
        xcube = float(0)
        xroot = float(0)
        Xroot4 = float(0)
        for x in range(0 , 20):
            x += 1
            xsquare = x**2
            xcube = x **3
            xroot =  math.sqrt(x)
            xroot4 = x ** 0.25
            line = str(x)+"\t\t" + str(xsquare)+"\t\t" +str(xroot)+"\t\t" +str(xcube)+"\t\t" +str(xroot4)
            self._listBox1.Items.Add(line)
            
            
        
        
        
       

    def ListBox1SelectedIndexChanged(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()
