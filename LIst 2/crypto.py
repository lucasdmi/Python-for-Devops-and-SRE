
import rsa
publicKey, privateKey = rsa.newkeys (512)
message = "mensagem secreta"
encMessage = rsa.encrypt (message.encode (),publicKey)
print("original: ", message)
print("encrypted: ", encMessage)
#decript
decMessage = rsa.decrypt (encMessage, privateKey).decode()
print("decrypted: ", decMessage)