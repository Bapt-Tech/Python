###Bapt-Tech
###Louka-Tech
###04/04/2024
###11:28

def ImportModules():#importation des modules
        try:
                import time, datetime
                print("super!")
                date_actuelle = datetime.date.today()
                print(date_actuelle)
                day = []
                month = []
                Year = []
        except ModuleNotFound :
                print("modulenotfound")
ImportModules()
def UserEntry():
        EntereDate = str(input("Enter the date on YYYY/MM/DD"))
