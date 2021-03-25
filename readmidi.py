from mido import MidiFile


def chettype(num):
    if num <= 3:
        return 8
    elif num >= 4 and num <= 15:
        return 4
    elif num >= 16:
        return 1


def vaguemun(num):
    if num <= 3:
        return 0
    elif num >= 9 and num <= 15:
        return 1
    elif num >= 19 and num <= 27:
        return 2
    elif num >= 45 and num <= 51:
        return 4
    elif num >= 69 and num <= 75:
        return 6
    elif num >= 92 and num <= 99:
        return 8
    elif num >= 189 and num <= 195:
        return 16
    else:
        print(num)
        exit(65424)



class Readmidi:
    def __init__(self,path):
        self.mid = MidiFile(path)
        self.musicnote = []
        self.nowon = []
        self.blocktime = 0
    def readmidi(self):

        for i, track in enumerate(self.mid.tracks):
            if i == 2:
                for msg in track:
                    msgdict = msg.dict()
                    self.blocktime+=vaguemun(int(msgdict['time']))
                    if 'note_off' in msgdict['type']:
                        for i in self.nowon:
                            if i['note']==msgdict['note']:
                                musicnoteinfo={'note':msgdict['note'],'velocity':i['velocity'],'chet':chettype(self.blocktime-i['time']),'time':i['time']}
                                self.musicnote.append(musicnoteinfo)
                                temp=i
                                self.nowon.remove(temp)
                                break
                    if 'note_on' in msgdict['type']:
                        noteinfo={'note':msgdict['note'],'velocity':msgdict['velocity'],'time':self.blocktime}
                        self.nowon.append(noteinfo)
        return sorted(self.musicnote, key=lambda x : x['time'])


