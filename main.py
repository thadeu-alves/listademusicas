import DataBase
import os
import create

index = 0

def read():
    os.system('cls')
    ind = 1
    for music in DataBase.DB:
        name = music["name"]
        tone = music["tone"]
        if(music["scale"] == 1):
            scale = "major"
        else:
            scale = "minor"
        print(f"[{ind}] - {name}: {tone} {scale}")
        ind += 1

def update():
    read()
    op = int(input("Digite qual musica voce deseja alterar: ")) - 1
    DataBase.DB.pop(op)
    create.new(op)

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
        create.new(index)
    elif(op==3):
        update()
    elif(op==4):
        delete()