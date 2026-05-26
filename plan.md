App de prueba para Reverse Proxy

Puerto ocupado por esta app:
- Frontend: http://192.168.2.5:5099

Configuracion en Synology Reverse Proxy:
- Origen: test.scm
- Destino: http://localhost:5099

Resultado esperado:
- https://test.scm muestra "Hola mundo"

Comandos en el NAS:

```bash
docker compose up -d
docker ps
```
