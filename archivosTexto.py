from io import open

"""archivo1 = open("archivo.txt","a")
archivo1.write("\n Saludo IDGS801")
archivo1.close()
"""
"""
archivo1= open("archivo.txt","r")
datos = archivo1.read()
archivo1.seek(0)
print(datos)
archivo1.close()
"""
archivo1= open("archivo.txt","r")
datos = archivo1.readlines()

print(datos)
archivo1.close()