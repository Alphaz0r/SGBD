

class Users():
    def __init__(self):
        pass

    def Menu(self):
        quit=False
        while(quit==False):
            interface_console.aff_menu_users(self.table_name[0])  #Affichage menu table
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
        try:    
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            sql="SELECT * FROM users"
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