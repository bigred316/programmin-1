import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._label9 = System.Windows.Forms.Label()
        self._label10 = System.Windows.Forms.Label()
        self._label11 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label12 = System.Windows.Forms.Label()
        self._label13 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.White
        self._label1.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(72, 49)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(83, 23)
        self._label1.TabIndex = 0
        self._label1.Text = "Class 1:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(161, 46)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 34)
        self._textBox1.TabIndex = 1
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(161, 121)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(100, 34)
        self._textBox2.TabIndex = 3
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.White
        self._label2.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(72, 124)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(83, 23)
        self._label2.TabIndex = 2
        self._label2.Text = "Class 2:"
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(161, 192)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(100, 34)
        self._textBox3.TabIndex = 5
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.White
        self._label3.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(72, 195)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(83, 23)
        self._label3.TabIndex = 4
        self._label3.Text = "Class 3:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.White
        self._label4.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(446, 195)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(83, 23)
        self._label4.TabIndex = 10
        self._label4.Text = "Class 3:"
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.White
        self._label5.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(446, 124)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(83, 23)
        self._label5.TabIndex = 8
        self._label5.Text = "Class 2:"
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.White
        self._label6.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(446, 49)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(83, 23)
        self._label6.TabIndex = 6
        self._label6.Text = "Class 1:"
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.White
        self._label7.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(89, 9)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(147, 23)
        self._label7.TabIndex = 12
        self._label7.Text = "TICKETS SOLD"
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.White
        self._label8.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(464, 9)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(171, 23)
        self._label8.TabIndex = 13
        self._label8.Text = "TOTAL REVENUE"
        # 
        # label9
        # 
        self._label9.BackColor = System.Drawing.Color.White
        self._label9.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label9.Location = System.Drawing.Point(535, 49)
        self._label9.Name = "label9"
        self._label9.Size = System.Drawing.Size(83, 31)
        self._label9.TabIndex = 14
        # 
        # label10
        # 
        self._label10.BackColor = System.Drawing.Color.White
        self._label10.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label10.Location = System.Drawing.Point(535, 124)
        self._label10.Name = "label10"
        self._label10.Size = System.Drawing.Size(83, 31)
        self._label10.TabIndex = 15
        # 
        # label11
        # 
        self._label11.BackColor = System.Drawing.Color.White
        self._label11.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label11.Location = System.Drawing.Point(535, 195)
        self._label11.Name = "label11"
        self._label11.Size = System.Drawing.Size(83, 31)
        self._label11.TabIndex = 16
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(12, 247)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(122, 52)
        self._button1.TabIndex = 18
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(140, 247)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(122, 52)
        self._button2.TabIndex = 19
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(268, 247)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(122, 52)
        self._button3.TabIndex = 20
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label12
        # 
        self._label12.BackColor = System.Drawing.Color.White
        self._label12.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label12.Location = System.Drawing.Point(416, 262)
        self._label12.Name = "label12"
        self._label12.Size = System.Drawing.Size(69, 27)
        self._label12.TabIndex = 21
        self._label12.Text = "Total:"
        # 
        # label13
        # 
        self._label13.BackColor = System.Drawing.Color.White
        self._label13.Font = System.Drawing.Font("Microsoft Tai Le", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label13.Location = System.Drawing.Point(500, 258)
        self._label13.Name = "label13"
        self._label13.Size = System.Drawing.Size(135, 31)
        self._label13.TabIndex = 22
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self.ClientSize = System.Drawing.Size(710, 311)
        self.Controls.Add(self._label13)
        self.Controls.Add(self._label12)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label11)
        self.Controls.Add(self._label10)
        self.Controls.Add(self._label9)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "pg186stadiumseating"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)
        self.PerformLayout()


    def MainFormLoad(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        revenue1 = self._textBox1.Text 