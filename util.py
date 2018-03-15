from conf import get_log_file

def create_log_file():

	f = open(get_log_file(), "w")

	f.close()