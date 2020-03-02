from enum import Enum
from abc import abstractmethod

class VehicleSize:
  LARGE = 1
  COMPACT = 2
  MOTOR_CYCLE = 3

class Vehicle:
  def __init__(self, size):
    self._size = size

  def getSize(self):
    return self._size

  @abstractmethod
  def canFitInSpot(self, spot):
    raise NotImplementedError()

  def park(self, spot):
    if self.canFitInSpot(spot):
      spot.parkVehicle(self)

class Car(Vehicle):
  def canFitInSpot(self, spot):
    if spot.getSize() == VehicleSize.LARGE:
      return True
    elif spot.getSize() == VehicleSize.COMPACT:
      return True
    else:
      return False

class ParkingLot:
  def __init__(self, levelCount, spotCount):
    self._levels = []
    for i in range(levelCount):
      self._levels.append(Level(i + 1, spotCount))

class Level:
  def __init__(self, floor, spotCount):
    self._floot = floor
    self._spots[ParkingSpot()] * spotCount

class ParkingSpot:
  def __init__(self, size):
    self._size = size
    self._vehicle = None

  def getSize(self):
    return self._size

  def getVehicle(self):
    return self._vehicle

  def parkVehicle(self, vehicle):
    self._vehicle = vehicle

  def vehicleLieved(self):
    del self._vehicle
