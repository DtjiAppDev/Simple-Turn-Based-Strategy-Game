import unittest
from simple_turn_based_strategy_game import *


class MyTestCase(unittest.TestCase):
    def test_add_heroes_1(self):
        team: Team = Team()
        for i in range(5):
            team.add_hero(Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3")))

        self.assertTrue(len(team.get_heroes()) == 5)

    def test_add_heroes_2(self):
        team: Team = Team()
        for i in range(10):
            team.add_hero(Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3")))

        self.assertTrue(len(team.get_heroes()) == 5)

    def test_add_heroes_3(self):
        team: Team = Team()
        for i in range(3):
            team.add_hero(Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3")))

        self.assertTrue(len(team.get_heroes()) == 3)

    def test_remove_hero_1(self):
        team: Team = Team()
        for i in range(5):
            team.add_hero(Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3")))

        team.remove_hero(team.get_heroes()[0])
        self.assertTrue(len(team.get_heroes()) == 4)

    def test_remove_hero_2(self):
        team: Team = Team()
        for i in range(10):
            team.add_hero(Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3")))

        team.remove_hero(team.get_heroes()[0])
        self.assertTrue(len(team.get_heroes()) == 4)

    def test_remove_hero_3(self):
        team: Team = Team()
        for i in range(3):
            team.add_hero(Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3")))

        team.remove_hero(team.get_heroes()[0])
        self.assertTrue(len(team.get_heroes()) == 2)

    def test_attack(self):
        hero_one: Hero = Hero("Thidse", mpf("5e4"), mpf("4e3"), mpf("2e3"))
        hero_two: Hero = Hero("Uesura", mpf("5.2e4"), mpf("4.4e3"), mpf("1.7e3"))
        for i in range(100):
            hero_one.attack(hero_two)

        self.assertFalse(hero_two.get_is_alive())


if __name__ == '__main__':
    unittest.main()
