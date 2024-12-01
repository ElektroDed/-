calls = 0
def count_calls():
    global calls
    calls = calls + 1
def string_info(string):
    string_info = (len(string), string.upper(), string.lower())
    count_calls()
    return string_info
def is_contains(string, list_to_search):
    if string.lower() in (item.lower() for item in list_to_search):
        t = True
    else:
        t = False
    count_calls()
    return t
print(string_info('Василий'))
print(string_info('Александр'))
print(is_contains('Дом', ['доМ', 'Квартира', 'дАчА']))
print(is_contains('колесо', ['Дверь', 'МотОР']))
print(calls)
