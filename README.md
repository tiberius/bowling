# simple-minded bowling score calculator. 

## How to run:

```
python3 bowling.py
```

## Interna

By default, there's a `ScoreInput` class active, which prompts all values. There's also a `FakeInput` class availble (no typing required). It uses the values of the exercise sheet as input.

The calculation of the total score checks special cases (as strikes) and takes bonus scores into account. Not sure though, if the calculation matches official rules with regards to two (or possibly three) strikes in the last frame, but that's not part of exercise anyways.

