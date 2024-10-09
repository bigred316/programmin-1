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
        self._label2 = System.Windows.Forms.Label()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label1.Font = System.Drawing.Font("Modern No. 20", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label1.Location = System.Drawing.Point(60, 37)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(85, 39)
        self._label1.TabIndex = 0
        self._label1.Text = "Cost:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Modern No. 20", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(151, 37)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(142, 39)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label2.Font = System.Drawing.Font("Modern No. 20", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label2.Location = System.Drawing.Point(60, 92)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(292, 39)
        self._label2.TabIndex = 2
        self._label2.Text = "Amount Recieved:"
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Modern No. 20", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(358, 92)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(142, 39)
        self._textBox2.TabIndex = 3
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.ControlDarkDark
        self._label3.Font = System.Drawing.Font("Modern No. 20", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(60, 163)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(227, 39)
        self._label3.TabIndex = 4
        self._label3.Text = "Change Due:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.Black
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(302, 163)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(339, 329)
        self._label4.TabIndex = 5
        self._label4.TextAlign = System.Drawing.ContentAlignment.TopCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Rockwell", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(60, 240)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(227, 86)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Rockwell", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(60, 371)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(227, 86)
        self._button2.TabIndex = 7
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("MS Gothic", 72, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(658, 24)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(126, 468)
        self._button3.TabIndex = 8
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = True
        # 
        # label5
        # 
        self._label5.Location = System.Drawing.Point(1083, 68)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(100, 23)
        self._label5.TabIndex = 9
        self._label5.Text = "label5"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ButtonShadow
        self.ClientSize = System.Drawing.Size(805, 513)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog58t"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        cost = float(self._textBox1.Text)
        Rec = float(self._textBox2.Text)
        Due = Rec - cost
        work = Due
        dollars = work // 1
        work = work - dollars
        quarters = work // 0.25 
        work = work - (quarters/4)
        dimes = work // 0.10
        work = work-(dimes / 10)
        nic = work // 0.05
        work = work - (nic / 20)
        pen = work // 0.01
        self._label4.Text ="Dollars: " + str(dollars) + "\n Quarters: " + str(quarters) + "\n Dimes: " + str(dimes) + "\n Nickles: " 
        self._label5.Text = work