import sys
import os


def run_test():
	os.system("python customerInviteTest.py")

def run_customerInvite():
	os.system("python customerInvite.py")


def main():
	arguments = sys.argv[1:]
	
	if len(arguments) < 1:
		run_test()
		run_customerInvite()

	elif arguments[0] == "test":
		run_test()
	
	elif arguments[0] == "run":
		run_customerInvite()
	
	else:
		print("invalid arguments please use either 'test' or 'run' ")



if __name__ == '__main__':
	main()

