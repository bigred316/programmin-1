import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._label1 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._label6 = System.Windows.Forms.Label()
        self._label7 = System.Windows.Forms.Label()
        self._label8 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._button3 = System.Windows.Forms.Button()
        self._comboBox1 = System.Windows.Forms.ComboBox()
        self.SuspendLayout()
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.Chartreuse
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.SystemColors.ControlText
        self._label1.Location = System.Drawing.Point(128, 51)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(215, 48)
        self._label1.TabIndex = 0
        self._label1.Text = "Pick a Car:"
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label3
        # 
        self._label3.BackColor = System.Drawing.Color.CadetBlue
        self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label3.ForeColor = System.Drawing.SystemColors.ControlText
        self._label3.Location = System.Drawing.Point(52, 176)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(145, 64)
        self._label3.TabIndex = 2
        self._label3.Text = "Miles:"
        self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        self._label3.Click += self.Label3Click
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.Color.CadetBlue
        self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label4.ForeColor = System.Drawing.SystemColors.ControlText
        self._label4.Location = System.Drawing.Point(52, 268)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(145, 64)
        self._label4.TabIndex = 3
        self._label4.Text = "Gallons:"
        self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.Color.CadetBlue
        self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label5.ForeColor = System.Drawing.SystemColors.ControlText
        self._label5.Location = System.Drawing.Point(52, 359)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(145, 64)
        self._label5.TabIndex = 4
        self._label5.Text = "MPG:"
        self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label6
        # 
        self._label6.BackColor = System.Drawing.Color.Azure
        self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label6.ForeColor = System.Drawing.SystemColors.ControlText
        self._label6.Location = System.Drawing.Point(203, 176)
        self._label6.Name = "label6"
        self._label6.Size = System.Drawing.Size(246, 64)
        self._label6.TabIndex = 5
        self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label7
        # 
        self._label7.BackColor = System.Drawing.Color.Azure
        self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label7.ForeColor = System.Drawing.SystemColors.ControlText
        self._label7.Location = System.Drawing.Point(203, 268)
        self._label7.Name = "label7"
        self._label7.Size = System.Drawing.Size(246, 64)
        self._label7.TabIndex = 6
        self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # label8
        # 
        self._label8.BackColor = System.Drawing.Color.Azure
        self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label8.ForeColor = System.Drawing.SystemColors.ControlText
        self._label8.Location = System.Drawing.Point(203, 359)
        self._label8.Name = "label8"
        self._label8.Size = System.Drawing.Size(246, 64)
        self._label8.TabIndex = 7
        self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.Location = System.Drawing.Point(455, 134)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(161, 64)
        self._button1.TabIndex = 8
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button2.Location = System.Drawing.Point(455, 244)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(161, 64)
        self._button2.TabIndex = 9
        self._button2.Text = "Clear"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # button3
        # 
        self._button3.Font = System.Drawing.Font("Microsoft YaHei", 21.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button3.Location = System.Drawing.Point(455, 358)
        self._button3.Name = "button3"
        self._button3.Size = System.Drawing.Size(161, 64)
        self._button3.TabIndex = 10
        self._button3.Text = "Exit"
        self._button3.UseVisualStyleBackColor = True
        self._button3.Click += self.Button3Click
        # 
        # comboBox1
        # 
        self._comboBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._comboBox1.FormattingEnabled = True
        self._comboBox1.Items.AddRange(System.Array[System.Object](
            ["1970 VW Bug",
            "1979 Firebird",
            "1980 Subaru",
            "1975 Cutlass"]))
        self._comboBox1.Location = System.Drawing.Point(349, 63)
        self._comboBox1.Name = "comboBox1"
        self._comboBox1.Size = System.Drawing.Size(248, 33)
        self._comboBox1.TabIndex = 11
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Beige
        self.ClientSize = System.Drawing.Size(635, 492)
        self.Controls.Add(self._comboBox1)
        self.Controls.Add(self._button3)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label8)
        self.Controls.Add(self._label7)
        self.Controls.Add(self._label6)
        self.Controls.Add(self._label5)
        self.Controls.Add(self._label4)
        self.Controls.Add(self._label3)
        self.Controls.Add(self._label1)
        self.Name = "MainForm"
        self.Text = "prog54a"
        self.ResumeLayout(False)


    def Label3Click(self, sender, e):
        pass

    def Button1Click(self, sender, e):
        miles = 1
        gal = 1
        car = self._comboBox1.Text 
        if car == "1970 VW Bug":
            miles = 286
            gal = 9
        elif car == "1979 Firebird":
            miles = 412
            gal = 40
        elif car == "1980 Subaru":
            miles = 361
            gal = 18
        elif car == "1975 Cutlass":
            miles = 161
            gal = 11
        else:
            MessageBox.Show("Invalid Car!")
            return
        mpg = round (float(miles)/float(gal) , 1)
        self._label7.Text = str(miles)
        self._label6.Text = str(gal)
        self._label8.Text = str(mpg)
        
        

    def Button2Click(self, sender, e):
        self._label7.Text = ""
        self._label6.Text = ""
        self._label8.Text = ""

    def Button3Click(self, sender, e):
        Application.Exit()