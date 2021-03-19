#
# import nbtlib
# nnn=nbtlib.load('3.nbt')
#
# print(nnn)
#
#
#
# from nbtlib.tag import *
# from nbtlib import File
#
# # dic={author:"MCEdit-Unified v1.5.6.0"}
#
# new_file =  File({"":{author:"MCEdit-Unified v1.5.6.0",DataVersion:Int(1),size:[Int(1),Int(1),Int(1)],blocks:[{state:Int(0),pos:[Int(0),Int(0),Int(0)],nbt:{auto:Byte(0)b,powered:Byte(0)b,LastExecution:Long(219560)l,SuccessCount:Int(1),UpdateLastExecution:Byte(1)b,conditionMet:Byte(1)b,CustomName:"@",Command:"/particleex endRod ~ 5 ~ tickParameter 1 0 1 1 240 0 0 0 0 3 x=t;y=(3-t)*t 0.05 3 3",id:"minecraft:command_block",TrackOutput:Byte(1)b}}],palette:[{Name:"minecraft:command_block",Properties:{facing:south,conditional:false}}],entities:[]}})
# new_file.save('1.nbt')

# from nbt import *
# nbtfile = NBTFile()
# nbtfile.name = "My Top Level Tag"
# nbtfile.tags.append(TAG_Float(name="My Float Name", value=3.152987593947))
# mylist = TAG_List(name="TestList", type=TAG_Long) #type needs to be pre-declared!
# mylist.tags.append(TAG_Long(100))
# mylist.tags.extend([TAG_Long(120),TAG_Long(320),TAG_Long(19)])
# nbtfile.tags.append(mylist)
# print(nbtfile.pretty_tree())
#
# nbtfile["TestList"].tags.sort(key = lambda tag: tag.value)
# print(nbtfile.pretty_tree())
#
# nbtfile.write_file("mynbt.dat")




# import nbt
# nnn = nbt.nbt.NBTFile("777.nbt")

from nbt import *
nnn = nbt.NBTFile()
nnn.name = "77.nbt"

# nnn=nbt.TAG_List(type=nbt.TAG_Compound)
nnn.tags.append(nbt.TAG_String(name="auther", value='12skoko'))
nnn.tags.append(nbt.TAG_Int(name="DataVersion", value=1))

entities=nbt.TAG_List(name='entities',type=nbt.TAG_Byte)

nnn.tags.append(entities)

size=nbt.TAG_List(name='size',type=nbt.TAG_Int)
size.tags.append(nbt.TAG_Int(2))
size.tags.append(nbt.TAG_Int(1))
size.tags.append(nbt.TAG_Int(2))

nnn.tags.append(size)

palette=nbt.TAG_List(name='palette',type=nbt.TAG_Compound)

air=nbt.TAG_Compound()

air.tags.append(nbt.TAG_String(name="Name", value='minecraft:air'))

command_block=nbt.TAG_Compound()

Properties=nbt.TAG_Compound()
Properties.name='Properties'


Properties.tags.append(nbt.TAG_String(name='facing',value='south'))
Properties.tags.append(nbt.TAG_String(name='conditional',value='false'))

command_block.tags.append(nbt.TAG_String(name="Name", value='minecraft:command_block'))
command_block.tags.append(Properties)

palette.tags.append(air)
palette.tags.append(command_block)

nnn.tags.append(palette)

# blocks=nbt.TAG_List(name='blocks',type=nbt.TAG_Compound)
# print(nnn)
print(nnn.pretty_tree())
nnn.write_file("7777.dat")




















# mylist = nbt.TAG_List(name="TestList", type=nbt.TAG_Long) #type needs to be pre-declared!
# mylist.tags.append(nbt.TAG_Long(100))
# mylist.tags.extend([nbt.TAG_Long(120),nbt.TAG_Long(320),nbt.TAG_Long(19)])
# nbtfile.tags.append(mylist)
# print(nbtfile.pretty_tree())
# nbtfile["TestList"].tags.sort(key = lambda tag: tag.value)
# print(nbtfile.pretty_tree())
# nbtfile.write_file("mynbt.dat")






# print(nnn["blocks"][0]['nbt']['Command'])
# for i in nnn['blocks']:
#     print(i)
# print(nnn["blocks"])
# print(nnn)