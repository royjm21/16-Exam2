"""
Exam 2, problem 1.

Authors: David Mutchler, Dave Fisher, Matt Boutell, Amanda Stouder,
         their colleagues and Jeremy Roy.  April 2018.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_problem1()


###############################################################################
# Done: 2.  READ the code of the  Rect  class below.
#
#   Once you are confident that you understand the  Rect  class and its code,
#   change the TO-DO for this problem to DONE.
#
#   If you do NOT understand the  Rect  class and its code,
#   talk to your instructor to see how to proceed.
###############################################################################
class Rect(object):
    def __init__(self, width, height):
        self.w = width
        self.h = height


def run_test_problem1():
    """ Tests the   problem1   function. """
    # -------------------------------------------------------------------------
    # Done: 3. Implement at least 2 tests of the  problem1  function.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   problem1   function:')
    print('--------------------------------------------------')

    #Test 1
    expected = 110
    answer = problem1([Rect(5, 6), Rect(5, 7), Rect(5, 9)])
    print('Test 1:')
    print('expected:', expected)
    print('answer:', answer)

    #Test 2
    expected = 1885
    answer = problem1([Rect(100, 2), Rect(50, 25), Rect(15, 29)])
    print('Test 2:')
    print('expected:', expected)
    print('answer', answer)

    #Test 3
    expected = 68
    answer = problem1([Rect(2, 3), Rect(4, 5), Rect(6, 7)])
    print("Test 3:")
    print('expected:', expected)
    print('answer', answer)


def problem1(rectangles):
    """
    What comes in:  A sequence of  Rect  objects.
    What goes out:  Returns the sum of the areas of the given  Rect  objects.
    Side effects:   None.
    Example:
      problem1([Rect(5, 10),
                Rect(4, 3),
                Rect(100, 7)]
         returns 50 + 12 + 700, which is 762

    Type hints:
    :param rectangles: [Rect]
    :return: int
    """
    # -------------------------------------------------------------------------
    # TODO: 4. Implement and test this function.
    # -------------------------------------------------------------------------
    for k in range(len(problem1([])-1)):
        area = area + Rect.width*Rect.height
        return area

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()