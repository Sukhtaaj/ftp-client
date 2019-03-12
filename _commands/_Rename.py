class Command:
	def do_rename(self, remote_path):
		"""
        Command to rename a file on the conected FTP Host.

        Args:
            current_name of the file
            new name of the file
        """
		remote_src_dest=remote_path.split(" ")
		if len(remote_src_dest)!=2:
			print "Rename command expects exactly two arguments"
		else:
			try: 
				response=self._perform_ftp_command('rename',remote_src_dest[0], remote_src_dest[1])
                                print ("Renamed: " + remote_src_dest[0] + " -> " + remote_src_dest[1])
			except IOError as e:
                                print("Failure")
				print(e)
