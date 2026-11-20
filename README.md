
# BIT 2118 – Scientific Computing Assignment

## Introduction
This repository contains my individual Scientific Computing assignment using Python. It demonstrates numerical methods for solving mathematical problems and their real-world applications.

# TASK 6: SOLUTION OF SYSTEMS OF LINEAR EQUATIONS

## 1. Introduction
This task demonstrates how Python and NumPy can be used to solve systems of linear equations. The `numpy.linalg.solve()` function is used to calculate unknown values.

## 2. Original Program

The original program calculates the number of Type A and Type B servers using CPU and memory requirements.

**Input values:**
- CPU units: 20
- Memory: 72 GB
- Type A: 4 CPU units and 8 GB memory
- Type B: 2 CPU units and 12 GB memory

**Output:**
- Type A servers: 3
- Type B servers: 4

**Interpretation:**

The program shows that 3 Type A servers and 4 Type B servers satisfy the given CPU and memory requirements.

## 3. Modified Program

The CPU requirement was changed from 20 to 24 units, while memory remained at 72 GB.

**Output:**
- Type A servers: 4.5
- Type B servers: 3

**Interpretation:**

Increasing the CPU requirement changed the results. Type A increased from 3 to 4.5, while Type B decreased from 4 to 3.

## 4. Real-World Application: Hospital Equipment Allocation

A hospital needs to allocate two types of equipment according to their electricity and storage requirements.

**Input values:**
- Total electricity requirement: 21 units
- Total storage requirement: 35 GB
- Type A equipment: 5 power units and 10 GB storage
- Type B equipment: 3 power units and 5 GB storage

**Output:**
- Type A equipment: 0
- Type B equipment: 7

**Interpretation:**

The program calculates that 7 Type B equipment units and no Type A units satisfy the given requirements.

## Task 7: Gaussian Elimination and LU Decomposition

### Mathematical Concept
Gaussian elimination solves systems of linear equations by eliminating variables. LU decomposition factors a matrix into lower and upper triangular matrices.

### Input Values
- Coefficient matrix (A)
- Measurement vectors (b)

### Mathematical Operation
The program uses LU decomposition to solve systems of linear equations.

### Real-World Application
This method can be applied in engineering simulations where the same system of equations is solved using different measurements.

### Output and Interpretation
The program solved three different measurement sets
using LU decomposition.

The first measurement set produced [5, 5, 5].
The other measurement sets produced different values
because their input values were different.

The residual values were very close to zero,
showing that the solutions were accurate.

### Parameter Modification
The first measurement value was changed from 15 to 18.
The original solution was [5, 5, 5].
After the change, the solution became approximately
[5.80, 5.22, 5.07].
This shows that changing input values affects the final solution.

### Modified Real-World Problem
A small water supply system has three connected pipes.
The coefficient matrix represents the relationship
between water flow in the pipes.

Different measurement values are used to calculate
the flow in each pipe.

The program uses LU decomposition to solve the
system and find the unknown flow values. 

### Task 8: Iterative Methods for Linear Systems

### Mathematical Concept
Jacobi and Gauss-Seidel are iterative methods that solve systems of linear equations by improving initial estimates repeatedly until they converge.

### Input Values
- Coefficient matrix (A)
- Boundary influence vector (b)
- Initial estimate
- Tolerance

### Mathematical Operation
The program uses Jacobi and Gauss-Seidel methods to estimate temperatures at different points.

### Real-World Application
These methods can be used in heat-transfer simulations to estimate temperatures in different locations.

### Output and Interpretation
The program calculated temperatures at five points.
Both Jacobi and Gauss-Seidel produced almost the same
results as the direct solution.

The graph shows how the two methods approach the
solution as the number of iterations increases.

### Parameter Modification
The left boundary temperature was changed from 100°C to 120°C.
The temperatures at the five points increased.
Both Jacobi and Gauss-Seidel gave almost the same results
as the direct solution.
This shows that changing boundary temperatures affects
the temperature distribution.

### Modified Real-World Problem
A greenhouse has two boundary temperatures.
One side is maintained at 30°C while the other side
is maintained at 20°C.

The five points represent different locations inside
the greenhouse. The program calculates the temperature
at each point.

The results show that temperature gradually decreases
from the warmer side towards the cooler side.

## Conclusion

This assignment helped demonstrate how Python can be used to solve different mathematical problems. Task 6 covered systems of linear equations, Task 7 covered Gaussian elimination and LU decomposition, and Task 8 covered iterative methods. The programs showed how changing input values affects results and how numerical methods can be applied to real-world problems.
