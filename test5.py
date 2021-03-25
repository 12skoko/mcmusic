from mido import MidiFile
import NBTeditpy




def vaguemun(num):
    if num <=3:
        return 0
    elif num >= 9 and num <= 15:
        # return 12
        return 1
    elif num >= 19 and num <= 27:
        # return 24
        return 2
    elif num >= 45 and num <= 51:
        # return 48
        return 4
    elif num >= 69 and num <= 75:
        # return 72
        return 6
    elif num >= 92 and num <= 99:
        # return 96
        return 8
    elif num >= 189 and num <= 195:
        # return 192
        return 16
    else:
        print(num)
        exit(65424)




mid = MidiFile('2.mid')

xz = [0,0]

musicnote=[]
nowon=[]
tick=0

# nn = NBTeditpy.NBTedit('12skoko', [200, 1, 8])

# nn.setcommandblock([1, 1, 0], 'helloworld', [0, 0, 0, 0])

# print(nn.blocktags)
# nn.printNBT()
# nn.saveNBT('h4.nbt')


# for i, track in enumerate(mid.tracks):
#
#     if i == 2:
#         k=0
#         for msg in track:
#             msgdict = msg.dict()
#             flag = vaguemun(int(msgdict['time']))
#             # if k==1:
#             if flag == 0 and 'note_on' in msgdict['type'] and (k==1 or 'note_on' in msglast['type']):
#                 xz[1] += 1
#             else:
#                 xz[0] += flag
#                 xz[1] = 0
#             # else:
#             #     if flag == 0 and 'note_on' in msgdict['type'] :
#             #         xz[1] += 1
#             #     else:
#             #         xz[0] += flag
#             #         xz[1] = 0
#             if 'note_on' in msgdict['type']:
#                 print('\033[1;31m' + str(msg) + '\033[0m')
#                 # nn.setcommandblock([xz[0], 0, xz[1]], 'execute @p ~ ~ ~ playsound 4.'+str(msgdict['note'])+' voice @p ~ ~ ~ '+str(msgdict['velocity']/128.0), [1, 0, 1, 1])
#             elif 'note_off' in msgdict['type']:
#                 print('\033[1;34m' + str(msg) + '\033[0m')
#             elif msgdict['time']!=0:
#                 print('\033[1;33m' + str(msg) + '\033[0m')
#             else:
#                 print(str(msg))
#             k=1
#             msglast=msgdict
# # nn.printNBT()
# # nn.saveNBT('t2.nbt')


for i, track in enumerate(mid.tracks):
    if i == 2:
        for msg in track:
            msgdict = msg.dict()
            flag = vaguemun(int(msgdict['time']))
            if flag !=0:
                tick+=flag

            if 'note_off' in msgdict['type']:
                for i in range(0,len(musicnote)):
                    if musicnote[i]['note']==msgdict['note']:
                        musicnoteinfo={'note':msgdict['note'],'velocity':musicnote[i]['time'],'time':tick-musicnote[i]['time']}
                        musicnote.append(musicnoteinfo)
                        temp=musicnote[i]
                        nowon.remove(temp)
                        break

            if 'note_on' in msgdict['type']:
                noteinfo={'note':msgdict['note'],'velocity':msgdict['velocity'],'time':tick}



for i in musicnote:
    print(i)