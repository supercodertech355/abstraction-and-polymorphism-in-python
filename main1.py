class India():
    def capital(self):
        print("New Delhi")

class USA():
    def capital(self):
        print("Washingtin D.C")

obj_ind =   India()
obj_usa = USA()

for country in (obj_ind,obj_usa):
    country.capital()
