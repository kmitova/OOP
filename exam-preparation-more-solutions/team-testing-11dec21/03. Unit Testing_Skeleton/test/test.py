from project.team import Team
from unittest import TestCase, main


class TeamTests(TestCase):
    def test_init_is_correct(self):
        team = Team('name')
        self.assertEqual('name', team.name)
        self.assertEqual({}, team.members)

    def test_invalid_team_name_raises(self):
        team = Team('name')
        with self.assertRaises(ValueError) as ex:
            team.name = '1234aaaaaa'
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_setter_invalid_name_raises_symbol(self):
        team = Team('name')
        with self.assertRaises(ValueError) as ex:
            team.name = '....||'
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_add_new_member(self):
        team = Team('name')
        self.assertEqual(0, len(team.members))
        result = team.add_member(Person=20, Person2=30)
        self.assertEqual(2, len(team.members))
        self.assertEqual("Successfully added: Person, Person2", result)
        team.add_member(Person=20, Person2=30)
        self.assertEqual(2, len(team.members))


    def test_add_existing_member(self):
        team = Team('test')
        team.members = {'name1': 20}
        result = team.add_member(name1=20)
        self.assertEqual("Successfully added: ", result)

    def test_remove_existing_member(self):
        team = Team('name')
        self.assertEqual(0, len(team.members))
        team.add_member(Person=20, Person2=30)
        self.assertEqual(2, len(team.members))
        result = team.remove_member("Person2")
        self.assertEqual(1, len(team.members))
        self.assertEqual(f"Member Person2 removed", result)

    def test_remove_invalid_member(self):
        team = Team('name')
        self.assertEqual(0, len(team.members))
        team.add_member(Person=20, Person2=30)
        self.assertEqual(2, len(team.members))
        result = team.remove_member("Person3")
        self.assertEqual(2, len(team.members))
        self.assertEqual("Member with name Person3 does not exist", result)

    def test_gt_if_team_is_greater_than_other(self):
        team = Team('name')
        team.add_member(Person=20, Person2=30)
        other = Team('other')
        other.add_member(Person3=44)
        self.assertTrue(team > other)
        # without next two lines: 93/100
        result = len(team) > len(other)
        self.assertEqual(result, team > other)

    def test_gt_if_other_is_greater(self):
        team = Team('name')
        team.add_member(Person=20, Person2=30)
        other = Team('other')
        other.add_member(Person3=44, Person4=66, Person5=22)
        self.assertFalse(team > other)


    def test_gt_if_equal(self):
        team = Team('name')
        team.add_member(Person=20, Person2=30)
        other = Team('other')
        other.add_member(Person3=44, Person4=66)
        self.assertFalse(team > other)

    def test_length_method(self):
        team = Team('name')
        team.add_member(Person=20, Person2=30)
        self.assertEqual(2, len(team.members))
        team2 = Team('a')
        self.assertEqual(0, len(team2))

    def test_add_method(self):
        team = Team('name')
        other = Team('other')
        team.add_member(Person=20, Person2=30)
        other.add_member(Person3=44, Person4=66)
        new = team + other
        self.assertEqual(4, len(new))
        self.assertEqual('nameother', new.name)

    def test_str_method(self):
        team = Team('name')
        team.add_member(Person=20, Person2=30)
        expected = f"Team name: name" + '\n' + f"Member: Person2 - 30-years old"\
                   + '\n' + f"Member: Person - 20-years old"
        self.assertEqual(expected, str(team))




if __name__ == '__main__':
    main()