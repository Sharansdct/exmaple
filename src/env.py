
# Python program to read
# json file
  
  
import json
import os

  
class json_manager(object):
    def __init__(self):
        self.emp_name = "shusdf"
        self.email =  "kk12?@gmail.com"
        self.job_profile = "intern"
        self.emp_details ={
                "emp_name": "shusdf",
                "email": "kk12?@gmail.com",
                "job_profile": "intern"
                }
        self.filepath = "data_new.txt"
        self.check_file_exits()
    
    def check_file_exits(self):
        if(os.path.exists(self.filepath)):
            self.load_from_file()
        else:
            self.store_to_file()
        
    def store_to_file(self):
        with open("texts.txt") as f:
            with open("out.txt", "w") as f1:
                 for line in f:
                    f1.write(line)
        f.close()
        
    def load_from_file(self):
        with open(self.filepath, 'r+') as f:
            self.emp_details = json.load(f)
        f.close()
        
    def print_details(self):
        for key in self.emp_details.keys():
            print(("{} : {}").format(key, self.emp_details[key]))


if __name__ == "__main__":
    manager = json_manager()
    manager.print_details()

