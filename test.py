import mysql.connector
import database
import table

ecole = database.Database() #voir connexion.py 
ecole.Show_Tables()

print("\n")

classe=table.Table(ecole.cnx, "classe") #On rentre dans la table "classe" de la base de données "ecole"
classe.Select_all() #On fait un select * de toutes les colonnes de "classe"

print("\n")

professeur=table.Table(ecole.cnx, "professeur") #On rentre dans la table "professeur" de la base de données "ecole"
professeur.Select_all() #On fait un select * de toutes les colonnes de "classe"




ecole.Se_Deconnecter()  #voir connexion.py
