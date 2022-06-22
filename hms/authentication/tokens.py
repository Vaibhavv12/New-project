from lib2to3.pgen2.tokenize import generate_tokens
from typing_extensions import Self
from MySQLdb import Timestamp
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(Self,user,Timestamp):
       return (
        text_type(user.pk) + text_type(Timestamp)
       )
generate_tokens = TokenGenerator()    