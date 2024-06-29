import logging
import os
from general_functions import GeneralFunctions
import allure

if not os.path.exists(r'D:\allure_testing\logs'):
    os.makedirs(r'D:\allure_testing\logs')

class Logs:

    def __init__(self, logger_name, logger_file):
        self.logger_name = logger_name
        self.logger_file = logger_file

    def logger(self):
        logger = logging.getLogger(self.logger_name)
        file_handler = logging.FileHandler(self.logger_file)
        formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        file_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
class Dummy:

    @staticmethod
    def dummy_test(event, logger_name, logger_file, log_file):
        Logs(logger_name, logger_file).logger()
        logger.info('starting test')
        log = GeneralFunctions.read_from_logs(event, log_file)
        logger.debug(log)
        if log [0]:
            return True, 'found log'
        else:
            return False, 'did not find log'

    @staticmethod
    def names_test(event, logger_name, logger_file, log_file):
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler(logger_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        file_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        logger.info('starting test')
        log = GeneralFunctions.read_from_logs(event, log_file)
        logger.debug(log)
        if log[0]:
            return True, 'found log'
        else:
            return False, 'did not find log'

    @staticmethod
    def insert_test(event, logger_name, logger_file, log_file):
        logger = logging.getLogger(logger_name)
        file_handler = logging.FileHandler(logger_file)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        file_handler.setLevel(logging.DEBUG)
        logger.setLevel(logging.DEBUG)
        logger.info('starting test')
        log = GeneralFunctions.read_from_logs(event, log_file, 120)
        logger.debug(log)
        if log[0]:
            return True, 'found log'
        else:
            return False, 'did not find log'

@allure.epic('logs for allure')
@allure.feature('dummy log tests')
class TestLogs:
    @staticmethod
    @allure.title('dummy test')
    def test_dummy():
        result = Logs.dummy_test('07:44:38.382 ( 605014.087) |    DEBUG: [UXDriver.ApiX.Features.CcdHelper] 164@Nvidia::UXDriver::ApiX::Features::CcdHelper::QueryDisplayConfig : sourceInfo.modeInfoIdx =  7  sourceInfo.sourceModeInfoIdx :  0  sourceInfo.cloneGroupId =  7  targetInfo.modeInfoIdx =  6  targetInfo.targetModeInfoIdx :  0  targetInfo.desktopModeInfoIdx =  6.', 'test_dummy', r'D:\allure_testing\logs\dummy.log', 'D:\\allure_testing\\DummyFiles\\dummylog.log')
        assert result[0], result[1]

    @staticmethod
    @allure.title('names test')
    def test_names():
        result = Logs.names_test(
            'Charlotte','test_names', r'D:\allure_testing\logs\names.log', 'D:\\allure_testing\\DummyFiles\\names.log')
        assert result[0], result[1]

    @staticmethod
    @allure.title('insert test')
    def test_insert():
        result = Logs.insert_test(
            'kuku','test_insert', r'D:\allure_testing\logs\insert.log', 'D:\\allure_testing\\DummyFiles\\insert.log')
        assert result[0], result[1]

