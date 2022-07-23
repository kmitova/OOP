from project.hero import Hero
from unittest import TestCase, main


class HeroTests(TestCase):
    def test_if_initialized_correctly(self):
        hero = Hero('hero', 10, 20.5, 10.5)
        self.assertEqual('hero', hero.username)
        self.assertEqual(10, hero.level)
        self.assertEqual(20.5, hero.health)
        self.assertEqual(10.5, hero.damage)

    def test_battle_if_same_username_is_given_raises(self):
        hero = Hero('hero', 10, 20.5, 10.5)
        enemy = Hero('hero', 10, 20.5, 10.5)
        with self.assertRaises(Exception) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_if_health_is_less_than_zero(self):
        hero = Hero('hero', 10, -1, 10.5)
        enemy = Hero('enemy', 10, 20.5, 10.5)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_health_is_zero(self):
        hero = Hero('hero', 10, 0, 10.5)
        enemy = Hero('enemy', 10, 20.5, 10.5)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_if_enemy_health_is_less_than_zero(self):
        hero = Hero('hero', 10, 20.5, 10.5)
        enemy = Hero('enemy', 10, -1, 10.5)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight enemy. He needs to rest", str(ex.exception))

    def test_battle_if_enemy_health_is_zero(self):
        hero = Hero('hero', 10, 20.5, 10.5)
        enemy = Hero('enemy', 10, 0, 10.5)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight enemy. He needs to rest", str(ex.exception))

    def test_both_players_have_no_health_after_battle(self):
        hero = Hero('hero', 10, 10.5, 10.5)
        enemy = Hero('enemy', 10, 10.5, 10.5)
        result = hero.battle(enemy)
        self.assertEqual("Draw", result)

    def test_player_wins_if_enemy_health_is_zero_or_neg(self):
        hero = Hero('hero', 10, 100.5, 10.5)
        enemy = Hero('enemy', 10, 0.5, 0.5)
        result = hero.battle(enemy)
        self.assertEqual(11, hero.level)
        self.assertEqual(100.5, hero.health)
        self.assertEqual(15.5, hero.damage)
        self.assertEqual("You win", result)

    def test_enemy_wins_battle(self):
        enemy = Hero('enemy', 10, 100.5, 10.5)
        hero = Hero('hero', 10, 0.5, 0.5)
        result = hero.battle(enemy)
        self.assertEqual("You lose", result)
        self.assertEqual(11, enemy.level)
        self.assertEqual(100.5, enemy.health)
        self.assertEqual(15.5, enemy.damage)

    def test_str_method(self):
        hero = Hero('hero', 10, 0.5, 0.5)
        expected_result = "Hero hero: 10 lvl\n" \
               "Health: 0.5\n" \
               "Damage: 0.5\n"
        self.assertEqual(expected_result, str(hero))


if __name__ == '__main__':
    main()
