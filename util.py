class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []
        self.explored_states = set()

    def add(self, node):
        self.frontier.append(node)

    def explore(self, person_id):
        self.explored_states.add(person_id)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def is_explored(self, person_id):
        return any(person_id == explored_person_id for explored_person_id in self.explored_states)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
