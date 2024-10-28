import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._listBox1 = System.Windows.Forms.ListBox()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self.SuspendLayout()
        # 
        # listBox1
        # 
        self._listBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(56, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(657, 342)
        self._listBox1.TabIndex = 0
        self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(498, 372)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(215, 126)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(56, 372)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(215, 126)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 20.25, System.Drawing.FontStyle.Bold | System.Drawing.FontStyle.Italic, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.Color.Red
        self._button3.Location = System.Drawing.Point(277, 372)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(215, 126)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 192, 128)
        self.ClientSize = System.Drawing.Size(776, 510)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122d"
        self.ResumeLayout(False)


    def Button1Click(self, sender, e):
        heading= "Number\t\tCube\t\tCube Root"
        self._listBox1.Items.Add(heading)
        x = -25
                              
        xcube = 0
        xroot = 0
        
        
        for x in range(-25, 26):
           xcube = x ** 3
           if x < 0:
            xroot = (-1.0 * x) ** (1.0/3)
            line = str(x) + "\t\t" + str(xcube) + "\t\t" + str(-1.0 * xroot)
           else:
            xroot = x ** (1.0/3)
            line = str(x) + "\t\t" + str(xcube) + "\t\t" + str(xroot)
           self._listBox1.Items.Add(line)
        
        
        
       

    def ListBox1SelectedIndexChanged(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()