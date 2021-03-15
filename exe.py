import mysql.connector
import interface_console
import database, drugs, facture, client, users, concentration

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.Menu()
        if choix=="1":
            clientDAO=client.Client(launcher.cnx)
            clientDAO.Menu()
        elif choix=="2":
            factureDAO=facture.Facture(launcher.cnx)
            factureDAO.Menu()
        elif choix=="3":
            drugDAO=drugs.Drugs(launcher.cnx)
            drugDAO.Menu()
        elif choix=="4":
            concentrationDAO=concentration.Concentration(launcher.cnx)
            concentrationDAO.Menu()
        elif choix=="5":
            usersDAO=users.Users(launcher.cnx)
            usersDAO.Menu()
    