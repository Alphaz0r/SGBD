class Facture_modele():
    """
    Facture model for table ``facture`` in db
    
    Attributes :
        - PK_facture_id 
        - total_price = count()
        - FK_client_id 
        - date_creation 
    """
    def __init__(self):
        self.PK_facture_id="None"
        self.total_price="None"
        self.FK_client_id="None"
        self.date_creation="None"