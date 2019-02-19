import os
import pysftp
from cmd import Cmd

import _commands._Login
import _commands._Logout
import _commands._List
import _commands._Exit

from paramiko import SSHException, AuthenticationException
from pysftp.exceptions import (CredentialException, ConnectionException,
                               HostKeysException)

class SFTPWrapper(Cmd, _commands._Login.Command, _commands._Logout.Command, _commands._List.Command, _commands._Exit.Command):
    """
    FTP client command line utility.
    """
    def __init__(self, debug=False):
        Cmd.__init__(self)
        self.intro = ('SFTP Client. Enter help or ? to see available actions')
        self.prompt = 'FTP > '
        self._ftp_client = pysftp
        self._connection_object = None

        self._hostname = None
        self._username = None
        self._password = None

    def _update_prompt(self):
        prompt = '\nFTP'
        if self._connection_object is not None:
            if self._connection_object._transport.hostname is not None and self._connection_object._tconnect['username'] is not None:
                prompt = '{} {}@{}'.format(prompt, self._connection_object._tconnect['username'], self._connection_object._transport.hostname)
        self.prompt = '{} > '.format(prompt)

    def _perform_ftp_command(self, command, *args):
        if not self._connection_object:
            method = getattr(self._ftp_client, command)
        else:
            method = getattr(self._connection_object, command)
        try:
            response = method(*args)
        
        except (ConnectionException,
                CredentialException) as e:
            response = e.message
        except SSHException as e:
            response = "Please check your hostname: {} \n".format(self._hostname)
        except  AuthenticationException as e:
            response = "Please make sure credentials are correct for user: {}\n".format(self._username)
        except PasswordRequiredException as e:
            response = "Password is not provided."

        return response


    def emptyline(self):
        pass