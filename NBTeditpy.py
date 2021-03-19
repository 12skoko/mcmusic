from nbt import *

class NBTedit():
    def __init__(self, author, sizes):
        self.nnn = nbt.NBTFile()
        self.create(author, sizes)
        self.size = [sizes[0], sizes[1], sizes[2]]
        self.blocktags = {'air':0}
        # self.cbtype=[{0:nbt.TAG_String('command_block'),1:nbt.TAG_String('chain_command_block'),2:nbt.TAG_String('repeating_command_block')},
        #              {0:nbt.TAG_String('false'),1:nbt.TAG_String('true')},
        #              {0:nbt.TAG_String('east'),1:nbt.TAG_String('south'),2:nbt.TAG_String('west'),3:nbt.TAG_String('north'),4:nbt.TAG_String('up'),5:nbt.TAG_String('down'),}
        #              ]

        self.cbtype=[{0:'command_block',1:'chain_command_block',2:'repeating_command_block'},
                     {0:'false',1:'true'},
                     {0:'east',1:'south',2:'west',3:'north',4:'up',5:'down',}
                     ]

    def create(self, author, sizes):
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
        self.addblockskind({'Name': 'minecraft:air','tag':'air'},1)
        for i in range(0, sizes[2]):
            for j in range(0, sizes[0]):
                for k in range(0, sizes[1]):
                    air = nbt.TAG_Compound()
                    pos = nbt.TAG_List(name='pos', type=nbt.TAG_Int)
                    pos.tags.extend([nbt.TAG_Int(j), nbt.TAG_Int(k), nbt.TAG_Int(i)])
                    air.tags.append(nbt.TAG_Int(name="state", value=0))
                    air.tags.append(pos)
                    self.nnn['blocks'].tags.append(air)




    def printNBT(self):
        print(self.nnn.pretty_tree())

    def saveNBT(self, path):
        self.nnn.write_file(path)

    def addblockskind(self, block,init=0):

        blockkind = nbt.TAG_Compound()
        blockkind.tags.append(nbt.TAG_String(name='Name', value=block['Name']))
        if 'Properties' in block:
            Properties = nbt.TAG_Compound(name='Properties')
            Properties.name = 'Properties'
            for i in block['Properties']:
                Properties.tags.append(nbt.TAG_String(name=i, value=block['Properties'][i]))
            blockkind.tags.append(Properties)
        self.nnn['palette'].tags.append(blockkind)

        if init==0:
            self.blocktags[block['tag']]=len(self.blocktags)


    def Calcoor(self, coor):
        if coor[0] < 0 or coor[1] < 0 or coor[2] < 0 or coor[0] > self.size[0] or coor[1] > self.size[1] or coor[2] > self.size[2]:
            return 0
        return coor[2]*self.size[0]*self.size[1]+coor[0]*self.size[1]+coor[1]

    def delete(self):
        self.nnn['blocks'][1]['state'].value=1
        self.nnn['palette'].tags.remove(self.nnn['palette'][3])
        # print(self.nnn['palette'][0])
        # self.nnn.tags.reverse(self.nnn['palette'][1]['Properties'])

    def setblock(self,coor,block):
        num=self.Calcoor(coor)
        # print(num)
        # print(self.nnn['blocks'][num]['state'])
        self.nnn['blocks'][num]['state'].value=self.blocktags[block['tag']]
        try:
            self.nnn['blocks'][num].tags.remove(self.nnn['blocks'][num]['nbt'])
        except:
            1

        if 'nbt' in block:
            nbtt = nbt.TAG_Compound()
            nbtt.name = 'nbt'

            for i in block['nbt']:
                tagtype=type(block['nbt'][i])
                if tagtype==nbt.TAG_String:
                    nbtt.tags.append(nbt.TAG_String(name=i, value=str(block['nbt'][i])))
                elif tagtype == nbt.TAG_Byte:
                    nbtt.tags.append(nbt.TAG_Long(name=i, value=block['nbt'][i]))
                elif tagtype==nbt.TAG_Int:
                    nbtt.tags.append(nbt.TAG_Int(name=i, value=block['nbt'][i]))
                elif tagtype==nbt.TAG_Long:
                    nbtt.tags.append(nbt.TAG_Long(name=i, value=block['nbt'][i]))
                elif tagtype==nbt.TAG_Float:
                    nbtt.tags.append(nbt.TAG_Float(name=i, value=block['nbt'][i]))
                else:
                    print(i)
                    exit(66666)
            self.nnn['blocks'][num].tags.append(nbtt)

    def setcommandblock(self,coor,command,type):
        typestr='cb'+str(type[0])+str(type[1])+str(type[2])+str(type[3])
        if typestr not in self.blocktags:
            # cbProperties=nbt.TAG_Compound()
            # cbProperties.name='Properties'
            # cbProperties.tags.append(nbt.TAG_String(name='conditional',value=self.cbtype[1][type[1]]))
            # cbProperties.tags.append(nbt.TAG_String(name='facing', value=self.cbtype[2][type[2]]))
            # cbnew=nbt.TAG_Compound()
            # cbnew.tags.append(nbt.TAG_String(name='Name',value=self.cbtype[0][type[0]]))
            # cbnew.tags.append(cbProperties)
            #
            cbnew = {'Name': self.cbtype[0][type[0]], 'tag': typestr, 'Properties': {'conditional': self.cbtype[1][type[1]],'facing':self.cbtype[2][type[2]]}}

            self.addblockskind(cbnew)
        cb={'tag':typestr,'nbt':{'Command':nbt.TAG_String(command),
                                 'auto':nbt.TAG_Byte(type[3]),
                                 'id':nbt.TAG_String('minecraft:commond_block'),
                                 'CustomName':nbt.TAG_String('@'),
                                 'powered':nbt.TAG_Byte(0),
                                 'UpdateLastExecution':nbt.TAG_Byte(1),
                                 'conditionMet':nbt.TAG_Byte(1),
                                 'TrackOutput':nbt.TAG_Byte(1),
                                 'SuccessCount':nbt.TAG_Int(1),
                                 'LastExecution':nbt.TAG_Long(0)
                                 }}
        self.setblock(coor,cb)



