import logging
logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)
handler = logging.FileHandler("logs/pointsman.log", mode="w")
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)


log.info("TESTDEBUT")