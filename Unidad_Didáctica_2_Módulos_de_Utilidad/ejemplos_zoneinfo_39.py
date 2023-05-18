from zoneinfo import ZoneInfo
from datetime import datetime

# Creamos una fecha para la ciudad de México.
dt = datetime(2020, 10, 31, 13, tzinfo=ZoneInfo("America/Mexico_City"))
print(f"Fecha en Mexico {dt}")
print(f"Zona Horaria Mexico: {dt.tzname()}")

berlin = ZoneInfo('Europe/Berlin')
madrid = ZoneInfo('Europe/Paris')
losangeles = ZoneInfo('America/Los_Angeles')
# Modificamos la zona horaria
print(f"Fecha en Berlin {dt.astimezone(berlin)}")
print(f"Fecha en Madrid {dt.astimezone(madrid)}")
print(f"Fecha en Madrid {dt.astimezone(losangeles)}")