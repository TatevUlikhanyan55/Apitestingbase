import logging

logging.basicConfig(filename='test_run.txt', format='%(asctime)s %(message)s',
                    level=logging.DEBUG)

#usually level is logging.DEBUG

def logger(msg="", error=False):
    if error:
        logging.error(msg)
    else:
        logging.info(msg)
