
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
    print("*****                  *****")



#
#                  Tables
#

def aff_menu_table(nomTable):
    print("\n################ Bienvenue dans la gestion des "+nomTable+" ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les "+ nomTable+" et leurs infos                                                            #")
    print("# Choix 2 : Modifier les informations d'un ou plusieurs " +nomTable+"                                            #")
    print("# Choix 3 : Supprimer un(e) ou plusieurs "+nomTable+" ainsi que ses informations /!\ action irréversible /!\        #")
    print("# Choix 4 : Ajouter un nouveau/une nouvelle "+nomTable+"                                                         #")
    print("# Choix 5 : Sortir de la gestion des " + nomTable + "                                                            #")
    print("##############################################################################################################")


def aff_menu_facture():
    print("\n################ Bienvenue dans la gestion des factures ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les factures et leurs clients associés                                                 #")
    print("# Choix 2 : Afficher les détails d'une facture                                                              #")
    print("# Choix 3 : Modifier les informations d'une facture                                                         #")
    print("# Choix 4 : Supprimer une ou plusieurs factures ainsi que ses informations /!\ action irréversible /!\      #")
    print("# Choix 5 : Insérer une nouvelle facture                                                                    #")
    print("# Choix 6 : Sortir de la gestion des factures                                                               #")
    print("##############################################################################################################")


def aff_menu_users():
    print("\n################ Bienvenue dans la gestion des utilisateurs ! ##########################")
    print("##############################################################################################################")
    print("# Choix 1 : Afficher les utilisateurs                                                                       #")
    print("# Choix 3 : Modifier les informations d'un utilisateur                                                      #")
    print("# Choix 4 : Supprimer un utilisateur ainsi que ses informations /!\ action irréversible /!\                 #")
    print("# Choix 5 : Insérer un nouvel utilisateur                                                                   #")
    print("# Choix 6 : Sortir de la gestion des utilisateurs                                                           #")
    print("##############################################################################################################")