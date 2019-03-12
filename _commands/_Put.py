class Command:
    def do_put(self, localPath):
        """
        Command to copy file(s) from local host to the connect FTP Host

        Args:
            fileName (str): File(s) to upload into current working directory of the remote host.
        """
        file_list = localPath.split(" ")
        if len(file_list) < 1:
            print ("Atleast one file/path expected")
        else:
            for file in file_list:
                try:
                    response = self._perform_ftp_command('put', file)
                    print("Uploaded file: " + file)
                except IOError as e:
                    print "Failure"
                    print(e)
