import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._groupBox2 = System.Windows.Forms.GroupBox()
        self._checkBox1 = System.Windows.Forms.CheckBox()
        self._checkBox2 = System.Windows.Forms.CheckBox()
        self._checkBox3 = System.Windows.Forms.CheckBox()
        self._radioButton1 = System.Windows.Forms.RadioButton()
        self._radioButton2 = System.Windows.Forms.RadioButton()
        self._radioButton3 = System.Windows.Forms.RadioButton()
        self._label1 = System.Windows.Forms.Label()
        self._button1 = System.Windows.Forms.Button()
        self._groupBox1.SuspendLayout()
        self._groupBox2.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._groupBox1.Controls.Add(self._radioButton3)
        self._groupBox1.Controls.Add(self._radioButton2)
        self._groupBox1.Controls.Add(self._radioButton1)
        self._groupBox1.Font = System.Drawing.Font("Franklin Gothic Demi", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(12, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(282, 311)
        self._groupBox1.TabIndex = 1
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Radio Buttons"
        self._groupBox1.Enter += self.GroupBox1Enter
        # 
        # groupBox2
        # 
        self._groupBox2.BackColor = System.Drawing.Color.FromArgb(255, 224, 192)
        self._groupBox2.Controls.Add(self._checkBox3)
        self._groupBox2.Controls.Add(self._checkBox2)
        self._groupBox2.Controls.Add(self._checkBox1)
        self._groupBox2.Font = System.Drawing.Font("Rockwell", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox2.Location = System.Drawing.Point(300, 13)
        self._groupBox2.Name = "groupBox2"
        self._groupBox2.Size = System.Drawing.Size(304, 311)
        self._groupBox2.TabIndex = 1
        self._groupBox2.TabStop = False
        self._groupBox2.Text = "Check Boxes"
        # 
        # checkBox1
        # 
        self._checkBox1.Location = System.Drawing.Point(19, 58)
        self._checkBox1.Name = "checkBox1"
        self._checkBox1.Size = System.Drawing.Size(240, 24)
        self._checkBox1.TabIndex = 0
        self._checkBox1.Text = "Choice 4"
        self._checkBox1.UseVisualStyleBackColor = True
        self._checkBox1.CheckedChanged += self.CheckBox1CheckedChanged
        # 
        # checkBox2
        # 
        self._checkBox2.Location = System.Drawing.Point(19, 131)
        self._checkBox2.Name = "checkBox2"
        self._checkBox2.Size = System.Drawing.Size(240, 24)
        self._checkBox2.TabIndex = 1
        self._checkBox2.Text = "Choice 5"
        self._checkBox2.UseVisualStyleBackColor = True
        self._checkBox2.CheckedChanged += self.CheckBox2CheckedChanged
        # 
        # checkBox3
        # 
        self._checkBox3.Location = System.Drawing.Point(19, 205)
        self._checkBox3.Name = "checkBox3"
        self._checkBox3.Size = System.Drawing.Size(240, 24)
        self._checkBox3.TabIndex = 2
        self._checkBox3.Text = "Choice 6"
        self._checkBox3.UseVisualStyleBackColor = True
        self._checkBox3.CheckedChanged += self.CheckBox3CheckedChanged
        # 
        # radioButton1
        # 
        self._radioButton1.Location = System.Drawing.Point(6, 58)
        self._radioButton1.Name = "radioButton1"
        self._radioButton1.Size = System.Drawing.Size(181, 24)
        self._radioButton1.TabIndex = 0
        self._radioButton1.TabStop = True
        self._radioButton1.Text = "Choice 1"
        self._radioButton1.UseVisualStyleBackColor = True
        self._radioButton1.CheckedChanged += self.RadioButton1CheckedChanged
        # 
        # radioButton2
        # 
        self._radioButton2.Location = System.Drawing.Point(6, 131)
        self._radioButton2.Name = "radioButton2"
        self._radioButton2.Size = System.Drawing.Size(181, 24)
        self._radioButton2.TabIndex = 1
        self._radioButton2.TabStop = True
        self._radioButton2.Text = "Choice 2"
        self._radioButton2.UseVisualStyleBackColor = True
        self._radioButton2.CheckedChanged += self.RadioButton2CheckedChanged
        # 
        # radioButton3
        # 
        self._radioButton3.Location = System.Drawing.Point(6, 205)
        self._radioButton3.Name = "radioButton3"
        self._radioButton3.Size = System.Drawing.Size(181, 24)
        self._radioButton3.TabIndex = 2
        self._radioButton3.TabStop = True
        self._radioButton3.Text = "Choice 3"
        self._radioButton3.UseVisualStyleBackColor = True
        self._radioButton3.CheckedChanged += self.RadioButton3CheckedChanged
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self._label1.Font = System.Drawing.Font("Modern No. 20", 15.749999, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(611, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(240, 311)
        self._label1.TabIndex = 2
        self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
        # 
        # button1
        # 
        self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 20.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._button1.ForeColor = System.Drawing.Color.Red
        self._button1.Location = System.Drawing.Point(858, 13)
        self._button1.Name = "button1"
        self._button1.Size = System.Drawing.Size(45, 311)
        self._button1.TabIndex = 3
        self._button1.Text = "EXIT"
        self._button1.UseVisualStyleBackColor = True
        self._button1.Click += self.Button1Click
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.Blue
        self.ClientSize = System.Drawing.Size(912, 330)
        self.Controls.Add(self._button1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._groupBox2)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg247radio"
        self._groupBox1.ResumeLayout(False)
        self._groupBox2.ResumeLayout(False)
        self.ResumeLayout(False)


    def CheckBox2CheckedChanged(self, sender, e):
        self.msg_str()
    
    def msg_str(self):
        message=""
        if self._radioButton1.Checked:
            message = "You chose Choice 1"
        elif self._radioButton2.Checked:
            message = "You chose Choice 2"
        elif self._radioButton3.Checked:
            message = "You chose Choice 3"
        
        if self._checkBox1.Checked:
            message += " and Choice 4"
        if self._checkBox2.Checked:
            message += " and Choice 5"
        if self._checkBox3.Checked:
            message += " and Choice 6"
        message+="."
        self._label1.Text = message
        
        
        

    def RadioButton1CheckedChanged(self, sender, e):
        self.msg_str()

    def Button1Click(self, sender, e):
        Application.Exit()

    def RadioButton2CheckedChanged(self, sender, e):
        self.msg_str()

    def GroupBox1Enter(self, sender, e):
        pass

    def RadioButton3CheckedChanged(self, sender, e):
        self.msg_str()

    def CheckBox1CheckedChanged(self, sender, e):
        self.msg_str()

    def CheckBox3CheckedChanged(self, sender, e):
        self.msg_str()