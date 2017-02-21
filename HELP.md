# Coconut Tutorial

<!-- MarkdownTOC -->

1. [Úvod](#úvod)
    1. [Instalace](#instalace)
1. [Začínáme](#začínáme)
    1. [Použití překladače](#použití-překladače)
    1. [Použití kompilátoru](#použití-kompilátoru)
    1. [Použití IPython / Jupyter](#použití-ipython--jupyter)
    1. [Případové studie](#případové-studie)
1. [Případová studie 1: `factorial`](#případová-studie-1-factorial)
    1. [Imperativní metoda](#imperativní-metoda)
    1. [Rekurzivní metoda](#rekurzivní-metoda)
    1. [Iterativní metoda](#iterativní-metoda)
    1. [Metoda `addpattern`](#metoda-addpattern)
1. [Případová studie 2: `quick_sort`](#případová-studie-2-quicksort)
    1. [Třídění sekvence](#třídění-sekvence)
    1. [Třídění iterátoru](#třídění-iterátoru)
1. [Případová studie 3: `vector` - část I](#případová-studie-3-vector---část-i)
    1. [2-Vector](#2-vector)
    1. [Konstruktor pro n-Vector](#konstruktor-pro-n-vector)
    1. [Metody pro n-vector](#metody-pro-n-vector)
1. [Případová studie 4: `vector_field`](#případová-studie-4-vectorfield)
    1. [`diagonal_line`](#diagonalline)
    1. [`linearized_plane`](#linearizedplane)
    1. [`vector_field`](#vectorfield)
    1. [Applikace](#applikace)
1. [Případová studie 5: `vector` - část II](#případová-studie-5-vector---část-ii)
    1. [`__truediv__`](#truediv)
    1. [`.unit`](#unit)
    1. [`.angle`](#angle)
1. [Vyplnění mezer](#vyplnění-mezer)
    1. [Líné seznamy](#líné-seznamy)
    1. [Skladba funkcí](#skladba-funkcí)
    1. [Implicitní parciály](#implicitní-parciály)
    1. [Další čtení](#další-čtení)

<!-- /MarkdownTOC -->

## Úvod <a id="introduction"></a>

Vítejte v tutoriálu pro [Coconut Programming Language](http://evhub.github.io/coconut/)! Coconut je varianta [Pythonu](https://www.python.org/) vytvořená pro **jednoduché, elegantní Pythonické functionální programování**.

Proč používat Coconut? Coconut rozšiřuje repertoár programátora v Pythonu o nástroje moderního funkcionálního programování. Kód Coconut běží na obou verzích Pythonu (2/3), činíce tak toto rozdělení věcí minulosti.

Coconut přidává do Pythonu _syntaktickou podporu_ pro:

- pattern-matching - porovnávání předlohy
- algebraic data types - ADT
- destructuring assignment - rozložené přiřazení
- partial application - částečnou aplikaci
- lazy lists - líné seznamy
- function composition - skládání funkcí
- prettier lambdas - úhlednější lambdy
- infix notation
- pipeline-style programming - směrované programování
- operator functions - operátorové funkce
- tail recursion optimization - optimalizace koncové rekurze
- parallel programming - paralelní programování

a mnoho dalšího!

### Instalace <a id="installation"></a>

Ve své podstatě je Coconut kompilátor, který převádí kód v Coconut na kód v Pythonu. To znamená, že tam, kde lze použít skript Pythonu, lze také použít skript Coconut. Pro přístup k tomuto kompilátoru poskytuje Coconute utilitu CLI (command line interface), která dovede:

- kompilovat jednotlivé soubory nebo celé projekty,
- překládat za pochodu kód Coconut,
- včlenit se (hook into) do existujících aplikací Pythonu, jako IPython či Jupiter.

Instalace Coconut je velmi jednoduchá:

1. instalujte [Python](https://www.python.org/downloads/),
2. otevřte konzolu s příkazovým řádkem
3. a zadejte:
```
pip install coconut
```

Pro kontrolu, že instalace proběhla správně, zkuste na příkazový řádek zadat
```
coconut -h
```
což by mělo zobrazit nápovědu pro Coconut.


## Začínáme <a id="starting-out"></a>

### Použití překladače <a id="using-the-interpreter"></a>

Nyní, když máte Coconut nainstalovaný, zkusíme s ním něco provádět. Překladač (interpret) spustíte z příkazového řádku zápisem
```
coconut
```
načež byste měl číst něco jako
```coconut
Coconut Interpreter:
(type "exit()" or press Ctrl-D to end)
>>>
```
což je oznámení Coconut, že je připraven pro zadávání a vyhodnocování kódu. Tož pusťme se do toho!

Pro případ, že jste to dříve přehlédli - _veškerý platný Python 3 je platný Coconut_. To neznamená, že kompilovaný Coconut poběží pouze na Python 3, protože poběží stejně i na Python 2, ale že pouze kód Python 3 je spolehlivě kompilován do kódu Coconut.

Z toho vyplývá, že jste-li důvěrně seznámen s Pythonem, jste již z větší části seznámen se skladbou Coconut a jeho celou standardní knihovnou. Zkusme pro ukázku zadat nějaký jednoduchý kód Pythonu do překladače Coconut:

```coconut_pycon
>>> "hello, world!"
hello, world!
>>> 1 + 1
2
```

### Použití kompilátoru <a id="using-the-compiler"></a>

Ovšemže, být schopen za běhu interpretovat kód Coconut je velká věc ale bez schopnosti psát a kompilovat programy by naše programování nebylo příliš užitečné. Pojďme si proto napsat první program v Coconut: "Hello, world!".

Nejprve vytvoříte soubor, do něhož náš kód vložíte. Doporučená extenze pro zdrojové soubory Coconut je `.coco`, vytvořte tedy soubor s názvem `hello_world.coco`. Poté, co to uděláte, měli byste nastavit svůj textový editor na správné zvýrazňování zdrojového kódu. Příslušné instrukce naleznete v odstavci [Zvýraznění skladby](http://coco-cs.readthedocs.io/cs/master/DOCS.html#zvyrazneni-skladby).

Nyní vložíme kód do souboru `hello_world.coco`. Na rozdíl od Pythonu, kde záhlaví a různé importy jsou obvyklé a velmi často velmi nezbytné,
```coconut_python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function, absolute_import, unicode_literals, division
```
provede kompilátor Coconut potřebné importy automaticky, takže jediné o co se musíte starat, je vlastní kód.

V čistém Pythonu 3 má příkaz k tisku formát:
```coconut_python
print("hello, world!")
```
a stejně tak i v Coconut, kde navíc je možné použít potrubní (pipeline) usměrnění v zápisu:
```coconut
"hello, world!" |> print
```
z něhož je zřetelně vidět, jak operátor `|>` způsobí předání řetězce coby argument následné funkci, jíž je v tomto případě příkaz k tisku. Nyní náž jednoduchý program "hello_world" uložíme a zkusíme jej spustit.

Kompilování souborů a projektů utilitou Coconut je vemi jednoduché. Zapíšeme pouze
```
coconut hello_world.coco
```
což vytvoří výstup
```
Coconut: Compiling       hello_world.coco ...
Coconut: Compiled to       hello_world.py .
```
Soubor `hello_world.py` uložte do stejného adresáře jako `hello_world.coco` a měl byste být schopen spustit soubor příkazem
```
python hello_world.py
```
což by mělo vyprodukovat výstup `hello, world!`.

Kompilování jednotlivých souborů ovšem není jediný způsob použití kompilátoru Coconut. Můžeme také kompilovat všechny soubory v daném adresáři najednou a to pouhým uvedením názvu adresáře.

```
coconut `název_adresáře`
```
Kompilátor si sám vyhledá všechny kompilovatelné soubory a vytvoří pomocný soubor `__coconut__.py`, do něhož uloží potřebné informace z jednotlivých souborů.

Kompilátor Coconut  podporuje velké množství různých kompilačních možností - viz nápověda `coconut -h`. Nejužitečnější z nich je opce `--linenumbers` (nebo zkráceně `-l`), která přidává čísla řádků ze zdrojového kódu do kompilovaného kódu, umožňujíce tak při ladění vidět číslo zdrojového kódu, odpovídající chybujícímu řádku kompilovaného kódu.

### Použití IPython / Jupyter <a id="using-ipython-jupyter"></a>

Coconut usiluje o rozsáhlou podporu zavedených nástrojů pro vědecké výpočty v Pythonu.

To zahrnuje podporu aplikace [IPython](http://ipython.org/) (jádro Pythonu pro framework [Jupyter](http://jupyter.org/)) místo klasické konzoly Pythonu. Coconut je použit jak jako jádro pro notebooky a konzoly Jupytera, tak jako rozšíření uvnitř jádra IPythonu.

Pro spuštění notebooku Jupytera s Coconut jako jádrem použijete příkaz
```
coconut --jupyter notebook
```
a pro spuštění konzoly Jupytera použijete příkaz
```
coconut --jupyter console
```
nebo lze ekvivalentně v obou příkazech zaměnit `--ipython` za `--jupyter`.

Pro použití Coconut jako extenzi uvnitř jádra IPythonu zapište
```coconut
%load_ext coconut
```
do svého notebooku či konzoly IPythonu a poté spusťte kód Coconut zápisem
```coconut
%coconut <code>
```
nebo
```coconut
%%coconut <command-line-args>
<code>
```

### Případové studie <a id="case-studies"></a>

Protože byl Coconut vytvořen se záměrem aby byl užitečný, bude nejlépe jej předvést v akci při řešení konkrétních problémů, které jsou v tomto tutoriálu označeny jako případové studie.

Tyto případové studie ovšem nepřinášejí úplný přehled všech vlastností Coconut. Ten lze nalézt v obsáhlé [documentaci](http://coco-cs.readthedocs.io/cs/master/DOCS.html).

## Případová studie 1: `factorial` <a id="case-study-1-factorial"></a>

V první ukázce budeme definovat funkci `factorial`, to jest funkci, která počítá součin `n!`, kde `n` je celé číslo `>= 0`.
To je poněkud dětinský příklad, protože tuto úlohu zvládne Python snadno také ale poslouží k demonstraci některých základních vlastnoctí Coconut a jejich výhodného použití.

Nejprve musíme rozhodnout, jaký způsob výpočtu faktoriálu budeme chtít. Možných způsobů řešení je více ale pro jednoduchost se omezíme na čtyři kategorie: imperativní, recurzivní, iterativní a s použitím `addpattern`.

### Imperativní metoda <a id="imperative-method"></a>

Imperativní přístup bychom při psaní `factoriálu` použili v jazyce typu C. Imperativní přístupy zahrnují mnohé změny stavu, kdy jsou pravidelně měněny proměnné při procházení smyčkou. Imperativní přístup v Coconut vypadá nějak takto:
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    if n `isinstance` int and n >= 0:
        acc = 1
        for x in range(1, n+1):
            acc *= x
        return acc
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
-1 |> factorial |> print # TypeError
0.5 |> factorial |> print # TypeError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```
Předtím, než se budeme zabývat průběhem výpočtu, ověřme si nejprve testovací případy. Kdybychom psali skutečný program, uložili bychom jej do souboru, jenž bychom kompilovali ale protože si jenom zkoušíme věci, vystačíme si s překopírováním kódu do překladače (byť úprava skriptu má také své výhody). Měli bychom dostat `1`, `6` a dvakrát `TypeError`.

Nyní, když jsme si ověřili, že nám kód chodí správně, pohleďmě o co v něm kráčí. Protože je imperativní přístup zcela nefunkcionální, Coconut nám v tomto případě příliš nepomůže. Avšak i zde činí použití infixové notace (vložení funkce `isinstance` mezi argumenty: `n` a `int`) kód čistší a čitelnější.

### Rekurzivní metoda <a id="recursive-method"></a>

Rekurzivní metoda je první ze zcela funkcionálních přístupů a to v tom, že nezahrnuje změnu stavu ve smyčce jako u imperativního přístupu. Rekurzivní přístup nahrazuje potřebu explicitně měněné proměnné její implicitní změnou v rekurzivním volání funkce:
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    case n:
        match 0:
            return 1
        match _ is int if n > 0:
            return n * factorial(n-1)
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
-1 |> factorial |> print # TypeError
0.5 |> factorial |> print # TypeError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```

Překopírujte si kód a testy do překladače.

Proberme si specifika syntaxe v tomto příkladu. První věcí je `case n`. Tento příkaz spouští blok `case`, v němž se mohou vyskytnout pouze příkazy `match`. Každý příkaz `match` se pokouší porovnat svou předlohu s hodnotou bloku `case`. U první úspěšné shody jsou realizována všechna připojení proměnných. Navíc, jak je tomu v tomto případě, mohou mít příkazy `match` také kontrolky (guards) `if`, které deklarují podmínku pro další provedení kódu. Posléze, za blokem `case` je příkaz `else` který se provede jen v případě absence jakékoliv shody.

Konkretně v tomto příkladě ověřuje první příkaz `match`, zda je `n` shodné s `0`. Pakliže ano, provede se `return 1`. Následně druhý příkaz `match` ověřuje, zda se `n` shoduje s `_ is int`, což je adekvátní idiomu `n je instancí int` a zda je `n > 0`. Jsou-li všechny kontroly pozitivní, provede se příkaz `return n * factorial(n-1)`. Nedojde-li k provedení žádného příkazu, přichází ke slovu příkaz `else`, který spustí a provede `raise TypeError("argument faktoriálu musí být celé číslo >= 0")`.

I když je tento příklad velmi prostý, je postup v něm použitý, zvaný  **pattern-matching** (porovnání předlohy), jedním z nejmocnějších i nejsložitějších postupů v Coconut. Jako obecné vodítko poslouží asociativní spojení pojmu _přiřazení_ s klíčovým slovem `match`.

Svým způsobem ještě složitější je inverzní postup k `pattern matching`, jímž je **destructuring assignment** (rozložené přiřazení), jež v našem případě pro funkci `factorial` má skladbu:
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    try:
        0 = n # destructuring assignment
    except MatchError:
        try:
            _ is int = n # also destructuring assignment
        except MatchError:
            pass
        else: if n > 0: # in Coconut, if, match, and try are allowed after else
            return n * factorial(n-1)
    else:
        return 1
    raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
-1 |> factorial |> print # TypeError
0.5 |> factorial |> print # TypeError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```

Ukázku si nejprve překopírujte do překladače! I když toto rozložené přiřazení bude také chodit, je mnohem více neohrabané než příkazy `match`. Tato alternativa nám ale ozřejmí, že příkazy `match` jsou ve skutečnosti nóbl _rozložená přiřazení_, jež jsou ve skutečnosti nóbl _normální přiřazení_. Při použití _rozloženého_ místo _normálního_ přiřazení, lze před rozložené přiřazení vložit pro zdůraznění klíčové slovo `match`.

Při používání příkazů pro pattern-matching a destructuring assignment v dalších uázkách bude užitečné, když si pomyslíme _přiřazení_ pokaždé, když uvidíme klíčové slovo `match`.

Až dosud jsme se u rekurzivní metody zabývali pouze porovnáním předlohy (pattern matching) ale ve skutečnosti existuje další způsob, jímž můžeme vylepšit naši funkci `factorial`. Coconut provádí automatickou optimalizaci koncového volání, což znamená že kdykoli funkce vrací přímo volání jiné funkce, zadrží (optimize away) Coconut další volání. Naši funkci `factorial` tedy přepíšeme pro použití koncového volání:
```coconut
def factorial(n, acc=1):
    """Compute n! where n is an integer >= 0."""
    case n:
        match 0:
            return acc
        match _ is int if n > 0:
            return factorial(n-1, acc*n)
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
-1 |> factorial |> print # TypeError
0.5 |> factorial |> print # TypeError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```

Copy, paste! Tato nová funkce `factorial` je ekvivalentní originální verzi s tou výjimkou, že nikdy nevyvolá `RuntimeError` v důsledku dosažení maximální hloubky rekurze v Pythonu, protože Coconut odstaví (optimize away) koncové rekurzivní volání.

### Iterativní metoda <a id="iterative-method"></a>

Tato metoda je dalším funkcionálním přístupem k řešení problému. Iterativní přístupy obcházejí potřebu změny stavu a smyček použitím funkcí vyššího řádu, které jako argumenty přijímají jiné funkce jako `map` a `reduce` k vyčlenění základních prováděných operací. Iterativní přístup k  `factoriálu` v Coconut je tento:
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    case n:
        match 0:
            return 1
        match _ is int if n > 0:
            return range(1, n+1) |> reduce$(*)
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
-1 |> factorial |> print # TypeError
0.5 |> factorial |> print # TypeError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```

Copy, paste! Tato definice se od rekurzivní definice liší pouze v jednom řádku a sice:
```coconut
return range(1, n+1) |> reduce$(*)
```

Rozložme si, co se v tomto řádku odehrává. Nejprve funkce `range` vytvoří iterátor pro všechna čísla, která mají být mezi sebou vynásobena. Ten je postoupen (piped) funkci `reduce$(*)`, která násobení provede. Ale jak? Co je to `reduce$(*)`?

Funkce `reduce` existovala jako vestavěná funkce v Python 2 a Coconut ji nyní přivádí zpět. `reduce` je funkce vyššího řádu, která přijímá jako svůj první argument funkci pro dva argumenty a iterátor jako svůj druhý argument (viz další ukázka), načež aplikuje přijmutou funkci na daný iterátor počínaje jeho prvním elementem a voláním funkce pro dosud akumulované volání a další element, dokud není iterátor vyčerpán. Zde je vizuální reprezentace:
```coconut
reduce(f, (a, b, c, d))

acc                 iter
                    (a, b, c, d)
a                   (b, c, d)
f(a, b)             (c, d)
f(f(a, b), c)       (d)
f(f(f(a, b), c), d)

return acc
```

Nyní pohleďme, jak jsme doplnili funkci `reduce` aby pronásobila všechna čísla, která ji dodáme. Úplný výraz měl tvar `reduce$(*)`. V tomto zápise jsou použity dva konstrukty Coconut a sice operátorová funkce pro násobení ve tvaru `(*)` a příkaz k částečné aplikaci ve tvaru `$`.

Operátorová funkce se v Coconut vytvoří uzavřením operátoru do závorek. V tomto případě je `(*)` zhruba ekvivalentní výrazu v Pythonu: `lambda x, y: x*y`. Ve skladbě lambdy v Coconut je `(*)` rovněž ekvivalentí zápisu `(x, y) -> x*y`, jenž budeme odteďka používat, byť i Pythonní forma je v Coconut legální. Pokud bychom si však zadali režim  `--strict`, vyvolalo by použití lambda z Pythonu chybové hlášení.

Nyní k částečné aplikaci. Lze si myslet, že částečná aplikace je _volání líné funkce_ s operátorem lenosti `$`, kde _lenost_ znamená: "nevyhodnocuj, dokud nemusíš". Je-li v Coconut volání funkce předznamenáno znakem `$`, jako v tomto případě, je normální provedení funkce nahrazeno novou funkcí s již poskytnutými argumenty, takže je funkce volána jak pro částečně použité argumenty, tak pro nové argumenty (v tomto pořadí). V tomto případě je `reduce$(*)` ekvivalentní k `(*args, **kwargs) -> reduce((*), *args, **kwargs)`.

Spojíme-li to vše dohromady, vidíme jak jediný řádek kódu
```coconut
range(1, n+1) |> reduce$(*)
```
je schopen spočítat celý faktoriál bez použití stavů či smyček, pouze s použitím funkce vyššího řádu funkcionálním stylem.

S nástroji Coconut, které zde používáme, jako je částečná aplikace  (`$`), usměrněné (pipeline-style) programování (`|>`), funkce vyššího řádu (`reduce`) a operátorové funkce (`(*)`) je možné sestavovat funkcionální programy snadno a úhledně.

### Metoda `addpattern` <a id="addpattern-method"></a>

I když je iterativní přístup velmi přehledný, je stále zapotřebí tří úrovní odsazení abychom se dostali od záhlaví funkce k vlastnímu vracenému objektu:
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    case n:
        match 0:
            return 1
        match _ is int if n > 0:
            return range(1, n+1) |> reduce$(*)
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")
```

Použijeme-li vestavěnou Coconut funkci  `addpattern`, můžeme zredukovat tři identační úrovně na jednu. Pohleďte:
```
def factorial(0):
    return 1

@addpattern(factorial)
def factorial(n is int if n > 0):
    """Compute n! where n is an integer >= 0."""
    return range(1, n+1) |> reduce$(*)

# Test cases:
-1 |> factorial |> print # MatchError
0.5 |> factorial |> print # MatchError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```
Copy, paste! Tato verze by měla pracovat stejně jako předchozí, až nato že místo `TypeError` vrací hlášení `MatchError`. Máme zde dva nové koncepty k prodiskutování: `addpattern` a definici funkce pro porovnání předlohy (pattern-matching).

Definice funkce pro pattern-matching dělá přesně to co říká její označení - porovnává předlohu se všemi zadanými argumenty. Je zde několik věcí, které je nutné si pohlídat. Předně, aby funkce vyvolala `MatchError`, nenalezne-li se žádná shoda. Dále že nejsou přípustné "keyword" argumenty a konečně stejně jako u rozloženého (destructuring) přiřazení, chcete-li být více explicitní u použití definice pro pattern-matching, můžete přidat `match` před `def`.

Dekorátor `addpattern` přijímá jako argument předtím definovanou p-m funkci a umožňuje v následné funkci přidat novou předlohu.

V našem případě je první předlohou hodnota argumentu `n=0` a druhou podmínka, že `n` je celé číslo `>=0`.

Dekorátorem `addpattern` můžeme upravit nejenom imperativní přístup, jak jsme právě provedli, ale i rekurzivní přístup, jak vidno zde:
```coconut
def factorial(0) = 1

@addpattern(factorial)
def factorial(n is int if n > 0):
    """Compute n! where n is an integer >= 0."""
    return n * factorial(n - 1)

# Test cases:
-1 |> factorial |> print # MatchError
0.5 |> factorial |> print # MatchError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```
Copy, paste! Nevyhovující seance jsou zde označeny opět jako `MatchError`.

## Případová studie 2: `quick_sort` <a id="case-study-2-quicksort"></a>

Ve druhé případové studii budeme používat [quick sort algorithm](https://en.wikipedia.org/wiki/Quicksort). Použijeme dvě verze funkce `quick_sort` - funkci, která přijímá i vrací seznam a funkci, která přijímá i vrací iterátor.

### Třídění sekvence <a id="sorting-a-sequence"></a>

Nejprve `quick_sort` pro seznamy. Použijeme rekurzivní přístup založený na `addpattern`, podobný posledně psané funkci `factorial`. A to proto, že jelikož nebudeme psát `quick_sort` koncově rekurzivním stylem, nemůžeme použít `tail_recursive`, tudíž není důvod psát celou věc jako jednu funkci a mohli bychom stejně dobře použít `addpattern` k redukci identací. Bez dalších okolků, zde je naše implementace `quick_sort` pro seznamy:
```coconut
def quick_sort([]):
    return []

@addpattern(quick_sort)
def quick_sort([head] + tail):
    """Sort the input sequence using the quick sort algorithm."""
    return (quick_sort([x for x in tail if x < head])
        + [head]
        + quick_sort([x for x in tail if x >= head]))

# Test cases:
[] |> quick_sort |> print # []
[3] |> quick_sort |> print # [3]
[0,1,2,3,4] |> quick_sort |> print # [0,1,2,3,4]
[4,3,2,1,0] |> quick_sort |> print # [0,1,2,3,4]
[3,0,4,2,1] |> quick_sort |> print # [0,1,2,3,4]
```
Copy, paste! Zde je pouze jedna nová věc: head-tail pattern-matching. Máme zde předlohu čelo-chvost (`[head] + tail`), která má obecně formu seznamu nebo entice přidanou k proměnné. Když se tato forma vyskytne v jakémkoli p-m kontextu, je s porovnávanou hodnotou zacházeno jako se sekvencí s jejímž počátkem je porovnáván seznam nebo entice jehož zbytek je vázán k proměnné. V tomto případě používáme head-tail předlohu abychom odstranili čelo, jež můžeme použít jako pivot pro rozštěpení zbytku seznamu.

### Třídění iterátoru <a id="sorting-an-iterator"></a>

Nyní vyzkoušíme `quick_sort` pro iterátory. Náš způsob řešení problému bude kombinace rekurzivního a iterativního přístupu, jež jsme použili u `factoriálu`, a sice v tom, že budeme rekurzivně vytvářet lenivý iterátor. Zde je kód:
```coconut
def quick_sort(l):
    """Sort the input iterator, using the quick sort algorithm, and without using any data until necessary."""
    match [head] :: tail in l:
        tail, tail_ = tee(tail)
        yield from (quick_sort((x for x in tail if x < head))
            :: (head,)
            :: quick_sort((x for x in tail_ if x >= head))
            )

# Test cases:
[] |> quick_sort |> list |> print # []
[3] |> quick_sort |> list |> print # [3]
[0,1,2,3,4] |> quick_sort |> list |> print # [0,1,2,3,4]
[4,3,2,1,0] |> quick_sort |> list |> print # [0,1,2,3,4]
[3,0,4,2,1] |> quick_sort |> list |> print # [0,1,2,3,4]
```
Copy, paste! Tento `quick_sort` algoritmus používá řadu nových konstruktů, takže hrr na ně.

Nejprve je to operátor `::`, který se zde objevuje jak v porovnávání shody, tak samostatně. V podstatě to je líný operátor `+` pro iterátory, který spojuje nebo řetězí líně dva iterátory, nic nevyhodnocujíc, není-li žádáno; lze jej použít pro vytváření nekonečných iterátorů. V porovnání shody tuto operaci invertuje, rozkládaje (destructuring) počátek iterátoru na předlohu a zbytek, který váže k proměnné.

Což nás přivádí k další nové věci, zápisu `match ... in ...`. Zápis
```coconut
match pattern in item:
    <body>
else:
    <else>
```
je zkratka pro
```coconut
case item:
    match pattern:
        <body>
else:
    <else>
```
která eliminuje potřebu další úrovně identace při porovnávání pouze jedné předlohy.

Třetím novým konstruktem je vestavěná funkce `tee`. Funkce `tee`
řeší problém funkcionálního programování vytvořený použitím Pythonních iterátorů: kdykoliv je prvek iterátoru evokován, je také zároveň ztracen. Funce `tee` rozdělí iterátor na dva (nebo více, je-li zadán volitelný argument) nezávislé iterátory, které oba pro přístup k datům používají týž skrytý iterátor, takže je-li evokován prvek jednoho iterátoru, zůstává zachován ve druhém.

Konečně, byť se nejedná o nový konstrukt, protože existuje v Python 3, naše použití `yield from` si zasluhuje zmínky. V Pythonu se příkaz `yield`, který pracuje podobně jako `return`, používá k vytváření iterátorů - s tou výjimkou, že se `yield` může vyskytnout vícekrát , pokaždé vraceje jiný element. Forma `yield from` je velmi podobná, až na to, že místo přidání jediného elementu do vytvářeného iterátoru přidává jiný celý iterátor.

Spojíme-li to všechno dohromady, máme zde opět naši funkci `quick_sort`:
```coconut
def quick_sort(l):
    """Sort the input iterator, using the quick sort algorithm, and without using any data until necessary."""
    match [head] :: tail in l:
        tail, tail_ = tee(tail)
        yield from (quick_sort((x for x in tail if x < head))
            :: (head,)
            :: quick_sort((x for x in tail_ if x >= head))
            )
```

Funkce se nejprve pokouší rozštěpit seznam `l` na počáteční element a zbývající iterátor. Je-li `l` prázdným iterátorem, porovnání selže, poskytujíce prázdný iterátor. V opačném případě vytváříme kopii zbytku iterátoru a poskytujeme (yield) spojení: (quick-sort všech zbývajících elementů menších než počáteční element) + (počáteční element) + (quick-sort všech zbyvajících elementů větších než počáteční element).

Výhody zde použitého základního přístupu s četným použitím iterátorů a rekurzí, v porovnání s klasickým imperativním přístupem, jsou mnohé. Za prvé je náš přístup čistší a čitelnější, protože popisuje co **je** `quick_sort` místo **jak** by měl být použit. Za druhé je náš přístup _líný_ v tom, že náš `quick_sort` nic nevyhodnocuje bez vyžádání. A konečně, byť to není relevantní pro `quick_sort`, je to relevantní v mnoha jiných případech, jejichž příklady ještě v tomto tutoriálu uvidíme, náš přístup umožňuje pracovat s _nekonečnými_ řadami jako by byly skutečně nekonečné.

Coconut činí programování s takto výhodným funkcionálním přístupem výrazně snadnější. V tomto příkladě nám  `pattern-matching` Coconutu umožňuje snadné dělení daného iterátoru a jeho slučovací operátor `::` nám umožňuje jej vrátit zpět ve srovnaném pořadí.

## Případová studie 3: `vector` - část I <a id="case-study-3-vector-part-i"></a>

V následující případové studii budeme provádět něco lehce odlišného - místo definování funkce budeme vytvářet objekt. Konkrétně se budeme pokoušet vytvořit neměnitelný n-vektor, který podporuje všechny základní vektorové operace.

Ve funkcionálním programování je často žádoucí definovat _neměnitelné_ objekty, jež nelze po vytvoření měnit, jako jsou řetězce a entice Pythonu. Stejně jako řetězce a entice (tuples) jsou neměnitelné objekty užitečné z celé řady důvodů:
- lze o nich snadněji uvažovat, protože víme že se nemění,
- jsou 'hashable and pickleable', takže je lze použít jako klíče a serializovat,
- jsou výrazně efektivnější, protože vyžadují mnohem méně doprovodných aktivit,
- při kombinaci s 'pattern-matching' mohou být použity jako takzvané **algebraické datové typy** ke snadnému vytváření velkých a složitých datových struktur.

### 2-Vector <a id="2-vector"></a>

Příkaz `data` v Coconut přivádí do Pythonu mocnou utilitu _neměnitelných algebraických datových typů_. Skladbu příkazu `data` si ukážeme na definici jednoduchého dvouprvkového vektoru. Tento vektor bude mít specielní metodu `__abs__`, která spočítá jeho délku, definovanou jako odmocninu součtu čtverců jeho prvků. Zde je:
```coconut
data vector2(x, y):
    """Immutable 2-vector."""
    def __abs__(self):
        """Return the magnitude of the 2-vector."""
        return (self.x**2 + self.y**2)**0.5

# Test cases:
vector2(1, 2) |> print # vector2(x=1, y=2)
vector2(3, 4) |> abs |> print # 5
v = vector2(2, 3)
v.x = 7 # AttributeError
```

Copy, paste! Tento příklad ukazuje základní skladbu příkazů `data`:
```coconut
data <name>(<attributes>):
    <body>
```
kde `<name>` a `<body>` znamenají totéž jako v ekvivalentní definici `class`, avšak `<attributes>` jsou zde různé atributy definovaného datového typu, jež může konstruktor přijmout jako argumenty. V tomto případě je `vector2` datový typ se dvěma atributy `x` a `y`, s jednou metodou `__abs__`, která počítá jeho délku.
Jak ukazují testovací případy, instance datového typu `vector2` lze vytvářet, tisknout, nikoliv však měnit.

### Konstruktor pro n-Vector <a id="n-vector-constructor"></a>

Nyní, když jsme dostali za opasek `2-vector`, vraťme se zpět k našemu původnímu, více komplikovanému problému s n-vektory, to jest s vektory libovolné délky. Pokusíme se, aby náš n-vector podporoval všechny základní vektorové operace ale začneme pouze s definicí `data` a konstruktorem:
```coconut
data vector(pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and pts[0] `isinstance` vector:
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return pts |> tuple |> datamaker(cls) # accesses base constructor

# Test cases:
vector(1, 2, 3) |> print # vector(pts=(1, 2, 3))
vector(4, 5) |> vector |> print # vector(pts=(4, 5))
```

Copy, paste! Velkou novou věcí zde je, jak psát konstruktory `data`. Protože jsou typy `data` neměnitelné, nebude zde chodit konstrukce `__init__`. Místo toho je použita jiná specielní metoda `__new__`, která musí vrátit nově vytvořenou instanci a na rozdíl od většiny metod přijímá jako první argument class, nikoliv objekt. Protože `__new__` potřebuje vrátit úplnou instanci, bude ve většině případů nezbytný přístup k výchozímu konstruktoru `data`. Pro tento účel poskytuje Coconut vestavěnou funkci `datamaker`, která přijímá datový typ, často jako první argument funkce `__new__` a vrací výchozí konstruktor `data`.

V tomto případě konstruktor kontroluje, zda nebylo zadáno nic jiného než další `vector`, v kterémžto případě jej vrací. Jinak vrací výsledek vytvoření entice argumentů a její předání výchozímu konstruktoru, jehož forma je `vector(pts)`; takto přiřazujíc entici k atributu `pts`.

### Metody pro n-vector <a id="n-vector-methods"></a>

Nyní, když máme konstruktor pro náš n-vektor, je čas napsat jeho metody. První je metoda `__abs__`, která má počítat délku vektoru. Tentokrát to bude mírně složitější než u 2-vektoru, protože musí chodit pro libovolný počet `pts`. Naštěstí můžeme použít korýtkový (pipeline) styl Coconutu a jeho částečnou aplikaci funkce:
```coconut
    def __abs__(self):
        """Return the magnitude of the vector."""
        return self.pts |> map$((x) -> x**2) |> sum |> ((s) -> s**0.5)
```
Základním algoritmem zde je 'mapování' (map) mocniny pro každý prvek, jejich celkový součet a druhá odmocnina výsledku. Zápis celého postupu je přehledně zapsán v jednom řádku.

Další metodou je součet vektorů stejné délky, realizovaný součtem jejich komponent. Využijeme k tomu schopnost Coconut provádět porovnávání shody (pattern-matching) či v tomto případě rozložené přiřazení (destructuring assignment) a to takto:
```coconut
    def __add__(self, other):
        """Add two vectors together."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((+), self.pts, other_pts) |*> vector
```

Máme zde několik nových konstruktů ale nejvýznamnějším je příkaz k rozloženému přiřazení `vector(other_pts) = other`, na němž vidíme skladbu pro porovnávání shody s datovými typy: přesně napodobuje originální deklaraci `data` pro daný datový typ. V tomto případě se `vector(other_pts) = other` bude shodovat pouze s vektorem, přičemž přiřadí atribut `pts` vektoru k proměnné `other_pts`. Nenajde-li se vhodný vektor pro shodu, je evokována výjimka `MatchError`.

Dalším novým konstruktem je zde znak `|*>`, což je korýtkový operátor (zde 'star-pipe') pro více argumentů. Rozdíl mezi `|*>` a `|>` je analogický rozdílu `f(args)` a `f(*args)`.

Další metodou je podíl vektorů, což je vlastně součet vektorů se záporným znaménkem (`(-)` místo `(+)`):
```coconut
    def __sub__(self, other):
        """Subtract one vector from another."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((-), self.pts, other_pts) |*> vector
```

Za povšimnutí zde stojí to, že na rozdíl od jiných operátorových funkcí, může `(-)` znamenat buď odečtení nebo negaci. Konkretní význam závisí na počtu poskytnutých argumentů - jeden pro negaci, dva pro odečtení. Abychom si to demonstrovali, použijeme funkci `(-)` k zavedení negace vektoru, což by mělo negovat každý jeho prvek:
```coconut
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return self.pts |> map$((-)) |*> vector
```

Další metodou je rovnost. Zde opět použijeme pattern-matching pro `data` ale tentokrát uvnitř příkazu `match` místo uvnitř rozloženého přiřazení, neboť při selhání shody chceme odezvu `False`, nikoliv chybové hlášení. Zde je kód:
```coconut
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        match vector(=self.pts) in other:
            return True
        else:
            return False
```

Jediným novým kostruktem zde je použití `=self.pts` v příkazu `match`. Tento konstrukt provádí kontrolu uvnitř pattern-matching, zajišťujíce, že ke shodě dojde pouze tehdy, když `other.pts == self.pts`.

Poslední metodou, kterou zavedeme, je násobení vektorů. To je poněkud komplikované, neboť matematicky existuje více způsobů. Pro naše účely se soustředíme na dva: na skalární součin, definovaný jako součet součinů jednotlivých elementů a na násobení vektoru číslem, definované jako násobení všech elementů stejným číslem. Zde je naše implementace:
```coconut
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector # scalar multiple
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other
```

Za pozornost zde stojí za prvé, že na rozdíl od součtu a podílu, kde jsme chtěli hlásit chybu při selhání shody vektoru, zde chceme při selhání shody provést násobení skalárem - takže místo použití rozloženého přiřazení použijeme příkaz `match`.

Za druhé si povšimneme použití kombinace korýtkového (pipeline) stylu programování, částečné aplikace, operátorových funkcí a funkcí vyššího řádu pro výpočet skalárního součinu a pro násobení skalárem. U skalárového součinu mapujeme násobení na dva vektory a sečteme výsledky. U násobení skalárem vytváříme nový vektor násobením všech prvků původního vektoru stejným číslem.

Nakonec to vše dáme dohromady:
```coconut
data vector(pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and pts[0] `isinstance` vector:
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return pts |> tuple |> datamaker(cls) # accesses base constructor
    def __abs__(self):
        """Return the magnitude of the vector."""
        return self.pts |> map$((x) -> x**2) |> sum |> ((s) -> s**0.5)
    def __add__(self, other):
        """Add two vectors together."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((+), self.pts, other_pts) |*> vector
    def __sub__(self, other):
        """Subtract one vector from another."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((-), self.pts, other_pts) |*> vector
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return self.pts |> map$((-)) |*> vector
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        match vector(=self.pts) in other:
            return True
        else:
            return False
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other

# Test cases:
vector(1, 2, 3) |> print # vector(pts=(1, 2, 3))
vector(4, 5) |> vector |> print # vector(pts=(4, 5))
vector(3, 4) |> abs |> print # 5
vector(1, 2) + vector(2, 3) |> print # vector(pts=(3, 5))
vector(2, 2) - vector(0, 1) |> print # vector(pts=(2, 1))
-vector(1, 3) |> print # vector(pts=(-1, -3))
(vector(1, 2) == "string") |> print # False
(vector(1, 2) == vector(3, 4)) |> print # False
(vector(2, 4) == vector(2, 4)) |> print # True
2*vector(1, 2) |> print # vector(pts=(2, 4))
vector(1, 2) * vector(1, 3) |> print # 7
```

Copy, paste! Je to pěkná řádka řádků. Když si to však poučeně procházíme, je to čisté, čitelné a stručné a dělá to přesně to, co jsme chtěli aby to dělalo: vytvořit algebraický datový typ pro neměnitelný n-vektor, který podporuje základní vektorové operace. Celou záležitost jsme přitom provedli čistě funkcionálně bez potřeby imperativních konstruktů, jako jsou stavy nebo smyčky.

## Případová studie 4: `vector_field` <a id="case-study-4-vectorfield"></a>

V poslední případové studii nebudu kód psát já a vy přihlížet, ale budete jej psát vy a já vám posléze ukážu, jak bych to napsal sám.

Premiovou výzvou u tohoto odstavce bude napsat každou definovanou funkci do jednoho řádku. Nápomocna k tomu bude tak zvaná přiřazovací funkce:
```coconut
def <name>(<args>) = <return value>
```
která je zjednodušením klasického zápisu v Pythonu:
```coconut
def <name>(<args>): return <return value>
```

Maje toto vyjasněno, je čas uvést obecný cíl naší případové studie. Chceme napsat program, který nám umožní vytvářet nekonečná vektorová pole, přes něž můžeme iterovat a s nimiž můžeme operovat. Úlohu si zúžime na vektory s pozitivními komponenty.

Naším prvním krokem tedy bude vytvoření pole všech bodů s pozitivními hodnotami `x` a `y`, to jest, nalézajících se v prvním kvadrantu roviny `x-y`, které vypadá nějak takto:
```
...

(0,2)   ...

(0,1)   (1,1)   ...

(0,0)   (1,0)   (2,0)   ...
```

Protože chceme být schopni přes toto pole procházet (iterovat), potřebujeme jej nějakým způsobem linearizovat a nejjednoduším způsobem to učiníme tak, že jej rozdělíme do diagonál, načež můžeme traverzovat po první diagonále, potom po druhé a tak dále, nějak takto:
```
...

(0,2)<  ...
      \_
(0,1)<  (1,1)<  ...
      \_      \_
(0,0) > (1,0) > (2,0) > ...
```

### `diagonal_line` <a id="diagonalline"></a>

Naše první funkce `diagonal_line(n)` by tedy měla vytvořít iterátor všech bodů, reprezentovaných jako souřadnicové entice v `n-té` diagonále, počínaje v bodě `(0, 0)` `nulté` diagonály. Jak jsme si řekli na počátku případové studie, o řešení se pokusíte nejdřív sami s použitím všech nástrojů funkcionálního programování, které Coconut poskytuje.
Zde je několik testů, které můžete použít:
```coconut
diagonal_line(0) `isinstance` (list, tuple) |> print # False (should be an iterator)
diagonal_line(0) |> list |> print # [(0, 0)]
diagonal_line(1) |> list |> print # [(0, 1), (1, 0)]
```

_Nápověda: `n-tá` diagonála by měla obsahovat `n+1` prvků, zkuste tedy začít s funkcí `range(n+1)` a posléze ji nějak přetvořit._

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Nebylo to tak hrozné, že ne? Nyní se podívejme na mé řešení:
```coconut
def diagonal_line(n) = range(n+1) |> map$((i) -> (i, n-i))
```
Prostinké, což? Vezmeme `range(n+1)` a použijeme `map` k její transformaci na potřebnou sekvenci entic.

### `linearized_plane` <a id="linearizedplane"></a>

Nyní, když jsme vytvořili naše diagonální čáry, potřebujeme je spojit dohromady abychom sestavili plně linearizovanou rovinu a za tím účelem napíšeme funkci `linearized_plane()`. Funkce `linearized_plane` by měla vytvořit iterátor, který prochází všemi body roviny po diagonálách, počínaje nultou, prvou, atd. Tento iterátor musí být nekonečný, protože musí procházet všemi body dané roviny.

Nápovědou pro sestavování funkce budiž připomínka, že operátor `::` je líný a nevyhodnotí své operandy bez požádání, což znamená, že může být použit k vytvoření nekonečných iterátorů. Až budete hotovi, posuňte se v textu dále.

Testy:
```coconut
# Note: these tests use $[] notation, which we haven't introduced yet
#  but will introduce later in this case study; for now, just run the
#  tests, and make sure you get the same result as is in the comment
linearized_plane()$[0] |> print # (0, 0)
linearized_plane()$[:3] |> list |> print # [(0, 0), (0, 1), (1, 0)]
```

_Nápověda: místo definování funkce jako `linearized_plane()`, zkuste ji definovat jako `linearized_plane(n=0)`, kde `n` je označení počáteční diagonály a pro rozvinutí funkce použijte rekurzi._

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

To bylo poněkud náročnější než předtím ale doufejme, že ne příliš. Nyní se podívejme na mé řešení:
```coconut
def linearized_plane(n=0) = diagonal_line(n) :: linearized_plane(n+1)
```
Jak vidíte, je to v základě jednoduché řešení: prostě ke spojení diagonál za sebou použijete `::` a rekurzi.

### `vector_field` <a id="vectorfield"></a>

Nyní, když máme funkci, která vytvoří všechny potřebné body, je čas přeměnit je na vektory a za tím účelem si definujeme novou funkci `vector_field()`, která přemění všechny entice v `linearized_plane` na vektory s použitím třídy `n-vector`, kterou jsme definovali dříve.

Testy:
```coconut
# You'll need to bring in the vector class from earlier to make these work
vector_field()$[0] |> print # vector(pts=(0, 0))
vector_field()$[2:3] |> list |> print # [vector(pts=(1, 0))]
```

_Nápověda: Vzpomeňte si, že vektor, který jsme definovali, přijímá komponenty jako separátní argumenty, nikoliv jako jedinou entici._

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Děláte velký pokrok! Než pokročíte dál, srovnejte si řešení se mnou:
```coconut
def vector_field() = linearized_plane() |> map$((xy) -> vector(*xy))
```
Vše, co jsme učinili, bylo to, že jsme mapovali funkci  `linearized_plane` přes `vector` s tím, že jsme volali každý element entice jako separátní argument.

### Applikace <a id="applications"></a>

Nyní, když máme všechny funkce, potřebné pro naše vektorové pole, dáme je všechny dohromady a otestujeme je. Nezdráhejte se dosadit vlastní verze funkcí:
```coconut
data vector(pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and pts[0] `isinstance` vector:
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return pts |> tuple |> datamaker(cls) # accesses base constructor
    def __abs__(self):
        """Return the magnitude of the vector."""
        return self.pts |> map$((x) -> x**2) |> sum |> ((s) -> s**0.5)
    def __add__(self, other):
        """Add two vectors together."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((+), self.pts, other_pts) |*> vector
    def __sub__(self, other):
        """Subtract one vector from another."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((-), self.pts, other_pts) |*> vector
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return self.pts |> map$((-)) |*> vector
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        match vector(=self.pts) in other:
            return True
        else:
            return False
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other

def diagonal_line(n) = range(n+1) |> map$((i) -> (i, n-i))
def linearized_plane(n=0) = diagonal_line(n) :: linearized_plane(n+1)
def vector_field() = linearized_plane() |> map$((xy) -> vector(*xy))

# Test cases:
diagonal_line(0) `isinstance` (list, tuple) |> print # False (should be an iterator)
diagonal_line(0) |> list |> print # [(0, 0)]
diagonal_line(1) |> list |> print # [(0, 1), (1, 0)]
linearized_plane()$[0] |> print # (0, 0)
linearized_plane()$[:3] |> list |> print # [(0, 0), (0, 1), (1, 0)]
vector_field()$[0] |> print # vector(pts=(0, 0))
vector_field()$[2:3] |> list |> print # [vector(pts=(1, 0))]
```

Copy, paste! Poté, co jste se ujistili, že po dosazení svých funkcí chodí vše jak má, zaměřte se na poslední čtyři testy. Zjistíte, že používají novou notaci, podobnou notaci pro částečnou aplikaci, již jsme viděli dříve - ale s hranatými závorkami místo kulatých. To je notace pro krájení (slicing) iterátoru. Podobně jako byla částečná aplikace líným voláním funkce, je dělení iterátoru _línym dělením sekvence_. Podobně jako u částečné aplikace, je užitečné považovat znak `$` za _zlenivějící_  (lazy-ify) operátor, v tomto případě přetvářející normální (ihned prováděné) krájení (slicing) Pythonu na líné krájení iterátoru, které se provádí jen tehdy, jsou-li prvky v řízcích (slice) potřebné.

Maje toto na mysli, nyní když jsme sestavili naše vektorové pole, je čas si s krájením iterátoru trochu pohrát. Zkuste něco smělého, jako například
- vytvořit `magnitude-field`, kde každý bod reprezentuje délku příslušného vektoru
- zkombinovat celá vektorová pole aplikací funkce `match` na dříve vytvořené metody dělení a násobení

potom použít krájení iterátoru pro vynětí a přezkoušení úseků.

## Případová studie 5: `vector` - část II <a id="case-study-5-vector-part-ii"></a>

U některých aplikací, používajících naše `vector_fields`, může být žádoucí přidat k našemu `vektoru` nějaké užitečné metody. V této případové studii se zaměříme na metodu, zvanou `.angle`.

Metoda `.angle` přijme dva vektory a spočítá úhel mezi nimi. Matematicky je úhel dvou vektorů skalárním součinem jejich příslušných jednotkových vektorů. Takže před tím, než budeme moci použít metodu `.angle`, budeme potřebovat metodu `.unit`. Matematicky je výraz pro jednotkový vektor daného vektoru dán jako podíl tohoto vektoru a jeho velikosti. Tudíž, před použitím `.unit` a potažmo `.angle`, musíme začít zavedením dělení.

### `__truediv__` <a id="truediv"></a>

Dělení vektorů je pouhé skalární dělení, pročež napíšeme metodu `__truediv__`, která přijímá `self` jako první argument a `other` jako druhý argument, vracejíc nový vektor téže velikosti jako `self`, s prvky dělenými vektorem `other`. Jako specielní výzvu, zkuste to zapsat v jediném řádku s použitím notace přiřazovací funkce.

Testy:
```coconut
vector(3, 4) / 1 |> print # vector(pts=(3.0, 4.0))
vector(2, 4) / 2 |> print # vector(pts=(1.0, 2.0))
```

_Nápověda: Podívejte se zpět, jak jsme zaváděli násobení skalárem._

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Zde je mé řešení pro vaši kontrolu:
```coconut
    def __truediv__(self, other) = self.pts |> map$((x) -> x/other) |*> vector
```

### `.unit` <a id="unit"></a>

Další je `.unit`. Napíšeme metodu `unit`, která přijímá jako argument pouze `self` a vrací nový vektor téže velikosti jako `self`, s každým prvkem děleným velikostí `self`, jež můžeme získat pomocí funkce `abs`. To by měl být velmi jednoduchý jedořádkový zápis.

Testy:
```coconut
vector(0, 1).unit() |> print # vector(pts=(0.0, 1.0))
vector(5, 0).unit() |> print # vector(pts=(1.0, 0.0))
```

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Zde je mé řešení:
```coconut
    def unit(self) = self / abs(self)
```

### `.angle` <a id="angle"></a>

Tato metoda bude poněkud složitější. Připomeňme, že matematicky se úhel mezi dvěma vektory vyjádří jako `math.acos` skalárního součinu obou vektorů, připadně jejich jednotkových vektorů a připomeňme si, že jsme již zavedli skalární součin dvou vektorů, když jsme napsali metodu `__mul__`. Takže, metoda `.angle` má přijmout `self` jako první argument a `other` jako druhý - a je-li `other` vektorem, použít tuto formuli k výpočtu úhlu mezi `self` `other`, nebo není-li `other` vektorem, má metoda `.angle` ohlásit `MatchError`. Abychom to zajistili, budeme potřebovat rozložené přiřazení k ověření, že `other` je skutečně vektor.

Testy:
```coconut
import math
vector(2, 0).angle(vector(3, 0)) |> print # 0.0
print(vector(1, 0).angle(vector(0, 2)), math.pi/2) # should be the same
vector(1, 2).angle(5) # MatchError
```

_Nápověda: Podívejte se zpět, jak jsme s použitím rozloženého přiřazení kontrolovali, zda argument pro `factorial` bylo celé číslo._

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

Pohleďte na mé řešení:
```coconut
    def angle(self, other is vector) = math.acos(self.unit() * other.unit())
```

A nyní je čas to dát všechno dohromady. Nezdráhejte se dosadit své vlastní verze posledně definovaných metod.

```coconut
import math # necessary for math.acos in .angle

data vector(pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        if len(pts) == 1 and pts[0] `isinstance` vector:
            return pts[0] # vector(v) where v is a vector should return v
        else:
            return pts |> tuple |> datamaker(cls) # accesses base constructor
    def __abs__(self):
        """Return the magnitude of the vector."""
        return self.pts |> map$((x) -> x**2) |> sum |> ((s) -> s**0.5)
    def __add__(self, other):
        """Add two vectors together."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((+), self.pts, other_pts) |*> vector
    def __sub__(self, other):
        """Subtract one vector from another."""
        vector(other_pts) = other
        assert len(other_pts) == len(self.pts)
        return map((-), self.pts, other_pts) |*> vector
    def __neg__(self):
        """Retrieve the negative of the vector."""
        return self.pts |> map$((-)) |*> vector
    def __eq__(self, other):
        """Compare whether two vectors are equal."""
        match vector(=self.pts) in other:
            return True
        else:
            return False
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector # scalar multiplication
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other
    # New one-line functions necessary for finding the angle between vectors:
    def __truediv__(self, other) = self.pts |> map$((x) -> x/other) |*> vector
    def unit(self) = self / abs(self)
    def angle(self, other is vector) = math.acos(self.unit() * other.unit())

# Test cases:
vector(3, 4) / 1 |> print # vector(pts=(3.0, 4.0))
vector(2, 4) / 2 |> print # vector(pts=(1.0, 2.0))
vector(0, 1).unit() |> print # vector(pts=(0.0, 1.0))
vector(5, 0).unit() |> print # vector(pts=(1.0, 0.0))
vector(2, 0).angle(vector(3, 0)) |> print # 0.0
print(vector(1, 0).angle(vector(0, 2)), math.pi/2) # should be the same
vector(1, 2).angle(5) # MatchError
```
_Jedna důležitá poznámka: dejte si pozor abyste nenechali prázdný řádek při dosazování vlastních metod, neboť v tom případě by interpret roztrhl kód. V normálním zápisu Coconut to není žádný problém, pouze zde, protože provádíme kopírování-vkládání do příkazového řádku_

Copy, paste! Jestliže všechno chodí jak má, doporučuji se vrátit ke hrátkám s [aplikacemi](#aplikace) `vector_field` s použitím našich nových metod.

## Vyplnění mezer <a id="filling-in-the-gaps"></a>

Tímto vyčerpal tento tutoriál své případové studie, avšak to neznamená, že Coconut předvedl všechny své možnosti! V tomto posledním odstavci se dotkneme tří nejdůležitějších struktur, jež se nám podařilo opominout v případových studiích: líné seznamy, skladba funkcí a implicitní parciály (partials).

### Líné seznamy <a id="lazy-lists"></a>

Líné seznamy jsou líně vyhodnocované iterátorové literály, podobné ve své lenosti operátoru `::` - a to v tom, že jakýkoli výraz uvnitř líného seznamu není vyhodnocen, dokud jej není zapotřebí. Syntaxe pro líné seznamy je přesně táž jako syntaxe pro normální seznamy, až na "banánové závorky" (`(|` and `|)`) místo normálních závorek, takto:
```coconut
abc = (| a, b, c |)
```

### Skladba funkcí <a id="function-composition"></a>

Skladba funkcí v Coconut se zajišťuje operátorem `..`, který přijímá dvě funkce a spojí je do nové funkce, ekvivalentní zápisu `(*args, **kwargs) -> f1(f2(*args, **kwargs))`. To může být užitečné u částečné aplikace při spojování několika funkcí vyššího řádu, jako zde:
```coconut
zipsum = map$(sum)..zip
```

Skladba funkcí se také zbavuje potřeby mnoha závorek při zřetězeném volání funkcí, jako zde:
```coconut
(plus1..square)(3) == 10
```

### Implicitní parciály <a id="implicit-partials"></a>

Coconut podporuje řadu různých "neúplných" výrazů, jež se rozvinou do funkce, která přijme jen část argumentů, nezbytných pro dokončení, to jest do funkce s implicitně částečnou aplikací. Různé přípustné výrazy jsou:
```coconut
.attr
.method(args)
obj.
func$
seq[]
iter$[]
.[slice]
.$[slice]
```

### Další čtení <a id="further-reading"></a>

Všechny vlastnosti popsané v tomto tutoriálu, stejně jako řada dalších, jsou podrobně dokumentovány v podrobné dokumentaci Coconut [DOCS.html](http://coco-cs.readthedocs.io/es/master/DOCS.html).

Also, if you have any other questions not covered in this tutorial, feel free to ask around at Coconut's [Gitter](https://gitter.im/evhub/coconut), a GitHub-integrated chat room for Coconut developers.

Finally, Coconut is a new, growing language, and if you'd like to get involved in the development of Coconut, all the code is available completely open-source on Coconut's [GitHub](https://github.com/evhub/coconut). Contributing is a simple as forking the code, making your changes, and proposing a pull request.
