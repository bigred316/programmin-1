import System.Drawing
import System.Windows.Forms
import math
from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label6 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 9)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(433, 88)
        self._label1.TabIndex = 0
        self._label1.Text = "Ax  +Bx+C=0"
        self._label1.Click += self.Label1Click
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(104, 18)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(34, 31)
        self._label2.TabIndex = 1
        self._label2.Text = "2"
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(24, 108)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(167, 41)
        self._label3.TabIndex = 2
        self._label3.Text = "Input A:"
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(24, 241)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(167, 41)
        self._label4.TabIndex = 3
        self._label4.Text = "Input C:"
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(24, 177)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(167, 41)
        self._label5.TabIndex = 4
        self._label5.Text = "Input B:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(129, 104)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(202, 38)
        self._textBox1.TabIndex = 5
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(129, 241)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(202, 38)
        self._textBox2.TabIndex = 6
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(129, 173)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(202, 38)
        self._textBox3.TabIndex = 7
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.CadetBlue
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 27.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(26, 317)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(305, 169)
        self._label6.TabIndex = 8
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.Aquamarine
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(394, 101)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(154, 73)
        self._button1.TabIndex = 9
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.Aquamarine
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(394, 413)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(154, 73)
        self._button2.TabIndex = 11
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.Aquamarine
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(394, 252)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(154, 73)
        self._button3.TabIndex = 12
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = False
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(870, 511)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog58b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label1Click(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        Application.Exit()