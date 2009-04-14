#!/usr/bin/env jython
""" """

# Script information for the file.
__author__ = "Philippe Pinard (philippe.pinard@gmail.com)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2009 Philippe Pinard"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = ""
__svnDate__ = ""
__svnId__ = ""

# Standard library modules.

# Third party modules.

# Local modules.
import rmlimage.io.IO as IO
import rmlimage.kernel as kernel
  
# Globals and constants variables.

def createMaskDisc(width, height, centroid, radius):
  """
  Create a circular mask for a pattern size of *size* centered at *centroid* with a given *radius*
  
  :arg size: dimensions of the mask (width, height)
  :type size: tuple
  
  :arg centroid: position in pixels of the center of the disc (x,y)
  :type centroid: tuple
  
  :arg radius: radius of the disc in pixels
  :type radius: int
  
  :rtype: :class:`BinMap <rmlimage.kernel.BinMap>`
  """
  pixArray = []
  
  for y in range(height):
    for x in range(width):
      if (x - centroid[0])**2 + (y - centroid[1])**2 < radius**2:
        pixArray.append(1)
      else:
        pixArray.append(0)
  
  binMap = kernel.BinMap(width, height, pixArray)
  
  return binMap

if __name__ == '__main__':
  """
  How to use the function
  """
  maskMap = createMaskDisc(width=168, height=128, centroid=(84,64), radius=59)
  
  maskMap.setFile(r'testmask.bmp')
  
  IO.save(maskMap)