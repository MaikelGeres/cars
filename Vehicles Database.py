"""


"""

import os
import vehicle

def record_all_vehicles(file_pth):
	"""
	Reads all vehicles from the text file and creates objects
	"""
	
	# check if it is a valid file
	if not os.path.isfile(file_pth):
		#
		raise Exception('{} is not a valid file'.format(file_pth))
		
	# open the file and read vehicles props
	all_vehicles
	with open(file_pth) as vhs_db_file:
		
		# loop thru vehicles
		for vh in vhs_db_file:
			
			# split
			vh_str = vh.split(',')
			
			vehicle(vh_str[0], vh_str[1], vh_str[2], vh_str[3], vh_str[4])
		
	# all vehicles were registered
	print('{}/n'.format(x for x in vehicle.all_vehicles_in_city))
	

tmp_pth = r'C:\Users\Maikel Geres\Documents\GitHub\cars\db.txt'
record_all_vehicles(tmp_pth)
