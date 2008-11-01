#!/usr/bin/env python
""" """

# Script information for the file.
__author__ = "Philippe Pinard (philippe.pinard@mail.mcgill.ca)"
__version__ = ""
__date__ = ""
__copyright__ = "Copyright (c) 2008 Philippe Pinard"
__license__ = ""

# Subversion informations for the file.
__svnRevision__ = ""
__svnDate__ = ""
__svnId__ = ""

# Standard library modules.
import Tkinter
import Pmw
from PIL import Image, ImageTk
from math import pi

# Third party modules.

# Local modules.
import EBSDTools.patternSimulations.patternSimulations as patternSimulations
import EBSDTools.crystallography.lattice as lattice
import EBSDTools.mathTools.eulers as eulers
import EBSDTools.mathTools.quaternions as quaternions

class App:
  def __init__(self, root, patternSize):
    self.root = root
    self.patternSize = patternSize
  
    #FCC
    atoms = {(0,0,0): 14,
             (0.5,0.5,0): 14,
             (0.5,0,0.5): 14,
             (0,0.5,0.5): 14}
  #  atoms = {(0,0,0): 14,
  #           (0.5,0.5,0.5): 14}
    self.L = lattice.Lattice(a=5.43, b=5.43, c=5.43, alpha=pi/2, beta=pi/2, gamma=pi/2, atoms=atoms, reflectorsMaxIndice=4)
    
    #Image
    frameMap = Tkinter.Frame(root)
    imageMap =  Image.new(mode='RGB', size=patternSize)
    self.objectMap = ImageTk.PhotoImage(imageMap)
    lblMap = Tkinter.Label(frameMap, image=self.objectMap, bd=0)
    lblMap.grid()
    frameMap.grid(row=0, column=0, columnspan=3)
    
    #Counters
    self.counterEuler1 = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='E1'
                               , entry_width=3
                               , entryfield_value=0
                               , datatype={'counter' : 'integer'}
                               , entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 360}
                               , increment=1)
    self.counterEuler1.grid(row=1, column=0, sticky='ew')
#    counterEuler1.components('entryfield').configure(command=lambda func=self.btnProjectsRootBrowse_Command: func())
    self.counterEuler1.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterEuler2 = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='E2'
                               , entry_width=3
                               , entryfield_value=0
                               , entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 360}
                               , increment=1)
    self.counterEuler2.grid(row=1, column=1, sticky='ew')
    self.counterEuler2.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterEuler3 = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='E3'
                               , entry_width=3
                               , entryfield_value=0
                               , datatype={'counter' : 'integer'}
                               , entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 360}
                               , increment=1)
    self.counterEuler3.grid(row=1, column=2, sticky='ew')
    self.counterEuler3.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterPatternCenterX = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='PCx'
                               , entry_width=3
                               , entryfield_value=0.0
                               , datatype={'counter' : 'real'}
                               , entryfield_validate={'validator' : 'real', 'min' : -0.5, 'max' : 0.5}
                               , increment=0.1)
    self.counterPatternCenterX.grid(row=2, column=0, sticky='ew')
    self.counterPatternCenterX.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())

    self.counterPatternCenterZ = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='PCz'
                               , entry_width=3
                               , entryfield_value=0.0
                               , datatype={'counter' : 'real'}
                               , entryfield_validate={'validator' : 'real', 'min' : -0.5, 'max' : 0.5}
                               , increment=0.1)
    self.counterPatternCenterZ.grid(row=2, column=1, sticky='ew')
    self.counterPatternCenterZ.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterDetectorDistance = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='DD'
                               , entry_width=3
                               , entryfield_value=0.3
                               , datatype={'counter' : 'real'}
                               , entryfield_validate={'validator' : 'real', 'min' : 0.1, 'max' : 1.0}
                               , increment=0.1)
    self.counterDetectorDistance.grid(row=2, column=2, sticky='ew')
    self.counterDetectorDistance.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterTilt = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='Tilt'
                               , entry_width=3
                               , entryfield_value=70
                               , datatype={'counter' : 'integer'}
                               , entryfield_validate={'validator' : 'integer', 'min' : 0, 'max' : 90}
                               , increment=1)
    self.counterTilt.grid(row=3, column=0, sticky='ew')
    self.counterTilt.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterEnergy = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='E0'
                               , entry_width=3
                               , entryfield_value=20
                               , datatype={'counter' : 'integer'}
                               , entryfield_validate={'validator' : 'integer', 'min' : 10, 'max' : 40}
                               , increment=1)
    self.counterEnergy.grid(row=3, column=1, sticky='ew')
    self.counterEnergy.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.counterReflectors = Pmw.Counter(root
                               , labelpos='w'
                               , label_text='R'
                               , entry_width=3
                               , entryfield_value=9
                               , datatype={'counter' : 'integer'}
                               , entryfield_validate={'validator' : 'integer', 'min' : 4, 'max' : 50}
                               , increment=1)
    self.counterReflectors.grid(row=3, column=2, sticky='ew')
    self.counterReflectors.component('entryfield').configure(modifiedcommand=lambda func=self.update: func())
    
    self.varCheckBandCenter = Tkinter.IntVar()
    self.varCheckBandCenter.set(0)
    checkBandCenter = Tkinter.Checkbutton(root
                                       , text='Band Center'
                                       , state='normal'
                                       , anchor='w'
                                       , variable=self.varCheckBandCenter
                                       , command=lambda func=self.update: func())
    checkBandCenter.grid(row=4, column=0)
    
    self.varCheckBandEdges = Tkinter.IntVar()
    self.varCheckBandEdges.set(0)
    checkBandEdges = Tkinter.Checkbutton(root
                                       , text='Band Edges'
                                       , state='normal'
                                       , anchor='w'
                                       , variable=self.varCheckBandEdges
                                       , command=lambda func=self.update: func())
    checkBandEdges.grid(row=4, column=1)
    
    self.varCheckBandFull = Tkinter.IntVar()
    self.varCheckBandFull.set(1)
    checkBandFull = Tkinter.Checkbutton(root
                                       , text='Band Full'
                                       , state='normal'
                                       , anchor='w'
                                       , variable=self.varCheckBandFull
                                       , command=lambda func=self.update: func())
    checkBandFull.grid(row=4, column=2)
    
    Pmw.alignlabels((self.counterEuler1, self.counterEuler2, self.counterEuler3, self.counterPatternCenterX, self.counterPatternCenterZ, self.counterDetectorDistance, self.counterTilt,  self.counterEnergy, self.counterReflectors))
    
    self.update()
  
  def update(self):
