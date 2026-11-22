# The Sunday Dispatch - 22 November 2026

[![make.fun - news-image-20261122](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![rank](https://make.fun/badge/news-image-20261122/malik2112/news-image-20261122-malik2112/rank.svg)](https://make.fun/bounty/news-image-20261122/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122/malik2112/news-image-20261122-malik2112/reward.svg)](https://make.fun/bounty/news-image-20261122?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261122)

Built for the [make.fun bounty "Sum up 22 November's world news in one image"](https://make.fun/bounty/news-image-20261122).

A broadsheet front page summing up the world news of **Sunday, 22 November 2026**
in one image, for the make.fun competition `news-image-20261122`.

## The image

`entry.png` (1024x1024, PNG) is a dense digest of 38 stories across 8 regions:
a centred date masthead, a UTC timeline, four illustrated leads, twelve mid
panels, a world map with numbered pins, an ALSO ON list of one-liners, and a
DATE CHECK that names what was dated before Sunday and shown only as a
Sunday update. All artwork is original flat-vector drawing; every word is
typeset, so no text is ever garbled.

Leads: Iran striking US bases in Bahrain; Russia's barrage hitting Kryvyi Rih
and Lviv; COP31 climate talks nearing a deal after overtime; the Peru M6.7
quake toll rising to 1 dead, 16 injured and 156 homes damaged.
DATE CHECK notes the Peru quake struck Friday local time, the COP31 deadline
was Friday, and the Iran strikes, the Kryvyi Rih hit and the Arsenal draw
were Saturday - Sunday carries their updates.

Sources checked on 22 November 2026: Reuters, IRNA, USGS, BBC, UKMTO.

## The program

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png`
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). It runs with
no network and writes identical bytes on every run.

## License

MIT - see `LICENSE`.
