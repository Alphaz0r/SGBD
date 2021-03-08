import mysql.connector
import interface_console
import database, client

if __name__=="__main__":
    while(True):
        letsgo=database.Database()
        choix=letsgo.QueFaire()
        if choix=="1":
            clientDAO=client.Client(letsgo.cnx)
        elif choix=="2":
            factureDAO=facture.Facture()
        elif choix=="3":
            drugDAO=drugs.Drugs()
        elif choix=="4":
            concentrationDAO=concentration.Concentration()
    