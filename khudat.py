class TRectangle():
    list_khudat = []
    def __init__(self, c_dai, c_rong):
        self.cdai = c_dai
        self.crong = c_rong
    
    def nhapDL(self):
        chieudai = int(input("Nhap chieu dai: "))
        chieurong = int(input("Nhap chieu rong: "))
    
    def hienthiDL(self):
        print("Chieu Dai: ",self.cdai)
        print("Chieu Rong: ",self.crong)
        
    def tinhCV(self):
        chuvi = round(self.cdai + self.crong)*2
        print("Chu vi la: ",chuvi)
        
    def dientichHCN(self):
        dientich = round(self.cdai * self.crong)
        
    def kiemtra(self):
        if self.cdai == self.crong:
            print("Hinh Vuong")
        else:
            print("Khong phai Hinh Vuong")
    
    def 
        
        
        
        