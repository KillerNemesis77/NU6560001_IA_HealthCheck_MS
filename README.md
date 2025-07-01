# Python Microservice

This is a simple Python microservice that implements a health check endpoint following clean architecture principles.

## Project Structure

```
python-microservice
├── src
│   └── app
│       ├── __init__.py
│       ├── main.py
│       ├── api
│       │   ├── __init__.py
│       │   └── health_check.py
│       ├── domain
│       │   └── __init__.py
│       ├── services
│       │   └── __init__.py
│       └── infrastructure
│           └── __init__.py
├── tests
│   ├── unit
│   │   └── test_health_check.py
│   ├── acceptance
│   │   └── test_health_check_acceptance.py
│   ├── e2e
│   │   └── test_health_check_acceptance.py
│   └── performance
│       └── test_health_check_benchmark.py
├── requirements.txt
├── README.md
├── pyproject.toml
├── Dockerfile
└── .github
    └── workflows
        └── ci.yml
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-microservice
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the microservice, execute the following command:
```
python src/app/main.py
```

The health check endpoint will be available at `http://localhost:5000/health`.

## Calidad y pruebas

Este proyecto incluye diferentes tipos de pruebas para asegurar la calidad y el correcto funcionamiento del microservicio:

- **Pruebas unitarias:** Validan el comportamiento de funciones o componentes individuales de forma aislada.
  - Ejecuta:  
    ```sh
    $env:PYTHONPATH="src"
    python -m pytest tests/unit
    ```
- **Pruebas de aceptación:** Verifican que el sistema cumple los requisitos funcionales desde el punto de vista del usuario.
  - Ejecuta:  
    ```sh
    $env:PYTHONPATH="src"
    python -m pytest tests/acceptance
    ```
- **Pruebas end-to-end (E2E):** Simulan peticiones reales al microservicio para validar el flujo completo, como lo haría un cliente externo.
  - Asegúrate de tener el microservicio corriendo (`python src/app/main.py`).
  - Ejecuta:  
    ```sh
    pytest tests/e2e
    ```
- **Pruebas de performance:** Evalúan el rendimiento del endpoint `/health` usando `pytest-benchmark`.
  - Ejecuta:  
    ```sh
    $env:PYTHONPATH="src"
    pytest tests/performance
    ```
- **Pruebas de smoke:** Incluidas en las pruebas de aceptación y E2E, validan que el servicio responde correctamente.

- **Cobertura de código:** (Opcional)  
  Ejecuta:
  ```sh
  pytest --cov=src/app tests/
  ```

> **Nota:**  
> En Linux/MacOS, reemplaza la variable de entorno por:
> ```sh
> export PYTHONPATH=src
> python -m pytest tests/unit
> ```

### ¿Qué hace cada tipo de prueba?

- **Unitarias:** Comprueban funciones internas de manera aislada.
- **Aceptación:** Validan que el endpoint responde correctamente según los requisitos.
- **E2E:** Simulan el uso real del microservicio desde el exterior.
- **Performance:** Miden la velocidad y capacidad de respuesta del endpoint.
- **Smoke:** Verifican que el servicio está "vivo" y responde.

---

## Quick Start

1. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
2. Ejecuta el microservicio:
   ```
   python src/app/main.py
   ```
3. Accede a [http://localhost:5000/health](http://localhost:5000/health)
4. Documentación Swagger en [http://localhost:5000/apidocs](http://localhost:5000/apidocs)


## Arquitectura (Diagrama)

```
+-------------------+         HTTP GET /health         +-----------------------------+
|                   |  ----------------------------->  |                             |
|  Cliente/Monitor  |                                  |  Python Microservicio Flask |
|  (Orquestador,    |  <-----------------------------  |  (Clean Architecture)      |
|   Balanceador,    |         JSON: {"status": ...}    |                             |
|   etc.)           |                                  |  - API Layer (/health)      |
|                   |                                  |  - Domain Layer             |
|                   |                                  |  - Services Layer           |
|                   |                                  |  - Infrastructure Layer     |
|                   |                                  |  - Swagger UI (/apidocs)    |
+-------------------+                                  +-----------------------------+
```

La arquitectura del proyecto sigue el patrón de **arquitectura limpia (Clean Architecture)**, promoviendo la separación de responsabilidades y facilitando la mantenibilidad, escalabilidad y testabilidad del sistema.

**Componentes principales:**

- **API Layer (`api/`)**: Expone los endpoints HTTP (por ejemplo, `/health`). Aquí se definen los controladores que reciben las solicitudes y devuelven las respuestas.
- **Domain Layer (`domain/`)**: Contiene la lógica de negocio central. En este caso, la lógica es simple, pero este módulo permite crecer el sistema sin acoplarlo a frameworks.
- **Services Layer (`services/`)**: Implementa la lógica de aplicación, orquestando la interacción entre el dominio y la infraestructura.
- **Infrastructure Layer (`infrastructure/`)**: Gestiona la interacción con recursos externos (bases de datos, servicios externos, etc.). En este microservicio, puede estar vacío o preparado para futuras integraciones.
- **Tests (`tests/`)**: Incluye pruebas unitarias y de aceptación para asegurar la calidad y el correcto funcionamiento del microservicio.

**Flujo de la solicitud:**

1. El cliente o sistema de monitoreo realiza una petición HTTP GET al endpoint `/health`.
2. El controlador en la capa API recibe la solicitud y delega la lógica a la función correspondiente.
3. La función retorna el estado de salud del sistema en formato JSON.
4. El controlador responde al cliente con el estado y el código HTTP adecuado.

**Ventajas de esta arquitectura:**

- Permite escalar y modificar el microservicio fácilmente.
- Facilita la realización de pruebas unitarias y de integración.
- Separa la lógica de negocio de los detalles de infraestructura

## License

This project is licensed under the MIT License.

## Despliegue con Docker/Podman/WSL

Puedes ejecutar el microservicio en un contenedor usando Docker o Podman:

1. **Construye la imagen:**
   ```sh
   docker build -t health-check-service .
   ```
   o con Podman:
   ```sh
   podman build -t health-check-service .
   ```

2. **Ejecuta el contenedor:**
   ```sh
   docker run -d -p 5000:5000 health-check-service
   ```
   o con Podman:
   ```sh
   podman run -d -p 5000:5000 health-check-service
   ```

3. **Verifica el endpoint:**
   Abre en tu navegador o usa curl:
   ```
   http://localhost:5000/health
   ```

> **Nota:** Si usas WSL, asegúrate de tener Docker Desktop o Podman Desktop instalado y corriendo.

---

### Ejemplo de nombre de rama y repositorio

````markdown
## Estandar de ramas y repositorio

- **Repositorio:** `NU6560001_IA_HealthCheck_MS`
- **Rama de feature:** `feature/health-check-endpoint`
- **Rama de release:** `release/v1.0.0`
`````