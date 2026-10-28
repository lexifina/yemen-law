# How this repository was made (Yemen)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Supreme Commission for Elections and Referendum (SCER), via Internet Archive | <http://www.scer.org.ye/arabic/dstora.htm> | 2026-10-28 | 3 | No terms published; official text |
| House of Representatives (parliament.gov.ye/dostoor/), via Internet Archive | <http://www.parliament.gov.ye/dostoor/index.htm> | 2026-10-28 | 2 | No terms published |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | دستور الجمهورية اليمنية | 1 | 2001-02-28 to 2001-02-28 |

The build made 1 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 0 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Asia/Aden) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution 1994, art. 156 (as quoted by SCER): an amendment approved by referendum takes effect from the announcement of the referendum result https://web.archive.org/web/20021211003634id_/http://www.scer.org.ye:80/arabic/constadma.htm

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/yemen-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `86f603fb2a350b8d4400629a3d4b9b1ba24e04492f8f81192f9910cc657f455b` (99870 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `3439bc6302fe4d20d3a72e22f708b23ef563d303` |
| parse.py | `702497ac43732c532cab3b4977ddbb489e350bd5` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

1 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- No official Yemeni government site answers from here; the official texts are read from Internet Archive id_ captures of scer.org.ye (and parliament.gov.ye for cross-checking).
- The Constitution is committed once, as the oldest version available (first_law null), dated 2001-02-28: the date SCER gives for the 2001 referendum on the amendments; the announcement day of the result, which the 1994 art. 156 makes the in-force day, is not printed in the sources read.
- The 1994 text could be partly rebuilt from the SCER table of old and new wording (constadma.htm), but the 2001 amendment renumbered articles 35 onward and the old texts of deleted arts 119 and 158 are not given, so that version is not built yet.
- Tatweel (U+0640), zero-width and direction marks are removed and whitespace is collapsed; part, chapter and section headings are not kept as units.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Opus 5.5 (claude-opus-5-5) wrote fetch.py and parse.py and chose the sources; no model wrote or changed legal text.
