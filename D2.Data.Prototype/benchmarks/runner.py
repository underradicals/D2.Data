import pyperf

def to_list_via_comprehension(data):
    return [(x, y) for x, y in data.items()]

def to_list_via_zip(data):
    return list(zip(*data.items()))

def to_list_via_zip1(data):
    return list(zip(data.keys(), data.values()))

def to_list_via_list_spread_operator(data):
    return [*data.items()]

def main():

    runner = pyperf.Runner()
    runner.timeit("list comprehension", stmt="to_list_via_comprehension(data)", setup = "data = {str(i): i for i in range(1000)}", globals=globals())
    runner.timeit("zip with *items()", stmt="to_list_via_zip(data)", setup = "data = {str(i): i for i in range(1000)}", globals=globals())
    runner.timeit("zip with keys() and values()", stmt="to_list_via_zip1(data)", setup = "data = {str(i): i for i in range(1000)}", globals=globals())
    runner.timeit("to_list_via_list_spread_operator", stmt="to_list_via_list_spread_operator(data)", setup = "data = {str(i): i for i in range(1000)}", globals=globals())

if __name__ == "__main__":
    main()