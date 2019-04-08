import os

__BASE_DIR = os.path.dirname(__file__)

__FILE1_PATH = os.path.join(
	__BASE_DIR,
	'obama1.txt',
)

__FILE2_PATH = os.path.join(
	__BASE_DIR,
	'obama2.txt',
)

__APIKEY_ERROR_MESSAGE = """INTELLEXER_API_KEY not in environment variables. Try:
$ export INTELLEXER_API_KEY='my-personal-api-key'
Then run example"""

try:
	INTELLEXER_API_KEY = os.environ['INTELLEXER_API_KEY']
except KeyError:
	print(__APIKEY_ERROR_MESSAGE)
	exit(1)


__FILE1 = open(__FILE1_PATH)
__FILE2 = open(__FILE2_PATH)


def FILE1():
	__FILE1.seek(0, 0)
	return __FILE1


def FILE2():
	__FILE2.seek(0, 0)
	return __FILE2


URL = 'https://www.infoplease.com/people/who2-biography/barack-obama'
OTHER_URL = 'http://www.infoplease.com/biography/var/barackobama.html'


TEXT = '''The products, information, and other content provided by this ''' \
	'''seller are provided for informational purposes only'''

OTHER_TEXT = '''The products and other content provided by this ''' \
	'''seller are provided for informational purposes only'''

