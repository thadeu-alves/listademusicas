import DataBase
import os

index = 0

def read():
    os.system('cls')
    ind = 1
    for music in DataBase.DB:
        name = music["name"]
        print(f"[{ind}] - {name}")
        ind += 1

def create(ind):
    os.system('cls')
    name = input("Digite o nome da musica que você deseja cadastrar: ")
    DataBase.DB.insert(ind, {"name": name})

def update():
    read()
    op = int(input("Digite qual musica voce deseja alterar: ")) - 1
    DataBase.DB.pop(op)
    create(op)

def delete():
    read()
    op = int(input("Digite qual musica voce deseja alterar: ")) - 1
    DataBase.DB.pop(op)

op = -1
while(op!=0):
    os.system('cls')
    print('[1] - Read')
    print('[2] - Create')
    print('[3] - Update')
    print('[4] - Delete')
    print('[0] - End')
    op = int(input("Digite o que voce deseja fazer: "))
    if(op==1):
        read()
        os.system('pause')
    elif(op==2):
        index = len(DataBase.DB)
        create(index)
    elif(op==3):
        update()
    elif(op==4):
        delete()