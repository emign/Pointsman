import logging
import yaml
from tariffapis.tibber import Tibber


def launch():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)
    handler = logging.FileHandler("logs/pointsman.log", mode="w")
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    log.addHandler(handler)

    with open("config.yaml", "r") as f:    
        config = yaml.safe_load(f)
        log.debug("Reading config file")
        log.debug(config)

    # TIBBER PREISE ABHOLEN

    tariff = Tibber(config['apis']['tibber']['key'])
    log.info(tariff.get_current_price())


launch()