#test 2D 
#Judith eluzai canul chavez 
#profe no pude subir el .py en git porque no me aceptaba las cuentas de gmail que le proporcionaba 
# y ya se me iba a cerrar el espacio para entregar en plataforma :( 

import matplotlib.pyplot as plt
import numpy as np

plt.axis([-100,100,-100,100])
plt.axis('on')
plt.grid(True)

#rectangulo 1
x1=-75
x2=0
y1=-7
y2=-75

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(.4,0,.3))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(.4,0,.3))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(.4,0,.3))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(.4,0,.3))

#rectangulo 2
x1=-37.5
x2=37.5
y1=27
y2=-41

plt.plot([x1,x1],[y1,y2],linewidth=1,color=(.4,0,.3))
plt.plot([x2,x2],[y1,y2],linewidth=1,color=(.4,0,.3))
plt.plot([x1,x2],[y1,y1],linewidth=1,color=(.4,0,.3))
plt.plot([x1,x2],[y2,y2],linewidth=1,color=(.4,0,.3))



#Circulo
xc=0
yc=-7
r=20

p1=0*np.pi/180
p2 =360*np.pi/180
dp=(p2-p1)/100

xlast=xc+r*np.cos(p1)
ylast=yc+r*np.sin(p1)

for p in np.arange(p1,p2+dp,dp):
    xp=xc+r*np.cos(p)
    yp=yc+r*np.sin(p) 
    
    plt.plot([xlast,xp],[ylast,yp], color=(0,.3,.4), linewidth=1)
    xlast=xp
    ylast=yp
    

plt.show()