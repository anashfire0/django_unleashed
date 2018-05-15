from logging import Filter
from pprint import pprint

class ManagementFilter(Filter):

    def filter(self, record):
        if (hasattr(record, 'funcName') and record.funcName == 'exexcute')
            return False
        else:
            return True