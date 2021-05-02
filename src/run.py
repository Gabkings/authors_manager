
from main import create_app
from api.config.config import DevelopmentConfig, ProductionConfig
import os



if __name__ == "__main__":
    if os.environ.get('WORK_ENV') == 'PROD':
        app_config = ProductionConfig
    else:
        app_config = DevelopmentConfig
    application = create_app(app_config)
    application.run(port=5000, host="0.0.0.0", use_reloader=False)