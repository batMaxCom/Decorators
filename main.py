from logs.decorator import logger_1, logger_2
LOG_PATH = 'logs/LOG.txt'
nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]]
@logger_1
def flat_generator(list_1):
    lt = []
    yield sum([item for item in list_1], lt)


for item in flat_generator(nested_list):
    print(item)
print('________________________________')
@logger_2(LOG_PATH)
def flat_generator(list_1):
    lt = []
    yield sum([item for item in list_1], lt)


for item in flat_generator(nested_list):
    print(item)