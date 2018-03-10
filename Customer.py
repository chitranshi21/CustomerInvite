class Customer:
	"""
	this is a skeleton class for the customer object
	"""
	def __init__(
		self,
		latitude=None,
		longitude=None,
		name=None,
		user_id=None
		):
		"""
		Initialize the instance variable
		"""
		self.latitude = latitude
		self.longitude = longitude
		self.name = name
		self.user_id = user_id
		
	