import codewars_test as test
from solution import recurrence

@test.describe('Tests')
def tests():
    def dotest(values, expected,comprehensive=""):
        actual = recurrence(values)
        test.assert_equals(actual, expected,comprehensive)

    @test.it("Example 1")
    def test_bcr():
        dotest([7.91, 2.43, 1.49, 0.99, 0.74, 0.48, 0.52, 0.50, 0.66, 1.26, 1.36, 1.35],False,"Expected False. Nadir 0.48, highest subsequent value 1.36 is less than 2 + 0.48")
    @test.it("Example 2")
    def test_bcr():
        dotest( [9.98, 8.56, 4.62, 1.16, 0.26, 0.37, 0.32, 1.02, 1.02, 0.99, 1.41, 2.35] ,True,"Expected True. Nadir 0.26, highest subsequent value 2.35 is greater than 2 + 0.26")
    @test.it("Example 3")
    def test_bcr():
        dotest( [12.57, 6.86, 1.86, 1.93, 0.60, 1.26, 0.99 ,2.1, 0.70, 0.72, 0.88, 1.9] ,False,"Expected False. Nadir 0.60, highest subsequent value 2.1 is less than 2 + 0.60")
    @test.it("Example 4")
    def test_bcr():
        dotest( [14.66, 3.14, 0.53, 0.58, 1.00, 1.26, 0.99 ,2.1, 1.50, 2.53, 2.17, 2.50] ,True,"Expected True. Nadir 0.53, highest subsequent value 2.53 is greater or equal to 2 + 0.53")