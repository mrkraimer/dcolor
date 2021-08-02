import numpy as np
import rgbcolor
dc = rgbcolor.DColor()
dc.plot(lambda z : z,title='z expand 2',expand=2)
dc.plot(lambda z : z+4,title='z+4 expand 2',expand=2)
dc.plot(lambda z : z-4,title='z-4 expand 2',expand=2)
dc.plot(lambda z : z+4j,title='z+4j expand 2',expand=2)
dc.plot(lambda z : z-4j,title='z-4j expand 2',expand=2)
dc.plot(lambda z : (((z+4)*(z-4)*(z+4j)*(z-4j))**(1/8)),
    title='(((z+4)*(z-4)*(z+4j)*(z-4j))**(1/8))')
dc.plot(lambda z : 1/z,title='1/z expand 2',expand=2)
dc.plot(lambda z : (np.sin(2*np.pi/z)),title='sin(2*np.pi/z)')
dc.plot(lambda z : (np.cos(2*np.pi/z)),title='cos(2*np.pi//z)')
dc.plot(lambda z : np.sin(z),title='sin(z)')
dc.plot(lambda z : np.cos(z),title='cos(z)')
dc.plot(lambda z : z**3 -1,title='z**3 -1 expand 2',expand=2)
dc.plot(lambda z : z**2+4+4j,title='z**2+4+4j expand 2',expand=2)
dc.plot(lambda z : z**8+4+4j,title='z**8+4+4j expand 8',expand=8)
dc.plot(lambda z : z**16+4+4j,title='z**16+4+4j expand 256',expand=256)
dc.plot(lambda z : ((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j),
    title='((z**2-1)*(z-2- 1j)**2)/(z**2 +2+ 2j) expand .5',expand=.5)
