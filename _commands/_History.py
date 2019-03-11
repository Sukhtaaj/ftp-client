import subprocess
class Command:
    def do_history(self,remote_path):
        """
        Command to print log history

        """
	f = open('log.txt', 'r')
        print f.read()
        f.close()
