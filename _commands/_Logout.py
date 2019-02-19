
class Command:
    def do_logout(self, *args):
        """
        Command to logout the current user from the connected FTP host.
        """
        self._perform_ftp_command('close')
        print "Logged out successfully\n"

        # resetting connection values
        self._connection_object = None
        self._hostname = None
        self._username = None
        self._password = None

        self._update_prompt()

