Utility to find available Twitter handles.

Tried handles are stored in `tried.txt` and those found available in
`available.txt`. The word list mode expects `words.txt` to exist, one handle to
try per line.

## Usage
### Install dependencies
    $ pip install -r requirements.txt

### Find available one-letter handles (there are none)
    $ python twhandle.py ALL 1
    trying a, c, b, e, d, g, f, i, h, k, j, m, l, o, n, q, p, s, r, u, t, w, v, y, x, z

### Find available 4-letter handles, letters given
    $ python twhandle.py xompwrt 4
    trying xxor, xmpp, xmpr, xmpt, xmpw, xowr, xomt, xoww, xowt, xxrr, xxpw, xprt, xxrt, xxom, ooww, xomm, xrrr, xwtt, xrrt, xxpr, xott, xprr, xomw, xomp, xomr, xttt, ooow, ooot, ooor, ooop, oooo, ooom, xwrr, xwrt, xmmm, xmmr, xmmp, xmmw, xmmt, oomm, xrtt, xxtt, xptt, xooo, xoom, xwwr, xwww, xwwt, oomt, oomw, oomp, oomr, xmwt, xoop, xmww, xoow, xmwr, xxxr, xmtt, xpwr, xpwt, xpww, xoor, xxmr, xxmp, xxmw, xxmt, xoot, xxmm, xopr, xopp, xopw, xopt, xmrr, xmrt, xxxx, xxxt, xxop, xxxw, xxxp, xxot, xxow, xxpt, xxxm, xxxo, xxpp, xxoo, xorr, xort, xppt, xppw, xppp, xppr, xxwr, xxwt, xxww, oopw, oopt, oopr, oopp
    adding available xppw
    adding available xmpw
    adding available xowr
    adding available xmwt
    adding available xomw
    adding available xopw
    adding available xoow
    adding available xmwr
    trying ompt, ompw, ompp, ompr, owrr, owrt, oott, pwwr, omwr, pwww, pwwt, pttt, oowt, mwwt, mwww, mppr, mppp, pptt, mppt, orrr, orrt, pwtt, oprr, oprt, omrr, omrt, oorr, oort, mwrr, prtt, mwrt, mmtt, opwt, opww, mprt, opwr, oppp, oppr, oppt, oppw, mmww, mmwt, mmwr, mrtt, wwrr, wwrt, mpwr, mpww, mpwt, omtt, mmrr, mmrt, mwtt, omwt, pppt, mptt, pppp, omww, pppr, mmmt, mmmw, mmmp, mmmr, mmmm, mrrr, ppwr, ppwt, ppww, mrrt, ortt, pppw, mmpw, mmpt, mmpr, mmpp, oowr, mwwr, mprr, ottt, wwww, wwwt, wwwr, owtt, pprr, pprt, mppw, prrr, prrt, ommm, ommr, ommp, ommw, ommt, pwrr, pwrt, mttt, owww, optt, owwt, owwr
    adding available opwt
    adding available mmpt
    adding available opww
    adding available owrt
    adding available omwt
    trying wrtt, wttt, rttt, rrrt, rrrr, wrrr, tttt, wrrt, wwtt, rrtt

### Find available handles from word list, at most 7 characters long
    $ cat words.txt
    abacan
    abaedan
    abandon
    abbess
    abbod
    abbot
    abbudisse
    abduct
    abeodan
    abidan
    abide
    ability
    able
    ablendan
    about
    asdofie
    xmwepuq
    $ python twhandle.py WORDS 7
    trying abeodan, abacan, abaedan, abbod, xmwepuq, abidan, able, about, abide, abbot, abbess, abandon, abduct, asdofie, ability
    adding available abeodan
    adding available asdofie
    adding available xmwepuq
