###Bapt-Tech
###Louka-Tech
###04/04/2024
###11:28

def ImportModules():#importation des modules
        try:
                import time, datetime
                print("super!")
                date_actuelle = datetime.date.today()
        except ModuleNotFound :
                print("modulenotfound")
ImportModules()
