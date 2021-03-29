import random
import readmidi
import NBTeditpy
import correctpiano
import motion

basestart=[-103.5,70,582.5]

baseend=[-144,66,630]

basetime=48

mid=readmidi.Readmidi_majo('./mid/Literature (Full ver.).mid')

note=mid.readmidi()

note_num=len(note)

for i in note:
    print(i)



nn=NBTeditpy.NBTedit([150,10,64])

x=0
z=0

throwdict=[]

# for i in range(len(note)):
#
#     # if i==0 or(note[i-1]['time']!=note[i]['time']):
#     #     y=0
#     #     z=note[i]['time']%16
#     #     x=int(note[i]['time']/16)
#     # elif note[i-1]['time']==note[i]['time']:
#     #     y+=1
#     #
#     # else:
#     #     exit(1200)
#
#     startcoor=[basestart[0]+random.randint(0,33),basestart[1],basestart[2]]
#
#     endcoor=correctpiano.calendcoor([-144,66,631],note[i]['note'])
#
#     randomdeltatime=basetime+random.randint(0,3)*16
#
#     thrownote={'note':note[i]['note'],'startcoor':startcoor,'endcoor':endcoor,'time':note[i]['time']-randomdeltatime,'deltatime':randomdeltatime}
#
#     throwdict.append(thrownote)



    # nn.setcommandblock([x, y, z],'execute @p ~ ~ ~ playsound '+str(note[i]['chet'])+'.' + str(note[i]['note']) + ' voice @p ~ ~ ~ ' + str(note[i]['velocity'] / 128.0), [1, 0, 4, 1])


for i in range(len(note)):

    if i==0 or(note[i-1]['time']!=note[i]['time']):
        y=0
        z=note[i]['time']%64
        x=int(note[i]['time']/64)
    elif note[i-1]['time']==note[i]['time']:
        y+=1

    else:
        exit(1200)

    # vmotion=motion.motion(throwdict[i]['startcoor'], throwdict[i]['endcoor'],throwdict[i]['deltatime'])

    # command='summon falling_block '+str(throwdict[i]['startcoor'][0])+' '+str(throwdict[i]['startcoor'][1])+' '+str(throwdict[i]['startcoor'][2])+' {TileID:89,Time:1,Motion:['+str(vmotion[0])+'d,'+str(vmotion[1])+'d,'+str(vmotion[2])+'d]}'
    endcoor = correctpiano.calendcoor([-144.5, 96, 631.5], note[i]['note'])

    command='/summon falling_block '+str(endcoor[0])+' '+str(endcoor[1])+' '+str(endcoor[2])+' {TileID:89,Time:1,Riding:{id:ItemFrame}}'

    nn.setcommandblock([x, y, z],command, [1, 0, 4, 1])

nn.saveNBT('./nbt/t9.nbt')