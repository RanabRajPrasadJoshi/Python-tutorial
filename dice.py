import random
from pathlib import Path
from xml.sax import parse


class dice:
    def row(self):
        number = (1,2,3,4,5,6)
        print(f"({random.choice(number)},{random.choice(number)})")


dice1 = dice()
dice1.row()
dice1.row()
dice1.row()

path = Path("convert")
print(path.exists())