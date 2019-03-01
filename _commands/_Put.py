class Command:
    def do_put(self, fileName, preserve_mtime=True):
        """
        copy file, to the current working directory on the server, preserving modification time
        Args:
            fileName (str): File to upload into current working directory of the remote host.
			preserve_mtime (bool) :  will make sure that the modification times on the server copy match those on the local.
        """
        try:
            response = self._perform_ftp_command('put', fileName, preserve_mtime)
			print "File uploaded Successfully"
        exceptIOError as e:
            print "No such File exists: " + fileName