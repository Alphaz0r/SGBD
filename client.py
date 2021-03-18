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


    def Insert_Row(self):      #INSERT INTO `clients` (`PK_client_id`, `name`, `first_name`, `birth_date`, `age`, `rue`, `house_number`, `postcode`, `email`, `phone_number`) 
                                #VALUES (NULL, 'Odenthal', 'Laetitia', '2017-06-13', '20', 'Rue de la Vallée', '82', '7852', 'unemail@email.email.emailemail', '045896525');
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            query_list=self.Build_Row()
            reponse=input("\nÊtes vous sûr de vouloir insérer les valeurs entrées précédemment dans la base de données ? Y/N\nVotre réponse : ")
            if reponse=="Y":
                sql="INSERT INTO pharmacie.clients (PK_client_id, name, first_name, birth_date, age, rue, house_number, postcode, email, phone_number) VALUES "
                sql+="("+query_list[0]+", '"+query_list[1]+"','"+query_list[2]+"','"+query_list[3]+"',"+query_list[4]+",'"+query_list[5]+"','"+query_list[6]+"','"+query_list[7]+"','"+query_list[8]+"','"+query_list[9]+"');"
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
        query_list=["NULL"]
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
                    rep=input("Valeur : ")      #TODO : Gérer la date et l'âge et rien
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###")
                    elif value=="Age":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###")
                            test_int=self.Intable(rep)
                    elif value=="Date de naissance":
                        test_date=self.Dateable(rep)
                        while(test_date==False):
                            rep=input("### Veuillez entrer une date selon ce format : YYYY-MM-DD  ###")
                            test_date=self.Dateable(rep)
                        rep+=' 00:00:00'
                        print(rep)
                    
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
                    return None
            except:
                print("+++ Erreur dans la validation des données +++")


    def Delete_Row(self):
        try:
            chiffre=False
            cursor=self.cnx.cursor()
            sql="DELETE FROM clients"
            while(chiffre==False):
                id=input("Veuillez choisir l'ID de la ligne à effacer\nVotre choix : ") #TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur
                chiffre=self.Intable(id)
            
            while(True):
                reponse=input("La ligne avec l'ID "+id+" va être supprimée. Confirmer ? Y/N\nVotre réponse : ")
                if reponse=="Y":
                    sql+=" WHERE clients.PK_client_id="+id
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
        finally:
            cursor.close()

    def Alter_Row(self):
        try:
            #Initialisation des variables... 
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            cursor=self.cnx.cursor()
            sql_update="UPDATE clients SET "

            #On demande l'ID nécessaire pour la modification de la ligne
            chiffre=False
            while(chiffre==False):
                id=input("Veuillez choisir l'ID de la ligne à modifier\nVotre choix : ") #TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur de son existence ou pas
                chiffre=self.Intable(id)    

            #Affichage pour l'utilisateur de la ligne AVANT modification
            sql_select="SELECT PK_client_id, name, first_name, CAST(birth_date AS CHAR),age, rue, house_number, postcode, email, phone_number FROM clients WHERE clients.PK_client_id="
            sql_select+=id
            cursor.execute(sql_select)
            for row in cursor:
                table_before.rows.append(row)  
            print(table_before)

            #Préparation de la modification de la ligne
            while(True):
                reponse=input("Préparation de la modification de la ligne ci-dessus. Confirmer ? Y/N\nVotre choix :")
                if reponse=="Y":
                    new_info=self.Build_Row()
                    print(new_info)
                    if new_info==None:
                        return None
                    else:           #["PK_client_id", "name", "first_name", "birth_date", "age", "rue", "house_number", "postcode", "email", "phone_number"]
                        sql_update+="name='"+new_info[1]+"', first_name='"+new_info[2]+"', birth_date='"+new_info[3]+"', age='"+new_info[4]+"', rue='"+new_info[5]+"', house_number='"+new_info[6]+"', postcode='"+new_info[7]+"', email='"+new_info[8]+"', phone_number='"+new_info[9]+"'"
                        sql_update+=" WHERE PK_client_id="+id
                        print(sql_update)
                        cursor.execute(sql_update)
                        self.cnx.commit()
                        return None

                elif reponse=="N":
                    print("Retour au menu...")
                    return None
        except:
            print("+++ Erreur dans la modification des données +++")
            self.cnx.rollback()
        finally:
            cursor.close()













    #
    # Méthodes de tests
    #
    def Intable(self, nombre):
        try:
            int_nombre=int(nombre)
            return True
        except:
            return False

    def Dateable(self, date):
        try:
            date=datetime.strptime(date, '%Y-%m-%d')
            return True
        except:
            return False
    #
    #
    #

       



        

