"""Yemen: turn the cached official SCER captures into corpus.json (no network).

One version of the Constitution: the current text (as amended 2001) as published by the Supreme Commission
for Elections and Referendum (scer.org.ye), archive.org captures 2002-10-15, 2002-12-30 and 2003-01-08.
"""
import hashlib
import html
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, '.cache')
PAGES = [
    ('http://www.scer.org.ye:80/arabic/dstora.htm', '20021015030929'),
    ('http://www.scer.org.ye:80/arabic/dstora2.htm', '20021230225511'),
    ('http://www.scer.org.ye:80/arabic/dstora3.htm', '20030108092609'),
]


def raw(url, ts):
    u = f'https://web.archive.org/web/{ts}id_/{url}'
    h = hashlib.sha256(u.encode()).hexdigest()
    b = open(os.path.join(CACHE, h), 'rb').read()
    return u, b


def blocks(b):
    m = re.search(rb'charset=([\w-]+)', b[:3000])
    s = b.decode(m.group(1).decode() if m else 'cp1256', errors='strict')
    s = re.sub(r'(?is)<script.*?</script>|<style.*?</style>', '', s)
    s = re.sub(r'(?i)<br\s*/?>|</?(p|h\d|div|tr|td|li)\b[^>]*>', '\n\x00\n', s)
    s = re.sub(r'<[^>]+>', ' ', s)
    s = html.unescape(s)
    out = []
    for part in s.split('\x00'):
        t = norm(part)
        if t:
            out.append(t)
    return out


def norm(t):
    t = t.replace('ـ', '')                     # tatweel (kashida): typesetting only
    t = re.sub('[‌‍‎‏]', '', t)
    t = re.sub(r'\s+', ' ', t).strip()
    t = re.sub(r'\s+([.،,:;])', r'\1', t)
    return t


ART = re.compile(r'^مادة\s*\((\d+)\)\s*:?\s*(.*)$')
HEAD = re.compile(r'^(الباب|الفصل|الفرع)\s')


