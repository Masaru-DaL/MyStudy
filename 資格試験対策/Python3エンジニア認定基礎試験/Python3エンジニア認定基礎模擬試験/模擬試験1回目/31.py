## 実行結果
# Saya is a
# intelligent
# speedster.

class OurException(Exception):
    pass
def raise_her_exception(a):
    print(a, 'is a')                    # ...③
    raise #【A】
    print('easygoing person.')
def func(key: int):
    try:
        if key == 0:
            raise_her_exception('Saya') # ...②
    except OurException as e:
        print('intelligent')            # ...④
        raise #【B】

key = 0
try:
    func(key)                           # ...①
except Exception as f:
    print('speedster.')                 # ...⑤
