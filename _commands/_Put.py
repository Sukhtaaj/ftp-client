class Command:
    def do_put(self, fileName):
        """
        copy file, to the current working directory on the server, preserving modification time
        Args:
            fileName (str): File to upload into current working directory of the remote host.
			preserve_mtime (bool) :  will make sure that the modification times on the server copy match those on the local.
        """
        try:
            response = self._perform_ftp_command('put', fileName)
	    print "File uploaded Successfully"
        except IOError as e:
            print "No such File exists: " + fileName
