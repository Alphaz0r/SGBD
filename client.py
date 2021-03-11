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


    def Insert_Rows(self):      #INSERT INTO `clients` (`PK_client_id`, `name`, `first_name`, `birth_date`, `age`, `rue`, `house_number`, `postcode`, `email`, `phone_number`) 
                                #VALUES (NULL, 'Odenthal', 'Laetitia', '2017-06-13', '20', 'Rue de la Vallée', '82', '7852', 'unemail@email.email.emailemail', '045896525');
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            query_list=self.Build_Row()
            reponse=input("\nÊtes vous sûr de vouloir insérer les valeurs entrées précédemment dans la base de données ? Y/N\nVotre réponse : ")
            if reponse=="Y":
                sql="INSERT INTO pharmacie.clients (PK_client_id, name, first_name, birth_date, age, rue, house_number, postcode, email, phone_number) VALUES "
                sql+="(NULL, '"+query_list[0]+"','"+query_list[1]+"','"+query_list[2]+"',"+query_list[3]+","+query_list[4]+",'"+query_list[5]+"','"+query_list[6]+"','"+query_list[7]+"','"+query_list[8]+"');"
                print(sql)
                cursor.execute(sql)
                self.cnx.commit()
            elif reponse=="N":
                print("### Annulation de l'insertion de données... Retour au menu...")
            else:
                print("La réponse doit être Y, N ou Q")
        except:
            print("+++ Erreur dans l'insertion des données +++")
        finally:
            cursor.close()



    def Build_Row(self):
        #Initialisation de la liste qui va récupérer les variables pour la query
        query_list=[]
        #Préparation de la table magique
        table_vide=BeautifulTable(maxwidth=300)
        result_table=BeautifulTable(maxwidth=300)
        result_table.columns.header=self.aff_col
        table_vide.columns.header=self.aff_col
        table_vide.rows.append(["","","","","","","","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in self.aff_col:
                if value!="ID":
                    print("Indiquez une valeur pour \""+value+"\"")     #TODO: Gérer erreur ici insertion
                    rep=input("Valeur : ")
                    if rep=="":
                      rep=input("\n\nIndiquez une valeur pour \""+value+"\"\nRien n'est pas une valeur\nValeur : ")
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
                    return("stop")
            except:
                print("")
       



        

