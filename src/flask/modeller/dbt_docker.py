import docker
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class docker_dbt:
    def __init__(self):
        self.docker_client = docker.from_env()

    def run_dbt_test(self):
        container = self.docker_client.containers.get("intalgo-dbt")
        container.start()
        output = container.exec_run("dbt test --project-dir src/dbt/intalgo", detach=True)
        container.stop()
        log.info(f"OUTPUT: {output}")
        return self.get_logs(container)

    def get_logs(self, container):
        return container.logs()