def main():
    units, srcs, order = {}, [], []
    cur = None
    for url, ts in PAGES:
        u, b = raw(url, ts)
        srcs.append((u, hashlib.sha256(b).hexdigest()))
        started = False
        for t in blocks(b):
            if t.startswith('الصفحة') or t.startswith('النظام الدستوري والانتخابي'):
                cur = None
                if started:
                    break
                continue
            m = ART.match(t)
            if m:
                started = True
                n = int(m.group(1))
                cur = f'art-{n:03d}'
                assert cur not in units, cur
                units[cur] = [f'# مادة ({n})']
                order.append(n)
                rest = m.group(2).lstrip(':').strip()
                if rest:
                    units[cur].append(rest)
                continue
            if not started or cur is None:
                continue
            if HEAD.match(t) or t in (':',):
                if HEAD.match(t):
                    cur = None
                continue
            units[cur].append(t)
    assert order == list(range(1, 163)), order
    us = {k: {'label': f'مادة ({int(k[4:])})', 'kind': 'art', 'text': '\n'.join(v) + '\n'} for k, v in units.items()}
    for k, v in us.items():
        assert len(v['text'].splitlines()) >= 2, k
    corpus = {
        'country': {
            'code': 'YE', 'name': 'Yemen', 'slug': 'yemen', 'lang': 'ar', 'tz': 'Asia/Aden', 'future_branch': 'future',
            'publisher': {'name': 'Supreme Commission for Elections and Referendum (scer.org.ye)', 'email': 'scer@scer.invalid'},
            'default_in_force_rule': {
                'text': 'Constitution 1994, art. 156 (as quoted by SCER): an amendment approved by referendum takes effect from the announcement of the referendum result',
                'source': 'https://web.archive.org/web/20021211003634id_/http://www.scer.org.ye:80/arabic/constadma.htm'},
            'licence_note': 'Text of the Constitution of the Republic of Yemen as published by the Supreme Commission for Elections and Referendum (scer.org.ye), read from Internet Archive captures. Official legislative text; no licence terms published.',
        },
        'sources': [
            {'name': 'Supreme Commission for Elections and Referendum (SCER), via Internet Archive', 'url': 'http://www.scer.org.ye/arabic/dstora.htm',
             'retrieved': '2026-10-28', 'requests': 3, 'licence': 'No terms published; official text', 'notes': '; '.join(f'{u} sha256 {h}' for u, h in srcs)},
            {'name': 'House of Representatives (parliament.gov.ye/dostoor/), via Internet Archive', 'url': 'http://www.parliament.gov.ye/dostoor/index.htm',
             'retrieved': '2026-10-28', 'requests': 2, 'licence': 'No terms published', 'notes': 'Parts 1-2 (arts 1-61) only; parts 3-5 were 404 on the site. Cites SCER as its source. Cross-check only.'},
        ],
        'laws': {
            'constitution-1991': {'label': 'Constitution 1991', 'title': 'دستور الجمهورية اليمنية (استفتاء 15-16 مايو 1991)', 'kind': 'referendum',
                                  'enacted': '1991-05-20', 'published': '1991-05-20',
                                  'url': 'https://web.archive.org/web/20030221000358id_/http://www.scer.org.ye:80/arabic/refe91.htm',
                                  'temporary_until': None, 'restores': None, 'note': None},
            'amendment-1994': {'label': 'Constitutional amendment 1994', 'title': 'تعديل الدستور 1994', 'kind': 'law',
                               'enacted': '1994-10-01', 'published': '1994-10-01',
                               'url': 'https://web.archive.org/web/20021221072937id_/http://www.scer.org.ye:80/arabic/maserh1a.htm',
                               'temporary_until': None, 'restores': None, 'note': 'SCER dates it only to October 1994; the day is not given.'},
            'amendment-2001': {'label': 'Constitutional amendment 2001', 'title': 'التعديلات الدستورية المستفتى عليها 2001', 'kind': 'referendum',
                               'enacted': '2001-02-28', 'published': '2001-02-28',
                               'url': 'https://web.archive.org/web/20021211003634id_/http://www.scer.org.ye:80/arabic/constadma.htm',
                               'temporary_until': None, 'restores': None, 'note': None},
        },
        'acts': [{
            'slug': 'constitution', 'short': 'Dustur', 'title': 'دستور الجمهورية اليمنية',
            'url': 'http://www.scer.org.ye/arabic/dstora.htm', 'first_law': None,
            'earlier_laws': ['constitution-1991', 'amendment-1994', 'amendment-2001'],
            'versions': [{
                'from': '2001-02-28', 'source_url': srcs[0][0], 'sha256': srcs[0][1], 'units': us, 'credits': {},
                'note': 'Current text (as amended 2001), committed as the oldest version available. Articles 53-107 and 108-162 come from the SCER pages dstora2.htm and dstora3.htm.'}],
        }],
        'applies': [],
        'decisions': [
            'No official Yemeni government site answers from here; the official texts are read from Internet Archive id_ captures of scer.org.ye (and parliament.gov.ye for cross-checking).',
            'The Constitution is committed once, as the oldest version available (first_law null), dated 2001-02-28: the date SCER gives for the 2001 referendum on the amendments; the announcement day of the result, which the 1994 art. 156 makes the in-force day, is not printed in the sources read.',
            'The 1994 text could be partly rebuilt from the SCER table of old and new wording (constadma.htm), but the 2001 amendment renumbered articles 35 onward and the old texts of deleted arts 119 and 158 are not given, so that version is not built yet.',
            'Tatweel (U+0640), zero-width and direction marks are removed and whitespace is collapsed; part, chapter and section headings are not kept as units.',
        ],
        'ai_use': ['Claude Opus 5.5 (claude-opus-5-5) wrote fetch.py and parse.py and chose the sources; no model wrote or changed legal text.'],
    }
    tmp = os.path.join(HERE, 'corpus.json.tmp')
    with open(tmp, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(corpus, f, ensure_ascii=False, indent=1, sort_keys=False)
        f.write('\n')
    os.replace(tmp, os.path.join(HERE, 'corpus.json'))
    print('articles', len(us))


if __name__ == '__main__':
    main()
