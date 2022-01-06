#3_11 列表的切片 

#所谓列表的切片是指由列表的部分元素组成的子列表，列表切片可以表示为“列表名[a:b]”

#列表中索引号为a的元素是切片中的第1个元素

#列表中索引号为b-1的元素是切片中的最后1个元素

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])  #输出['charles', 'martina', 'michael']

#切片players[0:3]也是一个列表，尽管它与列表players同名

#但是players[0:3]与players是两个不同的列表，两者的元素保存在内存中的不同位置

#在命令行模式下键入players[0:3]，系统会输出players[0:3]保存的列表元素

players = ['charles', 'martina', 'michael', 'florence', 'eli']

sub_players = players[1:4]

print(sub_players)  #输出['martina', 'michael', 'florence']

#切片中冒号':'前面的参数如果缺省，则表示其默认值为0

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[:4])  #输出['charles', 'martina', 'michael', 'florence']

#可以使用for循环遍历切片

players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")

for player in players[:3]:
    
    print(player.title())





