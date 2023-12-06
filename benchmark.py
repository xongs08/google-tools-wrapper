from time import perf_counter
import google_tools as gt

def test_currency_conversion(n):
    start = perf_counter()
    operations_time = []
    for _ in range(n):
        start_ = perf_counter()
        gt.currency_conversion('USD', 'BRL')
        operations_time.append(perf_counter() - start_)
    full_time = perf_counter() - start
    final_result = {
        'min_time': min(operations_time),
        'max_time': max(operations_time),
        'avg': {
            'operations': n,
            'time_per_operation': full_time / n
        }
    }
    return final_result

def test_translater(n):
    start = perf_counter()
    operations_time = []
    for _ in range(n):
        start_ = perf_counter()
        gt.translater('pt', 'en', 'Ola Mundo')
        operations_time.append(perf_counter() - start_)
    full_time = perf_counter() - start
    final_result = {
        'min_time': min(operations_time),
        'max_time': max(operations_time),
        'avg': {
            'operations': n,
            'time_per_operation': full_time / n
        }
    }
    return final_result

if __name__ == '__main__':
    # testing currency conversion
    result = test_currency_conversion(100)
    print(f"MIN TIME: {result['min_time']} seconds\nMAX TIME: {result['max_time']} seconds\nAVG TIME ({result['avg']['operations']} operations): {result['avg']['time_per_operation']} seconds")

    # testing translater
    result = test_translater(30)
    print(f"MIN TIME: {result['min_time']} seconds\nMAX TIME: {result['max_time']} seconds\nAVG TIME ({result['avg']['operations']} operations): {result['avg']['time_per_operation']} seconds")
