import os
def c():
	def addToClipBoard(text):
	    command = 'echo ' + text.strip() + '| clip'
	    os.system(command)

	Input = input("Input: ")
	Output = Input[0]+"".join([word.lower() for count, word in enumerate(Input) if count != 0])

	addToClipBoard(Output)
	print("("+Output+")", "Converted and copied to clipboard")

while True:
	try:
		c()
	except:
		print("invalid input")