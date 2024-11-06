import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._button6 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(67, 35)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(131, 54)
        self._button1.TabIndex = 0
        self._button1.Text = "Quote #1"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(227, 34)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(121, 55)
        self._button2.TabIndex = 1
        self._button2.Text = "Quote #2"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(379, 35)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(116, 54)
        self._button3.TabIndex = 2
        self._button3.Text = "Quote #3"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(539, 35)
        self._button4.Name = "button4"
        self._button4.Size = System.Drawing.Size(124, 55)
        self._button4.TabIndex = 3
        self._button4.Text = "Quote #4"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.BackColor = System.Drawing.Color.FromArgb(255, 128, 128)
        self._button5.Font = System.Drawing.Font("MS Reference Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.ForeColor = System.Drawing.Color.Red
        self._button5.Location = System.Drawing.Point(772, 108)
        self._button5.Name = "button5"
        self._button5.Size = System.Drawing.Size(75, 324)
        self._button5.TabIndex = 4
        self._button5.Text = "EXIT"
        self._button5.UseVisualStyleBackColor = False
        self._button5.Click += self.Button5Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Teal
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(67, 108)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(682, 288)
        self._label1.TabIndex = 5
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button6
        # 
        self._button6.Font = System.Drawing.Font("MS Reference Sans Serif", 72, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(227, 399)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(390, 129)
        self._button6.TabIndex = 7
        self._button6.Text = "CLEAR"
        self._button6.UseVisualStyleBackColor = True
        self._button6.Click += self.Button6Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(0, 64, 64)
        self.ClientSize = System.Drawing.Size(905, 540)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Quote"
        self.ResumeLayout(False)


    def Button5Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        self._label1.Text= "If you cant explain it simply, you dont understand it well enough- Albert Einstein"

    def Button2Click(self, sender, e):
        self._label1.Text="The world is a dangerous place to live; not because of the people who are evil, but because of the people who don't do anything about it.- Albert Einstein"

    def Button3Click(self, sender, e):
        self._label1.Text="The true sign of intelligence is not knowledge but imagination.- Albert Einstein"

    def Button4Click(self, sender, e):
        self._label1.Text="Life is like riding a bicycle. To keep your balance, you must keep moving.- Albert Einstein"

    def Button6Click(self, sender, e):
        self._label1.Text=""