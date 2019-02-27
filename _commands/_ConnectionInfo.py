class Command():
    def pull_connections(self):
        """
        Command to display saved connections to user

        """
        i = 1;

        text_file = open("_commands/info.csv", "r")
        for line in text_file:
            #print(i + ")")
            fields = line.split(",")
            host = fields[0]
            username = fields[1]
            print("{}{}" + " " + host + " " + username).format(i,")" )
            i = i+1

        '''
        lines = text_file.read().split(';')
        print lines
        print len(lines)
        text_file.close()
        '''
        
        self._hostname = "babbage.cs.pdx.edu"
        self._username= "cabunoc"

        return
