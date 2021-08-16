
# Python program to read
# json file
  
  
import json
import os

class json_manager(object):
    def __init__(self):
        self.emp_details ={
                "emp_name": "shusdf",
                "email": "kk12?@gmail.com",
                "job_profile": "intern"
                }
        self.filepath = "out.json"
        self.check_file_exits()
    
    def check_file_exits(self):
        if (os.path.exists(self.filepath)):
            self.load_from_file()
        else:
            self.store_to_file()
        
    def store_to_file(self):
        with open(self.filepath, 'w+') as f:
            json.dump(self.emp_details, f)
        f.close()
        
    def load_from_file(self):
        with open(self.filepath, 'r+') as f:
            self.emp_details = json.load(f)
        f.close()
        
    def update_line(self,key,value):
        self.emp_details[key] = value
        self.store_to_file()  
        self.print_details()
        
    def print_details(self):
        print("The contents of the file are ")
        print(self.emp_details)
    
if __name__ == "__main__":
    manager = json_manager()
    manager.print_details()
    inputk = str(input('\nenter the key\n'))
    inputv= str(input('\nenter the value \n')) 
    manager.update_line(inputk,inputv)






