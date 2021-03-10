import mysql.connector
import interface_console
import database, drugs, facture, client, users, concentration

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.Menu()
        if choix=="1":
            clientDAO=client.Client(launcher.cnx)
        elif choix=="2":
            factureDAO=facture.Facture(launcher.cnx)
        elif choix=="3":
            drugDAO=drugs.Drugs(launcher.cnx)
        elif choix=="4":
            concentrationDAO=concentration.Concentration(launcher.cnx)
        elif choix=="5":
            usersDAO=users.Users(launcher.cnx)
    