import asyncio
import logging
from datetime import timedelta

import aiohttp
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

class GammuMonitorCoordinator(DataUpdateCoordinator):
    def __init__(self, hass: HomeAssistant, host: str, port: int, scan_interval: int):
        """Inicializa el coordinador."""
        self.host = host
        self.port = port
        self.base_url = f"http://{host}:{port}"
        self.session = aiohttp.ClientSession()

        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=scan_interval),
        )

    async def _async_update_data(self):
        """Actualiza los datos del API de Gammu."""
        try:
            async with self.session.get(f"{self.base_url}/status") as response:
                if response.status != 200:
                    raise UpdateFailed(f"Error en la respuesta del servidor: {response.status}")
                return await response.json()
        except asyncio.TimeoutError as err:
            raise UpdateFailed(f"Timeout al conectar con {self.base_url}") from err
        except aiohttp.ClientError as err:
            raise UpdateFailed(f"Error de conexión con {self.base_url}") from err

    async def async_close(self):
        """Cierra la sesión HTTP al apagar."""
        await self.session.close()
