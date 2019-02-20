import getpass

class Command:
    def do_login(self, *args):
        """
        Command to login with user and password in the connected FTP host.
        """
        # Temporary only
        cnopts = self._ftp_client.CnOpts()
        cnopts.hostkeys = None

        print "Press Enter for selecting default values\n"

        while not self._hostname:
            self._hostname = raw_input('Host (default: test.rebex.net):') or 'test.rebex.net'
        
        while not self._username:
            self._username = raw_input('Username(default= demo): ') or 'demo'

        while not self._password:
            self._password = getpass.getpass('Password(default= password): ') or 'password'

        response = self._perform_ftp_command('Connection', self._hostname, self._username, None, self._password,
                                              22, None, None, False, cnopts, None)

        if isinstance(response, str):
            print response
        else:
            print "Logged in successfully\n"
            self._connection_object = response

        self._update_prompt()
