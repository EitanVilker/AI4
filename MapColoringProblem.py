from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem

class MapColoringProblem(ConstraintSatisfactionProblem):

    def __init__(self, variables, domains, constraints):

        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.variable_index_dict = {}
        for i in range(len(self.variables)):
            self.variable_index_dict[self.variables[i]] = i
        self.assignments_tried = 0
        self.assignment = None

    def check_constraints(self, x, y, assignment):

        if y not in self.constraints[x]:
            return True
        if x not in assignment or y not in assignment:
            return True
        if assignment[x] == assignment[y]:
            return False
        return True


variables = ["Mexico", "Texas", "New England", "California", "Canada"]
domains = []
for i in range(len(variables)):
    domains.append(["r", "g", "b"])

''' Solution: 
Texas = r
Mexico = Canada = g
California = New England = b
'''
constraints = {}
constraints["Mexico"] = ["Texas", "California"]
constraints["California"] = ["Mexico", "Texas", "Canada"]
constraints["Texas"] = ["Mexico", "California", "Canada", "New England"]
constraints["New England"] = ["Texas", "Canada"]
constraints["Canada"] = ["California", "Texas", "New England"]

mcp = MapColoringProblem(variables, domains, constraints)
mcp.backtracking_search(heuristic=None, ac3=True)
print(mcp.assignment)