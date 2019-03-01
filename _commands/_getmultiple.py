class Command:
	def do_getmultiple(self,remotepath):
		"""
        Command to perform get files command from the remote server.

        Args:
            filepath - path of the file to be deleted from the remote server.
        """
		file_list= remotepath.split(" ")
		if len(file_list) < 1:
			print ("Atleast one file/path expected")
		else:
		    try: 
			for file in file_list:
 		            response = self._perform_ftp_command('get', file)
		    except IOError as e:
			  print(e)
