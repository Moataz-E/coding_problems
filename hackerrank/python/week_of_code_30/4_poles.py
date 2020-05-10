import copy


class Pole(object):
    def __init__(self, altitude, weight):
        self.altitude = altitude
        self.weight = weight

    def calc_cost(self, new_altitude):
        if new_altitude > self.altitude:
            raise ValueError("Poles can only be moved to lower altitude.")
        return self.weight * (self.altitude - new_altitude)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.altitude == other.altitude) and (self.weight == other.weight)
        return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.altitude, self.weight))


def generate_permutations(poles, stacks):
    """Generates all possible stack permutations for poles.

    For n poles and s stacks, a given stack will contain at most (n-s)+1 poles.

    Args:
        poles: list containing the Pole objects we want to permute
        stacks: number of stacks in the problem space.

    Returns:
        List of lists where each list is a possible arrangement of poles in stacks.
    """
    permutations = []
    max_poles = (len(poles) - stacks) + 1

    # Initial arrangement is every stack contains at least one pole except for the last stack which
    # will contain all the remaining poles.
    arrangement = []
    for i in range(stacks):
        if i == (stacks-1):
            arrangement.append(poles[i:])
        else:
            arrangement.append([poles[i]])
    permutations.append(copy.deepcopy(arrangement))

    # Generate the remaining possible permutations using the initial arrangement as a start.
    stack = stacks - 1  # stack currently under processing
    while len(arrangement[0]) < max_poles:
        while len(arrangement[stack]) > 1:
            arrangement[stack-1].append(arrangement[stack][0])
            arrangement[stack].pop(0)
            permutations.append(copy.deepcopy(arrangement))
            sub_poles = [pole for pole in poles if pole not in arrangement[stack]]
            sub_permutations = [.append(arrangement)]
            permutations.append(generate_permutations(sub_poles, stack))
        stack -= 1

    return permutations


def cheapest_arrangement(poles_permutations):
    """Returns the cost of the cheapest arrangement of poles.

    Args:
        poles_permutations: list of sets where each set is an arrangement permutation.

    Returns:
        float representing cost of cheapest arrangement of poles.
    """
    minimum_cost = float('inf')
    for permutation in poles_permutations:
        cost = 0
        for stack in permutation:
            lowest_altitude = min(pole.altitude for pole in stack)
            cost += sum(pole.calc_cost(lowest_altitude) for pole in stack)
        minimum_cost = min(minimum_cost, cost)
    return minimum_cost


if __name__ == '__main__':
    num_poles, num_stacks = input().strip().split(' ')
    num_poles, num_stacks = [int(num_poles), int(num_stacks)]

    poles = []
    for a0 in range(num_poles):
        x_i, w_i = input().strip().split(' ')
        x_i, w_i = [int(x_i),int(w_i)]
        pole = Pole(x_i, w_i)
        poles.append(pole)
    poles = poles[::-1]

    if num_poles < 1 or num_poles > 5000:
        raise ValueError("Constraint breached! Number of poles should be between 1 and 5000.")

    if num_stacks < 1 or num_stacks > 5000:
        raise ValueError("Constraint breached! Number of stacks should be between 1 and 5000.")

    if num_poles < num_stacks:
        raise ValueError("Each stack must contain at least one pole!")

    permutations = generate_permutations(poles, num_stacks)
    min_cost = cheapest_arrangement(permutations)
    print(min_cost)
