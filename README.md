# Gammu Monitor para Home Assistant

Este proyecto integra el monitoreo de Gammu SMSD en Home Assistant para mostrar el estado de los SMS enviados, recibidos, fallidos y la calidad de señal de la red GSM.

## Instalación

1. Instala la integración desde HACS.
2. Agrega la configuración en Home Assistant a través de la UI.

## API

La API REST disponible ofrece los siguientes endpoints:

- **GET /status**: Consulta el estado del monitor Gammu.
- **GET /ping**: Estado simple OK.

## Gammu SMSD

Versión recomendada de Gammu Monitor: **1.40.0**.
