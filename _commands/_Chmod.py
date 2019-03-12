import sys, os
class Command:
    def do_chmod(self, input_args):
        """
        Command to change permissions for file/directory 

	Args:
             file (str): filename or path 
	     permissions (int): permissions to grant e.g. 755, 644, or 000.
        """
	if not input_args:
		print("Filename and permissions expected")
	else:
          if len(input_args.split(" ")) == 2:
                filepath = input_args.split(" ")[0]
                permission = input_args.split(" ")[1]
                try:
		    self._perform_ftp_command('chmod', filepath, permission)
                    print("Permissions changed successfully!")
                except IOError as e:
                    print "Failure"
                    print(e)
          else:
                print("Exactly two arguments expected")

