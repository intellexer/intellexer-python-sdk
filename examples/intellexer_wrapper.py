# adding previous directory to import intellexer
# You don't have to do it, if you installed it by pip
import sys as _sys
from os.path import abspath as _abspath
from os.path import dirname as _dirname
from os.path import join as _join


_intellexer_path = _abspath(__file__)
_intellexer_path = _dirname(_dirname(_intellexer_path))
_intellexer_path = _join(
	_intellexer_path,
)

_sys.path.insert(0, _intellexer_path)

from intellexer import *
