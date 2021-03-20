from mido import MidiFile
import mido

mid = MidiFile('2.mid')
# print(mid.ticks_per_beat)
# print(mid.)

on=0
off=0


for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        type=msg.dict()['type']

        if 'note_on' in type:
            on+=1
            print('\033[1;31m' + str(msg) + '\033[0m')

        elif 'note_off' in type:
            off+=1
            print('\033[1;34m' + str(msg) + '\033[0m')

        else:
            print(str(msg))

print(on,off)

# print('\033[1;31m '+str('asdfs')+'\033[0m')

# print(type(mid.tracks[2]))

# a=mido.messages.messages.Message.dict()