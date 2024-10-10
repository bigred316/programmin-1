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
        self._textBox1 = System.Windows.Forms.TextBox()
        self._textBox2 = System.Windows.Forms.TextBox()
        self._textBox3 = System.Windows.Forms.TextBox()
        self._label4 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.PaleTurquoise
        self._label1.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(8, 20)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(124, 38)
        self._label1.TabIndex = 0
        self._label1.Text = "Pounds:"
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.PaleTurquoise
        self._label2.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(8, 83)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(139, 37)
        self._label2.TabIndex = 1
        self._label2.Text = "Shillings:"
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.PaleTurquoise
        self._label3.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.Location = System.Drawing.Point(8, 139)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(106, 38)
        self._label3.TabIndex = 2
        self._label3.Text = "Pence:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(138, 20)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(219, 38)
        self._textBox1.TabIndex = 3
        # 
        # textBox2
        # 
        self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox2.Location = System.Drawing.Point(120, 139)
        self._textBox2.Name = "textBox2"
        self._textBox2.Size = System.Drawing.Size(237, 38)
        self._textBox2.TabIndex = 4
        # 
        # textBox3
        # 
        self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox3.Location = System.Drawing.Point(153, 83)
        self._textBox3.Name = "textBox3"
        self._textBox3.Size = System.Drawing.Size(204, 38)
        self._textBox3.TabIndex = 5
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.PaleTurquoise
        self._label4.Font = System.Drawing.Font("Perpetua", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.Location = System.Drawing.Point(8, 212)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(349, 222)
        self._label4.TabIndex = 6
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(373, 20)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(184, 83)
        self._button1.TabIndex = 7
        self._button1.Text = "Caluculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(373, 182)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(184, 83)
        self._button2.TabIndex = 8
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(373, 351)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(184, 83)
        self._button3.TabIndex = 9
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = True
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Azure
        self.ClientSize = System.Drawing.Size(646, 457)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._textBox3)
        self.Controls.Add(self._textBox2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "Decimal Pounds Calculator"
        self.ResumeLayout(False)
        self.PerformLayout()


    def Button1Click(self, sender, e):
        lbs = float(self._textBox1.Text)
        shil = float(self._textBox3.Text)
        pence = float(self._textBox2.Text)
        newpence = ((shil * 12) + pence)/2.4
        newpence = int(round(newpence , 0))
        newlbs = int(lbs)
        self._label4.Text =  "£" + str(newlbs) + "." + str(newpence)
        