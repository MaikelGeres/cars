"""
vehicles common funtions and classes
"""

class vehicle:
	"""
	A class for the basic objects and methods for any vehicle
	"""
	
	def __init__(self, sr, mk, mdl, yr, plt_num):
		"""
		Constructor to create a vhecile object with the make, model, and the plate number
		"""
		
		# main props
		self.vh_sn = str(sn)
		self.vh_mk = str(mk)
		self.vh_mk = str(mdl)
		self.vh_yr = str(yr)
		self.vh_mk = str(plt_num)
		
		# owners
		self.vh_owners = []
		
	
	def cur_owner_full_name(self, person_name):
		"""
		Sets the current vehicle owner full name
		"""
		
		self.vh_owners.append(str(person_name))
		





