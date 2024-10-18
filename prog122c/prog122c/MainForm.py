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
        self._listBox1.FormattingEnabled = True
        self._listBox1.Location = System.Drawing.Point(12, 12)
        self._listBox1.Name = "listBox1"
        self._listBox1.Size = System.Drawing.Size(215, 147)
        self._listBox1.TabIndex = 0
        self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
        # 
        # button1
        # 
        self._button1.BackColor = System.Drawing.Color.CadetBlue
        self._button1.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.SystemColors.Control
        self._button1.Location = System.Drawing.Point(263, 27)
        self._button1.Name = "button1"
        self._button1.RightToLeft = System.Windows.Forms.RightToLeft.Yes
        self._button1.Size = System.Drawing.Size(125, 36)
        self._button1.TabIndex = 1
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = False
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.BackColor = System.Drawing.Color.CadetBlue
        self._button2.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.ForeColor = System.Drawing.SystemColors.Control
        self._button2.Location = System.Drawing.Point(263, 68)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(125, 36)
        self._button2.TabIndex = 2
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = False
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.BackColor = System.Drawing.Color.CadetBlue
        self._button3.Font = System.Drawing.Font("Modern No. 20", 18, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.ForeColor = System.Drawing.SystemColors.Control
        self._button3.Location = System.Drawing.Point(263, 109)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(125, 36)
        self._button3.TabIndex = 3
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = False
        self._button3.Click += self.Button3Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.ActiveCaption
        self.ClientSize = System.Drawing.Size(415, 176)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._listBox1)
        self.Name = "MainForm"
        self.Text = "prog122c"
        self.ResumeLayout(False)


    def ListBox1SelectedIndexChanged(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        var = 0
        for num in range(0, 5):
            var = var+2
            addun = var + 1
            doub = var * 2
            sqr = var ** 2
            line = str(var) +"\t" + str(addun) + "\t" + str(doub) + "\t" + str(sqr)
            self._listBox1.Items.Add(line)
        
        
        
        
        

    def Button2Click(self, sender, e):
        self._listBox1.Items.Clear()

    def Button3Click(self, sender, e):
        Application.Exit()