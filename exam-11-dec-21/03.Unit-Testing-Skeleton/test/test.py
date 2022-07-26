from unittest import TestCase, main
from project1.team import Team


class TeamTests(TestCase):
    def test_team_init(self):
        team = Team('test')
        self.assertEqual('test', team.name)
        self.assertEqual({}, team.members)
        team.members = {'name': 20}
        self.assertEqual({'name': 20}, team.members)

    def test_name_prop_raises(self):
        team = Team('aa')
        with self.assertRaises(ValueError) as ex:
            team.name = '11'
        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_name_prop_symbol_raises(self):
        team = Team('aa')
        with self.assertRaises(ValueError) as ex:
            team.name = '/'

        self.assertEqual("Team Name can contain only letters!", str(ex.exception))

    def test_name_setter_correct(self):
        team = Team('test')
        team.name = 'aa'
        self.assertEqual('aa', team._Team__name)

    def test_name_prop(self):
        team = Team('test')
        name = team._Team__name
        self.assertEqual('test', name)

    def test_add_member_if_member_not_in_members(self):
        team = Team('test')
        result = team.add_member(name1=20, name2=25)
        self.assertTrue(team.members['name1'] == 20)
        self.assertTrue(team.members['name2'] == 25)
        self.assertEqual("Successfully added: name1, name2", result)

    def test_add_existing_member(self):
        team = Team('test')
        team.members = {'name1': 20}
        result = team.add_member(name1=20)
        self.assertEqual("Successfully added: ", result)

    def test_remove_member_which_exists(self):
        team = Team('test')
        team.add_member(name1=20, name2=25)
        result = team.remove_member('name1')
        self.assertFalse('name1' in team.members)
        self.assertTrue(len(team.members) == 1)
        self.assertEqual("Member name1 removed", result)

    def test_remove_not_existing_member(self):
        team = Team('test')
        team.add_member(name1=20, name2=25)
        result = team.remove_member('name3')
        self.assertEqual("Member with name name3 does not exist", result)

    def test_greater_than_if_self_greater_than_other(self):
        team = Team('test')
        team.add_member(name1=20, name2=25)
        other = Team('other')
        other.add_member(name3=30)
        result = len(team) > len(other)
        self.assertEqual(result, team > other)
        self.assertTrue(team > other)

    def test_greater_than_if_other_is_greater_than_self(self):
        team = Team('test')
        team.add_member(name3=30)
        other = Team('other')
        other.add_member(name1=20, name2=25)
        result = (len(team) > len(other))
        self.assertEqual(result, team > other)
        self.assertFalse(team > other)

    def test_len_method(self):
        team = Team('test')
        team.add_member(name1=20, name2=25)
        result = len(team)
        self.assertEqual(2, result)
        team2 = Team('a')
        self.assertEqual(0, len(team2))

    def test_add_method(self):
        team = Team('test')
        team.add_member(name1=20, name2=25)
        other = Team('other')
        other.add_member(name3=30)
        new_name = 'testother'
        new_team = Team(new_name)
        # new_team.add_member(name1=20, name2=25)
        # new_team.add_member(name3=30, name1=20)
        new_team.members = {'name1': 20, 'name2': 25, 'name3': 30}
        # self.assertEqual(str(new_team), str(team + other))
        self.assertEqual("Team name: testother\n"
                         "Member: name3 - 30-years old\n"
                         "Member: name2 - 25-years old\n"
                         "Member: name1 - 20-years old",
                         str(team+other))

    def test_str_method(self):
        team = Team('test')
        team.add_member(name1=20, name2=25, name3=25)
        expected = "Team name: test\nMember: name2 - 25-years old\nMember: name3 - 25-years old\nMember: name1 - 20-years old"
        self.assertEqual(expected, str(team))


if __name__ == '__main__':
    main()


