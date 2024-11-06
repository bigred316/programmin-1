import System.Drawing
import System.Windows.Forms

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
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.Highlight
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlLight
        self._label1.Location = System.Drawing.Point(78, 37)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(179, 31)
        self._label1.TabIndex = 0
        self._label1.Text = "Length:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.SystemColors.Highlight
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.ForeColor = System.Drawing.SystemColors.ControlLight
        self._label2.Location = System.Drawing.Point(78, 130)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(179, 31)
        self._label2.TabIndex = 1
        self._label2.Text = "Width:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.SystemColors.Highlight
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label3.Location = System.Drawing.Point(114, 226)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(179, 33)
        self._label3.TabIndex = 2
        self._label3.Text = "Area:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.Highlight
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlLightLight
        self._label4.Location = System.Drawing.Point(55, 334)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(179, 33)
        self._label4.TabIndex = 3
        self._label4.Text = "Perimeter:"
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(11, 415)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(143, 65)
        self._button1.TabIndex = 4
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(284, 415)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(143, 65)
        self._button2.TabIndex = 5
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Rockwell", 24, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(500, 166)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(50, 321)
        self._button3.TabIndex = 6
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.Location = System.Drawing.Point(177, 226)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(259, 68)
        self._label5.TabIndex = 7
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.Location = System.Drawing.Point(177, 334)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(259, 68)
        self._label6.TabIndex = 8
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(177, 37)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(247, 31)
        self._textBox1.TabIndex = 9
        self._textBox1.Text = "0"
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(177, 130)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(247, 31)
        self._textBox2.TabIndex = 10
        self._textBox2.Text = "0"
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(562, 500)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Label1Click(self, sender, e):
        pass

    def Label2Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        length = int(self._textBox1.Text)
        width = int(self._textBox2.Text)
        area = length * width
        perim = 2 * length + 2 * width
        self._label5.Text = str(area)
        self._label6.Text = str(perim)
        # + - * / %    ** pow    // divide and round down
        # int integer float floating point str string

    def Button2Click(self, sender, e):
        self._label5.Text= ""
        self._label6.Text= ""

    def Button3Click(self, sender, e):
        Application.Exit()