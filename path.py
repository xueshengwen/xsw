from os import listdir
from os.path import isfile, join
PATH = '/home/zhujun/.ssh/xue/'
onlyfiles = [ f for f in listdir(PATH) if isfile(join(PATH,f)) ]
print onlyfiles
