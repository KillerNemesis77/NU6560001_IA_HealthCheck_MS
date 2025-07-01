"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                         Health Check Microservice                          ║
║                                                                            ║
║  main.py                                                                   ║
║                                                                            ║
║  Microservicio Python ultra-ligero y robusto para monitoreo de sistemas.   ║
║  Expone un endpoint RESTful (/health) que responde en JSON el estado       ║
║  de salud del sistema, ideal para integraciones con orquestadores,         ║
║  balanceadores y plataformas cloud-native.                                 ║
║                                                                            ║
║  Incluye:                                                                  ║
║   - Documentación Swagger automática                                       ║
║   - Logging profesional                                                    ║
║   - Manejo global de errores                                               ║
║   - CORS listo para microservicios modernos                                ║
║                                                                            ║
║  Powered by Flask + Clean Architecture                                     ║
║                                                                            ║
║  Auhor Dev: Mateo Cruz Oviedo                                                    ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

import os
import logging
from flask import Flask, jsonify
from flasgger import Swagger
from flask_cors import CORS
from app.api.health_check import health_check

def create_app():
    """
    Inicializa y configura el microservicio Flask con Swagger, CORS y logging.
    """
    app = Flask(__name__)
    app.config['SWAGGER'] = {
        'title': 'Health Check Microservice',
        'uiversion': 3
    }
    Swagger(app)
    CORS(app)

    # Logging profesional
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    @app.route('/health', methods=['GET'])
    def health():
        """
        Health Check Endpoint
        ---
        responses:
          200:
            description: Returns the health status
            schema:
              type: object
              properties:
                status:
                  type: string
                  example: healthy
        """
        logger.info("Health check requested")
        return health_check()

    # Manejo global de errores
    @app.errorhandler(Exception)
    def handle_exception(e):
        logger.error(f"Unhandled exception: {e}")
        return jsonify({"error": "Internal server error"}), 500

    return app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)