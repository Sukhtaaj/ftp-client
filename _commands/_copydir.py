class Command:
	def do_copydir(self, directory_path):
		"""
        Command to perform get files command from the remote server.

        Args:
        
        """
		dir_path = directory_path.split(" ")
		if len(dir_path) != 2:
			print ("command expects exactly two arguments")
		else:
		    try: 
			    response = self._perform_ftp_command('put_r',dir_path[0], dir_path[1] )
		    except IOError as e:
			    print(e)