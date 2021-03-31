class Facture_row_modele():
    """
    Facture_row model for table ``facture_row`` in db
    
    Attributes :
        - PK_fd_id 
        - item_count 
        - FK_drug_id 
        - FK_facture_id
    """
    def __init__(self):
        self.PK_fd_id="None"
        self.item_count="None"
        self.FK_drug_id="None"
        self.FK_facture_id="None"