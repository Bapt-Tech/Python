###Bapt-Tech
###Louka-Tech
###04/04/2024
###11:28

def ImportModules(): #Importataion des modules.
        try:
                import time, datetime
                print("Modules Trouvés !")
                date_actuelle = datetime.date.today()
                print(date_actuelle)
                Day = []
                Month = []
                Year = []
        except ModuleNotFound:
                print("Modules non trouvés.")
ImportModules()

def UserEntry():
        EnteredDate = str(input("Entrez la date sous le format AAAA-MM-JJ"))
        username, password, UserStatus = line.split(";")
