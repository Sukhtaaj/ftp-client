class Command:
    def do_list(self, filename):
        """
        Command to perform LIST command on the connected FTP host.

        Args:
            filename (str): Name of file or directory to retrieve info for.
        """
        response = self._perform_ftp_command('listdir', filename)
        print response
