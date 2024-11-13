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
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(128, 128, 255)
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
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(546, 478)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg240comm"
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)

