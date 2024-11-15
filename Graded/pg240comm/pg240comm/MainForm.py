import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
        self._groupBox1.Controls.Add(self._label8)
        self._groupBox1.Controls.Add(self._label7)
        self._groupBox1.Controls.Add(self._label6)
        self._groupBox1.Controls.Add(self._label5)
        self._groupBox1.Controls.Add(self._label4)
        self._groupBox1.Controls.Add(self._label3)
        self._groupBox1.Controls.Add(self._textBox2)
        self._groupBox1.Controls.Add(self._label2)
        self._groupBox1.Controls.Add(self._textBox1)
        self._groupBox1.Controls.Add(self._label1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.ForeColor = System.Drawing.Color.White
        self._groupBox1.Location = System.Drawing.Point(12, 12)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(522, 364)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.White
        self._label1.Location = System.Drawing.Point(41, 51)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(208, 31)
        self._label1.TabIndex = 0
        self._label1.Text = "Sales this month: $"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(255, 49)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 34)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(41, 95)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(230, 35)
        self._label2.TabIndex = 2
        self._label2.Text = "Advance pay taken: $"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(267, 92)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 34)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(41, 147)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(230, 35)
        self._label3.TabIndex = 4
        self._label3.Text = "Commision Rate:"
        # 
        # label4
        # 
        self._label4.Location = System.Drawing.Point(41, 195)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(230, 35)
        self._label4.TabIndex = 5
        self._label4.Text = "Commision:"
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(41, 245)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(230, 35)
        self._label5.TabIndex = 6
        self._label5.Text = "Net pay:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label6.ForeColor = System.Drawing.Color.Black
        self._label6.Location = System.Drawing.Point(255, 147)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(100, 35)
        self._label6.TabIndex = 7
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label7.ForeColor = System.Drawing.Color.Black
        self._label7.Location = System.Drawing.Point(171, 195)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(119, 35)
        self._label7.TabIndex = 8
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label8.ForeColor = System.Drawing.Color.Black
        self._label8.Location = System.Drawing.Point(135, 245)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(136, 35)
        self._label8.TabIndex = 9
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 382)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(175, 84)
        self._button1.TabIndex = 2
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(183, 382)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(175, 84)
        self._button2.TabIndex = 3
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(359, 382)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(175, 84)
        self._button3.TabIndex = 4
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(546, 478)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg240comm"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        sales=float(self._textBox1.Text)
        advance = float(self._textBox2.Text)
        rate = 0
        if sales < 10000:
            rate = 0.05
        elif sales in range(10000, 15000):
            rate = 0.10
        elif sales in range(15000, 18000):
            rate = 0.12
        elif sales in range(18000, 22000):
            rate = 0.14
        elif sales >= 22000:
            rate = 0.16
        commision = sales * rate
        pay = commision - advance
        self._label8.Text=str(pay)
        self._label7.Text = str(commision)
        self._label6.Text = str(rate*100) + "%"
        
            

    def Button2Click(self, sender, e):
        self._label8.Text=""
        self._label7.Text = ""
        self._label6.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()