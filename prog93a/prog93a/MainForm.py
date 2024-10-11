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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.BurlyWood
        self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(41, 29)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(199, 32)
        self._label1.TabIndex = 0
        self._label1.Text = "Kilowatts used:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(246, 29)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(179, 31)
        self._textBox1.TabIndex = 1
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.BurlyWood
        self._label2.Font = System.Drawing.Font("Microsoft YaHei UI", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(45, 107)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(608, 304)
        self._label2.TabIndex = 2
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("MS Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(45, 431)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(200, 64)
        self._button1.TabIndex = 3
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("MS Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(453, 431)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(200, 64)
        self._button2.TabIndex = 4
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("MS Gothic", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(251, 431)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(200, 64)
        self._button3.TabIndex = 5
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(686, 502)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog93a"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        kwh = float(self._textBox1.Text)
        base = round((kwh * 0.0475) , 2)
        sur = round((base * 0.1) , 2)
        tax = round((base * 0.03) , 2)
        final = base + sur + tax
        finallate = round((final * 1.04) , 2)
        self._label2.Text = "Kilowatts used: " + str(kwh) + "\nBase Rate: " + str(kwh) +" @ $0.0475 + $" + str(base) +"\nSurcharge = $" + str(sur) + "\nTax = $" + str(tax) + "\n \nAmount Due = $" + str(final) + "\nIf not payed on time = $" + str(finallate)

    def Button3Click(self, sender, e):
        self._label2.Text = ""
        self._textBox1.Text = ""
      

    def Button2Click(self, sender, e):
        Application.Exit()