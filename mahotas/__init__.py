'''\
=======
Mahotas
=======

A set of functions for basic image processing and machine vision.
'''
from .bbox import bbox, croptobbox
from .bwperim import bwperim
from .center_of_mass import center_of_mass
from .convolve import convolve
from .distance import distance
from .edge import sobel
from .euler import euler
from .histogram import fullhistogram
from .labeled import label
from .moments import moments
from .morph import close_holes, get_structuring_elem, dilate, erode, cwatershed, majority_filter
from .resize import imresize
from .stretch import stretch
from .thin import thin
from .thresholding import otsu, rc

from mahotas_version import __version__

import features
import morph
import segmentation

__all__ = [
    'bbox',
    'bwperim',
    'center_of_mass',
    'close_holes',
    'convolve',
    'croptobbox',
    'cwatershed',
    'dilate',
    'distance',
    'erode',
    'euler',
    'fullhistogram',
    'get_structuring_elem',
    'imresize',
    'label',
    'majority_filter',
    'moments',
    'morph',
    'otsu',
    'rc',
    'sobel',
    'stretch',
    'thin',

    'features',
    'morph',
    'segmentation',

    '__version__',
    ]

try:
    from .freeimage import imread, imsave
    __all__ += [
        'imread',
        'imsave',
        ]
except OSError, e:
    error_message = '''
mahotas.%%s depends on freeimage, which could not be found.

You need to have the freeimage installed for imread/imsave (everything else
will work, though, so this error is only triggered when you attempt to use
these optional functions). Freeimage is not a Python package, but a regular
package.

Under Linux, look for a package called `freeimage` in your distribution (it is
actually called `libfreeimage3` in debian/ubuntu, for example).

Under Windows, consider using the third-party mahotas packages at
http://www.lfd.uci.edu/~gohlke/pythonlibs/ (kindly maintained by Christoph
Gohlke), which already package freeimage.

Full error was: %s''' % e
    def imread(*args, **kwargs):
        raise ImportError(error_message % 'imread')
    def imsave(*args, **kwargs):
        raise ImportError(error_message % 'imsave')

