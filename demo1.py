from nbt import *
nbtfile = nbt.NBTFile()

nbtfile.name = "My Top Level Tag"
nbtfile.tags.append(nbt.TAG_Float(name="My Float Name", value=3.152987593947))
mylist = nbt.TAG_List(name="TestList", type=nbt.TAG_Long) #type needs to be pre-declared!
mylist.tags.append(nbt.TAG_Long(100))
mylist.tags.extend([nbt.TAG_Long(120),nbt.TAG_Long(320),nbt.TAG_Long(19)])
nbtfile.tags.append(mylist)
print(nbtfile.pretty_tree())

nbtfile["TestList"].tags.sort(key = lambda tag: tag.value)
print(nbtfile.pretty_tree())

nbtfile.write_file("mynbt.dat")

print(nbtfile)
