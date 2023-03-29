import hmac
import hashlib
import binascii

def create_sha256_signature(key, message):
    byte_key = binascii.unhexlify(key)
    message = message.encode()
    hmacstr = hmac.new(byte_key, message, hashlib.sha256).hexdigest().upper()
    print(hmacstr)
    return hmacstr

create_sha256_signature("E49756B4C8FAB4E48222A3E7F3B97CC3", "TEST STRING")