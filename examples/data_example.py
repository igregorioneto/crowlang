import os, sys

data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(data_path)

from data import Data

# Example of use
data = Data()

data.write("x", 10)
data.write("y", 3.14)
data.write("z", "Hello, world!")

print(data.read("x"))

print(data.read_all())