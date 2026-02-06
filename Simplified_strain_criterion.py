import matlib

material=matlib.get('Carbon/Epoxy(a)')

saftety_factor=3


epsft = material['XT']/material['E1']   # tensile fiber failure strain
epsfc = material['XC']/material['E1']   # compressive fiber failure strain

print("tensile fiber failure strain: "+str(epsft))
print("compressive fiber failure strain: "+str(epsfc))



print('allowable tensile strain for a safety factor of ' + str(saftety_factor)+':     '+str(epsft/saftety_factor))
print('allowable compressive strain for a safety factor of ' + str(saftety_factor)+': '+str(epsfc/saftety_factor))

