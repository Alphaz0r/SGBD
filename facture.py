import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime


class Facture():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.table_name=["facture", "clients"]  # [0] = ce qu'on veut gérer 
        self.cnx=cnx
        self.col=["PK_facture_id","FK_client_id","name","first_name","email","rue","house_number","postcode","total_price","date_creation","PK_client_id"]
        self.aff_col=["ID Facture","ID Client", "Nom","Prénom","email","Rue","Numéro de maison","Code postal","Prix Total Facture €€€","Date de facturation"]
        self.PK_facture_id=""
        self.FK_client_id=""
        self.name=""
        self.first_name=""
        self.email=""
        self.rue=""
        self.house_number=""    #Initialisation des attributs qui accueilleront les infos de la bdd pour modification
        self.postcode=""
        self.total_price=""
        self.date_creation=""
        self.PK_client_id=""
        
    def Menu(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_facture()  #Affichage menu table
            choix=input("\nVotre choix : ") 
            if choix=="1":
                self.Afficher_Table()
            elif choix=="2":
                self.Afficher_Detail()
            elif choix=="3":
                pass #TODO : Supprimer_Row()
            elif choix=="4":
                pass
            elif choix=="5":
                pass
            elif choix=="6":
                quit=True

    
    def Afficher_Table(self):   
        cursor=self.cnx.cursor()
        sql="SELECT facture.PK_facture_id, facture.FK_client_id, clients.name, clients.first_name, clients.email, clients.rue, clients.house_number, clients.postcode, facture.total_price, CAST(facture.date_creation AS CHAR) FROM facture JOIN clients ON facture.FK_client_id=clients.PK_client_id"
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

        #Proposition de choix au client, soit on affiche toute la table, soit on crée une query personnalisée selon les ID qu'il souhaite afficher
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Toutes les factures \n 2) Je choisis quelle(s) facture(s) afficher\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass    #TODO : Delete ce truc
                elif choix=="2":
                    sql+=" WHERE facture.PK_facture_id in (" # SELECT * FROM clients WHERE clients.PK_client_id IN (
                    try:
                        nbrClient=input("~Veuillez indiquer le nombre exact de factures que vous souhaitez afficher : ")
                        for i in range(int(nbrClient)):
                            idClient=input("~~Veuillez indiquer l'ID du client recherché : ")
                            sql+=idClient + ","                                                                       
                        sql=sql[:-1]  
                        sql+=")"    
                        print(sql)                                                                                   
                    except:
                        print("\n+++Une erreur est survenue, un nombre est attendu+++")
            else:
                return "Veuillez choisir parmis les choix proposés"
            
            cursor.execute(sql)
            print("\nAffichage de votre requête : ")
            table.columns.header=self.aff_col
            for row in cursor:
                table.rows.append(row)
            print(table)

            input("\nPressez n'importe quelle touche pour continuer...")
        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")
        finally:
            cursor.close()