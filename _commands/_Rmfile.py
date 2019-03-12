class Command:
	def do_rmfile(self, filepath):
		"""
        Command to delete a file on the connected FTP host.

        Args:
            filepath - path of the file to be deleted from the remote server.
        """
		try: 
			response = self._perform_ftp_command('remove', filepath)
                        print("Deleted file: " + filepath)
		except IOError as e:
                        print("Failure")
			print(e)
