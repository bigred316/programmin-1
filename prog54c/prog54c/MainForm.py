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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._button4 = System.Windows.Forms.Button()
        self._button5 = System.Windows.Forms.Button()
        self._button6 = System.Windows.Forms.Button()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.AllowDrop = True
        self._label1.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(172, 61)
        self._label1.TabIndex = 1
        self._label1.Text = "Radius:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.UseWaitCursor = True
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(161, 24)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(146, 38)
        self._textBox1.TabIndex = 2
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(41, 109)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(156, 47)
        self._button1.TabIndex = 3
        self._button1.Text = "Circumfrence:"
        self._button1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._button1.UseVisualStyleBackColor = True
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(41, 293)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(111, 47)
        self._button2.TabIndex = 4
        self._button2.Text = "Diameter:"
        self._button2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(41, 198)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(73, 47)
        self._button3.TabIndex = 5
        self._button3.Text = "Area:"
        self._button3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # button4
        # 
        self._button4.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button4.Location = System.Drawing.Point(387, 24)
        self._button4.Name = "button4"
        self._button4.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._button4.Size = System.Drawing.Size(253, 102)
        self._button4.TabIndex = 6
        self._button4.Text = "Calculate"
        self._button4.UseVisualStyleBackColor = True
        self._button4.Click += self.Button4Click
        # 
        # button5
        # 
        self._button5.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button5.Location = System.Drawing.Point(387, 262)
        self._button5.Name = "button5"
        self._button5.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._button5.Size = System.Drawing.Size(253, 102)
        self._button5.TabIndex = 7
        self._button5.Text = "Exit"
        self._button5.UseVisualStyleBackColor = True
        self._button5.Click += self.Button5Click
        # 
        # button6
        # 
        self._button6.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button6.Location = System.Drawing.Point(387, 143)
        self._button6.Name = "button6"
        self._button6.Size = System.Drawing.Size(253, 102)
        self._button6.TabIndex = 8
        self._button6.Text = "Clear"
        self._button6.UseVisualStyleBackColor = True
        self._button6.Click += self.Button6Click
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.CadetBlue
        self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(203, 109)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(140, 46)
        self._label2.TabIndex = 9
        self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.CadetBlue
        self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(120, 199)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(140, 46)
        self._label3.TabIndex = 10
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.CadetBlue
        self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(158, 294)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(140, 46)
        self._label4.TabIndex = 11
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Azure
        self.ClientSize = System.Drawing.Size(646, 393)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._button6)
        self.Controls.Add(self._button5)
        self.Controls.Add(self._button4)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54c"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button3Click(self, sender, e):
        pass

    def Button4Click(self, sender, e):
        Radius = float(self._textBox1.Text)
        Diameter = Radius * 2
        Area = 3.14159 * Radius ** 2
        Circumfrence = 2 * 3.14159 * Radius
        Diameter = round(Diameter, 3)
        Circumfrence = round(Circumfrence, 3)
        Area = round(Area , 3)
        self._label2.Text = str(Circumfrence)
        self._label3.Text = str(Area)
        self._label4.Text = str(Diameter)

    def Button6Click(self, sender, e):
        self._label2.Text = ""
        self._label3.Text = ""
        self._label4.Text = ""

    def Button5Click(self, sender, e):
        Application.Exit()