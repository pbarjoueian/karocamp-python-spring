import cryptocode

myEncryptedMessage = cryptocode.encrypt("I like trains", "password123")
print(myEncryptedMessage)

myDecryptedMessage = cryptocode.decrypt(
    "oNJMMlsJC22qOGvqDg==*dVRKrKawB6q27elqA59WHw==*85/VWoLw0f/Wn4Wem/jcAg==*4nUdsI6n0Bp5ib6Y4nNK+g==",
    "password123",
)
print(myDecryptedMessage)
