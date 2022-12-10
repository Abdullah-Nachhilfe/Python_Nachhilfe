import os 
# Directory oder Dir ==> Folder, Ordner

print('Current Working Directory',os.getcwd())

# List of Files/Folders in CWD
print(os.listdir())
# Sucht im aktuellen Working Directory
print(os.path.isdir('Woche3'))
# Sucht im Path/Pfad E:....
print(os.path.isdir("E:\\ASOTE_Python_Nachhilfe\\Nachhilfe\\Kapitel3\\Woche3"))

# Sucht im aktuellen Working Directory
print(os.path.isfile('ModulOs01.py'))
# Sucht im Path/Pfad E:....
print(os.path.isfile("E:\\ASOTE_Python_Nachhilfe\\Nachhilfe\\Kapitel3\\Labor4_1.py"))

# Ordner anlegen:
if not os.path.isdir('Kapitel15'):
    os.mkdir('Kapitel15')
    
# Change CWD to Kapitel15
if os.path.isdir('Kapitel15'):
    os.chdir('Kapitel15')

# ..
print('CWD ist:',os.getcwd())
os.chdir('..')
print('CWD ist:',os.getcwd())

# Lösche Kapitel15
if os.path.isdir('Kapitel15'):
    os.rmdir('Kapitel15')