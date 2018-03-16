class home():
    def __init__(self,dx=2,dy=8,okx=2,oky=15):
        self.okno=okx*oky
        self.dver=dx*dy
    def plosh(self,x,y,z):
        self.dlina=x
        self.shirina=y
        self.visota=z
        self.ploshad=self.dlina*self.visota*2+ self.shirina*self.visota*2
    def ploshb(self):
        self.ploshadb=self.ploshad-self.okno-self.dver
    def inf(self):
        self.inform='Площадь:'+str(self.ploshad)+' Площадь без окна и двери :'+str(self.ploshadb)
    def __del__(self):
        print('ВЫЗВАН ДЕСТРУКТОР!')
a=home()
a.plosh(20,30,20)
a.ploshb()
a.inf()
print(a.inform)
del a
