class Command:
	def do_rmdir(self, dirpath):
		"""
        Command to delete a direcory on the connected FTP host.

        Args:
            filepath - path of the directory to be deleted from the remote server.
        """
		
		
		try: 
			response = self._perform_ftp_command('rmdir', dirpath)
                        print("Deleted directory: " + dirpath)
		except IOError as e:
                        print("Failure")
			print(e.message)
