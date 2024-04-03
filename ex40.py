class Song(object):
    #属性配置
    def __init__(self,lyrics):
        self.lyrics = lyrics
#method
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#实例1，输入参数
happy_bday  = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])
#实例2
bulls_on_parade = Song(["They rally around the family",
                        "with pockets full of shells"])
#调用class函数
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()