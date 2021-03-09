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
        self.QueFaire()
        
    def QueFaire(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table(self.table_name[0])  #Affichage menu table
            choix=input("\nVotre choix : ") 

            if choix=="1" or choix == "2" or choix=="3" or choix=="4":
                if choix!="5":
                    if choix=="1":
                        self.Afficher_Table()
                    elif choix=="2":
                        pass #TODO : Modifier_Row()
                    elif choix=="3":
                        pass #TODO : Supprimer_Row()
                    elif choix=="4":
                        quit=True

    
    def Afficher_Table(self):   #SELECT facture.PK_facture_id, clients.PK_client_id, clients.name, clients.first_name, clients.email, clients.rue, clients.house_number, clients.postcode, facture.total_price, CAST(facture.date_creation AS CHAR)
        cursor=self.cnx.cursor()
        sql="SELECT "
        for col in self.col:
            if col!="PK_facture_id" and col!="PK_client_id" and col!="total_price" and col!="date_creation" and col!="FK_client_id":
                if col=="PK_client_id":
                    pass
                if col!="PK_facture_id":
                    sql+=self.table_name[1]+"."+col+", "
            elif col!="date_creation":
                if col=="PK_client_id":
                    pass
                else:
                    sql+=self.table_name[0]+"."+col+", "
            else:
                sql+="CAST("+self.table_name[0]+"."+col+" AS CHAR), "
        sql=sql[:-2]
        sql+=" FROM "+self.table_name[0]+" JOIN "+self.table_name[1]+" ON "+self.table_name[0]+"."+self.col[1]+"="+self.table_name[1]+"."+self.col[10]
        print(sql)
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

        #Proposition de choix au client, soit on affiche toute la table, soit on crée une query personnalisée selon les ID qu'il souhaite afficher
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les " +self.table_name[0]+" \n 2) Je choisis quel(s)" +self.table_name[0]+ "afficher\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass    #TODO : Delete ce truc
                elif choix=="2":
                    sql+=" WHERE "+self.table_name[0]+"."+self.col[0]+" in (" # SELECT * FROM clients WHERE clients.PK_client_id IN (
                    try:
                        nbrClient=input("~Veuillez indiquer le nombre exact de "+self.table_name[0]+" que vous souhaitez afficher : ")
                        for i in range(int(nbrClient)):
                            idClient=input("~~Veuillez indiquer l'ID du client recherché : ")
                            sql+=idClient + ","                                                                        #SELECT * FROM clients WHERE clients.PK_client_id IN (2,4,8, <<< On note bien la virgule+espace à la fin qu'on doit enlever
                        sql=sql[:-1]  
                        sql+=")"    
                        print(sql)                                                                                   #SELECT * FROM clients WHERE clients.PK_client_id IN (2,4,8)
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