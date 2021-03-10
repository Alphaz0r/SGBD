import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime


class Client():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.table_name=["clients"]  # [0] = ce qu'on veut gérer 
        self.cnx=cnx
        self.col=["PK_client_id", "name", "first_name", "birth_date", "age", "rue", "house_number", "postcode", "email", "phone_number"]
        self.aff_col= ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"]
        self.Menu()
        
    def Menu(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table(self.table_name[0])  #Affichage menu table
            choix=input("\nVotre choix : ") 
            if choix=="1":
                self.Afficher_Table()
            elif choix=="2":
                pass
            elif choix=="3":
                pass
            elif choix=="4":
                pass
            elif choix=="5":
                quit=True
    
    def Afficher_Table(self):   
        cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
        sql="SELECT PK_client_id, name, first_name, CAST(birth_date AS CHAR),age, rue, house_number, postcode, email, phone_number"
        sql+=" FROM clients"
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

        #Proposition de choix au client, soit on affiche toute la table, soit on crée une query personnalisée selon les ID qu'il souhaite afficher
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les clients \n 2) Je choisis quel(s) client(s) afficher\n~Votre choix : ")
            if choix=="2":
                sql+=" WHERE clients.PK_client_id in (" # SELECT * FROM clients WHERE clients.PK_client_id=
                try:
                    nbrClient=input("~Veuillez indiquer le nombre exact de clients que vous souhaitez afficher : ")
                    for i in range(int(nbrClient)):
                        idClient=input("~~Veuillez indiquer l'ID du client recherché : ")
                        sql+=idClient + ","                                                                        #Query intermédiaire : SELECT * FROM clients WHERE clients.PK_client_id=2,4,8, <<< On note bien la virgule+espace à la fin qu'on doit enlever
                    sql=sql[:-1]  
                    sql+=")"    
                    print(sql)                                                                                   #Exemple query finale : SELECT * FROM clients WHERE clients.PK_client_id=2,4,8
                except:
                    print("\n+++Une erreur est survenue, un nombre est attendu+++")
            else:
                print("Veuillez choisir parmis les choix proposés")

            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
            cursor.execute(sql)
            print("\nAffichage de votre requête : ")
            table.columns.header=self.aff_col
            
            for row in cursor:
                table.rows.append(row)  
            print(table)

        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")
        finally:
            cursor.close()  #Dans tous les cas on ferme le curseur