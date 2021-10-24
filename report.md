<h1>

    CS76
    21F
    PA1
    Eitan Vilker

</h1>

### Description
I set things up so most of my code was in a parent CSP class. The main exceptions were the check_constraints methods, and for the circuit board problem, two functions to aid in constructing the domains and drawing the solution. The heuristics, except for LCV, were also modified by the circuit board problem because it uses the constraints differently than the map coloring problem and thus needed some modificiations.


### Evaluation
I was able to get a general CSP class that could be extended for specific problems. In addition, I managed to get heuristics that were useful for significantly speeding up the solution. My implementation of AC-3 didn't work very quickly without heuristics, but with them it improved program execution speed. LCV also did not really help at all; I usually looked at about the same number of assignments as without it.


### Responses

#### Map Coloring Problem
With MRV and the degree heuristic, I got the best results. Using arc-consistency never seemed to increase or decrease the number of recursive calls made, though it did make the code execute more quickly when combined with heuristics. Using LCV or no heuristic, I got reasonable but less efficient results.

#### Circuit Board Problem
For a variable of width w and height h, on a board of width n and height m, the domain size should be (n - w)(m - h), since the variable's x position cannot start after n - w and its y position cannot start after m - h or the variable will exceed the boundaries.

a is 3x2 and b is 5x2 on a 10x3 board. To enforce the constraint that they cannot overlap, 
