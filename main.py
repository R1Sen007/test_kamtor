import logging
from Client import Client
import settings
from binance.lib.utils import config_logging
# from binance.websocket.um_futures.websocket_client import UMFuturesWebsocketClient




# def message_handler(message):
#     try:
#         high = float(message.get("k").get("h"))
#         closed = float(message.get("k").get("c"))
#         print("HIGH: ", high, " , CLOSED: ", closed)
#         print("DIFF IN %: ", (closed - high) / high * 100)
#     except:
#         logging.error("NO DATA IN MESSAGE!")


if __name__ == "__main__":
#     my_client = UMFuturesWebsocketClient()
#     my_client.start()

#     my_client.kline(
#         symbol=settings.SYMBOL,
#         id=1,
#         interval=settings.INTERVAL,
#         callback=message_handler,
#     )

#     time.sleep(10)

#     logging.debug("closing ws connection")
#     my_client.stop()
    config_logging(logging, logging.DEBUG)
    client = Client()
    client.subscribe_to_coin(settings.SYMBOL, settings.INTERVAL)