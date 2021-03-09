import mysql.connector
import interface_console
import database, drugs, facture, client

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.QueFaire()
        if choix=="1":
            client=client.Client(launcher.cnx, ["clients"], ["PK_client_id", "name", "first_name", "birth_date", "age", "rue", "house_number", "postcode", "email", "phone_number"], ["ID", "Nom", "Prénom", "Date de naissance", "Age", "Rue", "Numéro de maison", "Code postal", "Email", "Numéro de téléphone"])
        elif choix=="2":
            facture=table.Table(launcher.cnx, ["facture"], ["PK_facture_id", "total_price"], ["CHANGEZ dans exe.py"])
        elif choix=="3":
            drug=drugs.Drugs(launcher.cnx, ["drugs", "concentration"], ["PK_drug_id","name","description","peremption_date","price", "stock", "concentration_mg", "PK_concentration_id"], ["ID Médicaments", "Nom", "Description", "Date de péremption", "Prix en €", "Stock", "Concentration en mg"])
        elif choix=="4":
            concentration=table.Table(launcher.cnx, ["concentration"], ["PK_concentration_id", "concentration_mg"], ["CHANGEZ dans exe.py"])
    