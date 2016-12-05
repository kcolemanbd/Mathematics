# Simple-Absolute-Solver-in-Python


from System import *
from System.Collections.Generic import *
from System.ComponentModel import *
from System.Data import *
from System.Drawing import *
from System.Linq import *
from System.Text import *
from System.Windows.Forms import *

class Form1(Form):
	def __init__(self):
		self.InitializeComponent()

	def button1_Click(self, sender, e):
		abs = 0
		solvedNumber = 0
		if not int.TryParse(textBox1.Text, ):
			MessageBox.Show(“Enter Number Here“)
			textBox1.Text = ""
			textBox1.Focus()
		else:
			abs = Convert.ToInt32(textBox1.Text)
			solvedNumber = Math.Abs(abs)
			label3.Text = "The absolute value of " + abs + " is " + solvedNumber + "."

	def button2_Click(self, sender, e):
		textBox1.Text = ""
		label3.Text = " "
		textBox1.Focus()
