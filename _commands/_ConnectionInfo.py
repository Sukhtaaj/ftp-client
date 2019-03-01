class Command():
    def pull_connections(self):
        """
        Command to display saved connections to user

        """
        i = 0
        text_file = open("_commands/info.csv", "r")

        for line in text_file:
            fields = line.split(",")
            host = fields[0]
            username = fields[1]
            print("{}{}" + " " + host + " | " + username).format(i+1,")" )
            i = i+1

        selection = input("\nSelection: ")

        text_file.seek(0)
        j = 0
        for line in text_file:
            fields = line.split(",")
            host = fields[0]
            username = fields[1]
            if(j == selection-1):
                break
            else:
                j = j+1
        text_file.close()
        
        self._hostname = host
        self._username = username
        print

        #print(self._hostname)
        #print(self._username)

        return

    def push_connections(self):
        """
        Command to ask if the user would like to save connections
        """

        text_file = open("_commands/info.csv", "a")
        text_file.write(self._hostname + ", " + self._username + ",")
        #print(self._hostname)
        #print(self._username)


