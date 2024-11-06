import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Maroon
        self._label1.ForeColor = System.Drawing.Color.Cyan
        self._label1.Location = System.Drawing.Point(61, 148)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(750, 328)
        self._label1.TabIndex = 0
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Perpetua", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(61, 52)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(145, 56)
        self._button1.TabIndex = 1
        self._button1.Text = "show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Perpetua", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(353, 52)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(144, 56)
        self._button2.TabIndex = 2
        self._button2.Text = "clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Perpetua", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(653, 52)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(158, 56)
        self._button3.TabIndex = 3
        self._button3.Text = "exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ControlText
        self.ClientSize = System.Drawing.Size(886, 485)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Font = System.Drawing.Font("Papyrus", 27.75, System.Drawing.FontStyle.Strikeout, System.Drawing.GraphicsUnit.Point, 0)
        self.Name = "MainForm"
        self.Text = "haha you looked"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def Label1Click(self, sender, e):
        pass

    def Button3Click(self, sender, e):
        Application.Exit()

    def Button2Click(self, sender, e):
        self._label1.Text=""

    def Button1Click(self, sender, e):
        self._label1.Text="Hello World! (woah he said the thing)"