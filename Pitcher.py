class Pitcher:
	Name = ""
	WHIP = 0
	ERAminus = 0
	FIPminus = 0

	def __init__(self, name, whip, ERAminus, FIPminus):
		self.Name = name
		self.WHIP = whip
		self.ERAminus = ERAminus
		self.FIPminus = FIPminus

	def __str__(self):
		print('Name: ', self.Name)
		print('WHIP: ', self.WHIP)
		print('ERA-: ', self.ERAminus)
		print('FIP-: ', self.FIPminus)