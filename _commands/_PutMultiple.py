class Command:
    def do_list(self, filesList):
        """
        Command to UPLOAD multiple files from local directory to the current directory on the connected FTP host.
        Args:
            fileLists (list): List of files to upload to the current remote path.
			Usage: mput filename1 filename2 filename3
        """
        response = self._perform_ftp_command('mput', fileList)
        print response		