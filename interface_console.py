
#
#                   Database.py
#

def aff_menu_principal(dbname):
    print("\n\n***********************************************************************************************************************************************")
    print("**********************************   Que souhaitez-vous faire dans la base de données " + dbname + "?             **********************************")
    print("**********************************     Choix 1 : Accéder aux clients                                         **********************************")
    print("**********************************     Choix 2 : Accéder aux factures                                        **********************************")
    print("**********************************     Choix 3 : Accéder aux drugs                                           **********************************")
    print("**********************************     Choix 4 : Accéder aux concentrations                                  **********************************")
    print("**********************************     Choix 5 : Accéder aux utilisateurs                                    **********************************")
    print("**********************************     Choix 6 : Se déconnecter                                              **********************************")
    print("***********************************************************************************************************************************************")


def aff_acces_table():
    print("\n\n*****                  *****")
    print("***** ACCES A LA TABLE *****")
    print("*****                  *****\n")



#
#                  Tables
#

def aff_menu_clients():
    print("\n################ Bienvenue dans la gestion des clients ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les clients et leurs infos                                                              #")
    print("# Choix 2 : Modifier les informations d'un client                                                            #")
    print("# Choix 3 : Supprimer un client ainsi que ses informations /!\ action irréversible /!\                       #")
    print("# Choix 4 : Ajouter un nouveau client                                                                        #")
    print("# Choix 5 : Sortir de la gestion des clients                                                                 #")
    print("##############################################################################################################")

def aff_menu_users():
    print("\n################ Bienvenue dans la gestion des utilisateurs ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les utilisateurs et leurs infos                                                         #")
    print("# Choix 2 : Modifier les informations d'un utilisateur                                                       #")
    print("# Choix 3 : Supprimer un utilisateur ainsi que ses informations /!\ action irréversible /!\                  #")
    print("# Choix 4 : Ajouter un nouveau utilisateur                                                                   #")
    print("# Choix 5 : Sortir de la gestion des utilisateurs                                                            #")
    print("##############################################################################################################")

def aff_menu_drugs():
    print("\n################ Bienvenue dans la gestion des médicaments ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les médicaments et leurs infos                                                          #")
    print("# Choix 2 : Modifier les informations d'un médicament                                                        #")
    print("# Choix 3 : Supprimer un médicament ainsi que ses informations /!\ action irréversible /!\                   #")
    print("# Choix 4 : Ajouter un nouveau médicament                                                                    #")
    print("# Choix 5 : Sortir de la gestion des médicaments                                                             #")
    print("##############################################################################################################")


def aff_menu_concentration():
    print("\n################ Bienvenue dans la gestion des concentrations ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les concentrations et leurs infos                                                       #")
    print("# Choix 2 : Modifier les informations d'une concentration                                                    #")
    print("# Choix 3 : Supprimer une concentration ainsi que ses informations /!\ action irréversible /!\               #")
    print("# Choix 4 : Ajouter une nouveau concentration                                                                #")
    print("# Choix 5 : Sortir de la gestion des concentrations                                                          #")
    print("##############################################################################################################")


def aff_menu_facture():
    print("\n################ Bienvenue dans la gestion des factures ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les factures et leurs clients associés                                                  #")
    print("# Choix 2 : Afficher les détails d'une facture et interagir avec                                             #")
    print("# Choix 3 : Supprimer une ou plusieurs factures ainsi que ses informations /!\ action irréversible /!\       #")
    print("# Choix 4 : Insérer une nouvelle facture                                                                     #")
    print("# Choix 5 : Sortir de la gestion des factures                                                                #")
    print("##############################################################################################################")


def aff_menu_facturerow(id):
    print("\n------------------ Bienvenue dans la gestion de la facture n°"+id+" ! ---------------------------")
    print("+------------------------------------------------------------------------------------------------------------+")
    print("| Choix 1 : Afficher la facture n°"+id+"                                                                     |")
    print("| Choix 2 : Modifier les informations d'une ligne                                                            |")
    print("| Choix 3 : Supprimer une ligne ainsi que ses informations /!\ action irréversible /!\                       |")
    print("| Choix 4 : Insérer une nouvelle ligne                                                                       |")
    print("| Choix 5 : Sortir de la gestion de la facture                                                               |")
    print("+------------------------------------------------------------------------------------------------------------+")