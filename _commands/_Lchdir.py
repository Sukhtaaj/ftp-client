import os

class Command:
    def do_lchdir(self, path):
        """
        Command to chnage directory on the local host.

        Args:
            path (str): Path of directory to change into.
        """
        if not path:
            print "command expects exactly one argument"
        else:
            try:
                os.chdir(path)
                print("Current local directory: " + path)
            except:
                print("Failure")
