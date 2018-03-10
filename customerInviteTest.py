import unittest
import customerInvite
from math import radians
from Customer import Customer


# Office Coordinates 
OFFICE_LAT = 53.339428
OFFICE_LONG = -6.257664

# Default value for the file path
CUSTOMER_LIST_FILE_PATH = "/data/customers.json"


class CustomerInviteTest(unittest.TestCase):
	def test_get_distance(self):
		lat = radians(52.986375)
		lon = radians(-6.043701)

		self.assertEqual(customerInvite._get_distance(radians(OFFICE_LAT),radians(OFFICE_LONG),lat,lon),41.781837641944584)

	def test_generate_customer_invite_list(self):
		customer = Customer()
		customer.latitude = 52.986375
		customer.longitude = -6.043701
		customer.name = "Test Name"
		customer.user_id = "test_user_id"
		customer_list = []
		customer_list.append(customer)
		self.assertListEqual(customerInvite.generate_customer_invite_list(customer_list,OFFICE_LAT,OFFICE_LONG), customer_list)

	
	def test_get_customer_list(self):
		self.assertEqual(len(customerInvite.get_customer_list(CUSTOMER_LIST_FILE_PATH)), 32)


def main():
	unittest.main()

if __name__ == '__main__':
	main()

