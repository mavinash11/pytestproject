import logging


class Util:
    def verify_item_is_added_to_the_cart(self, item_name, elements_list):
        result = False
        for child in elements_list:
            # logging.info(dir(child))
            logging.info(child.id)
            logging.info(child.text)
            if item_name in child.text:
                result = True
            # logging.info(child.get_property)
            # child_1 = child.find_element(By.XPATH, "//span[@class ='cart_item']")
            # logging.info(child_1.text)
        return result

    def log_handling(logLevel=logging.DEBUG):
        logger = logging.getLogger(__name__)

        logger.setLevel(logLevel)
        # console handler
        ch = logging.StreamHandler()
        # File handler
        fh = logging.FileHandler("../reports/demolog.log")

        # Formatter
        formatter = logging.Formatter("%(asctime)s - %(name)s: %(levelname)s: %(funcName)s - %(message)s")
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)

        # Logger add handler
        logger.addHandler(ch)
        logger.addHandler(fh)
        return logger

