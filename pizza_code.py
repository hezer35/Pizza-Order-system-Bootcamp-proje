import csv
from datetime import datetime
import time
import os
# Menu.txt dosyasını oluşturma
with open("Menu.txt", "w") as menu_file:
    menu_file.write("* Lütfen Bir Pizza Tabanı Seçiniz:\n")
    menu_file.write("1: Klasik\n")
    menu_file.write("2: Margarita\n")
    menu_file.write("3: TürkPizza\n")
    menu_file.write("4: Sade Pizza\n")
    menu_file.write("* ve seçeceğiniz sos:\n")
    menu_file.write("11: Zeytin\n")
    menu_file.write("12: Mantarlar\n")
    menu_file.write("13: Keçi Peyniri\n")
    menu_file.write("14: Et\n")
    menu_file.write("15: Soğan\n")
    menu_file.write("16: Mısır\n")
    menu_file.write("* Teşekkür ederiz!")

title=['PİZZA','NAME','SURNAME','TC KİMLİK','KREDİ KARTI NUMARASI','SİPARİŞ AÇIKLAMASI','SİPARİŞ ZAMANI','KREDİ KARTI ŞİFRESİ']

csv_file='Orders_Database.csv'
    


# pizza super sınıf
class Pizza:
    #pizza sınıfından olusturacağımız nesnelerin özellikleri.
    def __init__(self, description, cost): 
        self.description = description #açıklama        
        self.cost = cost #fiyat
    #pizza tanımı
    def get_description(self):
        return self.description
    #pizzanın maliyeti
    def get_cost(self):
        return self.cost
#pizza sınıfından miras alan diğer pizza sınıfları.
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 60.0)

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita Pizza", 80.0)

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__("Turkish Pizza", 100.0)

class NormalPizza(Pizza):
    def __init__(self):
        super().__init__("Sade Pizza", 50.0)
#pizzaya sos eklemek için alt sınıf decorator oluşturma
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component
    #pizzanın üzerine eklenen malzemelerle birlikte oluşan fiyatı göster.
    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)
    #pizzanın üzerine eklenen malzemeleri göster. 
    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)
#malzeme fiyat ve açıklama.
class Olive(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 10.0
        self.description = "Olive"
    
class Mushroom(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 20.0
        self.description = "Mushroom"

class GoatCheese(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 30.0
        self.description = "Goat Cheese"

class Meat(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 30.0
        self.description = "Meat"

class Onion(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 1.0
        self.description = "Onion"

class Corn(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.cost = 2.0
        self.description = "Corn"

def main():
    #pizza seç.
    print("Menu:\n1. Classic Pizza\n2. Margherita Pizza\n3. Turkish Pizza\n4. Normal Pizza")
    pizza_choice = input("Choose a pizza by entering its number: ")
    if pizza_choice == "1":
        pizza = ClassicPizza()
    elif pizza_choice == "2":
        pizza = MargheritaPizza()
    elif pizza_choice == "3":
        pizza = TurkishPizza()
    elif pizza_choice == "4":
        pizza = NormalPizza()
    else:
        print("Invalid choice")
        return
#malzeme seç.
    print("Choose toppings (enter numbers separated by commas):")
    print("1. Olive\n2. Mushroom\n3. Goat Cheese\n4. Meat\n5. Onion\n6. Corn")
    topping_choices = input().split(",")
    for topping_choice in topping_choices:
        if topping_choice == "1":
            pizza = Olive(pizza)
        elif topping_choice == "2":
            pizza = Mushroom(pizza)
        elif topping_choice == "3":
            pizza = GoatCheese(pizza)
        elif topping_choice == "4":
            pizza = Meat(pizza)
        elif topping_choice == "5":
            pizza = Onion(pizza)
        elif topping_choice == "6":
            pizza = Corn(pizza)
        else:
            print("Invalid topping choice")
            return
        
#toplam fiyat.
    print("Total cost:", pizza.get_cost())

#müşteri bilgiler
    name = input('Enter your name:')
    surname=input('Enter your surname:')
    tc = input('Turkish republic identification number:')
    kredi_card_no =input('Credit Card Number:')
    kredi_kartı_şifre = input('Credit Card password:')
#sipariş tarihi.
    şu_an = datetime.now()
    print(datetime.ctime(şu_an))
     
    pizz=pizza.get_description()
    # csvv dosyasına ekleme
    with open (csv_file,'a',newline='') as orders_file:
     writer = csv.writer(orders_file)
     writer.writerow(title)
     writer.writerows([[topping_choices,name,surname,tc,kredi_card_no,pizz,şu_an,kredi_kartı_şifre]])
     
    
     

if __name__ == '__main__':
    main()