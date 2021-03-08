import mysql.connector, interface_console, dicoType 
import client, concentration, drugs, facture # DAO
import connexion



class Database(connexion.Connexion):
    def __init__(self):
            super().__init__()

    #Fonction  menu principal
    def QueFaire(self):
        dc=False
        while(dc==False):
            try:
                interface_console.aff_menu_principal(self.db)   #Affichage menu principal
                choix=input("\nVotre choix : ") 

                if choix=="1" or choix == "2" or choix=="3" or choix=="4" or choix=="5":
                    if choix!="5":
                        interface_console.aff_acces_table() #Affichage menu accès aux tables
                        return choix
                    else:
                        dc = True  #Sortie de la boucle
                        self.Se_Deconnecter()
                else:
                    print("### Veuillez choisir l'un des choix proposés")
            except:
                print("+++Erreur rencontrée+++")


    #Méthode qui va afficher toutes les tables présentes dans la base de données
    def Show_Tables(self):
        sql="SHOW TABLES"
        print("\n***Tables présentes dans la base de données " + self.db + " ***")
        try:
            cursor=self.cnx.cursor(dictionary=True)
            cursor.execute(sql)
            for i in cursor:
                print(i)
            print("*******************************************************")
            self.cnx.close()
            
        except:
            print("+++Une erreur est survenue lors de l'affichage des tables+++")

    def Passe_La_Connexion(self):
        return self.cnx


        

