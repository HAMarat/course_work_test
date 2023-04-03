from utils import get_data_json, return_data, filter_data_by_state, sorted_data_by_date
from constants import FILE_NAME

data = get_data_json(FILE_NAME)

filter_data = filter_data_by_state(data, 'EXECUTED')

sort_data = sorted_data_by_date(filter_data, "date")

result = return_data(sort_data[0:5])

# Выводим результат
print('\n\n'.join(result))
