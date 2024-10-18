
import math
import System.Drawing
import System.Windows.Forms


from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(521, 354)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(304, 59)
        self._button1.TabIndex = 0
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._listBox1.Font = System.Drawing.Font("Microsoft YaHei", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._listBox1.FormattingEnabled = True
        self._listBox1.ItemHeight = 21
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(475, 487)
        self._listBox1.TabIndex = 1
        self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(521, 431)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(149, 59)
        self._button2.TabIndex = 2
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(676, 431)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(149, 59)
        self._button3.TabIndex = 3
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 192, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(509, 12)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(161, 36)
        self._label1.TabIndex = 4
        self._label1.Text = "Target Number:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(676, 12)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(125, 38)
        self._textBox1.TabIndex = 5
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self.ClientSize = System.Drawing.Size(863, 502)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._listBox1)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "prog122a"
        self.ResumeLayout(False)
        self.PerformLayout()


        

    def Button3Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button2Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        self._listBox1.Items.Clear()
        adder = 0
        workval = 0
        goal= int(self._textBox1.Text)
        heading = "Even Integer\t\tSum"
        self._listBox1.Items.Add(heading)
        while workval < goal:
            adder = adder + 2
            workval = workval + adder
            line = str(adder) + "\t\t\t " + str(workval)
            self._listBox1.Items.Add(line)
        else: 
            line = "The sum of all even integers from 0 to " + str(adder) + " >=" + str(goal)
            self._listBox1.Items.Add(line)


    def ListBox1SelectedIndexChanged(self, sender, e):
        pass