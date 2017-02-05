# Linear Algebra Refresher - Udacity

## Summary of the Course

This is a short refresher provided by Udacity. It offers very clear instructions and tutorial. It only covers some basics of the linear algebra, so it really doesn't teach you anything meaningful in linear algebra. 

It is very practical, however, in the instruction. The python code tutorial is very educational, at least for me, in terms of object-oriented programming and of implementing a math idea in code. So I have learned a lot from the coding experience, though not much for the knowledge.

## Knowledge Points

### Introduction

> This section talks about basic concepts of Points and Vectors.

- Point: Represent a Location, (x,y)
- Vector: Represent changes in locations, include magnitude and direction, [x, y, z]
- Point as a Vector:
	A point from the origin -> becomes a vector [x, y] = (x, y) - (0, 0)

### Vectors

> This section talks about the basic operations of Vectors

Given two vectors

$$\mathbf{v} = [x1, y1]$$
$$\mathbf{w} = [x2, y2]$$

- Addition
	- Geometrical Explanation: Connecting tail of $\mathbf{w}$ to head of $\mathbf{v}$, and the results is from the tail of $\mathbf{v}$ to the head of $\mathbf{w}$

$$\mathbf{v} + \mathbf{w} = [x1 + x2, y1 + y2]$$


- Subtraction
	- Geometrical Explanation: Connecting tails of $\mathbf{w}$ and $\mathbf{v}$, the results is from the head of $\mathbf{v}$ to the head of $\mathbf{w}$
	- Use addition idea: $\mathbf{w} + (\mathbf{v} - \mathbf{w}) = \mathbf{v}$

$$\mathbf{v} - \mathbf{w} = [x1 - x2, y1 - y2]$$

- Scaling
	- Geometrical Explanation: make the vector longer or shorter

$$a\mathbf{v} = [a x_1, a y_1]$$

- Length/Magnitude

$$||\mathbf{v}||^2 = x_1^2 + y_1^2$$

- More On Length
	- n-dimension: $||\mathbf{v}||^2 = \sum_i (x_i^2)$
	- Unit Vector: a vector magnitude = 1 
	- Normalize a vector: $\mathbf{v}_{normalized} = \mathbf{v} \cdot \frac{1}{||\mathbf{v}||}$
	- 0-vector has no normalization
	- 0-vector has no direction

- Inner Product

$$ dot(\mathbf{v},\mathbf{w}) = ||\mathbf{v}|| \times ||\mathbf{w}|| \cos(\theta)$$

- More on Inner Product
	- This can be used to calculate $\theta$ given the dot product is known. 
	- n-dimension: $dot(\mathbf{v},\mathbf{w}) = v_1w_1 + v_2w_2 + ... v_nw_n$
	- Cauchy-Schwart Inequality: $|dot(\mathbf{v},\mathbf{w})| <= ||\mathbf{v}|| \times ||\mathbf{w}||$
	- Geometrical Explanation 
		- If $\mathbf{v} \neq 0, \mathbf{w} \neq 0$
			- $dot(\mathbf{v},\mathbf{w}) = ||\mathbf{v}|| ||\mathbf{w}|| \rightarrow \theta = 0$
			- $dot(\mathbf{v},\mathbf{w}) = -||\mathbf{v}|| ||\mathbf{w}|| \rightarrow \theta = 180$
			- $dot(\mathbf{v},\mathbf{w}) = 0 \rightarrow \theta = 90$

- Parallel and Orthogonal
    - parallel -> $\mathbf{v}$ is parallel to  $a \cdot \mathbf{v}$
    - orthogonal -> $\mathbf{v}$ is parallel to $\mathbf{w}$ <==> $dot(\mathbf{v},w\mathbf{w}) = 0$ 
    - 0 is parallel and orthogonal to v, for any v
    - 0 is parallel and orthogonal to itself

- Projecting Vectors:
    - Orthogonality: tools for decomposing objects into combinations  of simpler objects in a structred way
    - $\mathbf{v}$ is probject on $\mathbf{b} \rightarrow proj_b(\mathbf{v}) = \mathbf{v} \cdot cos(\theta)$ 
    - $\mathbf{v} = \mathbf{v}^{parallel} + \mathbf{v}^{orthogonal}$
    - $\mathbf{u_b} = \mathbf{b} / ||\mathbf{b}||$, so $\mathbf{u_b}$ is a unit vector
    - $\mathbf{v}^{parallel} = \mathbf{v} \cdot \mathbf{u_b} = dot(dot(\mathbf{v}, u_b), u_b)$

- Cross Products (only in 3D space) 
    - $\mathbf{v}  \times \mathbf{w}  = ||\mathbf{v} || ||\mathbf{w} || \sin(\theta)$
    - Geometrical Explanation:
        - right thumb point to $\mathbf{v} $
        - right index point to $\mathbf{v}$ 
        - right middle point to $\mathbf{v}  \times \mathbf{w}$ 
        - Direction and magnitude (only in 3D)
        - Parallelgran: area of the the parallelgram of $\mathbf{v} $ and $\mathbf{w}$ 
            - area = $||\mathbf{v} \times \mathbf{w}||$
    - cross product is not symmetric
        - $\mathbf{\mathbf{v}}  \times \mathbf{\mathbf{w}}  = -(\mathbf{\mathbf{w}}  \times \mathbf{\mathbf{v}} )$

