import mysql.connector
import interface_console
import database, drugs, facture, client, users, concentration

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.Menu()
        if choix=="1":
            client=client.Client(launcher.cnx)
        elif choix=="2":
            facture=facture.Facture(launcher.cnx)
        elif choix=="3":
            drug=drugs.Drugs(launcher.cnx)
        elif choix=="4":
            concentration=concentration.Concentration(launcher.cnx)
        elif choix=="5":
            users=users.Users(launcher.cnx)
    