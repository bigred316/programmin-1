import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._radioButton4 = System.Windows.Forms.RadioButton()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._groupBox3 = System.Windows.Forms.GroupBox()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._groupBox4 = System.Windows.Forms.GroupBox()
        self._label2 = System.Windows.Forms.Label()
        self._label3 = System.Windows.Forms.Label()
        self._label4 = System.Windows.Forms.Label()
        self._label5 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._button2 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self._groupBox3.SuspendLayout()
        self._groupBox4.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox1.Controls.Add(self._radioButton4)
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(13, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(266, 222)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Membership type"
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(28, 41)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(104, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Adult"
        self._radioButton1.UseVisualStyleBackColor = True
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(28, 81)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(175, 31)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Child (Under 12)"
        self._radioButton2.UseVisualStyleBackColor = True
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(28, 118)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(104, 24)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Student"
        self._radioButton3.UseVisualStyleBackColor = True
        # 
        # radioButton4
        # 
        self._radioButton4.Location = System.Drawing.Point(28, 157)
        self._radioButton4.Name = "radioButton4"
        self._radioButton4.Size = System.Drawing.Size(213, 29)
        self._radioButton4.TabIndex = 3
        self._radioButton4.TabStop = True
        self._radioButton4.Text = "Senior Citizen (65+)"
        self._radioButton4.UseVisualStyleBackColor = True
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox2.Controls.Add(self._textBox1)
        self._groupBox2.Controls.Add(self._label1)
        self._groupBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(12, 259)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(266, 222)
        self._groupBox2.TabIndex = 4
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Membership length"
        # 
        # label1
        # 
        self._label1.Location = System.Drawing.Point(6, 67)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(254, 77)
        self._label1.TabIndex = 0
        self._label1.Text = """Input number of months you want your membership to last:
"""
        # 
        # textBox1
        # 
        self._textBox1.Location = System.Drawing.Point(50, 115)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(172, 29)
        self._textBox1.TabIndex = 1
        # 
        # groupBox3
        # 
        self._groupBox3.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox3.Controls.Add(self._checkBox3)
        self._groupBox3.Controls.Add(self._checkBox2)
        self._groupBox3.Controls.Add(self._checkBox1)
        self._groupBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox3.Location = System.Drawing.Point(314, 13)
        self._groupBox3.Name = "groupBox3"
        self._groupBox3.Size = System.Drawing.Size(266, 222)
        self._groupBox3.TabIndex = 4
        self._groupBox3.TabStop = False
        self._groupBox3.Text = "Add-Ons"
        # 
        # checkBox1
        # 
        self._checkBox1.Location = System.Drawing.Point(16, 40)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(124, 35)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Yoga"
        self._checkBox1.UseVisualStyleBackColor = True
        # 
        # checkBox2
        # 
        self._checkBox2.Location = System.Drawing.Point(16, 81)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(124, 35)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Karate"
        self._checkBox2.UseVisualStyleBackColor = True
        # 
        # checkBox3
        # 
        self._checkBox3.Location = System.Drawing.Point(16, 122)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(199, 35)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Personal Trainer"
        self._checkBox3.UseVisualStyleBackColor = True
        # 
        # groupBox4
        # 
        self._groupBox4.BackColor = System.Drawing.SystemColors.ActiveCaption
        self._groupBox4.Controls.Add(self._label5)
        self._groupBox4.Controls.Add(self._label4)
        self._groupBox4.Controls.Add(self._label3)
        self._groupBox4.Controls.Add(self._label2)
        self._groupBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox4.Location = System.Drawing.Point(314, 259)
        self._groupBox4.Name = "groupBox4"
        self._groupBox4.Size = System.Drawing.Size(266, 222)
        self._groupBox4.TabIndex = 5
        self._groupBox4.TabStop = False
        self._groupBox4.Text = "Totals"
        # 
        # label2
        # 
        self._label2.Location = System.Drawing.Point(6, 41)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(189, 23)
        self._label2.TabIndex = 0
        self._label2.Text = "Monthly Fee:"
        # 
        # label3
        # 
        self._label3.Location = System.Drawing.Point(6, 81)
        self._label3.Name = "label3"
        self._label3.Size = System.Drawing.Size(100, 23)
        self._label3.TabIndex = 1
        self._label3.Text = "Total:"
        # 
        # label4
        # 
        self._label4.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label4.Location = System.Drawing.Point(129, 41)
        self._label4.Name = "label4"
        self._label4.Size = System.Drawing.Size(117, 23)
        self._label4.TabIndex = 2
        # 
        # label5
        # 
        self._label5.BackColor = System.Drawing.SystemColors.ButtonFace
        self._label5.Location = System.Drawing.Point(60, 81)
        self._label5.Name = "label5"
        self._label5.Size = System.Drawing.Size(117, 23)
        self._label5.TabIndex = 3
        # 
        # button1
        # 
        self._button1.Location = System.Drawing.Point(62, 488)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(203, 25)
        self._button1.TabIndex = 6
        self._button1.Text = "Calculate"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # button2
        # 
        self._button2.Location = System.Drawing.Point(320, 487)
        self._button2.Name = "button2"
        self._button2.Size = System.Drawing.Size(203, 25)
        self._button2.TabIndex = 7
        self._button2.Text = "Exit"
        self._button2.UseVisualStyleBackColor = True
        self._button2.Click += self.Button2Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.SystemColors.Highlight
        self.ClientSize = System.Drawing.Size(605, 525)
        self.Controls.Add(self._button2)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._groupBox4)
        self.Controls.Add(self._groupBox3)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg250 membership fee"
        self.Load += self.MainFormLoad
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self._groupBox2.PerformLayout()
        self._groupBox3.ResumeLayout(False)
        self._groupBox4.ResumeLayout(False)
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def Button2Click(self, sender, e):
        Application.Exit()

    def Button1Click(self, sender, e):
        basefee = 0.0
        months = int(self._textBox1.Text)
        
        if months < 1 or months > 24:
            MessageBox.Show("Please input a month value greater than 0 and less than 25")
            return
        
        if self._radioButton1.Checked == True:
            basefee=40
        if self._radioButton2.Checked == True:
            basefee=20    
        if self._radioButton3.Checked == True:
            basefee=25
        if self._radioButton4.Checked == True:
            basefee=30
        if self._checkBox1.Checked == True:
            basefee += 10
        if self._checkBox2.Checked == True:
            basefee += 30
        if self._checkBox3.Checked == True:
            basefee += 50
        if months <= 3:
            basefee -= basefee * 0 
        if months in range(4, 7):
            basefee -= basefee * 0.05
        if months in range(7, 10):
            basefee -= basefee * 0.08
        if months >= 10:
            basefee -= basefee * 0.1
        self._label4.Text = str(basefee)
        self._label5.Text = str(basefee * months)
        
            
        
            
        


        