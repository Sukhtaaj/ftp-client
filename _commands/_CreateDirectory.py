class Command:
    def do_createdirectory(self, input_directory):
        """
        Command to create directory with name of new directory

	Args:
		input_directory (str): Name of directory you want to create
        """
	print(input_directory)
	response = self._perform_ftp_command('listdir')
	print(response)

