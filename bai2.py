class Student:
    def __init__(self, id, name, age, m1, m2, m3):
        self.id = id
        self.name = name
        self.age = age
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
        
    def inputSV(self):
        id = input("Nhap ID: ")
        name = input("Nhap ten sinh vien: ")
        age = input("Nhap tuoi sinh vien: ")
        m1 = input("Nhap diem Toan: ")
        m2 = input("Nhap diem Ly: ")
        m3 = input("Nhap diem Hoa: ")
    def calAverage(self):
        return round((self.m1 + self.m2 + self.m3)/3,2)
       
    def displaySV(self):
        print("ID: ",self.id)
        print("Name: ", self.name)
        print("Age: ", self.age)
    
    def showLevel(self):
        avg = self.calAverage()
        
        if(avg <= 10 and avg >=0)   :
            if(10<= avg >=9):
                print("Xep Loai A")
            elif(avg <9):
                print("Xep Loai B")
            elif(avg <7):
                print("Xep Loai C")
            else:
                print("Xep Loai D")
        else:
            print("Error")
    def inputSinhVien():
    def menu():
        while(True):
            listSV = []
            print("")

            
# st1 = Student('105701','Vo Quoc Vuong', 19,9,7,8)
# print("Diem Tung Binh: ", st1.calAverage())
# st1.showLevel()

            
        
        
        
        
        
        
        