import json
import os

  
class json_manager(object):
    def __init__(self):
        self.filepath = "textss.txt"
        self.check_file_exits()
         
    def check_file_exits(self):
        if(os.path.exists(self.filepath)):
            file1 = open('textss.txt', 'r')
            count = 0
 
            while True:
                count += 1
 
                # Get next line from file
                line = file1.readline()
 
                if not line:
                 break
             
                print("Line{}: {}".format(count, line.strip()))
 
            file1.close()


if __name__ == "__main__":
    manager = json_manager()
   