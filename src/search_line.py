
# Python program to read
# json file
  
  
import json
import os

class json_manager(object):
    def __init__(self):
        self.file_contents = "hello how are you\nmy name is sharan\nworking at digitectura".splitlines(keepends=True)
        self.filepath = "out.txt"
        self.check_file_exits()
    
    def check_file_exits(self):
        if (os.path.exists(self.filepath)):
            self.load_from_file()
        else:
            self.store_to_file()
        
    def store_to_file(self):
        with open(self.filepath, 'w+') as f:
            f.writelines(self.file_contents)
        f.close()
        
    def load_from_file(self):
        with open(self.filepath, 'r+') as f:
            self.file_contents = f.readlines()
        f.close()
        
    def update_line(self,line_num,msg):
        length = len(self.file_contents) 
        nxt_line = "\n"
        if(line_num>length):
            for i in range(length,line_num):
                self.file_contents.append(nxt_line)
            self.file_contents.append(msg)
        else:
            self.file_contents[line_num -1] = msg
        self.store_to_file()  
        self.print_details()
        
    def print_details(self):
        print("The contents of the file are ")
        print(self.file_contents)
    
if __name__ == "__main__":
    manager = json_manager()
    manager.print_details()
    ln = int(input('\nenter at which line the replacement shoud take place\n'))
    msg= str(input('\nenter the word to be replaced\n')) + '\n'
    manager.update_line(ln,msg)






