import mysql.connector
import interface_console
import database, drugs, facture, client

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.QueFaire()
        if choix=="1":
            client=client.Client(launcher.cnx)
        elif choix=="2":
            facture=facture.Facture(launcher.cnx)
        elif choix=="3":
            drug=drugs.Drugs(launcher.cnx)
        elif choix=="4":
            concentration=table.Table(launcher.cnx, ["concentration"], ["PK_concentration_id", "concentration_mg"], ["CHANGEZ dans exe.py"])
    