def torrent(files): 
    lst = sorted(files, key=lambda x: ((x['size_GB']*1000) / (x["speed_Mbps"]/8), x["name"]))
    return [file["name"] for file in lst], (lst[-1]['size_GB']*1000) / (lst[-1]["speed_Mbps"]/8)



# SIZE,SPEED,NAME = 'size_GB speed_Mbps name'.split()
# GB_TO_Mb = 8000
# def keyer(f): return (f[SIZE]/f[SPEED], f[NAME])
# def torrent(files):    
#     lst = sorted(files, key=keyer)
#     return [x[NAME] for x in lst], lst[-1][SIZE]*GB_TO_Mb / lst[-1][SPEED]