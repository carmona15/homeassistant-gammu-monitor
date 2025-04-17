from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_PORT
from .const import DOMAIN, CONF_SCAN_INTERVAL
import voluptuous as vol

@config_entries.HANDLERS.register(DOMAIN)
class GammuMonitorConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Gammu Monitor."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Gammu Monitor", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({
                vol.Required(CONF_HOST, default="localhost"): str,
                vol.Required(CONF_PORT, default=5555): int,
                vol.Optional(CONF_SCAN_INTERVAL, default=30): int,
            }),
        )
