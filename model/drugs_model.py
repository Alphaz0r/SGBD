class Drugs_modele():
    """
    Drugs model for table ``drugs`` in db
    
    Attributes :
        - PK_drug_id 
        - name
        - description 
        - peremption_date
        - price
        - FK_concentration_id
        - stock 
    """
    def __init__(self):
        self.PK_drug_id="None"
        self.name="None"
        self.description="None"
        self.peremption_date="None"
        self.price="None"
        self.FK_concentration_id="None"
        self.stock="None"