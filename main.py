import logging
from Client import Client
import settings
from binance.lib.utils import config_logging


if __name__ == "__main__":
    config_logging(logging, logging.DEBUG)
    client = Client()
    client.subscribe_to_coin(settings.SYMBOL, settings.INTERVAL)