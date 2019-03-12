class Command:
	def do_copydir(self, directory_path):
		"""
        Command to perform copy directory from local host to connected FTP Host

        Args:
             local_dirname(str): name or path of the directory
             remote_dirname(str): namee or path of the directory
        
        """
		dir_path = directory_path.split(" ")
		if len(dir_path) != 2:
			print ("command expects exactly two arguments")
		else:
		    try: 
			    response = self._perform_ftp_command('put_r',dir_path[0], dir_path[1] )
                            print("Copied successfully!")
		    except IOError as e:
                            print("Failure")
			    print(e)
                    except OSError as e:
                            print("Failure")
                            print(e)
