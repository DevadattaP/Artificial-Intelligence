# Artificial Intelligence (Semester 5 - Computer Science Engineering, AI & ML)

This repository contains various practical programs implemented as part of the Artificial Intelligence course (Semester 5) in the Computer Science Engineering (AI & ML) curriculum at the University of Mumbai. The programs are written in Prolog and Python, demonstrating key AI concepts such as logic programming, search algorithms, and Bayesian inference.


## Table of Contents

- [Introduction](#introduction)
- [Programs Included](#programs-included)
- [Prerequisites](#prerequisites)
- [How to Run](#how-to-run)
- [Program Descriptions](#program-descriptions)
- [Contributing](#contributing)

## Introduction

This repository showcases artificial intelligence programs covering topics like Prolog-based logic programming, search algorithms (uninformed and informed), expert systems, and probabilistic reasoning. The practicals are implemented in both Prolog and Python, making use of Prolog for symbolic logic-based AI and Python for algorithmic solutions.

## Programs Included

The repository contains the following practical programs:

1. **Prolog Programs**: Facts and rules, family tree, if-then logic, minimum-maximum number, series/parallel resistance calculation.
2. **First-Order Predicate Logic (FOPL)**: Implementation using Prolog.
3. **Mini Expert System**: Vacuum cleaner problem using Prolog.
4. **Hill Climbing Algorithm**: Travelling salesperson problem.
5. **A-star Algorithm**: Informed search for the 8-puzzle problem.
6. **BFS-DFS Graph Traversal**: Water jug problem.
7. **Adversarial Search Algorithm**: Tic-tac-toe game.
8. **Bayesian Belief Network**: Solving the Monty Hall problem.

## Prerequisites

To run these programs, you'll need:

- **SWI-Prolog** (for Prolog programs) or any other compatible Prolog interpreter.
- **Python 3.x** for Python-based algorithms.
- Basic knowledge of artificial intelligence concepts, logic programming, and search algorithms.

## How to Run

### Running Prolog Programs:

1. **Install SWI-Prolog:**
   - Download and install SWI-Prolog from [https://www.swi-prolog.org](https://www.swi-prolog.org).

2. **Clone the Repository:**
   ```sh
   git clone https://github.com/DevadattaP/Artificial-Intelligence.git
   cd Artificial-Intelligence/Prolog
    ```
3. **Open the Prolog File:**
    - Launch SWI-Prolog, then open the Prolog file:
    ```sh
    swipl
    ?- consult('filename.pl').
    ```
4. **Run the Queries:**
    - Execute queries based on the program by entering them in the Prolog interpreter.

### Running Python Programs:
1. **Clone the Repository:**
    ```sh
    git clone https://github.com/DevadattaP/Artificial-Intelligence.git
    cd Artificial-Intelligence
    ```
2. **Run the Python Programs:**
   ```sh
   python filename.py
    ```

## Program Descriptions

### 1. Prolog Programs
   - **Facts & Rules**: Introduction to defining basic facts and rules in Prolog, illustrating how Prolog's logical inference works.
   - **Family Tree**: A program to represent family relationships (parent, child, sibling, etc.) and query familial relationships using Prolog.
   - **If-Then Logic**: Demonstrating conditional logic in Prolog with simple `if-then` rules.
   - **Minimum-Maximum Number**: Prolog program to find the minimum and maximum numbers from a list of integers.
   - **Series & Parallel Resistance**: Calculating total resistance of circuits in series and parallel configurations using Prolog.

### 2. First-Order Predicate Logic (FOPL)
   - **FOPL in Prolog**: Implementation of First-Order Predicate Logic (FOPL) using Prolog, demonstrating logical deductions and inferences.

### 3. Mini Expert System
   - **Vacuum Cleaner Problem**: A mini expert system implemented in Prolog to simulate a simple vacuum cleaner agent that decides the next action (cleaning, moving left/right) based on current environment conditions.

### 4. Hill Climbing Algorithm
   - **Travelling Salesperson Problem (TSP)**: Implementation of the Hill Climbing algorithm, a local search algorithm, to solve the Travelling Salesperson Problem (TSP) in Python, where the goal is to find the shortest path visiting all cities.

### 5. A* Algorithm
   - **8-Puzzle Problem**: Solving the 8-puzzle problem using the A* search algorithm, an informed search technique that uses heuristics to find the optimal solution efficiently.

### 6. BFS-DFS Graph Traversal
   - **Water Jug Problem**: Implementing Breadth-First Search (BFS) and Depth-First Search (DFS) algorithms in Python to solve the water jug problem, where the goal is to measure a specific amount of water using two jugs of given capacities.

### 7. Adversarial Search Algorithm
   - **Tic-Tac-Toe Problem**: A Python implementation of the minimax algorithm, an adversarial search technique used to play and solve the Tic-Tac-Toe game optimally.

### 8. Bayesian Belief Network
   - **Monty Hall Problem**: Solving the Monty Hall problem using a Bayesian belief network in Python, demonstrating the application of probability and decision theory to make optimal choices in uncertain environments.


## Contributing
Contributions are welcome! If you have any suggestions or additional programs to add, feel free to fork the repository, make your changes, and submit a pull request.