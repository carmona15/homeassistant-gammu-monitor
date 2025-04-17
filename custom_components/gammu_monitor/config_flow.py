from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
import requests

class GammuMonitorConfigFlow(config_entries.ConfigFlow):
    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            try:
                # Validate connection with the API
                response = requests.get(f"http://{user_input[CONF_HOST]}:{user_input[CONF_PORT]}/status")
                response.raise_for_status()
                return self.async_create_entry(title="Gammu Monitor", data=user_input)
            except requests.exceptions.RequestException:
                errors["base"] = "cannot_connect"
        return self.async_show_form(step_id="user", errors=errors)
