from mido import MidiFile


mid = MidiFile('Koi no Uta_HalcyonMusic.mid')


for i, track in enumerate(mid.tracks):

    for msg in track:
        msgdict = msg.dict()
        if 'note_on' in msgdict['type']:
            print('\033[1;31m' + str(msg) + '\033[0m')

        elif 'note_off' in msgdict['type']:
            print('\033[1;34m' + str(msg) + '\033[0m')
        elif msgdict['time']!=0:
            print('\033[1;33m' + str(msg) + '\033[0m')
        else:
            print(str(msg))

