import random
import simpy

class CounterServiceSimulation:
    def __init__(self, env, num_counters, num_customers):
        self.env = env
        self.counter = simpy.Resource(env, capacity=num_counters)
        self.num_customers = num_customers

    def customer(self, name):
        print(f"{name} arrived at time {self.env.now}")
        with self.counter.request() as request:
            yield request
            print(f"{name} starts being served at time {self.env.now}")
            yield self.env.timeout(random.uniform(1, 3))
            print(f"{name} finished being served at time {self.env.now}")

    def run(self):
        for i in range(self.num_customers):
            self.env.process(self.customer(f"Customer {i+1}"))

def main():
    num_counters = 2
    num_customers = 5
    env = simpy.Environment()

    simulation = CounterServiceSimulation(env, num_counters, num_customers)
    simulation.run()

if __name__ == "__main__":
    main()
