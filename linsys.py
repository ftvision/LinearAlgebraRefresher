from decimal import Decimal, getcontext
from copy import deepcopy

from vector import Vector
from plane import Plane

getcontext().prec = 30


class LinearSystem(object):

    ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            d = planes[0].dimension
            for p in planes:
                assert p.dimension == d

            self.planes = planes
            self.dimension = d

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)

    def compute_solution(self):
        try:
            return self.do_gaussian_elimination_and_extract_solution()

        except Exception as e:
            if str(e) == self.NO_SOLUTIONS_MSG:
                return str(e)
            else:
                raise e

    def swap_rows(self, row1, row2):
        # add your code here
        self.planes[row1], self.planes[row2] = self.planes[row2], self.planes[row1] 


    def multiply_coefficient_and_row(self, coefficient, row):
        # add your code here
        self.planes[row].normal_vector = self.planes[row].normal_vector.times_scalar(coefficient)
        self.planes[row].constant_term = self.planes[row].constant_term * coefficient
        # another way of implementation
        # n = self.planes[row].normal_vector
        # k = self.planes[row].constant_term
        # new_normal_vector = n.times_scalar(coefficient)
        # new_constant_term = k * coefficient
        # self.planes[row] = Plane(normal_vector = new_normal_vector, constant_term = new_constant_term)

    def add_multiple_times_row_to_row(self, coefficient, row_to_add, row_to_be_added_to):
        # add your code here
        self.planes[row_to_be_added_to].normal_vector += self.planes[row_to_add].normal_vector.times_scalar(coefficient)
        self.planes[row_to_be_added_to].constant_term += self.planes[row_to_add].constant_term * coefficient
        # we can also use another way to implement --> create a new Plane for self.planes[row]

    def compute_triangular_form(self):
        system = deepcopy(self) #do not change the original self
        num_equations = len(self)
        num_variables = self.dimension

        dimension = min(num_equations, num_variables)
        for xi in xrange(dimension):
            # find that leading variable is not 0
            n = system.planes[xi].normal_vector
            c = MyDecimal(n.coordinates[xi])
            if c.is_near_zero():
                row_to_swap = xi
                for xj in xrange(xi + 1, num_equations):
                    cnew = MyDecimal(system.planes[xj].normal_vector.coordinates[xi])
                    if not cnew.is_near_zero():
                        row_to_wap = xj
                        break
                system.swap_rows(xi, xj)
            # if the new leading variable is not 0, go update
            n = system.planes[xi].normal_vector
            c = MyDecimal(n.coordinates[xi])
            if not c.is_near_zero():
                for xj in xrange(xi + 1, num_equations):
                    pnew = system.planes[xj]
                    coef = -pnew.normal_vector.coordinates[xi] / n.coordinates[xi]
                    system.add_multiple_times_row_to_row(coef, xi, xj)
        return system


    def compute_rref(self):
        tf = self.compute_triangular_form()
        num_equations = len(self)
        pivot_indices = tf.indices_of_first_nonzero_terms_in_each_row()

        for eqi in range(num_equations)[::-1]:
            j = pivot_indices[eqi]
            if j < 0:
                continue
            tf.scale_to_row_make_coefficient_equal_one(eqi, j)
            tf.clear_coefficients_above(eqi, j)
        
        return tf

    def do_gaussian_elimination_and_extract_solution(self):
        rref = self.compute_rref()

        rref.raise_exception_if_contradictory_equation()

        #if we only judge whether we have infinit number of solution
        #rref.raise_exception_if_two_few_pivots() 
        #num_variables = rref.dimension
        #solution_coordinates = [rref.planes[i].constant_term for i in range(num_variables)]
        #
        #return Vector(solution_coordinates)

        #if we want to have parametrization
        direction_vectors = rref.extract_direction_vectors_for_parametrization()
        basepoint = rref.extract_basepoint_for_parametrization()

        return Parametrization(basepoint, direction_vectors)
 
    def raise_exception_if_contradictory_equation(self):
        for p in self.planes:
            try:
                p.first_nonzero_index(p.normal_vector.coordinates)

            except Exception as e:
                if str(e) == 'No nonzero elements found':
                    constant_term = MyDecimal(p.constant_term)
                    if not constant_term.is_near_zero():
                        raise Exception(self.NO_SOLUTIONS_MSG)

                else:
                    raise e

    def raise_exception_if_two_few_pivots(self):
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        num_pivots = sum([1 if index > 0 else 0 for index in pivot_indices])
        num_variables = self.dimension
        if num_pivots < num_variables:
            raise Exception(self.INF_SOLUTIONS_MSG)

    def extract_direction_vectors_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()
        free_variable_indices = set(range(num_variables)) - set(pivot_indices)

        direction_vectors = []

        for free_var in free_variable_indices:
            vector_coords = [0] * num_variables
            vector_coords[free_var] = 1
            for i, p in enumerate(self.planes):
                pivot_var = pivot_indices[i]
                if pivot_var < 0:
                    break
                vector_coords[pivot_var] = -p.normal_vector.coordinates[free_var]
            direction_vectors.append(Vector(vector_coords))

        return direction_vectors

    def extract_basepoint_for_parametrization(self):
        num_variables = self.dimension
        pivot_indices = self.indices_of_first_nonzero_terms_in_each_row()

        basepoint_coords = [0] * num_variables

        for i, p in enumerate(self.planes):
            pivot_var = pivot_indices[i]
            if pivot_var < 0:
                break
            basepoint_coords[pivot_var] = p.constant_term

        return Vector(basepoint_coords)

    def scale_to_row_make_coefficient_equal_one(self, index_eq, index_var):
        n = self[index_eq].normal_vector.coordinates
        scale = Decimal('1.0') / n[index_var]
        self.multiply_coefficient_and_row(scale, index_eq)

    def clear_coefficients_above(self, index_eq, index_var):
        for eqj in range(index_eq):
            n = self[eqj].normal_vector.coordinates
            coef = - n[index_var]
            self.add_multiple_times_row_to_row(coef, index_eq, eqj)

    def indices_of_first_nonzero_terms_in_each_row(self):
        num_equations = len(self)
        num_variables = self.dimension

        indices = [-1] * num_equations

        for i,p in enumerate(self.planes):
            try:
                indices[i] = p.first_nonzero_index(p.normal_vector.coordinates)
            except Exception as e:
                if str(e) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise e

        return indices


    def __len__(self):
        return len(self.planes)


    def __getitem__(self, i):
        return self.planes[i]


    def __setitem__(self, i, x):
        try:
            assert x.dimension == self.dimension
            self.planes[i] = x

        except AssertionError:
            raise Exception(self.ALL_PLANES_MUST_BE_IN_SAME_DIM_MSG)


    def __str__(self):
        ret = 'Linear System:\n'
        temp = ['Equation {}: {}'.format(i+1,p) for i,p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps


class Parametrization(object):

    BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG = (
        'the basepoint and direction vector should all live in the same dimesion.')

    def __init__(self, basepoint, direction_vectors):

        self.basepoint = basepoint
        self.direction_vectors = direction_vectors
        self.dimension = self.basepoint.dimension

        try:
            for v in direction_vectors:
                assert v.dimension == self.dimension

        except AssertionError:
            raise Exception(BASEPT_AND_DIR_VECTORS_MUST_BE_IN_SAME_DIM_MSG)

    def __str__(self):
        num_decimal_places = 3
        basepoint_coords = self.basepoint.coordinates
        temp = []
        for d in range(self.dimension):
            output_d = 'x_{} = {}'.format(d + 1, round(basepoint_coords[d], 3))
            #add basepoint
            for i, v in enumerate(self.direction_vectors):
                vector_coords = v.coordinates
                if vector_coords[d] < 0:
                    output_d += ' - '
                if vector_coords[d] >= 0:
                    output_d += ' + '
                output_d += '{}'.format(round(abs(vector_coords[d]), 3))
                output_d += ' t_{}'.format(i + 1)
            temp.append(output_d)
        ret = 'Linear System Solution:\n'
        ret += '\n'.join(temp)
        return ret

