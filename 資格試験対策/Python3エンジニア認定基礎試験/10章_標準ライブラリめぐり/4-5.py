import unittest
from s43 import plus

# unittestのTestCaseを使用してTestPlusクラスを作成する
class TestPlus(unittest.TestCase):
    def test01(self):
        actual = plus(1, 1)
        expected = 2
        # 確認事項 -> assertEqual(a, b)が a == bであるということ
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
