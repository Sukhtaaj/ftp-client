class Command:
    def do_put(self, localPath):
        """
        copy file/files from current local path to the current working directory on the server
        Args:
            fileName (str): File to upload into current working directory of the remote host.
        """
		file_list = localPath.split(" ")
		if len(file_list) < 1:
            print ("Atleast one file/path expected")
        else:
			try:
				for file in file_list:
					response = self._perform_ftp_command('put', file)
				print "File(s) uploaded Successfully"
			exceptIOError as e:
              print(e)		
