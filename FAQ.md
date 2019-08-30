# Coconut FAQ

```eval_rst
.. contents::
    :local:
```         

## Frequently Asked Questions

### Mohu použít moduly Pythonu z Coconut a moduly Coconut z Pythonu? 

Yes and yes! Coconut kompiluje do Pythonu, takže moduly Coconut jsou přístupné z Pythonu a moduly Pythonu jsou přístupné z Coconut, včetně celé standardní knihovny Pythonu.

### Které verze Pythonu Coconut podporuje? 

Coconut podporuje všechny verze Pythonu `>= 2.6` ve větvi `2.x` nebo `>= 3.2` ve větvi `3.x`. Ve skutečnosti je kód Coconut kompilován tak aby běžel stejně na každé z podporovaných verzí.
Viz [kompatibilní verze Pythonu](DOCS.html#kompatibilni-verze-pythonu).


### Může být Coconut použit ke konverzi jedné verze Pythonu na jinou?

Ano, ale jen ve zpětném směru. Coconut může konvertovat Python 3 na Python 2 ale nikoliv obráceně. Coconut vlastně může přeměnit kód Pythonu 3 na Python na verzi nezávislý. Coconut zkompiluje skladbu Python 3, vestavěné entity i dokonce importy na kód, který bude pracovat v každé podporované verzi Pythonu (`2.6`, `2.7`, `>=3.2`).

Existuje však několik výminek: některé konstrukty, jako `async`, nelze replikovat   nižších verzích Pythonu a k tomu aby pracovaly, je potřebné je zavést flagem `--target`. Úplný seznam viz [compatibilní verze Pythonu](DOCS.html#compatible-python-versions).

### Jak lze publikovat paket Coconut na PyPI?

Protože Coconut pouze kompiluje do Pythonu, publikování paketu Coconut na PyPI je přesně totéž jako publikování paketu Pythonu, s určitým kompilačním krokem navíc. Napíšete svůj paket v Coconut, spustíte `coconut` pro zdrojový kód a načtete kompilovaný kód na PyPI. Můžete dokonce míchat kódy Pythonu a Coconut, protože se kompilace dotýká pouze souborů `.coco`. Chcete-li vidět příklad paketu PyPI, psaného v Coconut, včetně souboru [Makefile](https://github.com/evhub/pyprover/blob/master/Makefile), včetně použitých kompilačních příkazů, podívejte se na [pyprover](https://github.com/evhub/pyprover).

### Kde najdu záznam o posledních změnách Coconut?

Informace o každém vydání Coconat jsou zaznamenávány na stránce [GitHub](https://github.com/evhub/coconut/releases). Zde můžete nalézt všechny nové vlastnosti a výrazné změny, uvedené v jednotlivých vydáních.

### Podporuje Coconut kontrolu statických typů?

Ano, Coconut kompiluje [nejnovější](https://www.python.org/dev/peps/pep-0526/) a 
[nejlepší](https://www.python.org/dev/peps/pep-0484/) skladbu anotace typu na komentáře, nezávislé na verzi Pythonu, které potom mohou být kontrolovány s použitím nástroje [MyPy Integration](http://coconut.readthedocs.io/en/master/DOCS.html#mypy-integration).

### Pokoušel jsem se napsat rekurzivní iterátor a můj Python způsobil chybu segmentace!

Žádný problém - stačí použít dekorátor [`recursive_iterator`](DOCS.html#recursive-iterator) z Coconut a budete v pohodě. Toto je [známý problém  Pythonu](http://bugs.python.org/issue14010) a `recursive_iterator` vám jej vyřeší.

### Jak rozdělím výraz přes několik řádků v  Coconut?

Protože je skladba Coconut nadřazená skladbě Python 3, podporuje Coconut stejné pokračování řádků jako Python. To znamená, že jak pokračování zpětným lomítkem, tak implikované pokračování uvnitř kulatých, hranatych a složených závorek bude chodit. Závorkové pokračování je doporučená metoda a Coconut dokonce podporuje její [vylepšenou verzi](DOCS.html#enhanced-parenthetical-continuation).

### Jsem-li perfektně spokojený s Pythonem, proč bych se měl učit Coconut? 

Jste přesně ta osoba, pro kterou byl Coconut vytvořen! Coconut vás nechá psát Python bez starostí s kompabilitou verzí, přičemž vám umožňuje provádět věci, o nichž byste si nikdy nebyl pomyslel že jsou možné, jako je pattern-matching (porovnávání předlohy) a lazy evaluation (líný výpočet). Pokud jste někdy používal funkcionální programovací jazyk, budete vědět, že funkcionální kód je často mnohem jednodušší, čistší a čitelnější. Python je úžasný imperativní jazyk, ale když přijde na moderní funkcionální programování (pro něž nebyl vytvořen), má jisté mezery, které se Coconut snaží doplnit.

### Přináší Coconut také nějakou pomůcku pro ladění kódu? 

Snadnost ladění je dlouhodobý problém u všech kompilovaných jazyků, včetně jazyků `C` a `C++`, jež jsou v současné době považovány za low-level jazyky. Řešení tohoto problému je stále stejné: párování řádků. Pokud víte, který řádek zdrojového kódu koresponduje s určitým řádkem kompilovaného kódu, můžete snadno provádět ladění přímo ve zdrojovém kódu. V Coconut to lze snadno zařídit připojením flagu `--line-numbers` nebo `-l`, jenž zajistí připojení komentáře ke každému řádku v kompilovaném kódu s číslem odpovídajícího řádku ve zdrojovém kódu. Alternativní flag `--keep-lines` nebo `-k` zajistí vložení celého řádku ze zdrojového kódu místo nebo spolu s číslem řádku. Ohlásí-li tedy Python chybu, můžete na úryvku kompilovaného kódu číst informaci o čísle problematického řádku ve zdrojovém kódu.

### Nemám rád funkcionální programování, měl bych se přesto učit Coconut? 

Definitely! Kromě toho, že je Coconut skvělý pro funkcionální programování, obsahuje také řadu dalších úžasných vlastností, včetně schopnosti kompilovat kód Python 3 do univerzální verze, která poběží v jakékoli verzi Pythonu. I když Coconut není čistě funkcionální, je to skvělý úvod do funkcionálního stylu.

### Neznám funkcionální programování, mám se přesto pustit do Coconut? 

Yes, absolutely! [Tutoriál](HELP.html) nepředpokládá absolutně žádnou předchozí znalost funkcionálního programování, pouze Pythonu. Protože Coconut není čistě funkcionálním programovacím jazykem a veškerý platný Python je platný Coconut, je Coconut skvělým úvodem do funkcionálního programování. Osvojíte-li si Coconut, budete si moci vyzkoušet nový styl programování bez ztráty jakékoli znalosti Pythonu, který znáte a milujete.

### Neznám Python moc dobře, měl bych se přesto učit Coconut? 

Možná. Znáte-li aspoň základy Pythonu a jste dobře obeznámen s funkcionálním programováním, potom zcela určitě vám Coconut umožní pokračovat v používání všech vašich oblíbených nástrojů funkcionálního programování za současného dalšího seznamování s Pythonem. Nejste-li příliš obeznámen ani s Pythonem ani s funkcionálním programováním, potom učiníte lépe, když nejprve projdete vhodným tutoriálem Pythonu.

### Proč není Coconut čistě funkcionální? 

Stučně řečeno proto, že Coconut je nadstavba Pythonu, který má sice některé funkcionální vlastnosti ale jako celek je záměrně nefunkcionální. Coconut není čistě funkcionální ze stejných důvodů, ze kterých není Python čistě imperativní - různé problémy vyžadují různé přístupy. 

Coconut je záměrně vytvořen tak aby umožnil vytváření kódu v čistě funkcionálním stylu ale lze jej použít i pro jiná paradigmata.

### Neuškodí transpilovaný jazyk jako Coconut komunitě Pythonu? 

I certainly hope not! Na rozdíl od většiný transpilovaných (transpilled) jazyků, je veškerý Python platný Coconut. Cílem Coconut není nahradit Python ale _rozšířit_ jej. Coconut je dokonale interoperativní s Pythonem a používá stejné knihovny. Tudíž Coconut nemůže rozdělit komunitu Pythonu, protože komunita Coconu _je_ komunitou Pythonu.

### Chci používat Coconut v produkčním prostředí; jak dosáhnu maximálního výkonu?

Za prvé, budete potřebovat rychlý kompilátor, takže byste měl buďto použít [`cPyparsing`](https://github.com/evhub/cpyparsing) nebo použít [`PyPy`](https://pypy.org/). Za druhé, existují dvě jednoduché věci, které můžete udělat, abyste přinutili Coconut rychleji produkovat Python: kompilovat se specifikací `--no-tco` a kompilovat se specifikací `--target` pro určitou verzi Pythonu, na níž má váš kód běžet. Zadání specifikace `--target` pomůže optimalizovat kompilovaný kód pro danou verzi Pythonu a byť je koncová optimalizace [(Tail Call Optimization)](DOCS.html#tail-call-optimization) užitečná, 
obvykle výrazně zpomalí její provedení, takže nepoužití této možnosti způsobí výrazný nárůst výkonu.

### Chci přispívat do Coconut, jak mohu začít? 

That's great! Coconut is completely open-source, and new contributors are always welcome. Contributing to Coconut is as simple as forking Coconut on [GitHub](https://github.com/evhub/coconut), making changes to the [`develop` branch](https://github.com/evhub/coconut/tree/develop), and proposing a pull request. If you have any questions at all about contributing, including understanding the source code, figuring out how to implement a specific change, or just trying to figure out what needs to be done, try asking around at Coconut's [Gitter](https://gitter.im/evhub/coconut), a GitHub-integrated chat room for Coconut developers.

### Proč název Coconut? 

![Monty Python and the Holy Grail](http://i.imgur.com/PoFot.jpg)

Pokud vám to není známo, obrázek nahoře pochází z komedie [Monty Python and the Holy Grail](https://en.wikipedia.org/wiki/Monty_Python_and_the_Holy_Grail), ve které Rytíři Kulatého stolu tlučou kokosovými ořechy o sebe aby napodobili zvuk jezdce na koni. Jméno Coconut bylo zvoleno jako odkaz na skutečnost, že [Python je rovněž nazván podle Monty Python](https://www.python.org/doc/essays/foreword/).

### Kdo vytvořil Coconut? 

[Evan Hubinger](https://github.com/evhub) is an undergraduate student studying mathematics and computer science at [Harvey Mudd College](https://www.hmc.edu/).  He can be reached by asking a question on [Coconut's Gitter chat room](https://gitter.im/evhub/coconut), through email at <evanjhub@gmail.com>, or on [LinkedIn](https://www.linkedin.com/in/ehubinger).
