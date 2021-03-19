import hashlib, binascii, os
    
    
    
def hash_password(password):  #Trouvée sur internet
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                      password.encode('utf-8'), 
                                      salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash).decode('ascii')

def verify_password(stored_password, provided_password): #Trouvée sur internet
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                    provided_password.encode('utf-8'), 
                                    salt.encode('ascii'), 
                                    100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password


print(hash_password("password"))

print(verify_password("8d9f1a4ca22d565c2316dbb92ba152903e650962237ec3652bd1ec1b8192437a00a16d7ce13190598707d54dc0c1778c148c6535f2aa7defe71e63982d99ac6dd6a9a542058f09a16799231c848c8c85432dae3dc6bc65b32fe15aa742bf1238", "password"))