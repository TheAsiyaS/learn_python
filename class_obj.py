class shopInfo:
    def showingdata(self , shopdata):
        #self.showingdata = shopdata
        print("Shop name : "+shopdata['name'])
        print("no of workers in store : "+shopdata['workers'])


obj1 = shopInfo()
shopdata = {
    'name' : "AS STORES",
    'workers'  : "20",
    'place': "India"

 }
obj2 = shopInfo()
shopdata2 = {
    'name' : "MK STORES",
    'workers'  : "10",
    'place': "India, kochi"

 }
obj1.showingdata(shopdata)
obj2.showingdata(shopdata2)