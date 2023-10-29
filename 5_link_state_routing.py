# Create a dictionary to represent the routers and their links with associated costs
routers = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 2},
    'C': {'B': 2},
}

# Create a dictionary to store routing tables for each router
routing_tables = {router: {} for router in routers}

# Initialize routing tables with direct neighbors
for router, links in routers.items():
    routing_tables[router] = {neighbor: (cost, neighbor) for neighbor, cost in links.items()}

# Function to update routing tables
def update_routing_tables():
    for router in routers:
        for destination in routers:
            if router != destination:
                for neighbor in routers[router]:
                    cost_to_neighbor = routing_tables[router][neighbor][0]
                    if destination in routing_tables[neighbor]:
                        total_cost = cost_to_neighbor + routing_tables[neighbor][destination][0]
                        if destination not in routing_tables[router] or total_cost < routing_tables[router][destination][0]:
                            routing_tables[router][destination] = (total_cost, neighbor)

# Update routing tables until they converge
old_routing_tables = None
while routing_tables != old_routing_tables:
    old_routing_tables = {router: table.copy() for router, table in routing_tables.items()}
    update_routing_tables()

# Display routing tables
for router, table in routing_tables.items():
    print(f"Routing Table for Router {router}:")
    for destination, (cost, next_hop) in table.items():
        print(f"  Destination: {destination}, Cost: {cost}, Next Hop: {next_hop}")
