import pcbnew
import math

board   = pcbnew.GetBoard()
modules = board.GetModules() 

def rotate(origin, point, angle):
    """
    Rotate a point counterclockwise by a given angle around a given origin.

    The angle should be given in radians.
    """
    ox = origin.x
    oy = origin.y

    px = point.x
    py = point.y

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return pcbnew.wxPoint(qx, qy)
    
def findDiode(id):
  for module in modules:
    reference = module.GetReference()
    if reference.startswith('D'):
      if reference[1:] == id:
        return module


def postionDiodeForSwitch(switch):
  switchId       = switch.GetReference()[2:]
  # print(switchId)
  diode          = findDiode(switchId)
  # print(diode.GetReference())
  switchPosition    = switch.GetPosition()
  switchOrientation = switch.GetOrientation()
  swOrDeg = switch.GetOrientationDegrees()
  print(switchPosition)
  diodePosition = switchPosition + pcbnew.wxPoint((8300000 * math.sin(math.radians(switchOrientation/10))), (8300000 * math.cos(math.radians(switchOrientation/10))))
  
  # diodePosition = rotate(switchPosition, diodePosition, switchOrientation * 10)

  print(switchOrientation)

  diode.SetPosition(diodePosition) #switchPosition.__add__(pcbnew.wxPoint(10, 10)))
  diode.SetOrientation(switchOrientation)


#ds=pcbnew.DRAWSEGMENT(pcb)
#self._board.Add(ds)
#ds.SetShape(pcbnew.S_SEGMENT)
#ds.SetStart(pcbnew.wxPoint(1, 1))
#ds.SetEnd(pcbnew.wxPoint(10, 10))
#ds.SetLayer(pcb._LayerNumByName["B.SilkS"])
#ds.SetWidth(int(0.15*pcbnew.IU_PER_MM))

 
#em = pcbnew.EDGE_MODULE(pcb)

print("Hello")
pos = board.GetPosition()
print(pos)


for module in board.GetModules():
  reference = module.GetReference()
  if (reference.startswith('SW')):
    postionDiodeForSwitch(module)
    # print(module.GetReference()),
    # print(module.GetPosition())



pcbnew.Refresh()