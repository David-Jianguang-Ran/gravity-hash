from unittest import TestCase

from gravity_simulation.hashing import *


class TestDigest(TestCase):

    def test_get_digest(self):
        cases = [
            "An enchantress disguised as an old beggar woman arrives at a castle during a ball and offers the host, a cruel and selfish prince, a rose in return for shelter from a storm. When he refuses, she reveals her identity. As punishment for the prince's lack of compassion, the enchantress transforms him into a beast and his servants into household objects, then erases the castle, himself, and his servants from the memories of their loved ones and everyone else in the town. She casts a spell on the rose and warns the prince that the spell will only be broken if he learns to love another, and earn their love in return before the last petal falls, or he will remain a beast forever. ",
            "0=> th > operator use to overwrite the file if exist other wise it will create new file E.X. cat >example1 => If file 'example1' is exist than it will over write else create new file => the >> operator use to append the end of the file E.X. cat >>example1",
            "gogogaga",
            ""
        ]

        for each in cases:
            output = get_digest_v0(each)

            # test if output is a string of fixed length
            self.assertIsInstance(output, str)
            self.assertEqual(len(output), BLOCK_SIZE * 2)

    def test_avalanche(self):

        cases = [
            ("gogogaga", "kokokaka"),
            ("abcde", "adcde"),
            ("An enchantress disguised as an old beggar woman arrives at a castle during a ball and offers the host, a cruel and selfish prince, a rose in return for shelter from a storm. When he refuses, she reveals her identity. As punishment for the prince's lack of compassion, the enchantress transforms him into a beast and his servants into household objects, then erases the castle, himself, and his servants from the memories of their loved ones and everyone else in the town. She casts a spell on the rose and warns the prince that the spell will only be broken if he learns to love another, and earn their love in return before the last petal falls, or he will remain a beast forever. ","An enchantress disguised as an old beggar woman arrives at a castle during a ball and offers the host, a cruel and selfish prince, a rose in return for shelter from a storm. When he refuses, she reveals her identity. As punishment for the prince's lack of compassion, the enchantress transforms him into a beast and his servants into household objects, then erases the castle, himself, and his servants from the memories of their loved ones and everyone else in the town. She casts a spell on the rose and warns the prince that the spell will only be broken if he learns to love another, and earn their love in return before the last petal falls, or he will remain a beast forever and ever. "),
        ]

        for each_case in cases:

            d0 = get_digest_v0(each_case[0])
            d1 = get_digest_v0(each_case[1])

            # test if outputs are same length and distinct
            self.assertEqual(len(d0),len(d1))
            self.assertNotEqual(d0,d1)

            # test if there are less than 5 char collisions
            common = [zero == one for zero, one in zip(d0,d1)]
            print(f"avalanche effect test, char diff = {sum(common)}")
            self.assertLessEqual(sum(common),5)  # <= this threshold is arbitrary
