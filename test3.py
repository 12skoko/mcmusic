import NBTeditpy

stone = {'Name': 'minecraft:stone', 'tag': 'stone', 'Properties': {'variant': 'stone'}}
dirt = {'Name': 'minecraft:dirt', 'tag': 'dirt'}
grass = {'Name': 'minecraft:grass', 'tag': 'grass'}
cobblestone = {'Name': 'minecraft:cobblestone', 'tag': 'cobblestone'}

nn = NBTeditpy.NBTedit('12skoko', [2, 2, 2])

nn.addblockskind(stone)
nn.addblockskind(dirt)
nn.addblockskind(grass)
nn.addblockskind(cobblestone)

nn.setblock([0, 0, 0], {'tag': 'stone'})
nn.setblock([0, 0, 1], {'tag': 'dirt'})
nn.setblock([0, 1, 1], {'tag': 'grass'})
nn.setblock([1, 0, 1], {'tag': 'cobblestone'})

nn.setcommandblock([1, 1, 0], 'helloworld', [0, 0, 0, 0])

# print(nn.blocktags)
nn.printNBT()
# nn.saveNBT('h4.nbt')

