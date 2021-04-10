import mysql.connector
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
sys.path.append("..\\DAO\\")
from model.client_model import *
from view.client_vue import *
from DAO.client_DAO import *
from beautifultable import BeautifulTable
from datetime import datetime
from singleton import *

class Client_controller():
    """
    Client controller class for ``client`` table
    
    ``cnx`` is the connection object from ``mysql-connector`` needed to send sql commands to the database
    """
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col= ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"] #Colonnes d'affichage pour BeautifulTables
        self.vue_client=Client_vue()                                                                                                                #Création de la vue
        self.DAO_client=Client_DAO(self.cnx)                                                                                                        #Création du modèle
                                                                                                                                                    #J'ai choisi d'instancier ces classes directement dans le constructeur
                                                                                                                                                    #Comme ca je peux les réutiliser partout directement où je veux.
                                                                                                                                                    #Cependant j'ai remarqué que l'inconvénient majeur de cnx est qu'il n'est utilisable
                                                                                                                                                    #qu'une seule fois pour plusieurs objets. Càd que si j'instancie un autre objet
                                                                                                                                                    #utilisant cnx, le programme retournera une erreur sql

    def Menu(self):
        """Call client_vue to display menu then use its return to launch a chosen by user sequence
        """
        while(True):
            choix_utilisateur=self.vue_client.Menu()
            if choix_utilisateur=="1":
                self.Display_Rows()
            if choix_utilisateur=="2":
                self.Update_Row()
            elif choix_utilisateur=="3":
                self.Delete_Row()
            elif choix_utilisateur=="4":
                self.Create_Row()
            elif choix_utilisateur=="5":
                break
    
    def Create_Row(self):
        """Launch a sequence to create a row in the table

        Returns:
            [None]: If all went well it will return None, however it will display an error
        """
        try:
            #BeautifulTable
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            #On demande une confirmation au user
            confirmation=self.vue_client.getConfirmation(id,2)  
            if confirmation==True:   
                #On propose un formulaire au user     
                row=self.vue_client.getRow(self.aff_col)

                modele_client=Client_modele()
                modele_client.PK_client_id=row[0]
                modele_client.name=row[1]
                modele_client.first_name=row[2]
                modele_client.birth_date=row[3]
                modele_client.age=row[4]
                modele_client.rue=row[5]
                modele_client.house_number=row[6]
                modele_client.postcode=row[7]
                modele_client.email=row[8]
                modele_client.phone_number=row[9]

                #Insertion dans la base de données
                creation_reussie=self.DAO_client.Insert_Row(modele_client)
                if creation_reussie==True:
                    #Si tout a bien fonctionné on notifie le user de la réussite
                    self.vue_client.Display_BackToMenu()
                    return None
                #Si il y a eu une erreur quelque part... Appeler le service informatique
                self.vue_client.Display_Create_Error()
            else :
                print("\n### Aucune action n'a été entreprise, retour au menu ###")
        except:
            self.vue_client.Display_Create_Error()
    
    def Display_Rows(self):   
        """Launch a sequence to display the table to the user
        """
        try:
            #Préparation du curseur + BeautifulTable
            cursor=self.DAO_client.Select_Rows()
            table=BeautifulTable(maxwidth=300) 
            #On exécute la query et on y place tous ses éléments dans un module qui va gérer l'affichage (BeautifulTable)
            table.columns.header=self.aff_col  
            for row in cursor:
                table.rows.append(row)  
                
            #Affichage de la table
            self.vue_client.Display_Rows(table)
        except:
            self.vue_client.Display_Select_Error()    
        finally:
            if cursor!=None:
                cursor.close()
    
    def Delete_Row(self):
        """Launch a sequence to delete a row chosen by the user
        """
        try:
            #On va directement chercher l'id de la ligne à effacer + une confirmation pour informer l'utilisateur
            id=self.vue_client.Row_getId()
            confirmation=self.vue_client.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                #Suppression dans la bdd
                self.DAO_client.Delete_Row(id)
                #Information de la réussite
                self.vue_client.Display_BackToMenu()
            else:
                self.vue_client.AucuneActionEntreprise()
        except:
            self.vue_client.Display_Delete_Error()
    
    def Update_Row(self):
        """Launch a sequence to update a row chosen by the user
        """
        try:
            modele_client=Client_modele()
            #BeautifulTable
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   
            #On demande l'id de la ligne à modifier
            modele_client.PK_client_id=self.vue_client.Row_getId()
            if modele_client.PK_client_id !=False:
                #On va chercher la ligne correspondant à ce qu'a choisi l'utilisateur
                cursor=self.DAO_client.Select_Rows(modele_client.PK_client_id)
                #On stocke tout dans BeautifulTable
                for row in cursor:
                    table_before.rows.append(row)  
                #Affichage au client + confirmation
                self.vue_client.Display_Rows(table_before)

                confirmation=self.vue_client.getConfirmation(modele_client.PK_client_id,0)  
                if confirmation==True:  
                    #On propose un formulaire pour les nouvelles 
                    row=self.vue_client.getRow(self.aff_col)

                    modele_client.name=row[1]
                    modele_client.first_name=row[2]
                    modele_client.birth_date=row[3]
                    modele_client.age=row[4]
                    modele_client.rue=row[5]
                    modele_client.house_number=row[6]
                    modele_client.postcode=row[7]
                    modele_client.email=row[8]
                    modele_client.phone_number=row[9]

                    if row!=None:
                        modification_reussie=self.DAO_client.Update_Row(modele_client)
                        if modification_reussie==True:
                            self.vue_client.Display_BackToMenu()
                            return None
                self.vue_client.Display_Alter_Error()

        except:
            self.vue_client.Display_Alter_Error()


    def getClientId(self, id):
        """Call the DAO to get a client filtered by its id

        Args:
            id ([String]): client's id

        Returns:
            MySQLCursor: MySQLCursor with client id inside of it
        """
        try:
            cursor=self.DAO_client.Select_clientId(id)
            if cursor==None:
                print("Erreur")
            else:
                return cursor
        except:
            self.vue_client.Display_Select_Error()
        finally:
            cursor.close()

           


       