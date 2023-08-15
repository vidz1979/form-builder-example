import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import functools
from itertools import cycle

def parseNumberList(str, sep):
  # raises value ValueError
  if not str.strip():
    return []
  return list(
      map(lambda n: float(n.strip()), str.strip().replace(",", ".").split(sep))
  )

def calculateCumulativeDiscount(str):
  # 10+10+10 = 27.1
  # raises value ValueError
  discounts = parseNumberList(str, "+")
  return 100 - functools.reduce(
    lambda val, disc: val * (1 - disc / 100),
    discounts,
    100,
  )

def calculateAveragePeriod(str):
  # 30/60/90/120 = 75.0
  # raises value ValueError
  periods = parseNumberList(str, "/")
  if len(periods) == 0:
    return 0
  return sum(periods) / len(periods)

def validateCnpj(cnpj: str) -> bool:
  LENGTH_CNPJ = 14
  cnpj = cnpj.replace(".", "").replace("/", "").replace("-", "")
  
  if len(cnpj) != LENGTH_CNPJ:
    return False

  if cnpj in (c * LENGTH_CNPJ for c in "1234567890"):
    return False

  cnpj_r = cnpj[::-1]
  for i in range(2, 0, -1):
    cnpj_enum = zip(cycle(range(2, 10)), cnpj_r[i:])
    dv = sum(map(lambda x: int(x[1]) * x[0], cnpj_enum)) * 10 % 11
    if cnpj_r[i - 1:i] != str(dv % 10):
      return False

  return True

def to_upper(x):
    try:
        return x.strip().upper()
    except Exception:
        return x


# append a prefix in each key of a form_config (dict)
# crawls recursively into nested sublists
def form_config_prefix_key(form_config: list, prefix: str):
    def map_fn(item):
        if type(item) == list:
            return [*list(map(map_fn, item))]
        elif type(item) == dict:
            item = {**item}
            if "key" in item:
                item["key"] = f"{prefix}{item['key']}"
            return item
        raise Exception("form_config must be a list or dict")

    return list(map(map_fn, [*form_config]))