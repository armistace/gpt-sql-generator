import docker
import logging
import re
from markupsafe import Markup, escape
import os

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class docker_dbt:
    def __init__(self):
        self.docker_client = docker.from_env()

    def run_full_dbt(self):
        return self.container_exec("dbt build --project-dir src/dbt/intalgo")

    def run_dbt_test(self):
        return self.container_exec("dbt test --project-dir src/dbt/intalgo")

    def container_exec(self, command):
        '''
            Accepts a command as a string
            Assume only called from within class but could in 
            theory be called from in app if command isn't programmed
            or to complex
            returns the logs as output by get_logs
        '''
        container_name = os.getenv("INTALGO_DBT_CONTAINER")
        log.info(f"Using Container Name: {container_name}")
        log.info(f"Running Command: {command}")
        container = self.docker_client.containers.run(container_name, command, detach=True)
        log.info("Container has run")
        log.info(container.logs(stream=True))
        logs_string = self.get_logs(container)
        return logs_string

    def get_logs(self, container):
        '''
            performs the markup magic to make the logs string return
            in a way that flask doesn't bitch at
        '''
        log.info("Entered Get Logs")
        logs = b""
        for line in container.logs(stream=True):
            logs = logs + line
        return Markup("<br>".join(re.split(r'(?:\r\n|\r|\n)', \
                escape(''.join(map(chr, logs))))))

    
