import random
import time
import matplotlib.pyplot as plt

class IntegrationSimulator:
    def __init__(self, num_resources):
        self.num_resources = num_resources
        self.variants = []
        self.integration_times = []

    def add_variant(self, variant_name):
        self.variants.append(variant_name)

    def simulate_integration(self, functional_zones, num_branches, num_conflicts):
        print("Starting integration simulation...")
        time.sleep(1)

        integration_time = 0

        for zone in functional_zones:
            print(f"Integrating zone '{zone}'...")
            time.sleep(random.randint(1, 3))

        for i in range(num_branches):
            branch_name = f"branch{i+1}"
            print(f"Integrating branch '{branch_name}'...")
            time.sleep(random.randint(1, 3))

            if random.random() < num_conflicts / num_branches:
                print(f"Conflict detected in branch '{branch_name}'. Resolving...")
                time.sleep(random.randint(1, 3))
                print(f"Conflict in branch '{branch_name}' resolved.")

            integration_time += random.randint(1, 3)

        print("Integration completed.")
        time.sleep(1)
        self.integration_times.append(integration_time)

    def produce_variants(self):
        print("Producing different variants of the software...")
        time.sleep(1)

        for variant in self.variants:
            print(f"Producing variant: {variant}...")
            time.sleep(random.randint(2, 5))

        print("Production of all variants completed.")

    def plot_integration_times(self):
        plt.figure(figsize=(8, 6))
        plt.bar(range(1, len(self.integration_times) + 1), self.integration_times)
        plt.xlabel('Simulation Run')
        plt.ylabel('Integration Time (Days)')
        plt.title('Integration Time for Different Simulations')
        plt.show()

# Exemple d'utilisation
if __name__ == "__main__":
    simulator = IntegrationSimulator(num_resources=4)

    # Ajouter les différentes zones fonctionnelles
    functional_zones = ["zone1", "zone2", "zone3", "zone4"]
    
    # Faire varier le nombre de branches, de conflits et de variantes
    num_branches = random.randint(5, 10)
    num_conflicts = random.randint(1, num_branches)
    num_variants = random.randint(3, 5)

    # Ajouter les différentes variantes du logiciel
    for i in range(num_variants):
        variant_name = f"Variant{i+1}"
        simulator.add_variant(variant_name)

    # Lancer la simulation d'intégration
    simulator.simulate_integration(functional_zones, num_branches, num_conflicts)

    # Lancer la production des différentes variantes
    simulator.produce_variants()

    # Afficher le graphique des temps d'intégration
    simulator.plot_integration_times()
