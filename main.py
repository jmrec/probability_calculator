import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
          for i in range(value):
              self.contents.append(key)
        self.original_contents = copy.copy(self.contents)

    def get_content_length(self):
        return len(self.contents)

    def draw(self, number_of_balls_to_draw):
        if number_of_balls_to_draw > len(self.contents):
            self.contents = copy.copy(self.original_contents)

        lst = []
        for i in range(number_of_balls_to_draw):
            lst.append(self.contents.pop(
            random.randrange(len(self.contents))
            ))

        return lst

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
    HAT -> HAT OBJECT
    EXPECTED BALLS -> BALLS EXPECTED TO DRAW IN EACH EXPERIMENT
    NUM_BALLS_DRAWN -> NUMBER OF BALLS TO DRAW IN EACH EXPERIMENT
    NUM_EXPERIMENTS -> NUMBER OF EXPERIMENTS

    LOOP EXPERIMENT
      LOOP BALL DRAW
        DRAW A BALL
        APPEND TO LIST OF BALLS DRAWN

      IF BALLS EXPECTED IS IN BALLS DRAWN
        THEN INCREMENT COUNTER

    RETURNS -> NUMBER OF TIMES EXPECTED BALLS GOT DRAWN / NUMBER OF EXPERIMENTS
    """
    if num_balls_drawn > hat.get_content_length():
        return 1.0

    counter = 0
    for i in range(num_experiments):
        checker = []
        drawn_balls_in_experiment = hat.draw(num_balls_drawn)

        for key, value in expected_balls.items():
            if drawn_balls_in_experiment.count(key) >= value:
                checker.append(True)
            else:
                checker.append(False)

        if all(checker):
            counter += 1

    return counter / num_experiments
