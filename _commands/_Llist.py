import subprocess
class Command:
    def do_llist(self, remotepath):
        """
        Command to perform LIST command on the connected FTP host.

        Args:
            remotepath (str): Path of file or directory to retrieve info for.
        """
        try:
            cmd="dir"
            process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (result, error) = process.communicate()
            rc = process.wait()
            print(result)
        except IOError as e:
            print (e)
        # find max length of all the file/dir names
        #max_length = 0
        #for attr in response:
        #    if len(attr.filename) > max_length:
        #        max_length = len(attr.filename)
        #max_width_string = "%{}s".format(str(max_length))

        # print the files/dirs with their attribute details
        #for attr in response:
        #    print max_width_string % attr.filename,
        #    print attr
