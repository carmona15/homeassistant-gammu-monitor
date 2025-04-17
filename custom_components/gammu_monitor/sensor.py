from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import DOMAIN

SENSOR_TYPES = {
    "imei": {"name": "IMEI", "unit": None},
    "imsi": {"name": "IMSI", "unit": None},
    "sent": {"name": "SMS Enviados", "unit": "sms"},
    "received": {"name": "SMS Recibidos", "unit": "sms"},
    "failed": {"name": "SMS Fallidos", "unit": "sms"},
    "signal": {"name": "Señal GSM", "unit": "%"},
}


async def async_setup_entry(hass, config_entry, async_add_entities):
    coordinator = hass.data[DOMAIN][config_entry.entry_id]
    entities = []

    for key, description in SENSOR_TYPES.items():
        entities.append(GammuMonitorSensor(coordinator, key, description))

    async_add_entities(entities, update_before_add=True)


class GammuMonitorSensor(CoordinatorEntity, SensorEntity):
    def __init__(self, coordinator, key, description):
        super().__init__(coordinator)
        self._key = key
        self._attr_name = f"Gammu {description['name']}"
        self._attr_unique_id = f"{coordinator.host}_{key}"
        self._attr_native_unit_of_measurement = description["unit"]

    @property
    def native_value(self):
        return self.coordinator.data.get(self._key)
