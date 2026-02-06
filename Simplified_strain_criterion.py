import matlib

material=matlib.get('Carbon/Epoxy(a)')

epsft = material['XT']/material['E1']   # tensile fiber failure strain
epsfc = material['XC']/material['E1']   # compressive fiber failure strain

print("tensile fiber failure strain: "+str(epsft))
print("compressive fiber failure strain: "+str(epsfc))


saftety_factor=3

print('Tensile strain:     {:.4f}'.format(epsft/saftety_factor))
print('Compressive strain: {:.4f}'.format(epsfc/saftety_factor))
