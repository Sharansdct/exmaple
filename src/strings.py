
# Python program to read
# json file
  
  
import json
import os

  
class json_manager(object):
    def __init__(self):
        self.stringss = [ "hello how are you" , "my name is sharan" , "working at digitectura"]
        self.filepath =  "texts.txt"
        
        self.check_file_exits()
    
    def check_file_exits(self):
        if(os.path.exists(self.filepath)):
            self.store_to_file()
           
        else:
             self.load_from_file()
            
        
    def store_to_file(self):
        with open(self.filepath, 'w+') as f:
            f.write(self.stringss)
        f.close()
        
    def load_from_file(self):
        with open(self.filepath, 'r+') as f:
            self.value = f.read()
        f.close()
        
    def print_details(self):
        print(" the value in my file is {} ".format(self.stringss))


if __name__ == "__main__":
    manager = json_manager()
    manager.print_details()

