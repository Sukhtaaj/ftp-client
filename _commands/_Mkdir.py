import sys, os
class Command:
    def do_mkdir(self, input_directory):
        """
        Command to create directory with name of new directory

	Args:
		input_directory (str): Name of directory you want to create
        """
	if not input_directory:
		print("you must enter in one argument")
	else:
		directory = self._perform_ftp_command('lexists',input_directory)
		if directory:
			print("duplicate found")
		else:
			self._perform_ftp_command('mkdir',input_directory,777)
			print(input_directory) #prints the name
