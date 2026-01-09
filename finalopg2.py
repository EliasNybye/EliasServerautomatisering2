#3hJ3HB0V7lE9wlZ_qDVOFY5oE70kvS4PaPxvb9mRTqA=
ENCRYPTED_PRIVATE_KEY = '3hJ3HB0V7lE9wlZ_qDVOFY5oE70kvS4PaPxvb9mRTqA='
from cryptography.fernet import Fernet


fernet = Fernet(ENCRYPTED_PRIVATE_KEY)
private_key = fernet.decrypt(ENCRYPTED_PRIVATE_KEY)
print(private_key.decode())
