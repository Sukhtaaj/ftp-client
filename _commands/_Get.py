class Command:
	def do_get(self,remotepath):
		"""
        Command to get file(s) from the connectd FTP Host

        Args:
            filepath - path(s) of the file(s) to be downloaded from the remote server.
        """
		file_list= remotepath.split(" ")
		if len(file_list) < 1:
			print ("Atleast one file/path expected")
		else:
		        for file in file_list:
                                try:
 		                        response = self._perform_ftp_command('get', file)
                                        print("Downloaded file: " + file)
		                except IOError as e:
                                        print "Failure"
			                print(e)