$$\mathbf{v} = [x1, y1, z1]$$
$$\mathbf{w} = [x2, y2, z2]$$

$$\mathbf{v} \times \mathbf{w} = [y_1z_2 - y_2z_1, -(x_1z_2 - x_2z_1), x_1y_2 - x_2y_1]$$



### Intersections

> This section talks about how to calculate intersections of vectors, planes, and high dimensional space. Equivalently, it talks about whether a linear equation system has one solution, infinite many solutions, or no solusions.

E.g. stock portofolio: consider two stocks $a$ and $b$

- weight of buying one of the stock: $w_a + w_b = 1$
- $\beta$ of each stock: measure of correlation of a stock's price movements with market movements: $\beta_a, \beta_b$
- $\beta$ of the **portofolio** $\beta_{potrfolio} = w_a  \beta_a + w_b  \beta_b$ 
	- it $\beta_{portfolio} = 0$, portfolio is uncorrelated with market
- choose weights $(w_a, w_b)$, such that $\beta_a  w_a + \beta_b  w_b = 0$ 
	- this is a line

#### Line representation

- basepoint $x_0$ (any point on the line)
- direction $\mathbf{v}$  (any scale)
- any point on the line $x(t) = x_0 + t\mathbf{v}$ (parameterization)
- $y = mx + b$
    - basepoint $x_0 = (0, b)$
    - direction $\mathbf{v} = [1, m]$
- $Ax + By = k$ 
    - basepoint:
	   - $B \neq 0, x_0 = (0, k/B)$
	   - $A \neq 0, x_0 = (k/A, 0)$
    - direction: $v =[B, -A]$
    - $(x,y)$ on $Ax + By = 0$ <=> $[x, y]$ orthogonal to $[A,B]$
    - $[A, B]$ is the **normal vector** of the line $Ax + By = k$ 

#### Intersections

$Ax + By = k$ => $[A, B]$ is the normal vector

- Parallel: two lines are parallel if their *normal vectors* are parallel
	- concident line: infinitely many intersections
		- $p_1$ at $line_1$, $p_2$ at $line_2$
		- Two parallel lines are equal <=> the vector connecting one point
			on each line is *orthogonal to* the lines' normal vectors
	- no intersection: no intersections
- Intersection of
$$Ax + By = k_1$$
$$Cx + Dy = k_2$$

$$x = \frac{Dk_1 - Bk_2}{AD - BC}$$
$$y = \frac{Ak_2 - Ck_1}{AD - BC}$$


####Solving multiple lines intersection

- For example: three lines could have 0, 1, 2, 3 intersections
- Here we want to know whether multiple lines have *a single common* intersection
- Inconsistent: not a single consistant intersection

#### 2D plane in 3D space:
- $Ax + By + Cz = k$
    - $[A, B, C] \cdot [x, y, z] = 0$, for any point $(x,y,z)$ in the plane
    - for any point $(x, y, z)$ on the plane, $[A, B, C]$ is orthogonal to $[x, y, z]$
	- $[A, B, C]$ is orthogonal to the plane, is the **normal vector** of the plane
- 2 parallel planes do not intersect
    - parallel planes have parallel normal vectors
    - two parallel planes are equal <=> the vector connecting one point on each plane is *orthogonal to* the plane's normal vectors

##### Intersections between planes

$$Ax + By + Cz = k1$$
$$Dx + Ey + Fz = k2$$

We know:
$$n_1 = [A, B, C]$$
$$n_2 = [D, E, F]$$

assume $n_1$ and $n_2$ are not parallel, the intersection between 2 planes

- a line with direction vector  $cross.prod([A, B, C], [D, E, F])$
- no solution
- a plane of solution

Intersection between 3 planes

- a line
- no solution
- a plane
- a dot

Equations and geomatrical explanations

- One equation in two variables -> a line
- One equation in three variables -> a plane
- **Caution** we have to count variables with coefficient = 0
    - $X + Y = 2$ -> define a line in 2D
    - $X + Y + 0Z = 2$ -> defines a plane in 3D

Linear Operations that does not change the linear system

1. Swap order of equations
2. Multiple an equation by a number $\alpha \neq 0$ on both sides
3. Add (a multiply of) an equation to another 

#### Solving a System of Equations: Gaussian Elimination

Use the linear system operations to

- Change the sub-space but does not change the intersection
- each linear transformation is a transformation of sub-space

- Special Cases
	- No solution: original system is inconsistent
	- Infinity number of solution:
		- parametrize solution set
		- Identify a pivot variable: a variable that is in a leading term when the system is in triangular form
		- free variable: non-leading variable
		- reduced row-echelon form (rref)