class Command:
	def do_rename(self, remote_path):
		"""
        Command to perform Rename command on the connected FTP host.

        Args:
            remote_path- return the string including the both source and destination
        """
		remote_src_dest=remote_path.split(" ")
		if len(remote_src_dest)!=2:
			print "Rename command expects exactly two arguments"
		else:
			try: 
				response=self._perform_ftp_command('rename',remote_src_dest[0], remote_src_dest[1])
			except IOError as e:
				print(e)
		