import unittest

import star_realms


class MainProgramTests(unittest.TestCase):

    def test_player_two_damage_recorded(self):
        """
        When a damage amount for player two is input, the score of player two is decremented.
        """
        def input_function():
            return "2"

        all_output = []

        def print_function(output):
            all_output.append(output)

        star_realms.main(input_function, print_function)

        self.assertIn("Player 2 current score: 48.0", all_output)
