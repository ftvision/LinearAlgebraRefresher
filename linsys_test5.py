from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

from linsys import LinearSystem, MyDecimal, Parametrization

print "Test Starts...."

#Solve some linear system

p1 = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')
s = LinearSystem([p1,p2, p3])
r = s.compute_solution()
print r
#p1 = Plane(normal_vector=Vector(['5.862','1.178','-10.366']), constant_term='-8.15')
#p2 = Plane(normal_vector=Vector(['-2.931','-0.589','5.183']), constant_term='-4.075')
#s = LinearSystem([p1,p2])
#r = s.do_gaussian_elimination_and_extract_solution()
#print r

p1 = Plane(normal_vector=Vector(['5.262','2.739','-9.878']), constant_term='-3.441')
p2 = Plane(normal_vector=Vector(['5.111','6.358','7.638']), constant_term='-2.152')
p3 = Plane(normal_vector=Vector(['2.016','-9.924','-1.367']), constant_term='-9.278')
p4 = Plane(normal_vector=Vector(['2.167','-13.543','-18.883']), constant_term='-10.567')
s = LinearSystem([p1,p2,p3,p4])
r = s.compute_solution()
print r


p1 = Plane(normal_vector=Vector(['0.786','0.786','0.588']), constant_term='-0.714')
p2 = Plane(normal_vector=Vector(['-0.138','-0.138','0.244']), constant_term='0.319')
s = LinearSystem([p1,p2])
r = s.compute_solution()
print r


p1 = Plane(normal_vector=Vector(['8.631','5.112','-1.816']), constant_term='-5.113')
p2 = Plane(normal_vector=Vector(['4.315','11.132','-5.27']), constant_term='-6.775')
p3 = Plane(normal_vector=Vector(['-2.158','3.01','-1.727']), constant_term='-0.831')
s = LinearSystem([p1,p2, p3])
r = s.compute_solution()
print r

p1 = Plane(normal_vector=Vector(['0.935','1.76','-9.365']), constant_term='-9.955')
p2 = Plane(normal_vector=Vector(['0.187','0.352','-1.873']), constant_term='-1.991')
p3 = Plane(normal_vector=Vector(['0.374','0.704','-3.746']), constant_term='-3.982')
p4 = Plane(normal_vector=Vector(['-0.561','-1.056','5.619']), constant_term='5.973')
s = LinearSystem([p1,p2, p3])
r = s.compute_solution()
print r

print "Test Ends...."