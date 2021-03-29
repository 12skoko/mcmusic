import NBTeditpy
import readmidi

mid=readmidi.Readmidi_majo('./mid/Literature (Full ver.).mid')

note=mid.readmidi()

note_num=len(note)

for i in note:
    print(i)

nn=NBTeditpy.NBTedit([500,10,64])

x=0
z=0
for i in range(len(note)):

    if i==0 or(note[i-1]['time']!=note[i]['time']):
        y=0
        z=note[i]['time']%64
        x=int(note[i]['time']/64)
    elif note[i-1]['time']==note[i]['time']:
        y+=1

    else:
        exit(1200)


    nn.setcommandblock([x, y, z],'execute @p ~ ~ ~ playsound '+str(note[i]['chet'])+'.' + str(note[i]['note']) + ' voice @p ~ ~ ~ ' + str(note[i]['velocity'] / 128.0), [1, 0, 4, 1])


nn.saveNBT('./nbt/majo.nbt')