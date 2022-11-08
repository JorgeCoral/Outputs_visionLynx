import gdown
import sys
import os



if not os.path.exists(sys.argv[2]):
  os.makedirs(sys.argv[2])

gdown.download(sys.argv[1], sys.argv[2], quiet=False)

