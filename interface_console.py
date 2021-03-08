
#
#                   Database.py
#

def aff_menu_principal(dbname):
    print("\n\n***********************************************************************************************************************************************")
    print("**********************************   Que souhaitez-vous faire dans la base de données " + dbname + "?             **********************************")
    print("**********************************     Choix 1 : Accéder aux clients                                         **********************************")
    print("**********************************     Choix 2 : Accéder aux factures                                        **********************************")
    print("**********************************     Choix 3 : Accéder aux médicaments                                     **********************************")
    print("**********************************     Choix 4 : Accéder aux concentrations                                  **********************************")
    print("**********************************     Choix 5 : Se déconnecter                                              **********************************")
    print("***********************************************************************************************************************************************")


def aff_acces_table():
    print("\n\n*****                  *****")
    print("***** ACCES A LA TABLE *****")
    print("*****                  *****")



#
#                  Client, concentration, facture, drugs
#

def aff_menu_table(nomTable):
    print("\n################ Bienvenue dans la gestion des "+nomTable+" ! ##########################")
    print("########################################################################################")
    print("# Choix 1 : Afficher les "+ nomTable+" et leurs infos                                        #")
    print("# Choix 2 : Modifier les informations d'un ou plusieurs " +nomTable+"                                      #")
    print("# Choix 3 : Supprimer un ou plusieurs "+nomTable+" ainsi que ses informations /!\ action irréversible /!\ #")
    print("# Choix 4 : Sortir de la gestion des " + nomTable + "                                           #")
    print("########################################################################################")