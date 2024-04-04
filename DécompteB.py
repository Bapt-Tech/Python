###Bapt-Tech
###Louka-Tech
###04/04/2024
###11:28

def ImportModules(): #Importataion des modules.
        try:
                import time, datetime
                print("Modules Trouvés !")
                date_actuelle = datetime.date.today()
        except ModuleNotFound:
                print("Modules non trouvés.")
ImportModules()

