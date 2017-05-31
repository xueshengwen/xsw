import os
root = '/home/zhujun/.ssh/xue/'
for i in os.listdir(root):
        if os.path.isfile(os.path.join(root,i)):
                    print i
