import mysql.connector
import interface_console
import database
from beautifultable import BeautifulTable
from datetime import datetime

class Facture_row():
    def __init__(self):






    def Afficher_Table(self):
        sql="SELECT facture.PK_facture_id, facture_row.PK_fd_id, facture_row.FK_drug_id, drugs.name, drugs.description, concentration.concentration_mg, clients.PK_client_id, clients.name, clients.first_name, facture.FK_client_id "
        sql+="FROM clients JOIN facture "
        sql+="ON clients.PK_client_id=facture.FK_client_id " 
        sql+="JOIN facture_row "
        sql+="ON facture.PK_facture_id=facture_row.FK_facture_id "
        sql+="JOIN drugs "
        sql+="ON facture_row.FK_drug_id=drugs.PK_drug_id "
        sql+="JOIN concentration "
        sql+="ON drugs.FK_concentration_id=concentration.PK_concentration_id "

        cursor=self.cnx.cursor()
