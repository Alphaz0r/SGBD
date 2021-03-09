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
                        pass
                    elif choix=="3":
                        pass
                    elif choix=="4":
                        quit=True


    def Afficher_Table(self):   #Exemple QUERY : SELECT drugs.PK_drug_id, drugs.name, drugs.description, drugs.peremption_date, drugs.price, concentration.concentration_mg FROM drugs JOIN concentration ON drugs.FK_concentration_id = concentration.PK_concentration_id
        #Construction de la query de base NB: Impossible de sélectionner autre chose que TOUTES les colonnes de la table...
         cursor=self.cnx.cursor()
        sql="SELECT "  
        for col in self.col:
            if col!="concentration_mg" and col!="PK_concentration_id":
                if col=="peremption_date":
                    sql+="CAST("+self.table_name[0]+"."+col+" AS CHAR),"
                else:
                    sql+=self.table_name[0]+"."+col+", "
            elif col!="PK_concentration_id":
                sql+=self.table_name[1]+"."+col+", "
        sql=sql[:-2]
        sql+=" FROM " + self.table_name[0] + " JOIN " + self.table_name[1] +" ON "+self.table_name[0]+"."+self.col[0]+" = "+self.table_name[1]+"."+self.col[7]
        print(sql)
        table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée

        #Proposition de choix au client, soit on affiche toute la table, soit on crée une query personnalisée selon les ID qu'il souhaite afficher
        try: 
            choix=input("~Souhaitez-vous afficher \n 1) Tous les " +self.table_name[0]+" \n 2) Je choisis quel(s) " +self.table_name[0]+" afficher\n~Votre choix : ")
            if choix=="1" or choix=="2":
                if choix=="1":
                    pass    #TODO : Delete ce truc
                elif choix=="2":
                    sql+=" WHERE "+self.table_name[0]+"."+self.col[0]+" IN (" # SELECT * FROM clients WHERE clients.PK_client_id=
                    try:
                        nbrRow=input("~Veuillez indiquer le nombre exact de " +self.table_name[0]+" que vous souhaitez afficher : ")
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