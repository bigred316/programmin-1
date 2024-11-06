import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self.SuspendLayout()
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(188, 85)
        self._button1.TabIndex = 0
        self._button1.Text = "SHOW"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(229, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(170, 85)
        self._button2.TabIndex = 1
        self._button2.Text = "HIDE"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(419, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(147, 85)
        self._button3.TabIndex = 2
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(0, 0, 192)
        self._label1.Font = System.Drawing.Font("MS Reference Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
        self._label1.Location = System.Drawing.Point(13, 121)
        self._label1.Name = "label1"
        self._label1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._label1.Size = System.Drawing.Size(542, 329)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(582, 459)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Cougars"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text="GO COUGARS!"

    def Button2Click(self, sender, e):
        self._label1.Text=""

    def Button3Click(self, sender, e):
        Application.Exit()