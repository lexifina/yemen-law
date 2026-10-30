# Yemen: law history in git

The law of Yemen as a git history: one file per provision, one commit per law on the day it took effect, and the law that made each change as the commit's author. `git blame` names the law behind every paragraph; `git log` lists every change; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law).

**What is in it now (a first build, not complete)**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | دستور الجمهورية اليمنية (Constitution of the Republic of Yemen, as amended in 2001) | 1 | One version: the text as amended by the 2001 referendum, dated 28 February 2001. The 1991 and 1994 texts are not built. |

**Language.** Arabic, the official language. This README is in English.

**Source.** The text is published by the [Supreme Commission for Elections and Referendum](http://www.scer.org.ye/arabic/dstora.htm) (SCER) of Yemen, read from Internet Archive captures of 2002 and cross-checked on 30 October 2026 against an independent 2011 capture of the same pages.

## Dates

The Constitution has one version, "oldest version available", dated 28 February 2001, the date SCER gives for the referendum on the amendments, and credited to the publisher. The day the result was announced, which Article 156 of the 1994 text makes the in-force day, is not printed in the sources read.

## How it is checked

Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`) and must match `corpus.json`; results are in `REPRODUCE.md`.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist (`<law key>@scer.org.ye.invalid`). For this single version the author is the publisher. The committer is always Lexifina.

## Limits

Only the current (2001) text is held, so there is no amendment history. Articles 1 to 162 are included; part, chapter and section headings are not kept.
