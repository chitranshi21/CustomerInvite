import json
import os
from math import sin, cos, sqrt, atan2, radians
from Customer import Customer

# This is the main app file it runs with some default values
# you can change the location of the data file by changing 
# CUSTOMER_LIST_FILE_PATH variable declared on at the top

# It goes with the following logic: 

# read file and get customer list
# Iterate Customer list and find distance from Dublin office
# add Customers staying within 100 KM from office
# print customer list.


# Default value for the file path
CUSTOMER_LIST_FILE_PATH = "/data/customers.json"

# approximate radius of earth in km
EARTH_RADIUS = 6373.0

# Customer distance upper bound
DISTANCE_RANGE = 100.0

# Office Coordinates 
OFFICE_LAT = 53.339428
OFFICE_LONG = -6.257664

# Invite Letter template
INVITE_TEMPLATE = "Mr./Mrs. {}, user_id {}, Intercom invites you to join us at our Dublin office."

def get_customer_list(customer_file_path):
	"""
	Reads the file and returns a list of customer:
	Should throw error if json is not parsable.
	and work for the rest of the cases
	"""
	absolute_file_path = os.getcwd() + customer_file_path
	customer_list = []

	with open(absolute_file_path, "r") as file:
		for line in file:
			try:
				customer_dict = json.loads(line)
				customer = Customer(**customer_dict)
				customer_list.append(customer)
			except Exception as error:
				print("Error in get_customer_list ", error)

	return customer_list


def generate_customer_invite_list(
				customer_list, 
				office_lat,
				office_long,
				distance_range=100.0
				):
	"""
	This function will return a list of customer object
	sorted by user id within 100 KM of dublin office
	"""
	office_lat = radians(OFFICE_LAT)
	office_long = radians(OFFICE_LONG)

	customer_invite_list = []

	for customer in customer_list:
		customer_lat = radians(float(customer.latitude))
		customer_long = radians(float(customer.longitude))

		distance = _get_distance(
							office_lat,
							office_long,
							customer_lat,
							customer_long)
		
		if distance < distance_range:
			customer_invite_list.append(customer)
	
	customer_invite_list.sort(key=_sort_login)

	return customer_invite_list


def _sort_login(customer):
	"""
	Custom Sort method for the list sorting.
	"""
	return customer.user_id


def _get_distance(origin_lat, origin_long, away_lat, away_long):
	"""
	return the distance between two points on curved surface.
	Formula from https://en.wikipedia.org/wiki/Great-circle_distance
	"""
	dlat = away_lat - origin_lat
	dlong = away_long - origin_long
	a = sin(dlat / 2)**2 + cos(origin_lat) * cos(away_lat) * sin(dlong / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = EARTH_RADIUS * c

	return distance


def run():
	customer_list = []
	try:
		customer_list = get_customer_list(CUSTOMER_LIST_FILE_PATH)
	except FileNotFoundError as error:
		print("Couldn't find the file at specified location", error)

	customer_invite_list = generate_customer_invite_list(
				customer_list,
				OFFICE_LAT,
				OFFICE_LONG,
				DISTANCE_RANGE)

	for customer in customer_invite_list:
		print(INVITE_TEMPLATE.format(customer.name, customer.user_id))



if __name__ == '__main__':
	run()
