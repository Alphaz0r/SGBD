class Users_modele():
    """
    Users model for table ``users`` in db
    
    Attributes :
        - PK_client_id 
        - name 
        - pseudonyme 
        - password ( hash )

    """
    def __init__(self):
        self.PK_client_id="None"
        self.name="None"
        self.pseudonyme="None"
        self.password="None"