
class ConstraintSatisfactionProblem():

    def __init__(self, variables, domains, constraints):

        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.arcs = []
        self.variable_index_dict = {}
        for i in range(len(self.variables)):
            self.variable_index_dict[self.variables[i]] = i
        self.assignment = None
        self.assignments_tried = 0

    def backtracking_search(self, ac3=False, heuristic=False):
        result = self.backtrack({}, ac3=ac3, heuristic=heuristic)
        self.assignment = result
        return self.assignment

    def backtrack(self, assignment, ac3=False, heuristic=False):

        self.assignments_tried += 1

        if len(assignment) == len(self.variables):
            return assignment

        # Get variables not in assignment
        variables = []
        for variable in self.variables:
            if variable not in assignment:
                variables.append(variable)
        
        if len(variables) == 0:
            return None
        
        if not heuristic or heuristic == "LCV":
            var_index = self.variable_index_dict[variables[0]] # int, index of variable
        elif heuristic == "MRV":
            var_index = self.variable_index_dict[self.MRV(variables, assignment)]
        elif heuristic == "degree":
            var_index = self.variable_index_dict[self.degree_heuristic(variables, assignment)]
        
        if heuristic == "LCV":
            domain = self.least_constraining_value(self.variables[var_index], assignment)
        else:
            domain = self.domains[var_index]
            
        for value in domain:
            keys_removed = []
            next_assignment = assignment.copy()
            next_assignment[self.variables[var_index]] = value
            # keys_added.append(self.variables[var_index])
            if self.check_if_consistent(self.variables[var_index], next_assignment):
                if ac3:
                    keys_removed = self.arc_consistency(var_index, value, keys_removed, next_assignment)
                result = self.backtrack(next_assignment, ac3=ac3, heuristic=heuristic)
                if result is not None:
                    return result
            
            # Restore domain
            if ac3:
                for key in keys_added:
                    domain.append(keys_removed)

        return None


    def arc_consistency(self, var_index, value, keys_removed, assignment):
        
        # Set up queue of all connections between variables
        arc_queue = []
        for i in self.variables:
            for j in self.variables:
                if i != j:
                    arc_queue.append((i, j))

        while len(arc_queue) > 0:
            x_i, x_j = arc_queue.pop(0)
            revised, keys_removed = self.revise(x_i, x_j, assignment)
            if len(self.domains[x_i]) == 0:
                return None
            if revised:
                return keys_removed

    def revise(self, x_i, x_j, assignment):
        keys_removed = []
        assignment_copy = assignment.copy()
        revised = False
        for i in self.domains[x_i]:
            satisfied = False
            assignment_copy[x_i] = i
            for j in self.domains[x_j]:
                assignment_copy[x_j] = j
                if self.check_constraints(x_i, x_j, assignment):
                    satisfied = True
            if not satisfied:
                # Delete i from domain
                keys_removed.append(i)
                revised = True
        for key in keys_removed:
            self.domains[x_i].remove(key)
        return revised, keys_removed
                
                
    def check_if_consistent(self, x, assignment):
        for variable in self.variables:
            if not self.check_constraints(x, variable, assignment):
                return False
        return True

    # Function to count the number of neighbors still unassigned. Useful to heuristics
    def count_remaining_constraints(self, variable, assignment):
        constraints = self.constraints[variable]
        remaining_constraints = []
        for constraint in constraints:
            if constraint not in assignment:
                remaining_constraints.append(constraint)
        return len(remaining_constraints)

    # Function to get the most constrained unassigned variable
    def degree_heuristic(self, variables, assignment):
        next_variable = None
        next_constraint_count = -1
        for variable in variables:
            if self.count_remaining_constraints(variable, assignment) > next_constraint_count:
                next_constraint_count = len(self.constraints[variable])
                next_variable = variable
        return next_variable

    def check_domain_value(self, variable, value, assignment):
        new_assignment = assignment.copy()
        new_assignment[self.variables[variable]] = value
        if self.check_if_consistent(self.variables[variable], assignment):
            return True
        return False
    
    # Function to get the variable with the smallest number of possible values
    def MRV(self, variables, assignment):

        next_variable = None
        lowest_domain_size = 9999999
        for variable in variables:
            var_index = self.variable_index_dict[variable]
            temp_domain_size = len(self.domains[var_index])
            # For each possible value of the variable
            for current in self.domains[var_index]:
                # For each neighbor constraint
                for y in assignment:
                    if y in constraints:
                        if assignment[constraint] in self.domains[var_index]:
                            temp_domain_size -= 1
                            # Break to look at the next possible value since we don't care if multiple neighbors are blocking the same value
                            break
            if temp_domain_size < lowest_domain_size:
                lowest_domain_size = temp_domain_size
                next_variable = variable

        # If lowest domain size is 0 it means something has gone wrong and there can be no complete assignment
        # if lowest_domain_size == 0:
        #     return None

        return next_variable

    # Helper function for LCV
    def get_second(self, item):
        return item[1]

    # Orders domain so least constraining value is looked at first and most last
    def least_constraining_value(self, x, assignment):

        starting_domain = self.domains[self.variable_index_dict[x]]
        new_domain_of_tuples = []
        lowest_count = 9999999
        for value in starting_domain:
            current_count = 0
            for y in self.variables:
                if y not in assignment and x != y:
                    if value in self.domains[self.variable_index_dict[y]]:
                        current_count += 1
            new_domain_of_tuples.append((value, current_count))
            current_count = 0
        
        new_domain_of_tuples.sort(key=self.get_second)
        new_domain = []
        for value_count_tuple in new_domain_of_tuples:
            new_domain.append(value_count_tuple[0])
        return new_domain


    def check_constraints(self, x, y, assignment):
        return True