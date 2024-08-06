import os
import DataBase

def cTone():
    os.system('cls')
    ind = 1
    for i in DataBase.notes:
        print(f"[{ind}] - {i}")
        ind += 1
    op = int(input("Digite o tom da musica: "))
    return op - 1

def listNotes(i):
    notes = DataBase.notes
    new = []
    ind = 0
    for j in notes:
        if(ind>=i):
            new.insert(ind-i, notes[ind])
        else:
            new.append(notes[ind])
        ind += 1
    return new

def majMin():
    print("[1] - Major \n[2] - Minor")
    op = int(input("Digite qual escala: "))
    return op


def cScale(notes, op):
    if(op==1):
        ind = 0
        for i in notes:
            if(ind == 1 or ind == 2 or ind==4 or ind==5 or ind==6):
                notes.pop(ind)
            ind += 1
    elif(op==2):
        ind = 0
        for i in notes:
            if(ind == 1 or ind == 3 or ind==4 or ind==6 or ind==7):
                notes.pop(ind)
            ind += 1
    print(notes)
    os.system('pause')
    return notes

def new(ind):
    os.system('cls')
    name = input("Digite o nome da musica que você deseja cadastrar: ")
    tone = cTone()
    notes = listNotes(tone)
    majmin = majMin()
    scale = cScale(notes, majmin)
    DataBase.DB.insert(ind, {"name": name, "tone": DataBase.notes[tone], "notes": scale, "scale": majmin})