
# Python program to read
# json file
  
  
import json
import os

  
class json_manager(object):
    def __init__(self):
        self.value = "hello how are you\n"
        self.valuee = "my name is sharan\n"
        self.valueee = "working at digitectura"
        self.filepath = "out.txt"
        self.check_file_exits()
    
    def check_file_exits(self):
        if (os.path.exists(self.filepath)):
            self.load_from_file()
            
        else:
            self.store_to_file()
        
    def store_to_file(self):
        with open(self.filepath, 'w+') as f:
            f.write(self.value)
            f.write(self.valuee)
            f.write(self.valueee)
            
        f.close()
        
    def load_from_file(self):
        with open(self.filepath, 'r+') as f:
            self.value = f.read()
        f.close()
        


    def update_line(self,line_num,msg):
        file1 = open(self.filepath, 'r+')
        count = 0
        
    
        while True:
            count += 1

                # Get next line from file
            line = file1.readlines()
            
            
            if not line:
                break
        
              
            if(line_num==1):    
                with open(self.filepath, 'a+') as f:
                    line[0] = msg + '\n'
                    for ele in line:
                        f.write(ele)
                    print(line)
            elif(line_num==2):
                with open(self.filepath, 'a+') as f:
                    line[1] = msg + '\n'
                    for ele in line:
                        f.write(ele)
                    print(line)
            elif(line_num==3):
                with open(self.filepath, 'a+') as f:
                    line[2] = msg + '\n'
                    for ele in line: 
                        f.write(ele)
                    print(line)
            elif(line_num==4):
                with open(self.filepath, 'a+') as f:
                    line[3] = msg + '\n'
                    for ele in line:
                        f.write(ele)
                    print(line)
       
        
            with open(self.filepath, 'w+') as f:
                for ele in line:
                    f.write(ele)
        file1.close()
        self.print_details()
        
    def print_details(self):
        file1 = open(self.filepath, 'r')
        count = 0
        print("Th contents of the file are ")
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
    manager.print_details()
    ln = int(input('\nenter at which line the replacement shoud take place\n'))
    msg= str(input('\nenter the word to be replaced\n'))
    manager.update_line(ln,msg)






