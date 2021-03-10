import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime


class Drugs():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.table_name=["drugs", "concentration"]  # [0] = ce qu'on veut gérer 
        self.cnx=cnx
        self.col=["PK_drug_id","name","description","peremption_date","price", "stock", "concentration_mg", "PK_concentration_id"]
        self.aff_col=["ID Médicaments", "Nom", "Description", "Date de péremption", "Prix en €€€", "Stock", "Concentration en mg"]      #Pour affichage
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
        cursor=self.cnx.cursor()
        sql="SELECT drugs.PK_drug_id, drugs.name, drugs.description, CAST(drugs.peremption_date AS CHAR),drugs.price, drugs.stock, concentration.concentration_mg FROM drugs JOIN concentration ON drugs.PK_drug_id = concentration.PK_concentration_id"
        print(sql)
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

        #Proposition de choix au client, soit on affiche toute la table, soit on crée une query personnalisée selon les ID qu'il souhaite afficher
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les médicaments \n 2) Je choisis quel(s) médicament(s) afficher\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass    #TODO : Delete ce truc
                elif choix=="2":
                    sql+=" WHERE drugs.PK_drug_id IN (" # SELECT * FROM clients WHERE clients.PK_client_id=
                    try:
                        nbrRow=input("~Veuillez indiquer le nombre exact de médicaments que vous souhaitez afficher : ")
                        for i in range(int(nbrRow)):
                            idRow=input("~~Veuillez indiquer l'ID' du médicament recherché : ")
                            sql+=idRow + ","   
                        sql=sql[:-1]
                        sql+=")"        
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
        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")
        finally:
            cursor.close()