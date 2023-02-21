import os

################################
#  TODO                        #
#  sub/gsubまでは作成できるが    #
#  rename, removedirsが動かない #
################################
print(os.getcwd())
os.makedirs('./sub/gsub')
input('Hit any key...')
os.rename('./sub/gsub', './copy/gchild')

input('Hit any key...')
os.removedirs('./copy/gchild')

