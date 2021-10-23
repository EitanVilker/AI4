from ConstraintSatisfactionProblem import ConstraintSatisfactionProblem
import numpy as np

class CircuitBoardProblem(ConstraintSatisfactionProblem):

    def __init__(self, variables, domains, constraints, board_width, board_height):

        self.variables = variables
        self.domains = domains
        self.constraints = constraints
        self.variable_index_dict = {}
        for i in range(len(self.variables)):
            self.variable_index_dict[self.variables[i]] = i
        self.board_width = board_width
        self.board_height = board_height
        self.add_domains()
        self.assignment = None
        self.assignments_tried = 0

    def add_domains(self):

        for i in range(len(self.variables)):
            self.domains.append([])
            for j in range(self.board_width):
                for k in range(self.board_height):
                    self.domains[i].append((j, k))

        for i in range(len(self.variables)):
            indices_to_remove = []
            width = self.constraints[self.variables[i]][0]
            height = self.constraints[self.variables[i]][1]
            for j in range(len(self.domains[i])):
                if self.domains[i][j][0] + width > self.board_width:
                    indices_to_remove.append(self.domains[i][j])
                elif self.domains[i][j][1] + height > self.board_height:
                    indices_to_remove.append(self.domains[i][j])
            for index in indices_to_remove:
                self.domains[i].remove(index)

    def check_constraints(self, x, y, assignment):

        if x == y:
            return True

        if x not in assignment or y not in assignment:
            return True

        # Check if overlapping
        x_0 = assignment[x][0]
        x_1 = assignment[x][1]
        y_0 = assignment[y][0]
        y_1 = assignment[y][1]
        x_width = self.constraints[x][0]
        x_height = self.constraints[x][1]
        y_width = self.constraints[y][0]
        y_height = self.constraints[y][1]

        if (x_0 + x_width > y_0 and x_0 <= y_0) or (y_0 + y_width > x_0 and y_0 <= x_0):
            if (x_1 + x_height > y_1 and x_1 <= y_1) or (y_1 + y_height > x_1 and y_1 <= x_1):
                return False
        return True

    def draw_assignment(self):

        matrix = np.zeros(shape=(self.board_height, self.board_width))

        for variable in self.variables:
            left_pos = self.assignment[variable][0]
            down_pos = self.assignment[variable][1]
            for i in range(constraints[variable][0]):
                for j in range(constraints[variable][1]):
                    matrix[self.board_height - down_pos - j - 1][i + left_pos] = int(variable)
        print(matrix)

# Set up problem
# variables = ["1", "2", "3", "4"]
# domains = []
# constraints = {}
# constraints["1"] = (3, 2)
# constraints["2"] = (5, 2)
# constraints["3"] = (2, 3)
# constraints["4"] = (7, 1)
# board_width = 10
# board_height = 3

# variables = ["1", "2"]
# domains = []
# constraints = {}
# constraints["1"] = (3, 2)
# constraints["2"] = (3, 1)
# board_width = 3
# board_height = 3

variables = ["1", "2", "3", "4", "5", "6", "7", "8"]
domains = []
constraints = {}
constraints["1"] = (10, 1)
constraints["2"] = (3, 4)
constraints["3"] = (3, 2)
constraints["4"] = (3, 3)
constraints["5"] = (3, 2)
constraints["6"] = (2, 2)
constraints["7"] = (6, 1)
constraints["8"] = (8, 2)
board_width = 10
board_height = 8

cbp = CircuitBoardProblem(variables, domains, constraints, board_width, board_height)
cbp.backtracking_search(heuristic="degree")
cbp.draw_assignment()
print("Assignments tried: " + str(cbp.assignments_tried))