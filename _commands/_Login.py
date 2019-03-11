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
        
        user1 = None
        while user1 != 'y' and user1 != 'Y' and user1 !='n' and user1 !='N':
            user1 = raw_input("Use saved connection? (y/n): ")

        if user1 == 'y' or  user1 == 'Y':
            self.pull_connections()

        else:
            while not self._hostname:
                self._hostname = raw_input('Host (default: test.rebex.net):') or 'test.rebex.net'
            
            while not self._username:
                self._username = raw_input('Username(default= demo): ') or 'demo'

        while not self._password:
            self._password = getpass.getpass('Password(default= password): ') or 'password'
            

        response = self._perform_ftp_command('Connection', self._hostname, self._username, None, self._password,
                                              22, None, None, False, cnopts, None)

        #Clears the password so it'll be askes again
        self._password = None

        if isinstance(response, str):
            print response
        else:
            print "Logged in successfully\n"
            self._connection_object = response

            user2 = None
            if user1 == 'n' or  user1 == 'N':
                while user2 != 'y' and user2 != 'Y' and user2 !='n' and user2 !='N':
                    user2 = raw_input("Would you like to save this connection? (y/n): ")

                if user2 == 'y' or  user2 == 'Y':
                    self.push_connections()

        self._update_prompt()
