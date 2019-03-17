import numpy as np
import scipy.constants as c

def deg_to_rad(deg):
    rad = deg/360 * (2*c.pi)
    return round(rad,5)

def rad_to_deg(rad):
    deg = rad/(2*c.pi)*360
    return round(deg,5)

def spherical_to_cartesian(r,theta,phi):
    x = r *np.sin(theta)*np.cos(phi)
    y = r *np.sin(theta)*np.sin(phi)
    z = r *np.cos(theta)
    return round(x,5),round(y,5),round(z,5)

def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    if x == 0 and y>0:
        theta = c.pi / 2
    elif x == 0 and y<0:
        theta = -c.pi / 2
    elif x== 0 and y == 0:
        theta = 0
    else:
        theta = np.arctan(y / x)

    phi = np.arccos(z / r)

    return round(r,5), round(phi,5), round(theta,5)

def angular_wave_func(m,l,theta,phi):
    if m == 0 and l == 0:
        solution = np.sqrt(1/(4*c.pi))
        return np.round(np.complex(solution), 5)
    elif l == 1 and m == 0:
        solution = np.sqrt(3/(4*c.pi)) *np.cos(theta)
        return np.round(np.complex(solution), 5)
    elif l == 1 and m == 1:
        solution = -np.sqrt(3/(8*c.pi))*np.sin(theta)*(np.exp(1j * phi))
        return np.round(np.complex(solution), 5)
    elif l == 1 and m == -1:
        solution = np.sqrt(3/(8*c.pi))*np.sin(theta)*(np.exp(-1j * phi))
        return np.round(np.complex(solution), 5)
    elif l == 2 and m == 2:
        solution = np.sqrt(15/(32*c.pi))*(np.sin(theta))**2 *np.exp(2j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 2 and m == 1:
        solution = - np.sqrt(15/(8*c.pi))*(np.sin(theta))*np.cos(theta) *np.exp(1j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 2 and m == 0:
        solution = np.sqrt(5/(16*c.pi))*(3*(np.cos(theta))**2 - 1)
        return np.round(np.complex(solution), 5)
    elif l == 2 and m == -1:
        solution = np.sqrt(15/(8*c.pi))*(np.sin(theta))*np.cos(theta) *np.exp(-1j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 2 and m == -2:
        solution = np.sqrt(15/(32*c.pi))*(np.sin(theta))**2 *np.exp(-2j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == 3:
        solution = -np.sqrt(35/(64*c.pi))*(np.sin(theta))**3 *np.exp(3j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == 2:
        solution = np.sqrt(105/(32*c.pi))*(np.sin(theta))**2 *np.cos(theta) *np.exp(2j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == 1:
        solution = -np.sqrt(21/(64*c.pi))* np.sin(theta) * (5*(np.cos(theta))**2 - 1) * np.exp(1j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == 0:
        solution = np.sqrt(-7/(16*c.pi))* (5*(np.cos(theta))**3 - 3*np.cos(theta))
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == -1:
        solution = np.sqrt(21/(64*c.pi))* np.sin(theta) * (5*(np.cos(theta))**2 - 1) * np.exp(-1j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == -2:
        solution = np.sqrt(105/(32*c.pi))*(np.sin(theta))**2 *np.cos(theta) *np.exp(-2j*phi)
        return np.round(np.complex(solution), 5)
    elif l == 3 and m == -3:
        solution = np.sqrt(35/(64*c.pi))*(np.sin(theta))**3 *np.exp(-3j*phi)
        return np.round(np.complex(solution), 5)
    else:
        return "ERROR"

a=c.physical_constants['Bohr radius'][0]

def radial_wave_func(n,l,r):
    if n == 1 and l == 0:
        solution = 2 *a**(-3/2) * np.exp(-r/a)
        return np.round(solution,5)
    elif n == 2 and l == 0:
        solution = 1 / np.sqrt(2) * a **(-3/2) * (1 - r/(2*a)) * np.exp(-r/(2*a))
        return np.round(solution,5)
    elif n == 2 and l == 1:
        solution = 1 / np.sqrt(24) * a **(-3/2) * (r/a) *np.exp(-r/(2*a))
        return np.round(solution,5)
    elif n == 3 and l == 0:
        solution = 2 / (81* np.sqrt(3)) * a **(-3/2) * (27 - 18*(r/a) + 2 *(r/a)**2) *np.exp(-r/(3*a))
        return np.round(solution,5)
    elif n == 3 and l == 1:
        solution = 8 / (27* np.sqrt(6)) * a **(-3/2) * (1 - r/(6*a)) *(r/a) *np.exp(-r/(3*a))
        return np.round(solution,5)
    elif n == 3 and l == 2:
        solution = 4 / (81* np.sqrt(30)) * a **(-3/2) * (r/a)**2 *np.exp(-r/(3*a))
        return np.round(solution,5)
    elif n == 4 and l == 0:
        solution = 1 / 4 * a **(-3/2) * (1 - 3/4*(r/a) + 1/8 *(r/a)**2 - 1/192 *(r/a)**3) *np.exp(-r/(4*a))
        return np.round(solution,5)
    elif n == 4 and l == 1:
        solution = np.sqrt(5) / (16* np.sqrt(3)) * a **(-3/2) * (1 - 1/4*(r/a) + 1/80*(r/a)**2) *(r/a) *np.exp(-r/(4*a))
        return np.round(solution,5)
    elif n == 4 and l == 2:
        solution = 1 / (64* np.sqrt(5)) * a **(-3/2) * (1 - 1/12 * r / a ) *(r/a)**2 *np.exp(-r/(4*a))
        return np.round(solution,5)
    elif n == 4 and l == 3:
        solution = 1 / (768 * np.sqrt(35)) * a **(-3/2) * (r/a)**3 *np.exp(-r/(4*a))
        return np.round(solution,5)
    else:
        return "ERROR"

def mgrid2d(xstart,xend,xpoints,ystart,yend,ypoints):
    ary = [[],[]]
    counter = float(xstart)
    n1= 0
    while counter <= xend:
        ary[0].append([])
        for y in range(ypoints):
            ary[0][-1].append(counter)
        n1+=1
        counter = float(xstart) + n1* ((xend-xstart)/(xpoints-1))
    for y in range(xpoints):
        counter2 = float(ystart)
        ary[1].append([])
        n=0
        while counter2 <= yend:
            ary[1][-1].append(counter2)
            n+=1
            counter2 = float(ystart)+(((yend-ystart)/(ypoints-1)))*n
    return ary

def mgrid3d(xstart,xend,xpoints,ystart,yend,ypoints,zstart,zend,zpoints):
    ary = [[],[],[]]
    xint = (xend-xstart)/(xpoints-1)
    yint = (yend-ystart)/(ypoints-1)
    zint = (zend-zstart)/(zpoints-1)

    for a in range(xpoints):
        lista =[]
        for b in range(ypoints):
            listb =[]
            for c in range(zpoints):
                listb.append(xstart + a * xint)
            lista.append(listb)
        ary[0].append(lista)
    for a in range(xpoints):
        lista =[]
        for b in range(ypoints):
            listb =[]
            for c in range(zpoints):
                listb.append(ystart + b* yint)
            lista.append(listb)
        ary[1].append(lista)
    for a in range(xpoints):
        lista =[]
        for b in range(ypoints):
            listb =[]
            for c in range(zpoints):
                listb.append(zstart + c * zint)
            lista.append(listb)
        ary[2].append(lista)
    return ary

def mag(c):
    magnitude = np.sqrt(np.real(c)**2 + np.imag(c)**2)
    return magnitude
def hydrogen_wave_func(n,l,m,roa,Nx,Ny,Nz):
    aryxyz = mgrid3d(-roa,roa,Nx,-roa,roa,Ny,-roa,roa,Nz) #array of points in cartesian coordinates

    cart_to_sphr = np.vectorize(cartesian_to_spherical) #vectorizing the functions
    ang_wave_funct = np.vectorize(angular_wave_func)
    rad_wave_funct = np.vectorize(radial_wave_func)
    mag_vectorized = np.vectorize(mag)

    rad,phi,tetha = cart_to_sphr(aryxyz[0],aryxyz[1],aryxyz[2]) #rad,phi and tetha are in lists
    if m == 0: #for non-complex
        ang_sol = ang_wave_funct(m,l,tetha,phi)
    elif m<0 :
        ang_sol = 1j/(np.sqrt(2)) * (ang_wave_funct(-abs(m),l,tetha,phi) - (-1)**m *ang_wave_funct(abs(m),l,tetha,phi))
    else:
        ang_sol = 1/(np.sqrt(2)) * (ang_wave_funct(-abs(m),l,tetha,phi) - (-1)**m *ang_wave_funct(abs(m),l,tetha,phi))
    rad_sol = rad_wave_funct(n,l,rad*a)
    wave_squared = (mag_vectorized(ang_sol*rad_sol)) **2
    return np.around(aryxyz[0],5), np.around(aryxyz[1],5), np.around(aryxyz[2],5), wave_squared



