import sys
class NetworkNode:
    def __init__(self, name):
        self.name = name
        self.routing_table = {} # Destination -> (cost, next_hop)
        self.neighbor_nodes = []
    def add_neighbor(self, neighbor, cost):
        self.routing_table[neighbor] = (cost, neighbor)
        self.neighbor_nodes.append(neighbor)
    def update_routing_table(self):
        updated = False
        for neighbor in self.neighbor_nodes:
            for dest, (cost, next_hop) in neighbor.routing_table.items():
                new_cost = self.routing_table.get(neighbor, (sys.maxsize, None))[0] + cost
                if new_cost < self.routing_table.get(dest, (sys.maxsize, None))[0]:
                    self.routing_table[dest] = (new_cost, neighbor)
                    updated = True
                return updated
    def print_routing_table(self):
        print(f"Routing Table for Node {self.name}:")
        for dest, (cost, next_hop) in self.routing_table.items():
            print(f" Destination: {dest.name}, Cost: {cost}, Next Hop: {next_hop.name}")

def main():
 A = NetworkNode("A")
 B = NetworkNode("B")
 C = NetworkNode("C")
 D = NetworkNode("D")
 A.add_neighbor(B, 1)
 A.add_neighbor(C, 3)
 B.add_neighbor(A, 1)
 B.add_neighbor(C, 1)
 C.add_neighbor(A, 3)
 C.add_neighbor(B, 1)
 C.add_neighbor(D, 2)
 D.add_neighbor(C, 2)
 nodes = [A, B, C, D]
 iteration = 0
 updated = True
 while updated:
    print(f"Iteration {iteration}:")
    updated = False
    for node in nodes:
        updated |= node.update_routing_table()
        node.print_routing_table()
    
    iteration += 1
if __name__ == "__main__":
 main()