import os, sys
class Command:
	def do_lrename(self, path):
		"""
        Command to rename a file on the local host.

        Args:
            current_name of the file
            new name of the file
        """
		path_src_dest=path.split(" ")
		if len(path_src_dest)!=2:
			print "Rename command expects exactly two arguments"
		else:
			try: 
				os.rename(path_src_dest[0], path_src_dest[1])
			except IOError as e:
				print(e)
