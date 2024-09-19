from django.contrib.auth.hashers import PBKDF2PasswordHasher

# Put all hashers here

class UserPasswordHasherPBKDF2(PBKDF2PasswordHasher):
    # Set iterations
    iterations = PBKDF2PasswordHasher.iterations * 100
