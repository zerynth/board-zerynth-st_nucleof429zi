from stm.f4eth import f4eth as ethdrv

def init():
    print("start eth")
    ethdrv.auto_init()
    ethdrv.link()
    print(ethdrv.link_info())

def interface():
    return ethdrv






