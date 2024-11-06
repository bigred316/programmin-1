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
        self._button1.BackColor = System.Drawing.Color.DarkBlue
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Cyan
        self._button1.Location = System.Drawing.Point(12, 12)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(178, 85)
        self._button1.TabIndex = 0
        self._button1.Text = "Show"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.DarkBlue
        self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.Color.Cyan
        self._button2.Location = System.Drawing.Point(211, 12)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(178, 85)
        self._button2.TabIndex = 1
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.DarkBlue
        self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Cyan
        self._button3.Location = System.Drawing.Point(410, 12)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(178, 85)
        self._button3.TabIndex = 2
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.DarkTurquoise
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(12, 104)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(576, 266)
        self._label1.TabIndex = 3
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.CornflowerBlue
        self.ClientSize = System.Drawing.Size(601, 379)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Name = "MainForm"
        self.Text = "Go cougars!"
        self.Load += self.MainFormLoad
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        self._label1.Text="Craig Rules!"

    def MainFormLoad(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._label1.Text=""

    def Button3Click(self, sender, e):
        Application.Exit()