class Command:
	def do_rmdir(self, filepath):
		"""
        Command to delete a direcory on the connected FTP host.

        Args:
            filepath - path of the directory to be deleted from the remote server.
        """
		
		
		try: 
			response = self._perform_ftp_command('rmdir', filepath)
		except IOError as e:
			print(e.message)
