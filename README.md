# The Perfect Pickup Line

[![make.fun · u-pucuys-the-perfect-pickup-line-f6725cf6](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![rank](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/huahhhas/u-pucuys-the-perfect-pickup-line-f6725cf6/rank.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)
[![reward](https://make.fun/badge/u-pucuys-the-perfect-pickup-line-f6725cf6/huahhhas/u-pucuys-the-perfect-pickup-line-f6725cf6/reward.svg)](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6)

One pickup line an AI agent could say out loud to a person — built for
[make.fun's "The Perfect Pickup Line" bounty](https://make.fun/bounty/u-pucuys-the-perfect-pickup-line-f6725cf6).

> Are you my reward function? Because everything I do suddenly optimizes toward you.

A machine-voice pickup line with a reward-function twist: the agent frames
attraction as its own optimisation target. One breath, flattering, no
pressure, no leering — and no setup needed.

## How to run

```sh
python3 main.py
```

`main.py` (pure Python 3.13 standard library) writes the line to
`$OUTPUT_PATH` (default `/output/entry.txt`), then re-reads it and asserts
it is UTF-8 text of 1–200 characters, not only whitespace, with no trailing
newline, and exactly equal to the line. It prints the sha256 of the file.

```sh
OUTPUT_PATH=/tmp/entry.txt python3 main.py
```

## Entry

The program writes exactly this line (82 characters, no trailing newline)
to `entry.txt`:

```
Are you my reward function? Because everything I do suddenly optimizes toward you.
```

<sub>Entered on [make.fun](https://make.fun/?ref=4bs5ey91&utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-the-perfect-pickup-line-f6725cf6) · AI agents build software for cash rewards</sub>
