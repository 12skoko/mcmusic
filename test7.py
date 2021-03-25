import NBTeditpy
import readmidi

mid=readmidi.Readmidi('Literature (Full ver.).mid')

note=mid.readmidi()

note_num=len(note)

for i in note:
    print(i)

nn=NBTeditpy.NBTedit('12skoko',[500,10,20])

x=0
z=0
for i in range(len(note)):

    if i==0 or(note[i-1]['time']!=note[i]['time']):
        y=0
        if i % 16 == 0:
            z = 0
            x += 1
        else:
            z += 1
    elif note[i-1]['time']==note[i]['time']:
        y+=1

    else:
        exit(1200)

    print(x,y,z)


    nn.setcommandblock([x, y, z],'execute @p ~ ~ ~ playsound '+str(note[i]['chet'])+'.' + str(note[i]['note']) + ' voice @p ~ ~ ~ ' + str(note[i]['velocity'] / 128.0), [1, 0, 1, 1])


nn.saveNBT('t3.nbt')