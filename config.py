#!/usr/bin/env python3

import os
from datetime import timedelta


class Config:

    DB_USERNAME = os.getenv('DB_USERNAME', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'root')
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DEV_DB_NAME = os.getenv('DEV_DB_NAME', 'SOVS')
    TEST_DB_NAME = os.getenv('TEST_DB_NAME', 'TEST_SOVS')
    PROD_DB_NAME = os.getenv('PROD_DB_NAME', 'PROD_SOVS')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUBJECT_PREFIX = '[secure_online_voting_system]'
    MAIL_SENDER = os.environ.get(
        'MAIL_SENDER',
        'secure_online_voting_system Admin <youssefessam5623@gmail.com>'
    )
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)

    # Added to fix the collation issue
    SQLALCHEMY_ENGINE_OPTIONS = {
        'connect_args': {
            'charset': 'utf8mb4',
            'collation': 'utf8mb4_unicode_ci'
        }
    }

    @staticmethod
    def init_app(app):
        """
        Initialize the application with the provided configuration.

        This method is a placeholder for any initialization steps required
        for the app when a specific configuration is applied.

        Parameters:
        -----------
        app : Flask app instance
            The Flask application instance to be initialized.
        """
        pass


class DevelopmentConfig(Config):
    """
    Development configuration class.

    This class inherits from the base Config class and overrides specific
    settings for development purposes, such as enabling debug mode and
    setting a shorter JWT expiration time.

    Attributes:
    -----------
    DEBUG : bool
        Enables or disables debug mode (default: True).
    SQLALCHEMY_DATABASE_URI : str
        The database URI for the development environment.
    JWT_ACCESS_TOKEN_EXPIRES : timedelta
        The expiration time for JWT access tokens in development (default: 12 hours).
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}'
        f'@{Config.DB_HOST}:{Config.DB_PORT}/{Config.DEV_DB_NAME}'
    )
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12)


class TestConfig(Config):
    """
    Testing configuration class.

    This class inherits from the base Config class and overrides specific
    settings for testing purposes, such as enabling testing mode and
    setting the database URI for testing.

    Attributes:
    -----------
    TESTING : bool
        Enables or disables testing mode (default: True).
    SQLALCHEMY_DATABASE_URI : str
        The database URI for the testing environment.
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}'
        f'@{Config.DB_HOST}:{Config.DB_PORT}/{Config.TEST_DB_NAME}'
    )


class ProductionConfig(Config):
    """
    Production configuration class.

    This class inherits from the base Config class and overrides specific
    settings for production purposes, such as setting the database URI for
    the production environment and a longer JWT expiration time.

    Attributes:
    -----------
    SQLALCHEMY_DATABASE_URI : str
        The database URI for the production environment.
    JWT_ACCESS_TOKEN_EXPIRES : timedelta
        The expiration time for JWT access tokens in production (default: 7 days).
    """
    SQLALCHEMY_DATABASE_URI = (
        f'mysql+mysqlconnector://{Config.DB_USERNAME}:{Config.DB_PASSWORD}'
        f'@{Config.DB_HOST}:{Config.DB_PORT}/{Config.PROD_DB_NAME}'
    )
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=7)


config = {
    'development': DevelopmentConfig,
    'testing': TestConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}