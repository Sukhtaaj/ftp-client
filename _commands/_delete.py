class Command:
	def do_delete(self, filepath):
		"""
        Command to delete a file on the connected FTP host.

        Args:
            filepath - path of the file to be deleted from the remote server.
        """
		
		
		try: 
			response = self._perform_ftp_command('remove', filepath)
		except IOError as e:
			print("File doesn't exists")
