class Tab:

    menu = {'wine': 5 , "beer": 3 , 'soda':2,'burger':7,'fries':4,'salad':9}  # dict

    def __init__(self):
        self.total = 0
        self.items = []  # the list of items as we add them


    def add_item(self,item):
        self.items.append(item) # adding item to list

        self.total += self.menu[item]  # adding to the total


    def bill(self,tax,service):
        tax = (tax/100)
        service = (service/100)
        total_bill = self.total + tax + service

        for i in self.items:
            print(" item: "+ i + " $" +str(self.menu[i]))

        print("$"+str(total_bill))



table1 = Tab()
table1.add_item("wine")
table1.add_item("burger")

table1.bill(7,15)

