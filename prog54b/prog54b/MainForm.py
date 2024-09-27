import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._textBox4 = System.Windows.Forms.TextBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(25, 24)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(152, 32)
        self._label1.TabIndex = 0
        self._label1.Text = "Number 1"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label3
        # 
        self._label3.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(25, 344)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(152, 32)
        self._label3.TabIndex = 2
        self._label3.Text = "Number 4"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label4
        # 
        self._label4.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(25, 234)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(152, 32)
        self._label4.TabIndex = 3
        self._label4.Text = "Number 3"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # label5
        # 
        self._label5.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(25, 113)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(152, 32)
        self._label5.TabIndex = 4
        self._label5.Text = "Number 2"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(154, 25)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(154, 31)
        self._textBox1.TabIndex = 5
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(154, 235)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(154, 31)
        self._textBox3.TabIndex = 7
        # 
        # textBox4
        # 
        self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox4.Location = System.Drawing.Point(154, 344)
        self._textBox4.Name = "textBox4"
        self._textBox4.Size = System.Drawing.Size(154, 31)
        self._textBox4.TabIndex = 8
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(25, 411)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(209, 77)
        self._button1.TabIndex = 10
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(460, 411)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(209, 77)
        self._button2.TabIndex = 11
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Rockwell", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(245, 411)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(209, 77)
        self._button3.TabIndex = 12
        self._button3.Text = "Clear"
        self._button3.UseVisualStyleBackColor = True
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(154, 114)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(154, 31)
        self._textBox2.TabIndex = 13
        # 
        # label2
        # 
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(443, 28)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(239, 117)
        self._label2.TabIndex = 14
        self._label2.Text = "label2"
        self._label2.Click += self.Label2Click
        # 
        # label6
        # 
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(314, 22)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(123, 37)
        self._label6.TabIndex = 15
        self._label6.Text = "Area:"
        # 
        # label7
        # 
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.Location = System.Drawing.Point(447, 193)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(239, 117)
        self._label7.TabIndex = 16
        self._label7.Text = "label7"
        # 
        # label8
        # 
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.Location = System.Drawing.Point(318, 187)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(123, 37)
        self._label8.TabIndex = 17
        self._label8.Text = "Sum:"
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(698, 500)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._textBox4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54b"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label2Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        pass