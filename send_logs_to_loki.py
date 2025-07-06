import logging
import traceback
import logging_loki

logger = ''

def send_logs(application_name:str, logger_name:str):
    """This function will be used to send logs to LOKI

    Args:
        application_name (str): Application name for log, can be modified based on use case
        logger_name (str): Logger name, can be modifies based on use case
    """
    try:
        global logger

        handler = logging_loki.LokiHandler(
            url="http://localhost:3100/loki/api/v1/push",
            tags={"application": application_name},
            version="1",
        )

        logger = logging.getLogger(logger_name)
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    except:
        print(f'Exception in send_logs(): {traceback.format_exc()}')

def function_needing_log_capture():
    try:
        global logger

        logger.info('This is a test message...')

        logger.warning('Warning!!! raising error')

        raise ValueError("Division by zero is not allowed.")
    except:
        print(f'Exception in function_needing_log_capture(): {traceback.format_exc()}')
        logger.error(traceback.format_exc())

# Initialise logger
send_logs('Test-Application', 'Test-Logger')

# Sending logs
function_needing_log_capture()
