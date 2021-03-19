from nbt import *

class NBTedit():
    def __init__(self, author, sizes):
        self.nnn = nbt.NBTFile()
        self.init(author, sizes)
        self.size = [sizes[0], sizes[1], sizes[2]]
        self.blocks = []

    def init(self, author, sizes):
        self.nnn.tags.append(nbt.TAG_String(name="author", value=author))
        self.nnn.tags.append(nbt.TAG_Int(name="DataVersion", value=1))
        entities = nbt.TAG_List(name='entities', type=nbt.TAG_Byte)
        self.nnn.tags.append(entities)
        size = nbt.TAG_List(name='size', type=nbt.TAG_Int)
        size.tags.append(nbt.TAG_Int(sizes[0]))
        size.tags.append(nbt.TAG_Int(sizes[1]))
        size.tags.append(nbt.TAG_Int(sizes[2]))
        self.nnn.tags.append(size)
        palette = nbt.TAG_List(name='palette', type=nbt.TAG_Compound)
        self.nnn.tags.append(palette)
        blocks = nbt.TAG_List(name='blocks', type=nbt.TAG_Compound)
        self.nnn.tags.append(blocks)

    def printNBT(self):
        print(self.nnn.pretty_tree())

    def saveNBT(self, path):
        self.nnn.write_file(path)

    def addblockskind(self, block):
        blockkind = nbt.TAG_Compound()
        blockkind.tags.append(nbt.TAG_String(name='Name', value=block['Name']))
        if 'Properties' in block:
            Properties = nbt.TAG_Compound(name='Properties')
            Properties.name = 'Properties'
            for i in block['Properties']:
                Properties.tags.append(nbt.TAG_String(name=i, value=block['Properties'][i]))
            blockkind.tags.append(Properties)
        self.nnn['palette'].tags.append(blockkind)
        self.blocks.append(block)

    def Calcoor(self, coor):
        if coor[0] < 0 or coor[1] < 0 or coor[2] < 0 or coor[0] > self.size[0] or coor[1] > self.size[1] or coor[2] > self.size[2]:
            return 0
        return coor[2]*self.size[0]*self.size[1]+coor[0]*self.size[1]+coor[1]

    def delete(self):
        self.nnn.tags.remove(self.nnn['author'])

cb1 = {'Name': 'minecraft:command_block', 'Properties': {'conditional': 'false', 'facing': 'south'}}
cb2 = {'Name': 'minecraft:command_block', 'Properties': {'conditional': 'false', 'facing': 'nouth'}}
air = {'Name': 'minecraft:air'}
size = [5,7,5]
nbb = NBTedit('12skoko', size)
nbb.addblockskind(cb1)
nbb.addblockskind(cb2)
nbb.addblockskind(air)
nbb.delete()
nbb.printNBT()
# nbb.saveNBT('2.nbt')

# coor=[2,5,1]
# print(nbb.Calcoor(coor))
