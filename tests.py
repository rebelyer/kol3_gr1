# OD RAFALA WIENSKO
# https://github.com/rebelyer/kol2_gr1
import Main


class Test(object):
        
    @classmethod
    def test_1(cls):
        print 'Should be able to get students total average score (across classes)'

    @classmethod
    def test_2(cls):
        print 'Should be able to get students average score in class'

    @classmethod
    def test_3(cls):
        print 'Should hold students first name'
        student = Main.Student("Andrzej", "Marczyk", [], [])
        assert student.student_name == "Andrzej"


    @classmethod
    def test_4(cls):
        print 'Should hold students last name'
        student = Main.Student("Wieslaw", "Charka", [], [])
        assert student.student_surname == "Charka"

    @classmethod
    def test_5(cls):
        print 'Should be able to count total attendance of student'

    @classmethod
    def test_6(cls):
        print ''

    @classmethod
    def test_7(cls):
        print ''

    @classmethod
    def test_8(cls):
        print ''

    @classmethod
    def test_9(cls):
        print ''

    @classmethod
    def test_11(cls):
        print ''

    @classmethod
    def test_12(cls):
        print ''

    @classmethod
    def run_tests(cls):
        cls.test_1()
        cls.test_2()
        cls.test_3()
        cls.test_4()
        cls.test_5()
        cls.test_6()
        cls.test_7()
        cls.test_8()
        cls.test_9()
        cls.test_10()
        cls.test_11()
        cls.test_12()


if __name__ == "__main__":
    Test.run_tests()
