#compositelib.py
import numpy as np

def S3D(m):
    '''
    Input:
    - m: dictionary of material properties
    Output:
    - returns the compliance matrix as a 6x6 array
    '''
    return np.array(
    [[        1/m['E1'],-m['v12']/m['E1'],-m['v13']/m['E1'],         0,    0,     0],
     [-m['v12']/m['E1'],        1/m['E2'],-m['v23']/m['E2'],         0,    0,     0],
     [-m['v13']/m['E1'],-m['v23']/m['E2'],        1/m['E3'],         0,    0,     0],
     [                0,                0,                0,1/m['G23'],    0,     0],
     [                0,                0,                0,    0,1/m['G13'],     0],
     [                0,                0,                0,    0,     0,1/m['G12']] ],
    float)

def C3D(m):
    '''
    Input:
    - m: dictionary of material properties
    Output:
    - returns the stiffness matrix as a 6x6 array
    '''
    return np.linalg.inv(S3D(m))

def T3Dez(rot):
    rot=np.radians(rot)
    c=np.cos(rot)
    s=np.sin(rot)
    return    np.array([[ c*c ,  s*s ,  0.0 , 0.0 , 0.0  ,    c*s ],
                        [ s*s ,  c*c ,  0.0 , 0.0 , 0.0  ,   -c*s ],
                        [ 0.0 ,  0.0 ,  1.0 , 0.0 , 0.0  ,    0.0 ],
                        [ 0.0 ,  0.0 ,  0.0 ,   c ,  -s  ,    0.0 ],
                        [ 0.0 ,  0.0 ,  0.0 ,   s ,   c  ,    0.0 ],
                        [-2*c*s, 2*c*s, 0.0 , 0.0 , 0.0  ,c*c-s*s ]],
                        float)

def T3Dsz(rot):
    rot=np.radians(rot)
    c=np.cos(rot)
    s=np.sin(rot)
    return    np.array([[ c*c ,  s*s ,  0.0 , 0.0 , 0.0  ,  2*c*s ],
                        [ s*s ,  c*c ,  0.0 , 0.0 , 0.0  , -2*c*s ],
                        [ 0.0 ,  0.0 ,  1.0 , 0.0 , 0.0  ,    0.0 ],
                        [ 0.0 ,  0.0 ,  0.0 ,   c ,  -s  ,    0.0 ],
                        [ 0.0 ,  0.0 ,  0.0 ,   s ,   c  ,    0.0 ],
                        [-c*s ,  c*s ,  0.0 , 0.0 , 0.0  ,c*c-s*s ]],
                        float)

def C3Dtz(C,rot):
    return np.dot(np.linalg.inv(T3Dsz(rot)), np.dot(C,T3Dez(rot)))

