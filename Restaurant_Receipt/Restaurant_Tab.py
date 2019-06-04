class Resturant_Tab:

    menu = {'sprite': 3 , "beer": 3 , 'coke':3,'burger':7,'fries':4,'salad':9,"nuggets":5,
            "smoothie":7}  # dict

    def __init__(self):
        self.total_check = 0
        self.items_eaten = []  # the list of items as we add them


    def add_item(self,item):
        self.items_eaten.append(item) # adding item to list

        self.total_check += self.menu[item]  # adding to the total


    def bill(self,state_tax,tip_server):
        state_tax = (state_tax/100)
        tip_server = (tip_server/100)
        total_bill = self.total_check + state_tax + tip_server

        for i in self.items_eaten:
            print(" item: "+ i + " $" +str(self.menu[i]))

        print("$"+str(total_bill))



table1 =Resturant_Tab()
table1.add_item("sprite")
table1.add_item("burger")
table1.add_item("fries")
print(" Your total is :")
table1.bill(7,15) # tax , server tip
print("Have a good day!")
