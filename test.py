import random

# Given parameters
order_cost = 100
holding_cost = 5
initial_inventory_level = 8
demand_distribution = [0, 1, 2, 3, 4]  # Example demand distribution
lead_time_distribution = [1, 2, 3, 4, 5]  # Example lead time distribution


def simulate_inventory_system(order_quantity, reorder_point, num_periods=12):
    total_orders_placed = 0
    total_ordering_cost = 0
    total_holding_cost = 0
    total_sales_lost = 0
    inventory_level = initial_inventory_level
    total_cost = 0

    for period in range(num_periods):
        # Check if an order needs to be placed
        if period == 0 or inventory_level <= reorder_point:
            order = order_quantity
            total_orders_placed += 1
            total_ordering_cost += order_cost
        else:
            order = 0

        # Simulate demand and lead time
        demand = random.choice(demand_distribution)

        # Update inventory levels based on demand and order
        if demand <= inventory_level:
            inventory_level -= demand
            total_holding_cost += inventory_level * holding_cost
        elif demand > inventory_level:
            lead_time = random.choice(lead_time_distribution)
            inventory_level = inventory_level
            total_holding_cost += inventory_level * holding_cost

            # Check if stockout occurred during lead time
            if (num_periods - period) == lead_time:
                inventory_level += 5

        # Calculate costs
        total_cost += order_cost + total_holding_cost

    return {
        "total_orders_placed": total_orders_placed,
        "total_ordering_cost": total_ordering_cost,
        "total_holding_cost": total_holding_cost,
        "total_sales_lost": total_sales_lost,
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
#print(f"Total Sales Lost: {best_results['total_sales_lost']}")
