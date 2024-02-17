class ListaDeCompras:
    def __init__(self,name,montant,date_of_expiration,id_number):
        self.Alimento_name = name
        self.Alimento_montant = montant
        self.Alimento_date_of_expiration = date_of_expiration
        self.Alimento_id_number = id_number
        
    def add_Alimento(self):
        print("Name: "+ self.Alimento_name)
        print("Age: "+ self.Alimento_montant)
        print("Dob: "+ self.Alimento_date_of_expiration)
        print("Id_number: "+ self.Alimento_id_number)
        
Alimento1 = ListaDeCompras("Tomates", "6", "27/7/73", "#123876992")
Alimento1.add_Alimento()

Alimento2 = ListaDeCompras("Lechuga", "1", "27/7/97", "#98761234118")
Alimento2.add_Alimento()