import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
    
    def InitializeComponent(self):
        self._groupBox1 = System.Windows.Forms.GroupBox()
        self._score1 = System.Windows.Forms.Label()
        self._score2 = System.Windows.Forms.Label()
        self._score3 = System.Windows.Forms.Label()
        self._scorebox1 = System.Windows.Forms.TextBox()
        self._scorebox2 = System.Windows.Forms.TextBox()
        self._scorebox3 = System.Windows.Forms.TextBox()
        self._Calculate = System.Windows.Forms.Button()
        self._Clear = System.Windows.Forms.Button()
        self._exit = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._groupBox1.SuspendLayout()
        self.SuspendLayout()
        # 
        # groupBox1
        # 
        self._groupBox1.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._groupBox1.Controls.Add(self._scorebox3)
        self._groupBox1.Controls.Add(self._scorebox2)
        self._groupBox1.Controls.Add(self._scorebox1)
        self._groupBox1.Controls.Add(self._score3)
        self._groupBox1.Controls.Add(self._score2)
        self._groupBox1.Controls.Add(self._score1)
        self._groupBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._groupBox1.Location = System.Drawing.Point(39, 13)
        self._groupBox1.Name = "groupBox1"
        self._groupBox1.Size = System.Drawing.Size(256, 232)
        self._groupBox1.TabIndex = 0
        self._groupBox1.TabStop = False
        self._groupBox1.Text = "Enter test scores"
        # 
        # score1
        # 
        self._score1.Location = System.Drawing.Point(24, 54)
        self._score1.Name = "score1"
        self._score1.Size = System.Drawing.Size(100, 23)
        self._score1.TabIndex = 0
        self._score1.Text = "Score 1:"
        # 
        # score2
        # 
        self._score2.Location = System.Drawing.Point(24, 94)
        self._score2.Name = "score2"
        self._score2.Size = System.Drawing.Size(100, 23)
        self._score2.TabIndex = 1
        self._score2.Text = "Score 2:"
        # 
        # score3
        # 
        self._score3.Location = System.Drawing.Point(24, 140)
        self._score3.Name = "score3"
        self._score3.Size = System.Drawing.Size(100, 23)
        self._score3.TabIndex = 2
        self._score3.Text = "Score 3:"
        # 
        # scorebox1
        # 
        self._scorebox1.Location = System.Drawing.Point(130, 46)
        self._scorebox1.Name = "scorebox1"
        self._scorebox1.Size = System.Drawing.Size(100, 31)
        self._scorebox1.TabIndex = 3
        # 
        # scorebox2
        # 
        self._scorebox2.Location = System.Drawing.Point(130, 94)
        self._scorebox2.Name = "scorebox2"
        self._scorebox2.Size = System.Drawing.Size(100, 31)
        self._scorebox2.TabIndex = 4
        # 
        # scorebox3
        # 
        self._scorebox3.Location = System.Drawing.Point(130, 140)
        self._scorebox3.Name = "scorebox3"
        self._scorebox3.Size = System.Drawing.Size(100, 31)
        self._scorebox3.TabIndex = 5
        # 
        # Calculate
        # 
        self._Calculate.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._Calculate.ForeColor = System.Drawing.Color.Lime
        self._Calculate.Location = System.Drawing.Point(13, 251)
        self._Calculate.Name = "Calculate"
        self._Calculate.Size = System.Drawing.Size(132, 44)
        self._Calculate.TabIndex = 1
        self._Calculate.Text = "Calculate"
        self._Calculate.UseVisualStyleBackColor = True
        self._Calculate.Click += self.CalculateClick
        # 
        # Clear
        # 
        self._Clear.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._Clear.ForeColor = System.Drawing.Color.Lime
        self._Clear.Location = System.Drawing.Point(152, 251)
        self._Clear.Name = "Clear"
        self._Clear.Size = System.Drawing.Size(170, 23)
        self._Clear.TabIndex = 2
        self._Clear.Text = "clear"
        self._Clear.UseVisualStyleBackColor = True
        self._Clear.Click += self.ClearClick
        # 
        # exit
        # 
        self._exit.Font = System.Drawing.Font("Microsoft Sans Serif", 8.25, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._exit.ForeColor = System.Drawing.Color.Lime
        self._exit.Location = System.Drawing.Point(152, 272)
        self._exit.Name = "exit"
        self._exit.Size = System.Drawing.Size(170, 23)
        self._exit.TabIndex = 3
        self._exit.Text = "Exit"
        self._exit.UseVisualStyleBackColor = True
        self._exit.Click += self.ExitClick
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(128, 255, 128)
        self._label1.Font = System.Drawing.Font("Microsoft YaHei", 15.75, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.ForeColor = System.Drawing.Color.Blue
        self._label1.Location = System.Drawing.Point(341, 13)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(241, 232)
        self._label1.TabIndex = 4
        # 
        # MainForm
        # 
        self.ClientSize = System.Drawing.Size(632, 306)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._exit)
        self.Controls.Add(self._Clear)
        self.Controls.Add(self._Calculate)
        self.Controls.Add(self._groupBox1)
        self.Name = "MainForm"
        self.Text = "pg198avgscore"
        self.Load += self.MainFormLoad
        self._groupBox1.ResumeLayout(False)
        self._groupBox1.PerformLayout()
        self.ResumeLayout(False)


    def MainFormLoad(self, sender, e):
        pass

    def CalculateClick(self, sender, e):
        scoreun = float(self._scorebox1.Text)
        scoredos = float(self._scorebox2.Text)
        scoretres = float(self._scorebox3.Text)
        averagescore= (scoreun+scoredos+scoretres)/3
        if averagescore >= 95:
            self._label1.Text = "Your average score was "+ str(averagescore) + " percent! Congratulations! Great Job!"
        elif averagescore >= 85:
            self._label1.Text = "Your average score was "+ str(averagescore) + " percent. Good Job!"
        else:
            self._label1.Text = "Your average score was "+ str(averagescore) + " percent."

    def ClearClick(self, sender, e):
        self._label1.Text=""

    def ExitClick(self, sender, e):
        Application.Exit()