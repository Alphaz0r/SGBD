import mysql.connector
import interface_console
import database, concentration
from beautifultable import BeautifulTable
from datetime import datetime


class Drugs():
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor()
        self.table_name=["drugs", "concentration"] 
        self.cnx=cnx
        self.col=["PK_drug_id","name","description","peremption_date","price", "stock", "concentration_mg", "PK_concentration_id"]
        self.aff_col=["ID Médicaments", "Nom", "Description", "Date de péremption", "Prix en €€€", "Stock", "ID Concentration en mg"]      #Pour affichage
        
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

            input("\nPressez n'importe quelle touche pour continuer...")
        except:
            print("\n+++Une erreur est survenue lors de l'affichage de valeurs dans la table+++")
        finally:
            cursor.close()


    def Insert_Rows(self):      #INSERT INTO `clients` (`PK_client_id`, `name`, `first_name`, `birth_date`, `age`, `rue`, `house_number`, `postcode`, `email`, `phone_number`) 
                                #VALUES (NULL, 'Odenthal', 'Laetitia', '2017-06-13', '20', 'Rue de la Vallée', '82', '7852', 'unemail@email.email.emailemail', '045896525');
        try:
            cursor=self.cnx.cursor()    #Initialisation du curseur qui va exécuter la requête SQL
            query_list=self.Build_Row()
            reponse=input("\nÊtes vous sûr de vouloir insérer les valeurs entrées précédemment dans la base de données ? Y/N\nVotre réponse : ")
            if reponse=="Y":
                sql="INSERT INTO pharmacie.drugs(PK_drug_id, name, description, peremption_date, price, stock, FK_concentration_id) VALUES "
                sql+="("+query_list[0]+", '"+query_list[1]+"','"+query_list[2]+"','"+query_list[3]+"',"+query_list[4]+",'"+query_list[5]+"','"+query_list[6]+"');"
                print(sql)
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
        table_vide.rows.append(["","","","","","",""])  #Ajout de valeur "invisible" dans la table magique pour pouvoir afficher à l'utilisateur la row qu'il souhaite remplir de valeurs
        print(table_vide)
        try:
            for value in self.aff_col:
                if value!="ID Médicaments":
                    if value=="ID Concentration en mg":
                        input("Affichage des concentration pour sélection de l'ID, appuyer sur n'importe quelle touche pour afficher les concentrations disponibles.\nSi la concentration voulue n'est pas disponible, veuillez l'ajouter via le menu des concentrations.")
                        concentration_affiche=concentration.Concentration(self.cnx)
                        concentration_affiche.Display_Rows()
                    print("Indiquez une valeur pour \""+value+"\"")    
                    rep=input("Valeur : ")     
                    if rep=="":    
                        while rep=="":
                            rep=input("### Veuillez entrer une valeur ###\nValeur : ")
                    elif value=="stock":
                        test_int=self.Intable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###\nValeur : ")
                            test_int=self.Intable(rep)
                    elif value=="price":
                        test_int=self.Floatable(rep)
                        while(test_int==False):
                            rep=input("### Veuillez entrer un NOMBRE  ###\nValeur : ")
                            test_int=self.Floatable(rep)
                    elif value=="Date de péremption":
                        test_date=self.Dateable(rep)
                        while(test_date==False):
                            rep=input("### Veuillez entrer une date selon ce format : YYYY-MM-DD  ###\nValeur : ")
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
                    return("")
            except:
                print("+++ Erreur dans la validation des données +++")


    def Delete_Row(self):
        try:
            chiffre=False
            cursor=self.cnx.cursor()
            sql="DELETE FROM drugs"
            while(chiffre==False):
                id=input("Veuillez choisir l'ID de la ligne à modifier\nVotre choix : ")
                chiffre=self.Intable(id)
            
            while(True):
                reponse=input("La ligne avec l'ID "+id+" va être supprimée. Confirmer ? Y/N\nVotre réponse : ")
                if reponse=="Y":
                    sql+=" WHERE drugs.PK_drug_id="+id
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


    def Alter_Row(self):
        try:
            #Initialisation des variables... 
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            cursor=self.cnx.cursor()
            sql_update="UPDATE drugs SET "

            #On demande l'ID nécessaire pour la modification de la ligne
            chiffre=False
            while(chiffre==False):
                id=input("Veuillez choisir l'ID de la ligne à modifier\nVotre choix : ") #TODO: Vérifier que l'id se trouve dans la bdd pour notifier l'utilisateur de son existence ou pas
                chiffre=self.Intable(id)    

            #Affichage pour l'utilisateur de la ligne AVANT modification
            sql_select="SELECT drugs.PK_drug_id, drugs.name, drugs.description, CAST(drugs.peremption_date AS CHAR),drugs.price, drugs.stock, concentration.concentration_mg FROM drugs JOIN concentration ON drugs.PK_drug_id = concentration.PK_concentration_id WHERE PK_drug_id="
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
                        sql_update+=" WHERE PK_drug_id="+id
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
    # Méthodes de tests & validation des input spécifiques
    #
    def Intable(self, nombre):
        try:
            int_nombre=int(nombre)
            return True
        except:
            return False

    def Floatable(self, nombre):
        try:
            float_nombre=float(nombre)
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