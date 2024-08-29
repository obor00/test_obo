import time

class JenkinsJobSimulator:
    def __init__(self):
        self.branches = {}

    def add_branch(self, branch_name):
        self.branches[branch_name] = {
            'status': 'Not started',
            'progress': 0
        }

    def simulate_job(self, branch_name):
        if branch_name not in self.branches:
            print(f"Branch '{branch_name}' not found.")
            return

        print(f"Starting Jenkins job simulation for branch '{branch_name}'...")
        self.branches[branch_name]['status'] = 'Running'

        for i in range(1, 11):
            self.branches[branch_name]['progress'] = i * 10
            print(f"Branch '{branch_name}' progress: {i * 10}%")
            time.sleep(1)

        self.branches[branch_name]['status'] = 'Completed'
        print(f"Branch '{branch_name}' Jenkins job simulation completed.")

    def merge_branch_to_master(self, branch_name):
        if branch_name not in self.branches:
            print(f"Branch '{branch_name}' not found.")
            return

        print(f"Merging '{branch_name}' into 'master'...")
        time.sleep(2)

        # Simulation de gestion de conflits (exemple simple)
        if branch_name == 'feature/branch1':
            print("Conflict detected. Manual resolution needed.")
            # Appeler une fonction de résolution de conflit ici
            time.sleep(2)
            print("Conflict resolved.")

        # Simulation de la fusion réussie
        print(f"Branch '{branch_name}' successfully merged into 'master'.")

    def get_branch_status(self, branch_name):
        return self.branches.get(branch_name, {}).get('status', 'Branch not found')

    def get_branch_progress(self, branch_name):
        return self.branches.get(branch_name, {}).get('progress', 0)

# Exemple d'utilisation
if __name__ == "__main__":
    jenkins_simulator = JenkinsJobSimulator()

    # Ajouter des branches à simuler
    jenkins_simulator.add_branch('master')
    jenkins_simulator.add_branch('feature/branch1')
    jenkins_simulator.add_branch('feature/branch2')

    # Simuler des jobs pour chaque branche
    jenkins_simulator.simulate_job('master')
    jenkins_simulator.simulate_job('feature/branch1')
    jenkins_simulator.simulate_job('feature/branch2')

    # Fusionner la branche 'feature/branch1' dans 'master'
    jenkins_simulator.merge_branch_to_master('feature/branch1')

    # Obtenir l'état et la progression d'une branche
    print("Status of 'master' branch:", jenkins_simulator.get_branch_status('master'))
    print("Progress of 'feature/branch1' branch:", jenkins_simulator.get_branch_progress('feature/branch1'))
