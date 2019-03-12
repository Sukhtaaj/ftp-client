import subprocess
class Command:
    def do_llist(self, remotepath):
        """
        Command to list files/directories on the Local host.

        Args:
            remotepath (str): Path of file or directory to list info for.
        """
        try:
            cmd="ls -l"
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (result, error) = process.communicate()
            rc = process.wait()
            print(result)
        except IOError as e:
            print (e)

