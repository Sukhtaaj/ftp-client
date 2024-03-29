class Command:
    def do_chdir(self, remotepath):
        """
        Command to chnage directory on the connected FTP host.

        Args:
            remotepath (str): Path of directory to change into.
        """
        try:
            response = self._perform_ftp_command('chdir', remotepath or '.')
            print("Current directory: " + remotepath)
        except IOError as e:
            print "No such directory as: " + remotepath + "\n"
