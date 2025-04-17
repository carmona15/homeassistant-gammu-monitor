from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_HOST, CONF_PORT
import requests

class GammuMonitorSensor(Entity):
    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._name = "Gammu Monitor Sensor"
        self._state = None

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

    def update(self):
        response = requests.get(f"http://{self._host}:{self._port}/status")
        data = response.json()
        self._state = data.get("signal")
