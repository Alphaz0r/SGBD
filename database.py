import mysql.connector, interface_console, dicoType 
import connexion



class Database(connexion.Connexion):
    def __init__(self ):
            super().__init__()

    #Fonction  menu principal
    def Menu(self):
        dc=False
        while(dc==False):
            try:
                interface_console.aff_menu_principal(self.db)   #Affichage menu principal
                choix=input("\nVotre choix : ") 

                if choix=="1" or choix == "2" or choix=="3" or choix=="4" or choix=="5" or choix=="6":
                    if choix!="6":
                        interface_console.aff_acces_table() #Affichage menu accès aux tables
                        return choix
                    else:
                        dc = True  #Sortie de la boucle
                        self.Se_Deconnecter()
                else:
                    print("### Veuillez choisir l'un des choix proposés ###")
            except:
                print("+++Erreur rencontrée+++")



                #TODO: Afficher dans exe


        

