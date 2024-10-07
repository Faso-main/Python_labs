from datetime import datetime as dt


class Storage():

    def __init__(self,name_:str,price_:int,year_:int):
        self.name=name_
        self.price=price_
        self.year=year_
        self.storage={'item1':[200,'21 02 2001'],
                      'item2':[300,'12 01 2012'],
                      'item3':[200,'25 09 2013']}
        
    def get_age(self):
        print(self.get_list())
        return dt.now().year-dt.strptime(self.storage[input('Choose an item: ')][1], '%d %m %Y').year
        
    def get_list(self): return self.storage

    def check_add(self):
        if 'TV' in self.name:
            self.storage.update({self.name:[self.price*1.2,dt.strptime(self.year,'%d %m %Y').strftime('%d %m %Y')]})
            print(self.get_list())
        else:  
            self.storage.update({self.name:[self.price,dt.strptime(self.year,'%d %m %Y').strftime('%d %m %Y')]})
            print(self.get_list())
    
    def __del__(self):
        del self.storage 
        
print(Storage('item4TV',1200,'12 12 2012').check_add())

