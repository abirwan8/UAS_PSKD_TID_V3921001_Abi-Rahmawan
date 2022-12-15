# import modul
from cryptography.fernet import Fernet

# Enkripsi

# key generation
key = Fernet.generate_key()
 
# read string kunci
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)


# pakai kunci
fernet = Fernet(key)
 
# buka file csv
with open('D:/SKD/file_csv.csv', 'rb') as file:
    original = file.read()
     
# enkripsi csv
encrypted = fernet.encrypt(original)
 
# simpan file enkripsi
with open('D:/SKD/file_csv_terenkripsi.csv', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

# Deskripsi

# read string kunci
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)
 
# pakai kunci yang tadi
fernet = Fernet(key)

# buka file hasil enkrpisi
with open('D:/SKD/file_csv_terenkripsi.csv', 'rb') as enc_file:
	encrypted = enc_file.read()

# langsung di dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek hasil dekripsi cocok apa tidak ??
with open('D:/SKD/file_csv_terenkripsi.csv', 'wb') as dec_file:
	dec_file.write(decrypted)
