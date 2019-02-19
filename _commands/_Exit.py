class Command:
    def do_exit(self, *args):
        """
        Command to logout and exit the FTP client
        """
        if self._connection_object is not None:
            self.do_logout(self)
        return True
