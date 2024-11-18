import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
    def __init__(self):
        self.InitializeComponent()
        self.num1 = 0
        self.num2 = 0
        self.num3 = 0
    
    def InitializeComponent(self):
        self._components = System.ComponentModel.Container()
        resources = System.Resources.ResourceManager("slot_machine.MainForm", System.Reflection.Assembly.GetEntryAssembly())
        self._pictureBox1 = System.Windows.Forms.PictureBox()
        self._pictureBox2 = System.Windows.Forms.PictureBox()
        self._pictureBox3 = System.Windows.Forms.PictureBox()
        self._pictureBox4 = System.Windows.Forms.PictureBox()
        self._gamble = System.Windows.Forms.Button()
        self._therightchoice = System.Windows.Forms.Button()
        self._label1 = System.Windows.Forms.Label()
        self._textBox1 = System.Windows.Forms.TextBox()
        self._label2 = System.Windows.Forms.Label()
        self._collegefund = System.Windows.Forms.Label()
        self._progressBar1 = System.Windows.Forms.ProgressBar()
        self._pictureBox5 = System.Windows.Forms.PictureBox()
        self._pictureBox6 = System.Windows.Forms.PictureBox()
        self._pictureBox7 = System.Windows.Forms.PictureBox()
        self._pictureBox8 = System.Windows.Forms.PictureBox()
        self._pictureBox9 = System.Windows.Forms.PictureBox()
        self._pictureBox10 = System.Windows.Forms.PictureBox()
        self._pictureBox11 = System.Windows.Forms.PictureBox()
        self._timer1 = System.Windows.Forms.Timer(self._components)
        self._pictureBox1.BeginInit()
        self._pictureBox2.BeginInit()
        self._pictureBox3.BeginInit()
        self._pictureBox4.BeginInit()
        self._pictureBox5.BeginInit()
        self._pictureBox6.BeginInit()
        self._pictureBox7.BeginInit()
        self._pictureBox8.BeginInit()
        self._pictureBox9.BeginInit()
        self._pictureBox10.BeginInit()
        self._pictureBox11.BeginInit()
        self.SuspendLayout()
        # 
        # pictureBox1
        # 
        self._pictureBox1.BackColor = System.Drawing.Color.White
        self._pictureBox1.Location = System.Drawing.Point(62, 50)
        self._pictureBox1.Name = "pictureBox1"
        self._pictureBox1.Size = System.Drawing.Size(100, 209)
        self._pictureBox1.TabIndex = 0
        self._pictureBox1.TabStop = False
        # 
        # pictureBox2
        # 
        self._pictureBox2.BackColor = System.Drawing.Color.White
        self._pictureBox2.Location = System.Drawing.Point(190, 50)
        self._pictureBox2.Name = "pictureBox2"
        self._pictureBox2.Size = System.Drawing.Size(100, 209)
        self._pictureBox2.TabIndex = 1
        self._pictureBox2.TabStop = False
        # 
        # pictureBox3
        # 
        self._pictureBox3.BackColor = System.Drawing.Color.White
        self._pictureBox3.Location = System.Drawing.Point(325, 50)
        self._pictureBox3.Name = "pictureBox3"
        self._pictureBox3.Size = System.Drawing.Size(100, 209)
        self._pictureBox3.TabIndex = 2
        self._pictureBox3.TabStop = False
        # 
        # pictureBox4
        # 
        self._pictureBox4.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox4.Image = resources.GetObject("pictureBox4.Image")
        self._pictureBox4.Location = System.Drawing.Point(62, 302)
        self._pictureBox4.Name = "pictureBox4"
        self._pictureBox4.Size = System.Drawing.Size(363, 156)
        self._pictureBox4.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox4.TabIndex = 3
        self._pictureBox4.TabStop = False
        # 
        # gamble
        # 
        self._gamble.BackgroundImage = resources.GetObject("gamble.BackgroundImage")
        self._gamble.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._gamble.Location = System.Drawing.Point(515, 50)
        self._gamble.Name = "gamble"
        self._gamble.Size = System.Drawing.Size(221, 261)
        self._gamble.TabIndex = 4
        self._gamble.UseVisualStyleBackColor = True
        self._gamble.Click += self.GambleClick
        # 
        # therightchoice
        # 
        self._therightchoice.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._therightchoice.Location = System.Drawing.Point(554, 317)
        self._therightchoice.Name = "therightchoice"
        self._therightchoice.Size = System.Drawing.Size(134, 40)
        self._therightchoice.TabIndex = 5
        self._therightchoice.Text = "Pickpocket"
        self._therightchoice.UseVisualStyleBackColor = True
        self._therightchoice.Click += self.TherightchoiceClick
        # 
        # label1
        # 
        self._label1.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label1.Location = System.Drawing.Point(515, 378)
        self._label1.Name = "label1"
        self._label1.Size = System.Drawing.Size(100, 23)
        self._label1.TabIndex = 6
        self._label1.Text = "Bet:"
        # 
        # textBox1
        # 
        self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._textBox1.Location = System.Drawing.Point(567, 375)
        self._textBox1.Name = "textBox1"
        self._textBox1.Size = System.Drawing.Size(100, 31)
        self._textBox1.TabIndex = 7
        # 
        # label2
        # 
        self._label2.BackColor = System.Drawing.Color.FromArgb(192, 255, 255)
        self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._label2.Location = System.Drawing.Point(499, 421)
        self._label2.Name = "label2"
        self._label2.Size = System.Drawing.Size(100, 23)
        self._label2.TabIndex = 9
        self._label2.Text = "Cash:"
        # 
        # collegefund
        # 
        self._collegefund.BackColor = System.Drawing.Color.FromArgb(192, 255, 192)
        self._collegefund.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
        self._collegefund.Location = System.Drawing.Point(567, 421)
        self._collegefund.Name = "collegefund"
        self._collegefund.Size = System.Drawing.Size(100, 23)
        self._collegefund.TabIndex = 10
        self._collegefund.Text = "100"
        # 
        # progressBar1
        # 
        self._progressBar1.Location = System.Drawing.Point(456, 449)
        self._progressBar1.Maximum = 15000
        self._progressBar1.Name = "progressBar1"
        self._progressBar1.Size = System.Drawing.Size(267, 23)
        self._progressBar1.TabIndex = 11
        # 
        # pictureBox5
        # 
        self._pictureBox5.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox5.BackgroundImage = resources.GetObject("pictureBox5.BackgroundImage")
        self._pictureBox5.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox5.Location = System.Drawing.Point(72, 302)
        self._pictureBox5.Name = "pictureBox5"
        self._pictureBox5.Size = System.Drawing.Size(49, 39)
        self._pictureBox5.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox5.TabIndex = 12
        self._pictureBox5.TabStop = False
        self._pictureBox5.Visible = False
        # 
        # pictureBox6
        # 
        self._pictureBox6.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox6.BackgroundImage = resources.GetObject("pictureBox6.BackgroundImage")
        self._pictureBox6.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox6.Location = System.Drawing.Point(127, 302)
        self._pictureBox6.Name = "pictureBox6"
        self._pictureBox6.Size = System.Drawing.Size(49, 39)
        self._pictureBox6.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox6.TabIndex = 13
        self._pictureBox6.TabStop = False
        self._pictureBox6.Visible = False
        # 
        # pictureBox7
        # 
        self._pictureBox7.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox7.BackgroundImage = resources.GetObject("pictureBox7.BackgroundImage")
        self._pictureBox7.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox7.Location = System.Drawing.Point(190, 302)
        self._pictureBox7.Name = "pictureBox7"
        self._pictureBox7.Size = System.Drawing.Size(49, 39)
        self._pictureBox7.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox7.TabIndex = 14
        self._pictureBox7.TabStop = False
        self._pictureBox7.Visible = False
        # 
        # pictureBox8
        # 
        self._pictureBox8.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox8.BackgroundImage = resources.GetObject("pictureBox8.BackgroundImage")
        self._pictureBox8.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox8.Location = System.Drawing.Point(245, 302)
        self._pictureBox8.Name = "pictureBox8"
        self._pictureBox8.Size = System.Drawing.Size(49, 39)
        self._pictureBox8.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox8.TabIndex = 15
        self._pictureBox8.TabStop = False
        self._pictureBox8.Visible = False
        # 
        # pictureBox9
        # 
        self._pictureBox9.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox9.BackgroundImage = resources.GetObject("pictureBox9.BackgroundImage")
        self._pictureBox9.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox9.Location = System.Drawing.Point(300, 302)
        self._pictureBox9.Name = "pictureBox9"
        self._pictureBox9.Size = System.Drawing.Size(48, 39)
        self._pictureBox9.SizeMode = System.Windows.Forms.PictureBoxSizeMode.AutoSize
        self._pictureBox9.TabIndex = 16
        self._pictureBox9.TabStop = False
        self._pictureBox9.Visible = False
        # 
        # pictureBox10
        # 
        self._pictureBox10.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox10.BackgroundImage = resources.GetObject("pictureBox10.BackgroundImage")
        self._pictureBox10.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox10.Location = System.Drawing.Point(72, 405)
        self._pictureBox10.Name = "pictureBox10"
        self._pictureBox10.Size = System.Drawing.Size(49, 39)
        self._pictureBox10.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox10.TabIndex = 17
        self._pictureBox10.TabStop = False
        self._pictureBox10.Visible = False
        # 
        # pictureBox11
        # 
        self._pictureBox11.BackColor = System.Drawing.Color.FromArgb(255, 192, 192)
        self._pictureBox11.BackgroundImage = resources.GetObject("pictureBox11.BackgroundImage")
        self._pictureBox11.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        self._pictureBox11.Location = System.Drawing.Point(127, 405)
        self._pictureBox11.Name = "pictureBox11"
        self._pictureBox11.Size = System.Drawing.Size(49, 39)
        self._pictureBox11.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage
        self._pictureBox11.TabIndex = 18
        self._pictureBox11.TabStop = False
        self._pictureBox11.Visible = False
        # 
        # MainForm
        # 
        self.BackColor = System.Drawing.Color.FromArgb(255, 255, 192)
        self.ClientSize = System.Drawing.Size(804, 484)
        self.Controls.Add(self._pictureBox11)
        self.Controls.Add(self._pictureBox10)
        self.Controls.Add(self._pictureBox9)
        self.Controls.Add(self._pictureBox8)
        self.Controls.Add(self._pictureBox7)
        self.Controls.Add(self._pictureBox6)
        self.Controls.Add(self._pictureBox5)
        self.Controls.Add(self._progressBar1)
        self.Controls.Add(self._collegefund)
        self.Controls.Add(self._label2)
        self.Controls.Add(self._textBox1)
        self.Controls.Add(self._label1)
        self.Controls.Add(self._therightchoice)
        self.Controls.Add(self._gamble)
        self.Controls.Add(self._pictureBox4)
        self.Controls.Add(self._pictureBox3)
        self.Controls.Add(self._pictureBox2)
        self.Controls.Add(self._pictureBox1)
        self.Name = "MainForm"
        self.Text = "slot machine"
        self._pictureBox1.EndInit()
        self._pictureBox2.EndInit()
        self._pictureBox3.EndInit()
        self._pictureBox4.EndInit()
        self._pictureBox5.EndInit()
        self._pictureBox6.EndInit()
        self._pictureBox7.EndInit()
        self._pictureBox8.EndInit()
        self._pictureBox9.EndInit()
        self._pictureBox10.EndInit()
        self._pictureBox11.EndInit()
        self.ResumeLayout(False)
        self.PerformLayout()




    def CollegefundClick(self, sender, e):
        pass

    def TherightchoiceClick(self, sender, e):
        rnd = System.Random()
        money= rnd.Next(1, 51)
        if money > 25:
            MessageBox.Show("You failed to steal money! yay!")
        else:
            funds = float(self.collegefund.Text)
            self.collegefund.Text = str(round(funds + money, 2))
                
        
        pass
    

    def GambleClick(self, sender, e):
        im1 = self._pictureBox5.BackroundImage
        im2 = self._pictureBox6.BackroundImage
        im3 = self._pictureBox7.BackroundImage
        im4 = self._pictureBox8.BackroundImage
        im5 = self._pictureBox9.BackroundImage
        levoff = self._pictureBox11.BackroundImage
        levon = self._pictureBox10.BackroundImage
        rnd = System.Random()
        num1 = 0
        num2 = 0
        num3 = 0
        
        if self._textBox1.Text == "":
            MessageBox.Show("You cant play without a bet, silly")
            return
        money = float(slef._collegefund.Text)
        bet = float(self._textbox1.Text)
        newmoney = money - bet
        if money == 0:
            MessageBox.Show("Youre outta money kid. Go steal some or something, but sure as hell dont stop playing.")
        elif bet < 1:
            MessageBox.Show("C'mon kid, ya broke? At least bet a dollar!")
        elif bet > money:
            MessageBox.Show("Youre supposed to bluff your cards, not whether or not you've got the money.")
        pass