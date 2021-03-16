import mysql.connector
import interface_console
import database, concentration
from beautifultable import BeautifulTable
from datetime import datetime

class Concentration():
    def __init__(self, cnx):
        self.table_name="concentration"
        self.aff_col=["ID Concentration","Concentration en mg"]
        self.cnx=cnx


    def Menu(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_table(self.table_name)  #Affichage menu table
            choix=input("\nVotre choix : ") 
            if choix=="1":
                self.Display_Rows()
            elif choix=="2":
                pass
            elif choix=="3":
                pass
            elif choix=="4":
                self.Insert_Rows()
            elif choix=="5":
                quit=True

    def Display_Rows(self):   
        try:    
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT * FROM concentration"
            table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée
            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
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
            cursor.close()  #Dans tous les cas on ferme le curseur


    def Display_Rows(self):   
        try:    
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT concentration.PK_concentration_id, concentration.concentration_mg FROM concentration ORDER BY concentration.concentration_mg"
            table=BeautifulTable(maxwidth=300)      #Préparation de l'affichage des lignes de façon organisée
            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage
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
            cursor.close()  #Dans tous les cas on ferme le curseur


    def Insert_Rows(self):       
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            query_list=self.Build_Row()
            reponse=input("\nÊtes vous sûr de vouloir insérer les valeurs entrées précédemment dans la base de données ? Y/N\nVotre réponse : ")
            if query_list=="Q":
                return ("")
            if reponse=="Y":
                sql="INSERT INTO pharmacie.concentration (PK_concentration_id, concentration_mg) VALUES "
                sql+="("+query_list[0]+", "+query_list[1]+");"
                cursor.execute(sql)
                self.cnx.commit()
            elif reponse=="N":
                print("### Annulation de l'insertion de données... Retour au menu...")
            else:
                print("La réponse doit être Y, N ou Q")
        except:
            print("+++ Erreur dans l'insertion des données +++")
            self.cnx.rollback()
        finally:
            cursor.close()



    def Build_Row(self):
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=["NULL"]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=300)
        result_table.columns.header=self.aff_col
        table_vide.columns.header=self.aff_col
        table_vide.rows.append(["",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in self.aff_col:
                if value!="ID Concentration":
                    print("Indiquez une valeur pour \""+value+"\"")     
                    rep=input("Valeur : ")      
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###")
                    elif value=="Concentration en mg":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###")
                            test_int=self.Intable(rep)
                    
                    query_list.append(rep)
        except:
            print("+++ Erreur dans l'insertion de données, veuillez recommencer +++")

        result_table.rows.append(query_list)
        print(result_table)
        while(True):
            try:
                print("\n\nVeuillez vérifier ces valeurs, sont-elles correctes ? Y/N \nou annuler et revenir au menu ? Q")
                reponse=input("Votre réponse : ")
                if reponse=="Y":
                    return query_list
                elif reponse=="N":
                    print("### Redémarrage de l'insertion de données ###")
                    self.Build_Row()
                elif reponse=="Q":
                    print("### Retour au menu... ###")
                    return("Q")
            except:
                print("+++ Erreur dans la validation des données +++")

    def Delete_Row(self):
        try:
            chiffre=False
            cursor=self.cnx.cursor()
            sql="DELETE FROM concentration"
            while(chiffre==False):
                id=input("Veuillez choisir l'ID de la ligne à effacer\nVotre choix : ")
                chiffre=self.Intable(id)
            
            while(True):
                reponse=input("La ligne avec l'ID "+id+" va être supprimée. Confirmer ? Y/N\nVotre réponse : ")
                if reponse=="Y":
                    sql+=" WHERE concentration.PK_concentration_id="+id
                    print(sql)
                    cursor.execute(sql)
                    self.cnx.commit()
                    return ("")
                elif reponse=="N":
                    input("### Aucune action n'a été entreprise, retour au menu.\nAppuyer sur n'importe quelle touche pour continuer... ###")
                    return ("")
                else:
                    print("### Veuillez choisir une des réponses proposées. ###")
        except:
            print("+++ Erreur dans la suppression de données +++")
            self.cnx.rollback()
        finally:
            cursor.close()







    def Intable(self, nombre):
        try:
            int_nombre=int(nombre)
            return True
        except:
            return False