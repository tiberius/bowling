#! /usr/bin/python3
import sys


class ScoreInput(object):

    def raw_input(self, prompt, frame, roll):
        return input(prompt % {
            'roll': roll,
            'frame': frame,
        })

    def read(self, frame, roll, prev=0):
        if prev > 9:
            # strike, roll#2 can be zero only. 
            return 0

        while True:
            try:
                score = self.raw_input("Frame/Roll %(frame)d/%(roll)d: ", frame + 1, roll + 1)

            except EOFError:
                print()
                sys.exit(1)

            try:
                score = int(score)

            except ValueError:
                print("Unable to parse value, please enter score as a number")
                continue

            if score < 0 or score > 10:
                print("Value must be in range 0 .. 10")
                continue

            return score


class FakeInput(object):

    _test_frames = [
        (1, 4, 5),
        (4, 5, 14),
        (6, 4, 29),
        (5, 5, 49),
        (10, 0, 60),
        (0, 1, 61),
        (7, 3, 77),
        (6, 4, 97),
        (10, 0, 117),
        (2, 8, 6, 133),
    ]

    def read(self, frame, roll, prev):
        return self._test_frames[frame][roll]


def _read_n_rolls(_input, frame, n):
    scores = []

    prev = 0

    for roll in range(n):
        score = _input.read(frame, roll, prev)
        scores.append(score)
        prev = score

    return scores


def _bonus(scores, house):
    return scores[house][0]


def _doublebonus(scores, house):
    return scores[house][0] + scores[house][1]


def _sum(scores, prev_score, house):
    frame = scores[house]
    first, second, third = (None, None, 0)

    if len(frame) > 2:
        # last frame
        first, second, third = frame
        curr_score = prev_score + first + second + third

        return curr_score

    else:
        first, second = frame
        bonus = 0

        if first > 9:
            # strike
            bonus = _doublebonus(scores, house + 1)

        elif first + second > 9:
            # spare
            bonus = _bonus(scores, house + 1)
       
        curr_score = prev_score + first + second + bonus
        return _sum(scores, curr_score, house + 1)

    

def columbine(_input):
    """ `columbine` as in: `bowling for columbine`; just the main thread """

    scores = []

    for frame in range(9):
        scores.append(_read_n_rolls(_input, frame, 2))

    # frame 10
    scores.append(_read_n_rolls(_input, frame + 1, 3))

    print("Total:", _sum(scores, 0, 0))
    


if __name__ == "__main__":

	columbine(ScoreInput())
