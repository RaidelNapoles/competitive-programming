import time


def measure_time(function):
    def measured_funct(*args, **kwargs):
        init = time.time()
        result = function(*args, **kwargs)
        end = time.time()
        print(f"{function.__name__}: {end-init} seconds")
        return result

    return measured_funct
