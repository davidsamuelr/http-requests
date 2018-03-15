from conf import get_log_file

def to_save(ln):

	f = open(get_log_file(), 'r')
	text = f.readlines()
	text.append(ln + '\n')

	f = open(get_log_file(), 'w')
	f.writelines(text)

	f.close()





