
# sample: cli arguments

import sys
import argparse

print ('Argument total number {} - List: {}'.format(len(sys.argv), str(sys.argv)))

for x in range(0,len(sys.argv)):
    print ('Argument: {} - {}'.format(x, sys.argv[x]))

# exit()
