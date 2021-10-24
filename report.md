<h1>

    CS76
    21F
    PA1
    Eitan Vilker

</h1>

### Description
I set things up so most of my code was in a parent CSP class. The main exceptions were the check_constraints methods, and for the circuit board problem, two functions to aid in constructing the domains and drawing the solution. The heuristics, except for LCV, were also modified by the circuit board problem because it uses the constraints differently than the map coloring problem and thus needed some modificiations. I have some helper functions like check_domain_values, get_second, revise, and check_if_consistent that make my heuristics and inferences work. check_if_consistent is used by the backtrack method and any other place where an assignment needs to be assessed for validity.


### Evaluation
I was able to get a general CSP class that could be extended for specific problems. In addition, I managed to get heuristics that were useful for significantly speeding up the solution. My implementation of AC-3 didn't work very quickly without heuristics, but with them it improved program execution speed. LCV also did not really help at all; I usually looked at about the same number of assignments as without it. Generally spekaing, I think I got everything working, though I'm not sure if AC-3 is performing fully as it doesn't seem to have much impact on my results.


### Responses

#### Map Coloring Problem
With MRV and the degree heuristic, I got the best results using my example, 10 recursive calls. Using arc-consistency never seemed to increase or decrease the number of recursive calls made, though it did make the code execute more quickly when combined with heuristics. Using LCV or no heuristic, I got reasonable but less efficient results, 12 recursive calls. Since the minimum possible is 10 given that there are ten variables, my first two heuristics seem to be optimal in this admittedly smale scale version of the problem.

#### Circuit Board Problem
For a variable of width w and height h, on a board of width n and height m, the domain size should be (n - w)(m - h), since the variable's x position cannot start after n - w and its y position cannot start after m - h or the variable will exceed the boundaries.

a is 3x2 and b is 5x2 on a 10x3 board. To enforce the constraint that they cannot overlap, we must set it so that one of the following statements is true:
1. If the x coordinate of a is less than that of b, it cannot be within 3 of b, and if it is greater, it must be at least 5 units away horizontally. 
2. The same idea applies for y, where a and b must be at least 2 units away from each other vertically.
Legal pairs using this method, with the ; symbol meaning any value in between two numbers, inclusive, are: ((a_x = 0;4, a_y = 0;1), (b_x = 5 ; 10 - a_x - 5, b_y = 0-1)), ((a_x = 0;b_x - 1, a_y = 0;1), (b_x = 3;5, b_y = 0;1)), ((a_x = 10 - b_x, a_y = 0;1), (b_x = 0;2, b_y = 0;1)), ((a_x = 5;8, a_y = 0;1), (b_x = 0 ; 10 - a_x - 5, b_y = 0;1))

My code converts constraints to integer values by representing the rectangular circuit constraints as widths and heights. For the domains, I represented each square as a pair of integer coordinates.
