import unittest
import parkinglot as pkl

class TestParkingSpot(unittest.TestCase):
  def setUp(self):
    self.car = pkl.Car(pkl.VehicleSize.COMPACT)

  # 複数箇所に同時に駐車はできないけどサンプルなので
  def test_park(self):
    parkingSpot = pkl.ParkingSpot(pkl.VehicleSize.MOTOR_CYCLE)
    self.car.park(parkingSpot)
    self.assertNotEqual(self.car, parkingSpot.getVehicle())

    parkingSpot = pkl.ParkingSpot(pkl.VehicleSize.COMPACT)
    self.car.park(parkingSpot)
    self.assertEqual(self.car, parkingSpot.getVehicle())

    parkingSpot = pkl.ParkingSpot(pkl.VehicleSize.LARGE)
    self.car.park(parkingSpot)
    self.assertEqual(self.car, parkingSpot.getVehicle())

if __name__ == '__main__':
    unittest.main()
