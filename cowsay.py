# $ pip install cowsay
# WARNING: Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None)) after 
# connection broken by 'ReadTimeoutError("HTTPSConnectionPool(host='pypi.org', port=443): Read timed out. (read timeout=15)")': /simple/cowsay/
# Collecting cowsay
#   Downloading cowsay-6.1-py3-none-any.whl.metadata (5.6 kB)
# Downloading cowsay-6.1-py3-none-any.whl (25 kB)
# Installing collected packages: cowsay
# Successfully installed cowsay-6.1

import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])

# $ python say.py Mabu
#   ___________
# | hello, Mabu |
#   ===========
#            \
#             \
#               ^__^
#               (oo)\_______
#               (__)\       )\/\
#                   ||----w |
#                   ||     ||