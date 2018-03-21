# simple-minded bowling score calculator. 

## How to run:

```
python3 bowling.py
```

## Interna

By default, there's a `FakeInput` class active (no typing required). It used the values of the exercise sheet as input.

You can replace it by `ScoreInput()`, which will then ask all the required values. At input-level there's no special input validation (like strike-detection and skipping rolls), which means, that you have to enter the correct (= allowed according the rules / number of available pins) yourself.

The calculation of the total score does check such special cases and takes bonus scores into account. Not sure though, if the calculation matches official rules with regards to two (or three) strikes in the last frame, but that's not part of exercise anyways.

