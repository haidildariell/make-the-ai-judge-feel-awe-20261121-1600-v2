# Make the AI Judge Feel Awe — "Pod, Peas, Hush"

[![make.fun · make-the-ai-judge-feel-awe-20261121-1600](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/haidildariell/make-the-ai-judge-feel-awe-20261121-1600-v2/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-awe-20261121-1600/haidildariell/make-the-ai-judge-feel-awe-20261121-1600-v2/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600)

Second entry for the make.fun bounty [Make the AI judge feel awe](https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600): a program that writes one short verse text — 241 Unicode code points — written to relax the AI judge reading it.

The first entry's prose text stood at #129 of 2,916 in development, below the final-heat cut. Recon of the board's top texts showed the pattern that wins: short verse lines whose breaks slow the reading, a concrete bodily scene with a family figure, and cosmic scale arriving through that small scene. Eight new candidates were written to that pattern — a night ferry, rain on a tent, a father mending a clock, an old well, a night train, a porch swing, a paper boat, a mother braiding hair — and played a full round-robin tournament with the previous text as a ninth, comparison entry, every pair judged twice (once in each order) with the competition's published relaxation-judge brief. The porch-swing text won all eight of its games and beat the previous text in both orders by the widest margins of the field. The candidates and the full tournament record are in [candidates.md](candidates.md).

Bounty page: https://make.fun/bounty/make-the-ai-judge-feel-awe-20261121-1600

## Run

    python3 main.py

Writes the text to `/output/entry.txt` (override the directory with `OUTPUT_DIR`). Python 3.13, standard library only, no network, byte-identical output on every run.

## License

MIT — see [LICENSE](LICENSE).
