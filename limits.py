import numpy as np
import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style, quantity_support
plt.style.use(astropy_mpl_style)
quantity_support()

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import SkyCoord, EarthLocation, AltAz



arcturus = SkyCoord.from_name('Arcturus')

keck = EarthLocation.of_site('Keck Observatory')
utcoffset = +10*u.hour  # Hawaii Time
time = Time('2021-3-12 23:00:00') + utcoffset

arcturusaltaz = arcturus.transform_to(AltAz(obstime=time,location=keck))

midnight = Time('2021-3-13 00:00:00') + utcoffset
delta_midnight = np.linspace(-12, 12, 1000)*u.hour
frame_March13night = AltAz(obstime=midnight+delta_midnight,
                          location=keck)
arcturusaltazs_March13night = arcturus.transform_to(frame_March13night)

# Keck2 elevation limits
x1, y1 = [0, 186], [15, 15]
x2, y2 = [186, 332.7], [36.8, 36.8]
x3, y3 = [332.7, 360], [15, 15]
x4, y4 = [186, 186], [15, 36.8]
x5, y5 = [332.7, 332.7], [15, 36.8]


plt.plot(arcturusaltazs_March13night.az, arcturusaltazs_March13night.alt)	
plt.xlim(0*u.deg, 360*u.deg,)
plt.ylim(0*u.deg, 90*u.deg)
plt.xlabel('Azimuth')
plt.ylabel('Altitude')

plt.plot(x1, y1, x2, y2, x3, y3, x4, y4, x5, y5)
plt.show()

	
	
	
	
	
	
	#ax == -180
	#if i in ax < 0:
	#	i == i+360
    #ax.plot(180+azimuth_east)
    #ax.plot(azimuth_west-180)
    
#for N in range(0,366,60):
#    plot_az(ax,N)    
    
#xticks = [i for i in range(0,361, 20)]
#xtick_labels = ['{}'.format(t+180) if t < 180 else '{}'.format(t-180) for t in xticks]

#ax.set_xticks(xticks)
#ax.set_xticklabels(xtick_labels)

#ax.set_xlim([0,360])
#ax.set_ylim([0,90])



#nas el 36.8, out 15

#nas az 186, 332.7