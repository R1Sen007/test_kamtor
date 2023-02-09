import logging
import time
import settings
from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient


class Client():
    def __init__(self):
        self.client = UMFuturesWebsocketClient()
        self.client.start()
    
    def subscribe_to_coin(self, symbol, interval):
        self.client.kline(
            symbol=symbol,
            id=1,
            interval=interval,
            callback= message_handler,
        )

        if settings.TIME_TO_KILL > 0:
            time.sleep(10)
            logging.debug("closing ws connection")
            self.client.stop()


def message_handler(message):
    try:
        high = float(message.get("k").get("h"))
        closed = float(message.get("k").get("c"))        
        percent = (closed - high) / high * 100

        if abs(percent) > settings.DIFF_IN_PERCENT:
            logging.info(f"PRICE CHANGE ON: {percent} %")
    except:
        logging.error("NO DATA IN MESSAGE!")
    
