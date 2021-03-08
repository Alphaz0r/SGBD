import mysql.connector
import interface_console
import database, client, table

if __name__=="__main__":
    while(True):
        letsgo=database.Database()
        choix=letsgo.QueFaire()
        if choix=="1":
            clientDAO=table.Table(letsgo.cnx, "clients", ["PK_client_id", "name", "first_name", "birth_date", "age", "rue", "house_number", "postcode", "email", "phone_number"])
        elif choix=="2":
            factureDAO=facture.Facture(letsgo.cnx)
        elif choix=="3":
            drugDAO=drugs.Drugs(letsgo.cnx)
        elif choix=="4":
            concentrationDAO=concentration.Concentration(letsgo.cnx)
    