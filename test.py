import random

# Given parameters
order_cost = 100
holding_cost = 5
initial_inventory_level = 8
demand_distribution = [10, 20, 30, 40, 50]  # Example demand distribution
lead_time_distribution = [2, 3, 4, 5]  # Example lead time distribution


def simulate_inventory_system(order_quantity, reorder_point, num_periods=12):
    total_orders_placed = 0
    total_ordering_cost = 0
    total_holding_cost = 0
    total_orders_lost = 0
    inventory_level = initial_inventory_level
    total_cost = 0

    for period in range(num_periods):
        # Check if an order needs to be placed
        if inventory_level <= reorder_point:
            order = order_quantity
            total_orders_placed += 1
            total_ordering_cost += order_cost
        else:
            order = 0

        # Simulate demand and lead time
        demand = random.choice(demand_distribution)
        lead_time = random.choice(lead_time_distribution)

        # Update inventory levels
        if inventory_level >= demand:
            inventory_level -= demand
            total_holding_cost += inventory_level * holding_cost
        else:
            total_holding_cost += inventory_level * holding_cost
            inventory_level = 0

            # Check if stockout occurred during lead time
            if period <= lead_time:
                inventory_level += 5

            if inventory_level < demand:
                total_orders_lost += demand

        total_cost += order_cost + total_holding_cost

    return {
        "total_orders_placed": total_orders_placed,
        "total_ordering_cost": total_ordering_cost,
        "total_holding_cost": total_holding_cost,
        "total_orders_lost": total_orders_lost,
        "total_cost": total_cost
    }


# Main code to examine different order quantities and reorder points
best_policy = None
min_total_cost = float('inf')

for order_quantity in range(4, 11):
    for reorder_point in range(3, 7):
        results = simulate_inventory_system(order_quantity, reorder_point)
        total_cost = results["total_cost"]

        # Find the best policy that minimizes total cost
        if total_cost < min_total_cost:
            min_total_cost = total_cost
            best_policy = (order_quantity, reorder_point, results)

# Print the results for the best policy
best_order_quantity, best_reorder_point, best_results = best_policy
print(f"Best Policy: Order Quantity = {best_order_quantity}, Reorder Point = {best_reorder_point}")
print(f"Minimum Total Cost: {min_total_cost:.2f}")
print(f"Number of Orders Placed: {best_results['total_orders_placed']}")
print(f"Total Ordering Cost: {best_results['total_ordering_cost']:.2f}")
print(f"Total Holding Cost: {best_results['total_holding_cost']:.2f}")
print(f"Total Orders Lost: {best_results['total_orders_lost']}")
