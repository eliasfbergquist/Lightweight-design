import numpy as np
import matlib, compositelib
m1 = matlib.get('Carbon/Epoxy(a)')

# Material stiffness matrix:
C = compositelib.C3D(m1)

# Example: quazi-isotropic layup:
thicknesses =  [0.5,  0.1 ,   0.2,   0.2]
orientations = [0, 90, -45,  45]

# Initiating the average stiffness matrix:
Cav = np.zeros((6,6))

# Loop over all layers:
for thi, ori in zip(thicknesses, orientations):
    Ck = compositelib.C3Dtz(C,ori)
    Cav = Cav + (Ck*thi)/(sum(thicknesses))

# The average compliance matrix:
Sav = np.linalg.inv(Cav)

# Extracting the engineering constants of the homogenized laminate:
m_hl =   {'E1':  1/Sav[0,0],
          'E2':  1/Sav[1,1],
          'E3':  1/Sav[2,2],
          'v12': -Sav[0,1]*(1/Sav[0,0]),
          'v13': -Sav[0,2]*(1/Sav[0,0]),
          'v23': -Sav[1,2]*(1/Sav[1,1]),
          'G12': 1/Sav[5,5],
          'G13': 1/Sav[4,4],
          'G23': 1/Sav[3,3]}

#a version of these calculations in a function that can be called from other scripts if needed:
#takes fiber configuration and material type as inputs, returns stiffness matrix and dictionary with engineering values
def homogenize(thickness_array=[0.5,0.1,0.2,0.2], orientation_array=[], material_name="Carbon/Epoxy(a)"):
    Cav = np.zeros((6,6))
    for thi, ori in zip(thicknesses, orientations):
        Ck = compositelib.C3Dtz(C,ori)
        Cav = Cav + (Ck*thi)/(sum(thicknesses))
    Sav = np.linalg.inv(Cav)
    m_hl =   {'E1':  1/Sav[0,0],
          'E2':  1/Sav[1,1],
          'E3':  1/Sav[2,2],
          'v12': -Sav[0,1]*(1/Sav[0,0]),
          'v13': -Sav[0,2]*(1/Sav[0,0]),
          'v23': -Sav[1,2]*(1/Sav[1,1]),
          'G12': 1/Sav[5,5],
          'G13': 1/Sav[4,4],
          'G23': 1/Sav[3,3]}
    return Cav, m_hl




print('Homogenized stiffness matrix:')
print()
print(np.array2string(Cav, precision=0, suppress_small=True, separator='  ', floatmode='maxprec') )
print()
print('Homogenized engineering constants as a new material:')
for ele in m_hl:
    print(ele+": "+str(m_hl[ele]))