#    try:
      euler1 = self.counterEuler1.component('entryfield').getvalue()
      if len(euler1) > 0: 
        euler1 = float(euler1)
      else:
        return
      
      euler2 = self.counterEuler2.component('entryfield').getvalue()
      if len(euler2) > 0: 
        euler2 = float(euler2)
      else:
        return
      
      euler3 = self.counterEuler3.component('entryfield').getvalue()
      if len(euler3) > 0: 
        euler3 = float(euler3)
      else:
        return
      
      pcx = self.counterPatternCenterX.component('entryfield').getvalue()
      if len(pcx) > 0: 
        pcx = float(pcx)
      else:
        return
      
      pcz = self.counterPatternCenterZ.component('entryfield').getvalue()
      if len(pcz) > 0: 
        pcz = float(pcz)
      else:
        return
      
      dd = self.counterDetectorDistance.component('entryfield').getvalue()
      if len(dd) > 0: 
        dd = float(dd)
      else:
        return
      
      tilt = self.counterTilt.component('entryfield').getvalue()
      if len(tilt) > 0: 
        tilt = float(tilt)
      else:
        return
      
      energy = self.counterEnergy.component('entryfield').getvalue()
      if len(energy) > 0: 
        energy = float(energy) * 1e3
      else:
        return
      
      reflectors = self.counterReflectors.component('entryfield').getvalue()
      if len(reflectors) > 0: 
        reflectors = int(reflectors)
      else:
        return
      
      bandcenter = bool(self.varCheckBandCenter.get())
      
      bandedges = bool(self.varCheckBandEdges.get())
      
      bandfull = bool(self.varCheckBandFull.get())
      
      
      
      angles = eulers.negativeEulers(euler1/180.0*pi, euler2/180.0*pi, euler3/180.0*pi) 
      
      vx = quaternions.quaternion(0,1,0,0)
      vy = quaternions.quaternion(0,0,1,0)
      vz = quaternions.quaternion(0,0,0,1)
      
      qSpecimenRotation = quaternions.quaternion(1,0,0,0)
      
      qCrystalRotation = quaternions.eulerAnglesToQuaternion(angles)
      
      qTilt = quaternions.axisAngleToQuaternion(-tilt/180.0*pi, (1,0,0))
      
      qDetectorOrientation = quaternions.axisAngleToQuaternion(pi, (0,0,1)) * quaternions.axisAngleToQuaternion(-90/180.0*pi, (1,0,0))
      qDetectorOrientation_ = qTilt * qDetectorOrientation.conjugate() * qTilt.conjugate()
      
      qRotations = [qDetectorOrientation_ * qTilt * qCrystalRotation * qSpecimenRotation]
      
      
      image = patternSimulations.drawPattern(self.L
                  , bandcenter=bandcenter
                  , bandedges=bandedges
                  , bandfull=bandfull
                  , intensity=False
                  , patternCenter=(pcx,pcz)
                  , detectorDistance=dd
                  , energy=energy
                  , numberOfReflectors=reflectors
                  , qRotations=qRotations
                  , patternSize=self.patternSize
                  , patternCenterVisible=True
                  , colorMode=True)
#    finally:
      self.objectMap.paste(image)

def main():
  root = Tkinter.Tk()
  root.resizable(0,0)

  patternSize = (1005,765)
  
  app = App(root, patternSize)
  

  root.mainloop()

if __name__ == '__main__':
  main()