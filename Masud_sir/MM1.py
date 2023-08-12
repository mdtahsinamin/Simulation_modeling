import numpy as np


def mm1_queue_simulation(arrival_rate, service_rate, max_customers):
    inter_arrival_time = np.random.exponential(scale=1 / arrival_rate)
    service_time = np.random.exponential(scale=1 / service_rate)

    arrival_time = inter_arrival_time
    departure_time = arrival_time + service_time

    queue = []
    total_delay = 0
    total_queue_length = 0
    total_service_time = service_time
    completed_customers = 1

    while completed_customers < max_customers:
        if arrival_time < departure_time:
            queue.append(arrival_time)
            inter_arrival_time = np.random.exponential(scale=1 / arrival_rate)
            arrival_time += inter_arrival_time
        else:
            total_delay += departure_time - queue.pop(0)
            total_service_time += service_time
            if queue:
                departure_time = departure_time + service_time
            else:
                departure_time = arrival_time + service_time
            completed_customers += 1

        if len(queue) == 0:
            departure_time = arrival_time + service_time

    avg_delay = total_delay / max_customers
    avg_queue_length = total_service_time / arrival_time
    server_utilization = total_service_time / (max_customers * service_time)

    print("Simulation ended at time:", departure_time)
    print("Average delay in queue:", avg_delay)
    print("Average number in queue:", avg_queue_length)
    print("Server utilization:", server_utilization)


if __name__ == "__main__":
    mean_inter_arrival_time = float(input("Enter mean inter-arrival time of customers: "))
    mean_service_time = float(input("Enter mean service time: "))
    max_customers = int(input("Enter maximum number of customers: "))

    mm1_queue_simulation(mean_inter_arrival_time, mean_service_time, max_customers)

'''
Average Delay in Queue: Sum of all customer delays divided by the total number of customers.
Average Number in Queue: Area under the queue length curve divided by the total simulation time.
Server Utilization: Total service time divided by the total simulation time.
Time Simulation Ended: The time at which the simulation loop terminates.


The average number in queue in an M/M/1 queue simulation is the average number of customers that are waiting in the queue to be served. It is calculated by dividing the total time that customers spend in the queue by the total number of customers that are served.
erver utilization in an M/M/1 queue simulation is the percentage of time that the server is busy serving customers
The average delay in queue in an M/M/1 queue simulation is the average amount of time that a customer spends waiting in the queue before being served. 
'''

