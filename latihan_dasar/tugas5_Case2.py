import abc
from abc import ABC, abstractmethod
class X(ABC):
  def perintah1(self):
   print("ABC adalah Abstract Base Class")
class Y(X):
  def perintah1(self):
    super().perintah1()
    print("subclass ")
# Driver code
Z = Y()
Z.perintah1()