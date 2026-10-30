# How this repository was made (Yemen)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Supreme Commission for Elections and Referendum (SCER), via Internet Archive | <http://www.scer.org.ye/arabic/dstora.htm> | 2026-10-28 | No terms published; official text |
| House of Representatives (parliament.gov.ye/dostoor/), via Internet Archive | <http://www.parliament.gov.ye/dostoor/index.htm> | 2026-10-28 | No terms published |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

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
- 0 commits on the branch `future`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 3 laws in the record.
- 1 tags.

## Dates

Each commit is dated at noon (Asia/Aden) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Constitution 1994, art. 156 (as quoted by SCER): an amendment approved by referendum takes effect from the announcement of the referendum result https://web.archive.org/web/20021211003634id_/http://www.scer.org.ye:80/arabic/constadma.htm

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `3727f31608496c4eac9d90d4e08446b7514c6698a446067e73da9a85951c83c6` (100787 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3e59cb6f05eccb94a9ec14431a7f6781221e83ef`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- The Constitution is committed once, as the oldest version available (first_law null), dated 2001-02-28: the date SCER gives for the 2001 referendum on the amendments; the announcement day of the result, which the 1994 art. 156 makes the in-force day, is not printed in the sources read.
- The 1994 text could be partly rebuilt from the SCER table of old and new wording (constadma.htm), but the 2001 amendment renumbered articles 35 onward and the old texts of deleted arts 119 and 158 are not given, so that version is not built yet.
- Tatweel (U+0640), zero-width and direction marks are removed and whitespace is collapsed; part, chapter and section headings are not kept as units.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Opus 5.5 (claude-opus-5-5) wrote Lexifina's code and chose the sources; no model wrote or changed legal text.
