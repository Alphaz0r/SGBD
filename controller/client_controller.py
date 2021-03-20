import mysql.connector
import sys
sys.path.append("..\\model\\")
sys.path.append("..\\view\\")
from view.client_vue import *
from model.client_modele import *
from beautifultable import BeautifulTable
from datetime import datetime
from singleton import *

"""
 CLASSE Client_controller
          Nécessite la connexion à la base de données pour s'instancier
"""
class Client_controller(Singleton):
    def __init__(self, cnx): #Il faut récupérer la connexion "cnx" à la base de données pour l'utiliser avec les pointeurs cursor() 
        self.cnx=cnx
        self.aff_col= ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"] #Colonnes d'affichage pour BeautifulTables
        self.vue_client=Client_vue()                                                                                                                #Création de la vue
        self.modele_client=Client_modele(self.cnx)                                                                                                  #Création du modèle
                                                                                                                                                """ J'ai choisi d'instancier ces classes directement dans le constructeur
                                                                                                                                                    Comme ca je peux les réutiliser partout directement où je veux.
                                                                                                                                                    Cependant j'ai remarqué que l'inconvénient majeur de cnx est qu'il n'est utilisable
                                                                                                                                                    qu'une seule fois pour plusieurs objets. Càd que si j'instancie un autre objet
                                                                                                                                                    utilisant cnx, le programme retournera une erreur sql"""
    """
    Menu principal
    """
    def Menu(self):
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
    """
    Création
    """
    def Create_Row(self):
        try:
            #BeautifulTable
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col
            #On demande une confirmation au user
            confirmation=self.vue_client.getConfirmation(id,0)  
            if confirmation==True:   
                #On propose un formulaire au user     
                row=self.vue_client.getRow(self.aff_col)
                if row!=None:
                    #Insertion dans la base de données
                    creation_reussie=self.modele_client.Insert_Row(row)
                    if creation_reussie==True:
                        #Si tout a bien fonctionné on notifie le user de la réussite
                        self.vue_client.Display_BackToMenu()
                        return None
            #Si il y a eu une erreur quelque part... Appeler le service informatique
            self.vue_client.Display_Alter_Error()
        except:
            return None
    """
    Affichage
    """
    def Display_Rows(self):   
        try:
            #Préparation du curseur + BeautifulTable
            cursor=self.modele_client.Select_Rows()
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
    """
    Suppression
    """
    def Delete_Row(self):
        try:
            #On va directement chercher l'id de la ligne à effacer + une confirmation pour informer l'utilisateur
            id=self.vue_client.Row_getId()
            confirmation=self.vue_client.getConfirmation(id,1)
            if  confirmation == True and id!=False:
                #Suppression dans la bdd
                self.modele_client.Delete_Row(id)
                #Information de la réussite
                self.vue_client.Display_BackToMenu()
            else:
                self.vue_client.Display_Delete_Error()
        except:
            self.vue_client.Display_Delete_Error()
    """
    Modification
    """
    def Update_Row(self):
        try:
            #BeautifulTable
            table_before=BeautifulTable(maxwidth=300)                   
            table_before.columns.header=self.aff_col   
            #On demande l'id de la ligne à modifier
            id=self.vue_client.Row_getId()
            if id !=False:
                #On va chercher la ligne correspondant à ce qu'a choisi l'utilisateur
                cursor=self.modele_client.Select_Rows(id)
                #On stocke tout dans BeautifulTable
                for row in cursor:
                    table_before.rows.append(row)  
                #Affichage au client + confirmation
                self.vue_client.Display_Rows(table_before)

                confirmation=self.vue_client.getConfirmation(id,0)  
                if confirmation==True:  
                    #On propose un formulaire pour les nouvelles 
                    row=self.vue_client.getRow(self.aff_col)
                    if row!=None:
                        modification_reussie=self.modele_client.Update_Row(row, id)
                        if modification_reussie==True:
                            self.vue_client.Display_BackToMenu()
                            return None
                self.vue_client.Display_Alter_Error()

        except:
            return None


    def getClientId(self, id):
        try:
            cursor=self.modele_client.Select_clientId(id)
            if cursor==None:
                print("Erreur")
            else:
                return cursor
        except:
            self.vue_client.Display_Select_Error()
        finally:
            cursor.close()

           


       