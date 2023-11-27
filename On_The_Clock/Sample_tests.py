test.describe("Get money")

test.it("Should return the hours worked for each shift that employee had clocked in")

# assert equals will pass if both items equal each other (using ==). If
# the test fails, assert_equals will output a descriptive message indicating
# what the values were expected to be.
test.assert_equals(get_hours([["2:00pm", "8:00pm"], ["8:00am", "4:30pm"]]), [6.0, 8.5])
test.assert_equals(get_hours([["5:02am", "2:30pm"], ["10:00pm", "3:00am"]]), [9.5, 5.0])
test.assert_equals(get_hours([["1:41pm", "6:50pm"]]), [5.25])
test.assert_equals(get_hours([["12:01am", "3:00am"], ["3:00pm", "12:00pm"]]), [3.0, 21.0])