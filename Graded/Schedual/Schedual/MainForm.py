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
        self._button1.BackColor = System.Drawing.Color.CadetBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(13, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(212, 102)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.CadetBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(323, 13)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(212, 102)
        self._button2.TabIndex = 1
        self._button2.Text = "Hide"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.CadetBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(649, 13)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(212, 102)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.SystemColors.ButtonShadow
        self._label1.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(13, 134)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(847, 344)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(887, 504)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Schedual"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text="1st Hour: Keyboarding \n2nd Hour: Computer Programming 1 \n3rd Hour: Chemistry Honors\n 4th Hour: AP Human Geography \n5th Hour: Geometry Honors \n6th Hour: Spanish 2 \n7th Hour: English 9 Honors\n 8th Hour: Freshman Seminar"

    def Button2Click(self, sender, e):
        self._label1.Text=""

    def Button3Click(self, sender, e):
        Application.Exit()