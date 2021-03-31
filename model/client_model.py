class Client_modele():
    """
    Client model for table ``client`` in db
    
    Attributes :
        - PK_client_id 
        - name
        - first_name 
        - birth_date
        - age
        - rue
        - house_number
        - postcode
        - email
        - phone_number 
    """
    def __init__(self):
        self.PK_client_id="None"
        self.name="None"
        self.first_name="None"
        self.birth_date="None"
        self.age="None"
        self.rue="None"
        self.house_number="None"
        self.postcode="None"
        self.email="None"
        self.phone_number="None"