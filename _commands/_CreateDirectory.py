class Command:
    def do_createdirectory(self, input_directory):
        """
        Command to create directory with name of new directory

	Args:
		input_directory (str): Name of directory you want to create
        """
#	self._perform_ftp_command('mkdir',input_directory,777)
#	print(input_directory)
#	response = self._perform_ftp_command('listdir')
#	print(response)
		directory_mode = input_directory.split(" ")
		if len(directory_mode)!=2:
			print "Mkdir command expects exactly two arguments"
		else:
			try:
				os.rename(directory_mode[0], directory_mode[1])
			except IOError as e:
				print(e)
