from homeassistant import config_entries
from homeassistant.core import callback
import voluptuous as vol

from .const import DOMAIN

class GammuMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Gammu Monitor."""

    VERSION = 1

    def __init__(self):
        self._host = None
        self._port = None
        self._interval = None

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Gammu Monitor", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required("host", default="localhost"): str,
                vol.Required("port", default=5555): int,
                vol.Optional("interval", default=30): int,
            }),
            errors=errors,
        )
