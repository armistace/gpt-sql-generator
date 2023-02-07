import docker

class docker_dbt:
    docker_client = docker.from_env()

    def run_dbt_test(self):
        container = self.docker_client.run("intalgo-app_intalgo-dbt:latest","dbt test --project-dir src/dbt/intalgo", detach=True)
        return get_logs(container)

    def get_logs(container):
        return container.logs()
