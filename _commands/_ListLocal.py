class Command:
    def do_list(self, localDirPath):
        """
        Command to perform LIST command on the local directory.
        Args:
            localDirPath (str) (Optional): Print Directories and files of the local directory.
			Usage: lls localDirPath
        """
        response = self._perform_ftp_command('lls', localDirPath)
        print response