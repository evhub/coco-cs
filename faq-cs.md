# Coconut Frequently Asked Questions

<!-- MarkdownTOC -->

1. [Mohu použít moduly Pythonu z Coconut a moduly Coconut z Pythonu?](#can-i-use-python-modules-from-coconut-and-coconut-modules-from-python)
1. [Které verze Pythonu Coconut podporuje?](#what-versions-of-python-does-coconut-support)
1. [Help! Pokoušel jsem se napsat rekurzivní iterátor a můj Python způsobil chybu segmentace (segfault)!](#help-i-tried-to-write-a-recursive-iterator-and-my-python-segfaulted)
1. [Jsem-li perfektně spokojený s Pythonem, proč bych se měl učit Coconut?](#if-im-already-perfectly-happy-with-python-why-should-i-learn-coconut)
1. [Přináší Coconut také nějakou pomůcku pro ladění kódu?](#how-will-i-be-able-to-debug-my-python-if-im-not-the-one-writing-it)
1. [Nemám rád funkcionální programování, měl bych se přesto učit Coconut?](#i-dont-like-functional-programming-should-i-still-learn-coconut)
1. [Neznám funkcionální programování, mám se přesto pustit do Coconut?](#i-dont-know-functional-programming-should-i-still-learn-coconut)
1. [Neznám Python moc dobře, měl bych se přesto učit Coconut?](#i-dont-know-python-very-well-should-i-still-learn-coconut)
1. [Proč není Coconut čistě funkcionální?](#why-isnt-coconut-purely-functional)
1. [Neuškodí transpilovaný jazyk jako Coconut komunitě Pythonu?](#wont-a-transpiled-language-like-coconut-be-bad-for-the-python-community)
1. [Chci přispívat do Coconut, jak mohu začít?](#i-want-to-contribute-to-coconut-how-do-i-get-started)
1. [Proč název Coconut?](#why-the-name-coconut)
1. [Kdo vytvořil Coconut?](#who-developed-coconut)

<!-- /MarkdownTOC -->

### Mohu použít moduly Pythonu z Coconut a moduly Coconut z Pythonu?

Yes and yes! Coconut kompiluje do Pythonu, takže moduly Coconut jsou přístupné z Pythonu a moduly Pythonu jsou přístupné z Coconut, včetně celé standardní knihovny Pythonu.

### Které verze Pythonu Coconut podporuje?

Coconut podporuje všechny verze Pythonu `>= 2.6` ve větvi `2.x` nebo `>= 3.2` ve větvi `3.x`. Viz [kompatibilní verze Pythonu](http://coconut.readthedocs.io/en/master/DOCS.html#compatible-python-versions).

### Help! Pokoušel jsem se napsat rekurzivní iterátor a můj Python způsobil chybu segmentace (segfault)!

Žádný problém - stačí použít dekorátor [`recursive_iterator`](http://coconut.readthedocs.io/en/master/DOCS.html#recursive_iterator) z Coconut a budete v pohodě. Toto je [známý problém  Pythonu](http://bugs.python.org/issue14010) a `recursive_iterator` vám jej vyřeší.

### Jsem-li perfektně spokojený s Pythonem, proč bych se měl učit Coconut?

Jste přesně ta osoba, pro kterou byl Coconut vytvořen! Coconut vás nechá psát Python bez starostí s kompabilitou verzí, přičemž vám umožňuje provádět věci, o nichž byste si nikdy nebyl pomyslel že jsou možné, jako je pattern-matching (porovnávání předlohy) a lazy evaluation (líný výpočet). Pokud jste někdy používal funkcionální programovací jazyk, budete vědět, že funkcionální kód je často mnohem jednodušší, čistší a čitelnější. Python je úžasný imperativní jazyk, ale když přijde na moderní funkcionální programování (pro něž nebyl vytvořen), má jisté mezery, které se Coconut snaží doplnit.

### Přináší Coconut také nějakou pomůcku pro ladění kódu?

Snadnost ladění je dlouhodobý problém u všech kompilovaných jazyků, včetně jazyků `C` a `C++`, jež jsou v současné době považovány za low-level jazyky. Řešení tohoto problému je stále stejné: párování řádků. Pokud víte, který řádek zdrojového kódu koresponduje s určitým řádkem kompilovaného kódu, můžete snadno provádět ladění přímo ve zdrojovém kódu. V Coconut to lze snadno zařídit připojením flagu `--line-numbers` nebo `-l`, jenž zajistí připojení komentáře ke každému řádku v kompilovaném kódu s číslem odpovídajícího řádku ve zdrojovém kódu. Alternativní flag `--keep-lines` nebo `-k` zajistí vložení celého řádku ze zdrojového kódu místo nebo spolu s číslem řádku. Ohlásí-li tedy Python chybu, můžete na úryvku kompilovaného kódu číst informaci o čísle problematického řádku ve zdrojovém kódu.

### Nemám rád funkcionální programování, měl bych se přesto učit Coconut?

Definitely! Kromě toho, že je Coconut skvělý pro funkcionální programování, obsahuje také řadu dalších úžasných vlastností, včetně schopnosti kompilovat kód Python 3 do univerzální verze, která poběží v jakékoli verzi Pythonu. I když Coconut není čistě funkcionální, je to skvělý úvod do funkcionálního stylu.

### Neznám funkcionální programování, mám se přesto pustit do Coconut?

Yes, absolutely! [Tutorial](http://coconut.readthedocs.io/en/master/HELP.html) pro Coconut nepředpokládá absolutně žádnou předchozí znalost funkcionálního programování, pouze Pythonu. Protože Coconut není čistě funkcionálním programovacím jazykem a veškerý platný Python je platný Coconut, je Coconut skvělým úvodem do funkcionálního programování. Osvojíte-li si Coconut, budete si moci vyzkoušet nový styl programování bez ztráty jakékoli znalosti Pythonu, který znáte a milujete.

### Neznám Python moc dobře, měl bych se přesto učit Coconut?

Maybe. Znáte-li aspoň základy Pythonu a jste dobře obeznámen s funkcionálním programováním, potom zcela určitě vám Coconut umožní pokračovat v používání všech vašich oblíbených nástrojů funkcionálního programování za současného dalšího seznamování s Pythonem. Nejste-li příliš obeznámen ani s Pythonem ani s funkcionálním programováním, potom učiníte lépe, když nejprve projdete vhodným tutoriálem Pythonu.

### Proč není Coconut čistě funkcionální?

Stučně řečeno proto, že Coconut je nadstavba Pythonu, který má sice některé funkcionální vlastnosti ale jako celek je záměrně nefunkcionální. Coconut není čistě funkcionální ze stejných důvodů, ze kterých není Python čistě imperativní - různé problémy vyžadují různé přístupy. 

Coconut je záměrně vytvořen tak aby umožnil vytváření kódu v čistě funkcionálním stylu ale lze jej použít i pro jiná paradigmata.

### Neuškodí transpilovaný jazyk jako Coconut komunitě Pythonu?

I certainly hope not! Na rozdíl od většiný transpilovaných (transpilled) jazyků, je veškerý Python platný Coconut. Cílem Coconut není nahradit Python ale _rozšířit_ jej. Coconut je dokonale interoperativní s Pythonem a používá stejné knihovny. Tudíž Coconut nemůže rozdělit komunitu Pythonu, protože komunita Coconu _je_ komunitou Pythonu.

### Chci přispívat do Coconut, jak mohu začít?

That's great! Coconut is completely open-source, and new contributors are always welcome. Contributing to Coconut is as simple as forking Coconut on [GitHub](https://github.com/evhub/coconut), making changes to the [`develop` branch](https://github.com/evhub/coconut/tree/develop), and proposing a pull request. If you have any questions at all about contributing, including understanding the source code, figuring out how to implement a specific change, or just trying to figure out what needs to be done, try asking around at Coconut's [Gitter](https://gitter.im/evhub/coconut), a GitHub-integrated chat room for Coconut developers.

### Proč název Coconut?

![Monty Python and the Holy Grail](http://i.imgur.com/PoFot.jpg)

Pokud vám to není známo, obrázek nahoře pochází z komedie [Monty Python and the Holy Grail](https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail), ve které Rytíři Kulatého Stolu tlučou kokosovými ořechy o sebe aby napodobili zvuk jezdce na koni. Jméno Coconut bylo zvoleno jako odkaz na skutečnost, že
in which the Knights of the Round Table bang Coconuts together to mimic the sound of riding a horse. The name was chosen to reference the fact that [Python je nazván podle Monty Python](https://www.python.org/doc/essays/foreword/) as well.

### Kdo vytvořil Coconut?

[Evan Hubinger](https://github.com/evhub) is an undergraduate student studying mathematics and computer science at [Harvey Mudd College](https://www.hmc.edu/). You can find his resume online at <http://evhub.github.io/resume.pdf>.
