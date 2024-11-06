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
        self._button1.Font = System.Drawing.Font("Papyrus", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Underline, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(71, 24)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(126, 50)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Comic Sans MS", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 161)
        self._button2.Location = System.Drawing.Point(343, 24)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(160, 50)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Modern No. 20", 20.2499981, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(694, 24)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(143, 50)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.Cursor = System.Windows.Forms.Cursors.Cross
        self._label1.Font = System.Drawing.Font("OCR A Extended", 36, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(139, 163)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(605, 229)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self.ClientSize = System.Drawing.Size(872, 459)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Cursor = System.Windows.Forms.Cursors.No
        self.Name = "MainForm"
        self.Text = "About Me"
        self.ResumeLayout(False)


  
    def Button1Click(self, sender, e):
        self._label1.Text="Im Will, Im pretty good at CS"
   
   
   

    def Button2Click(self, sender, e):
        self._label1.Text=""

    def Button3Click(self, sender, e):
        Application.Exit()