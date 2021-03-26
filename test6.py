import readmidi

mid=readmidi.Readmidi_majo('Literature (Full ver.).mid')

note=mid.readmidi()

note_num=len(note)

for i in note:
    print(i)