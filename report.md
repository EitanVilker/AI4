<h1>

    CS76
    21F
    PA1
    Eitan Vilker

</h1>

### Description
I set things up so most of my code was in a parent CSP class. The main exceptions were the check_constraints methods, and for the circuit board problem, two functions to aid in constructing the domains and drawing the solution. The heuristics were also modified by the circuit board problem because it uses the constriants differently than the map coloring problem and thus needed some modificiations.


### Evaluation
I was able to get a general CSP class that could be extended for specific problems. In addition, I managed to get heuristics that were useful for significantly speeding up the solution. My implementation of AC-3 didn't work very quickly without heuristics, but with them it improved program execution speed.


### Responses