cb1 = {'Name': 'minecraft:command_block', 'tag':'cbblock1','Properties': {'conditional': 'false', 'facing': 'south'}}
cb2 = {'Name': 'minecraft:command_block', 'tag':'cbblock2','Properties': {'conditional': 'false', 'facing': 'nouth'}}
air = {'Name': 'minecraft:air','tag':'air2'}

set1={'state':1,'nbt':{'Command':nbt.TAG_String('the 1 commond'),'id':nbt.TAG_String('minecraft:commond_block')}}

# size = [2,2,1]
# nbb = NBTedit('12skoko', size)
# nbb.addblockskind(cb1)
# nbb.addblockskind(cb2)
# # nbb.addblockskind(air)
# # nbb.delete()
# nbb.setblock([0,1,0],set1)
# nbb.printNBT()
# nbb.saveNBT('2.nbt')


# nbb.blocks.append('sdsds')
# print(nbb.blocktags)
#
# for i in set1['nbt']:
#     print(type(i))
#     print(i)
#     print(type(set1['nbt'][i]))
#     if type(set1['nbt'][i])==nbt.TAG_String:
#         print(1)
#     print(set1['nbt'][i])

stone={'Name':'minecraft:stone','tag':'stone','Properties':{'variant':'stone'}}
dirt={'Name':'minecraft:dirt','tag':'dirt'}
grass={'Name':'minecraft:grass','tag':'grass'}
cobblestone={'Name':'minecraft:cobblestone','tag':'cobblestone'}
nn=NBTedit('12skoko',[2,2,2])
nn.addblockskind(stone)
nn.addblockskind(dirt)
nn.addblockskind(grass)
nn.addblockskind(cobblestone)

nn.setblock([0,0,0],{'tag':'stone'})
nn.setblock([0,0,1],{'tag':'dirt'})
nn.setblock([0,1,1],{'tag':'grass'})
nn.setblock([1,0,1],{'tag':'cobblestone'})

nn.setcommandblock([1,1,0],'helloworld',[0,0,0,0])

# print(nn.blocktags)
nn.printNBT()
# nn.saveNBT('h3.nbt')


