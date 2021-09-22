import os
from glob import glob

png=glob("E:\\BisikletGörüntüsü\Ek Görüntüler\Ekin Eki Görüntüleri\*.PNG")   # It provides to output file names as a list.
                                                                             # Enter the file path where the images are located.
                                                                             # " *PNG " provides collection of all PNG format images.


for j in png:                 # Looping over filenames with loop structure

    os.rename(j, j[:-3] + "jpg")            # os.rename(Current File Name, Nwe File Name)





