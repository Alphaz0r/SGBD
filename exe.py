import mysql.connector
import interface_console
import database, table

if __name__=="__main__":
    launcher=database.Database()
    while(True):
        choix=launcher.QueFaire()
        if choix=="1":
            client=table.Table(launcher.cnx, ["clients"], ["PK_client_id", "name", "first_name", "birth_date", "age", "rue", "house_number", "postcode", "email", "phone_number"])
        elif choix=="2":
            facture=table.Table(launcher.cnx, ["facture"], ["PK_facture_id", "total_price"])
        elif choix=="3":
            drug=table.Table(launcher.cnx, ["drugs"], ["PK_drug,id","name","description","peremption_date","price"])
        elif choix=="4":
            concentration=table.Table(launcher.cnx, ["concentration"], ["PK_concentration_id", "concentration_mg"])
    