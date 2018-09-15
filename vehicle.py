"""
vehicles common funtions and classes
"""

class repairs:
	"""
	Repair object
	"""
	
	def __init__(self, arg_vh_obj, arg_rpr_loc, arg_rpr_description, arg_rpr_cost, arg_rpr_time):
		"""
		Creates a repair object
		"""
		
		self.rpr_vh = arg_vh_obj
		self.rpr_location = str(arg_rpr_loc)
		self.rpr_description = str(arg_rpr_description)
		self.rpr_cost = float(arg_rpr_cost)
		self.rpr_time = str(arg_rpr_time)
		
		
	def func1(self):
		pass
	
	def func2(self):
		pass
		
	def func3(self):
		pass

class vehicle:
	"""
	A class for the basic objects and methods for any vehicle
	"""
	
	# a list of all the vehicles in the city
	all_vehicles_in_city = []
	
	
	def __init__(self, sn, mk, mdl, yr, plt_num):
		"""
		Constructor to create a vhecile object with the make, model, and the plate number
		"""
		
		# main props
		self.vh_sn = str(sn)
		self.vh_mk = str(mk)
		self.vh_mk = str(mdl)
		self.vh_yr = str(yr)
		self.vh_mk = str(plt_num)
		
		# a list of vehicle owners objects
		self.vh_owners = []
		
		# save the vehicle in the all vehicles list
		all_vehicles_in_city.append(self)
		
	
	def set_owner(self, vh_owner):
		"""
		Sets the current vehicle owner object
		"""
		
		self.vh_owners.append(vh_owner))
		







