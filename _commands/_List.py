class Command:
    def do_list(self, remotepath):
        """
        Command to list files/directories on the connected FTP host.

        Args:
            remotepath (str): Path of file or directory to list info for.
        """
        try:
            response = self._perform_ftp_command('listdir_attr', remotepath or '.')
            for attr in response:
                print attr
            print "\n"
        except IOError as e:
            print "No such directory as: " + remotepath + "\n"

