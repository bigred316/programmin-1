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
        self._button1.Font = System.Drawing.Font("Rockwell", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(199, 53)
        self._button1.Name = "button1"
        self._button1.RightToLeft = System.Windows.Forms.RightToLeft.No
        self._button1.Size = System.Drawing.Size(200, 80)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Rockwell", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(498, 53)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(200, 80)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.MintCream
        self._button3.Font = System.Drawing.Font("OCR A Extended", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(840, 62)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(67, 403)
        self._button3.TabIndex = 2
        self._button3.Text = "EXIT"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 255, 255)
        self._label1.Font = System.Drawing.Font("Rockwell", 24, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(86, 147)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(724, 318)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label1.Click += self.Label1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self.ClientSize = System.Drawing.Size(919, 487)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Full Name"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text="My full name is Gale William Price."

    def Button2Click(self, sender, e):
        self._label1.Text=""

    def Button3Click(self, sender, e):
        Applitcation.Exit()

    def Label1Click(self, sender, e):
        self._label1.Text="quit clicking the text, thats what the buttons are for"