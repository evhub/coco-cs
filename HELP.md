# Tutoriál

```eval_rst
.. contents::
    :local:
```

## Úvod 

Vítejte v tutoriálu pro [Coconut Programming Language](http://evhub.github.io/coconut/)! Coconut je varianta [Pythonu](https://www.python.org/) vytvořená pro **jednoduché, elegantní Pythonické functionální programování**.

Proč používat Coconut? Coconut rozšiřuje repertoár programátora v Pythonu o nástroje moderního funkcionálního programování. Kód Coconut běží na obou verzích Pythonu (2/3), činíce tak toto rozdělení věcí minulosti.

Coconut přidává do Pythonu _syntaktickou podporu_ pro:

- pattern-matching - vyhledávání shody s předlohou
- algebraic data types (ADT) - algebraické datové typy 
- destructuring assignment - rozložené přiřazení
- partial application - částečnou aplikaci
- lazy lists - líné seznamy
- function composition - skládání funkcí
- prettier lambdas - úhlednější lambdy
- infix notation - infixovou notaci 
- pipeline-style programming - směrované programování
- operator functions - operátorové funkce
- tail recursion optimization - optimalizace koncové rekurze
- parallel programming - paralelní programování

a mnoho dalšího!

### Instalace 

Ve své podstatě je Coconut kompilátor, který převádí kód v Coconut na kód v Pythonu. To znamená, že tam, kde lze použít skript Pythonu, lze také použít skript Coconut. Pro přístup k tomuto kompilátoru poskytuje Coconut utilitu CLI (command line interface), která dovede:

- kompilovat jednotlivé soubory nebo celé projekty,
- překládat za pochodu kód Coconut,
- včlenit se (hook into) do existujících aplikací Pythonu, jako IPython/Jupiter a MyPy.

Instalace Coconut je velmi jednoduchá:

1. instalujte [Python](https://www.python.org/downloads/),
2. otevřte konzolu s příkazovým řádkem
3. a zadejte:
```
pip install coconut
```

_Note: Setkáváte-li se s chybami, zkuste spustit výše uvedený příkaz s flagem `--user`. Ujistěte se, že umístění instalace Coconut (v Unixu `/usr/local/bin` pokud jste nepoužil `--user` nebo `${HOME}/.local/bin/`) pokud ano je uvedeno v proměnné prostředí `PATH`. Pokud se při instalaci pomocí `pip`stále vyskytují chyby, můžete instalovat Coconut pomocí `conda` podle těchto [pokynů](DOCS.html#using-conda)._

Pro kontrolu, že instalace proběhla správně, zkuste na příkazový řádek zadat
```
coconut -h
```
což by mělo zobrazit nápovědu pro Coconut.

_Note: If you're having trouble installing Coconut, or if anything else mentioned in this tutorial doesn't seem to work for you, feel free to [ask for help on Gitter](https://gitter.im/evhub/coconut) and somebody will try to answer your question as soon as possible._

### Bez instalace

Chcete-li používat Coconut bez jeho instalování, zkuste [online interpreter](https://cs121-team-panda.github.io/coconut-interpreter).

## Začínáme 

### Použití překladače 

Nyní, když máte Coconut nainstalovaný, zkusíme s ním něco provádět. Překladač (interpret) spustíte z příkazového řádku zápisem
```
coconut
```
načež byste měl číst něco jako
```coconut
Coconut Interpreter:
(type 'exit()' or press Ctrl-D to end)
>>>
```
což je oznámení Coconut, že je připraven pro zadávání a vyhodnocování kódu. Tož pusťme se do toho!

Pro případ, že jste to dříve přehlédli - _veškerý platný Python 3 je platný Coconut_. To neznamená, že kompilovaný Coconut poběží pouze na Python 3, protože poběží stejně i na Python 2, ale že pouze kód Python 3 je spolehlivě kompilován do kódu Coconut.

Z toho vyplývá, že jste-li důvěrně seznámen s Pythonem, jste již z větší části seznámen se skladbou Coconut a jeho celou standardní knihovnou. Zkusme pro ukázku zadat nějaký jednoduchý kód Pythonu do překladače Coconut:

```coconut_pycon
>>> "hello, world!"
'hello, world!'
>>> 1 + 1
2
```
### Psaní zdrojových souborů

Zajisté - být schopen za pochodu interpretovat kód Coconutu, je báječné - bylo by to však málo prospěšné bez schopnosti psát a kompilovat větší programy. Sestavení jednoduchého programu "hello, world!" si nyní ukážeme.

Nejprve vytvoříme soubor, do něhož svůj kód vložíme. Přípona zdrojových souborů pro Coconut je `.coco`, takže vytvořte soubor `hello_world.coco`. Poté byste měl věnovat čas nastavení vašeho textového editoru na řádné zvýrazňování kódu Coconut. Příslušné pokyny naleznete v dokumentaci [Zvýraznění skladby](DOCS.html#syntax-highlighting).

Nyní do našeho souboru `hello_world.coco` vložíme kód. Na rozdíl od Pythonu, jehož záhlaví jsou obvyklá a často nezbytná,
```coconut_python
#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from __future__ import print_function, absolute_import, unicode_literals, division
```
provede to kompilátor Coconut za nás automaticky, takže se o formální nezbytnosti vůbec nemusíme starat a můžeme se věnovat přímo svému kódu. Vložíme tedy kód našeho programu "hello, world!".

V Python 3 je text programu tento:
```coconut_python
print("hello, world!")
```
Byť tento kód chodí v Coconut také, lze jej specielně pro Coconut napsat v alternativní pojítkové formě (pipeline-style):
```coconut
>>> "hello, world!" |> print
```
Na příkladu pěkně vidíme, jak operátor Coconutu `|>` umožňuje pojítky směrované (pipeline-style) programování: předává objekt z funkce do funkce s postupně odlišnými operacemi. V tomto případě vkládáme objekt `"hello, world!"` do operace `print`. 
Uložme nyní náš jednoduchý program "hello, world!" program a zkusme jej spustit.

### Použití kompilátoru 

Kompilování souborů a projektů utilitou CLI je vemi jednoduché. Nacédujeme (`cd`) se do adresáře se souborem `hello_world.coco` a zapíšeme
```
>>> coconut hello_world.coco
```
což vytvoří výstup
```
Coconut: Compiling         hello_world.coco ...
Coconut: Compiled to       hello_world.py .
```
a nově vytvořený soubor `hello_world.py` vloží do stejného adresáře jako `hello_world.coco`. Potom je možné tento soubor spustit příkazem
```
>>> python hello_world.py
```
což by mělo v konzole vyprodukovat výstup `hello, world!`.

_Note: Můžete provést kompilaci a spuštění v jednom kroku, použijete-li flag `--run` (zkráceně `-r`).

Kompilování jednotlivých souborů postupně není jediný způsob jejich kompilace. Můžeme také kompilovat všechny soubory v daném adresáři najednou a to pouhým uvedením názvu adresáře jako prvního argumentu. Máme-li například soubory `havel.coco` a `ravel.coco` v adresáři `F:\codetest\coconut\compil`, zařídíme jejich kompilaci příkazem
```
F:\codetest\coconut\compil> coconut ./
Compiling        havel.coco ...
Compiled to      havel.py
Compiling        ravel.coco ...
Compiled to      ravel.py
```
V adresáři `compil` se navíc vytvoří soubor `__coconut__.py`.

Kompilátor si sám vyhledá všechny kompilovatelné soubory a vytvoří pomocný soubor `__coconut__.py`, do něhož uloží potřebné informace z jednotlivých souborů.

Kompilátor Coconutu podporuje velké množství různých kompilačních možností - viz nápověda `coconut -h`. Nejužitečnější z nich je opce `--linenumbers` (nebo zkráceně `-l`), která přidává čísla řádků ze zdrojového kódu do kompilovaného kódu, umožňujíce tak při ladění vidět číslo zdrojového kódu, odpovídající chybujícímu řádku kompilovaného kódu.

_Note: Nepotřebujete-li plnou kontrolu kompilátoru, můžete použít [automatickou kompilaci](DOCS.html#automatic-compilation).

### Použití IPython/Jupyter 

Coconut usiluje o rozsáhlou podporu zavedených nástrojů pro vědecké výpočty v Pythonu.

Za tím účlem poskytuje Coconut podporu aplikace [IPython/Jupiter](DOCS.html#ipython-jupyter-support). Pro spuštění notebooku Jupytera s Coconut jako jádrem, použijete příkaz
```
coconut --jupyter notebook
```

### Případové studie 

Protože byl Coconut vytvořen se záměrem aby byl užitečný, bude nejlépe jej předvést v akci při řešení konkrétních problémů, které jsou v tomto tutoriálu označeny jako případové studie.

Tyto případové studie ovšem nepřinášejí úplný přehled všech vlastností Coconut. Ten lze nalézt v obsáhlé [dokumentaci](DOCS.html). 

## Případová studie 1: `factorial` 

V první studii budeme definovat funkci `factorial`, to jest funkci, která počítá součin `n!`, kde `n` je celé číslo `>= 0`. 
To je poněkud dětinský příklad, protože tuto úlohu zvládne Python snadno také ale poslouží k demonstraci některých základních vlastnoctí Coconut a jejich výhodného použití.

Nejprve musíme rozhodnout, jaký způsob výpočtu faktoriálu budeme chtít. Možných způsobů řešení je více ale pro jednoduchost se omezíme na čtyři hlavní kategorie: imperativní, recurzivní, iterativní a s použitím `addpattern`.

### Imperativní metoda 

Imperativní přístup bychom při psaní `factoriálu` použili v jazyce typu C. Imperativní přístupy zahrnují mnohé změny stavu, kdy jsou pravidelně měněny proměnné při procházení smyčkou. Imperativní přístup v Coconut k problému `factorial` vypadá nějak takto:
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
Předtím, než se budeme podrobně zabývat průběhem výpočtu, prověřme si nejprve jeho testovací případy. Kdybychom psali skutečný program, uložili bychom jej do souboru, jenž bychom kompilovali ale protože si jenom zkoušíme věci, vystačíme si s překopírováním kódu do překladače. Měli bychom dostat dvakrát `TypeError`, potom `1` a `6`.

Nyní, když jsme si ověřili, že nám kód chodí správně, pohleďmě o co v něm kráčí. Protože je imperativní přístup zcela nefunkcionální, Coconut nám v tomto případě příliš nepomůže. Avšak i zde použití infixové notace (vložení funkce mezi své argumenty `n` a `int`: `` n `isinstance` int `` ) činí kód čistší a čitelnější.

### Rekurzivní metoda 

Rekurzivní přístup je první ze zcela funkcionálních přístupů a to v tom, že nezahrnuje změnu stavu a smyčky jako u imperativního přístupu. Rekurzivní přístup se vyhýbá potřebě měnit proměnné tím, že tato změna je implicitně zahrnuta v rekurzivním volání funkce. Zde je rekurzivní přístup k problému `factorial`:
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    case n:
        match 0:
            return 1
        match x is int if x > 0:
            return x * factorial(x-1)
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")

# Test cases:
-1 |> factorial |> print # TypeError
0.5 |> factorial |> print # TypeError
0 |> factorial |> print # 1
3 |> factorial |> print # 6
```

Překopírujte si kód a testy do překladače. Měl byste dostat stejné vysledky jako v imperativní verzi.

Proberme si specifika syntaxe v tomto příkladu. Příkaz `case n:` spouští blok se dvěma příkazy `match`. Každý příkaz `match` se pokouší porovnat svou deklaraci (pattern) s argumentem bloku `case`. Příkaz `else` se provede jen v případě absence jakékoliv shody.

Konkretně v tomto příkladě ověřuje `match`, zda je `n` shodné s `0`. Pakliže ano, provede se `return 1`. Pokud ne, prověřuje se druhý `match`, v němž je zavedena lokální poměnná `x` s počáteční hodnotou `x = n` a v níž je opakovaně (rekurzivně) volána funkce `factorial(x)` pro snižující se hodnotu argumentu. V okamžiku, kdy `x=1`, vrátí příkaz `return` součin čísel `1` až `n-1`. Pokud se neprovede žádný z obou příkazů, příkaz `else` spustí a provede `raise TypeError("argument faktoriálu musí být celé číslo >= 0")`. 

I když je tento příklad velmi prostý, je postup v něm použitý,  jedním z nejmocnějších i nejsložitějších postupů v Coconut. Tento postup se nazývá  **pattern-matching** neboli  _porovnávání s předlohou_. Jak jsme viděli, pivotním slovem v tomto konstruktu je klíčové slovo `match`, které jsme v našem příkladě používali opakovaně pro ověření různých případů (`case`).

Jako intuitivní vodítko si lze představit _přiřazení_ tam, kde vidíme klíčové slovo `match`.  Případně si lze uvědomit, že všechny příkazy `match` mohou být konvertovány na ekvivalentní příkazy rozkladného (destructuring) přiřazení, které jsou rovněž platným konstruktem Coconut. V tomto případě by ekvivalentním `rozkladným přiřazením` k funkcí `factorial` nahoře bylo:
 
```coconut
def factorial(n):
    """Compute n! where n is an integer >= 0."""
    try:
    # Jediná hodnota, kterou lze přiřadit k 0 je 0, protože 0
	# je neměnitelná konstanta; proto přiřazení selže pokud n=!0:
       0 = n
	except MatchError:
	   pass
	else:
       return 1
    try
    # To se pokusí přiřadit n k x, jež bylo deklarováno jako
	# int; protože k int může být přiřazen pouze int,            # následující  podmínka selže, nebude-li n celým číslem:
       x is int = n
	except MatchError:
	   pass
	else: if x > 0:   # v Coconut lze ze else použít if, match, try
       return x * factorial(x-1)
	raise TypeError("argumentem pro faktorial musí být int >= 0")

# Test cases:
-1 |> factorial |> print  # TypeError
0.5 |> factorial |> print  # TypeError
0 |> factorial |> print  # 1
3 |> factorial |> print  # 6	
```

Nejprve copy and paste! I když by toto rozkladné přiřazení mělo pracovat, je mnohem nemotornější než příkaz `match` v případě, že očekáváte, že by mohlo dojít k selhání, což je důvod pro existenci příkazu `match`. Ekvivalent rozkladného (destructuring) přiřazení však objasňuje, co přesně pattern-matching dělá - ukazujíc na to, že příkazy `match` jsou vlastně něco jako příkazy rozkladného přiřazení. 

In fact, to be explicit about using destructuring assignment instead of normal assignment, the `match` keyword can be put before a destructuring assignment statement to signify it as such.
	
Při používání příkazů pro pattern-matching a destructuring assignment v dalších uázkách bude užitečné, když si pomyslíme _přiřazení_ pokaždé, když uvidíme klíčové slovo `match`.

Dalším snadným vylepšením naší funkce `factorial` je použití žolíkového označení  `_`. Vlastně nepotřebujeme přiřadit `x` jako novou proměnnou, protože má stejnou hodnotu jako `n`, takže když použijeme `_` místo `x`, Coconut tuto proměnnou vlastně nikdy nepřiřadí. Naši funkci `factorial` můžeme tedy přepsat takto:
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
-1 |> factorial |> print  # TypeError
0.5 |> factorial |> print  # TypeError
0 |> factorial |> print  # 1
3 |> factorial |> print  # 6
```

Copy, paste! Tato nová funkce `factorial` by se měla chovat úplně stejně jako předtím.

Až dosud jsme se u rekurzivní metody zabývali pouze porovnáním předlohy (pattern matching) ale ve skutečnosti existuje další způsob, jímž můžeme vylepšit naši funkci `factorial`. Coconut provádí automatickou optimalizaci koncového volání, což znamená že kdykoli funkce přímo vrací volání jiné funkce, zadrží (optimalizuje) Coconut další volání. Naši funkci `factorial` tedy přepíšeme pro použití koncového volání (tail call):
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

Copy, paste! Tato nová funkce `factorial` je ekvivalentní originální verzi s tou výjimkou, že nikdy nevyvolá `RuntimeError` v důsledku dosažení maximální hloubky rekurze v Pythonu, protože Coconut odstaví (optimalizuje) koncové rekurzivní volání.

### Iterativní metoda 

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

Copy, paste! Tato definice se od rekurzivní definice liší pouze v jednom řádku, což je záměrné, protože jak iterativní, tak rekurzivní přístupy jsou funkcionální. Odlišný řádek je tento:
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

Nejprve operátorová funkce. Operátorová funkce se v Coconut vytvoří uzavřením operátoru do závorek. V tomto případě je `(*)` zhruba ekvivalentní výrazu v Pythonu: `lambda x, y: x*y`. Ve skladbě lambdy v Coconut je `(*)` rovněž ekvivalentí zápisu `(x, y) -> x*y`, jenž budeme odteďka používat pro všechny lambdy, byť obě formy jsou v Coconut legální. 

_Note: Kdybychom povolili režim `--strict`, jenž hlídá náš kód z hlediska úpravy textu, dostali bychom chybové hlášení, kdykoliv bychom použili příkaz `lambda` Pythonu._

Nyní k částečné aplikaci funkce. Lze si myslet, že částečná aplikace je _volání líné funkce_ s operátorem lenosti `$`, kde _lenost_ znamená: "nevyhodnocuj, dokud nemusíš". Je-li v Coconut volání funkce předznamenáno znakem `$`, jako v tomto případě, je normální provedení funkce nahrazeno novou funkcí s již poskytnutými argumenty, takže je funkce volána jak pro částečně použité argumenty, tak pro nové argumenty (v tomto pořadí). V tomto případě je `reduce$(*)` ekvivalentní k `(*args, **kwargs) -> reduce((*), *args, **kwargs)`.

Spojíme-li to vše dohromady, vidíme jak jediný řádek kódu
```coconut
range(1, n+1) |> reduce$(*)
```
je schopen spočítat celý faktoriál bez použití stavů či smyček, pouze s použitím funkcí vyššího řádu funkcionálním stylem.

S nástroji Coconut, které zde používáme, jako je částečná aplikace  (`$`), usměrněné (pipeline-style) programování (`|>`), funkce vyššího řádu (`reduce`) a operátorové funkce (`(*)`) je možné sestavovat funkcionální programy snadno a úhledně.

### Metoda `addpattern` 

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

Použijeme-li vestavěnou funkci  [`addpattern`](DOCS.html#addpattern), můžeme zredukovat tři identační úrovně na jednu. Pohleďte:
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
Copy, paste! Tato verze by měla pracovat stejně jako předchozí, až nato že místo `TypeError` vrací hlášení `MatchError`. Máme zde tři nové koncepty k prodiskutování: `addpattern`, zápis přiřazovací funkce a definici funkce pro porovnání předlohy (pattern-matching).

*Nejprve* zápis přiřazovací funkce. To je docela prosté. Je-li funkce definována s rovnítkem `=` místo dvojtečkou `:`, musí být poslední řádek výrazem, jenž je také automaticky vracen.

*Dále* definice porovnávací (pattern-matching) funkce. Tato definice zajišťuje provedení přesně toho, co je uvedeno v názvu - porovnání všech argumentů funkce se zadaným vzorem. Pokud se vzor neshoduje s žádným z argumentů (nebo je-li zadán nesprávný počet argumentů), vyvolá funkce chybové hlášení `MatchError`. Chcete-li explicitně deklarovat definici p-m funkce, můžete přidat `match` před `def`.

*Za třetí*, `addpattern`. Dekorátor `addpattern` přijímá jako argument předtím definovanou p-m funkci a vrací dekorátor, který dekoruje novou m-p funkci přidáním nového vzoru jako další případ (case) ke starým vzorům. Dekorátor `addpattern` dělá tedy přesně to, co říká - přidává další vzor k existující p-m funkci.


Dekorátorem `addpattern` můžeme přepsat nejenom imperativní přístup, jak jsme právě provedli, ale můžeme také přepsat rekurzivní přístup, jak vidno zde:
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
Copy, paste! Mělo by to chodit stejně jako předtím, kromě toho, že (stejně jako předtím) je `TypeError` nahrazen `MatchError`.

## Případová studie 2: `quick_sort` 

Ve druhé případové studii budeme používat algoritmus [quick sort](https://en.wikipedia.org/wiki/Quicksort). Použijeme dvě verze: funkci `quick_sort`, která přijímá i vrací seznam a tutéž funkci, která přijímá i vrací iterátor.

### Třídění sekvence 

Nejprve `quick_sort` pro seznamy. Použijeme rekurzivní přístup založený na dekorátoru `addpattern` - podobný k přístupu, použitého u posledně psané funkce `factorial` k omezení počtu odsazení. Bez dalších okolků, zde je naše implementace `quick_sort` pro seznamy:
```coconut
def quick_sort([]) = []


@addpattern(quick_sort)
def quick_sort([head] + tail) =
    """Sort the input sequence using the quick sort algorithm."""
	
    (quick_sort([x for x in tail if x < head])
        + [head]
        + quick_sort([x for x in tail if x >= head]))

# Test cases:
[] |> quick_sort |> print # []
[3] |> quick_sort |> print # [3]
[0,1,2,3,4] |> quick_sort |> print # [0,1,2,3,4]
[4,3,2,1,0] |> quick_sort |> print # [0,1,2,3,4]
[3,0,4,2,1] |> quick_sort |> print # [0,1,2,3,4]
```
Copy, paste! Zde jsou pouze dvě nové věci: head-tail pattern-matching a příkazy `where`. 

Příkazy `where` velmi průzračné a jistě jste jejich působení sami objevili. Příkaz `where` je způsob výpočtu pro vložené upřesnění.

Head-tail pattern-matching ('porovnání předlohy od čela až po chvost'), zde vidíme jako`[head] + tail`, jenž má formu seznamu nebo entice přidanou k proměnné. Když se tato forma vyskytne v jakémkoli p-m kontextu, je s porovnávanou hodnotou zacházeno jako se sekvencí, seznamem nebo enticí porovnávanou s počátkem této sekvence, jejiž zbytek je vázán k proměnné. V tomto případě používáme schema head-tail, abychom odstranili čelo, jež můžeme použít jako pivot pro rozštěpení zbytku seznamu.

### Třídění iterátoru 

Nyní vyzkoušíme `quick_sort` pro iterátory. Náš způsob řešení problému bude kombinace rekurzivního a iterativního přístupu, jež jsme použili u `factoriálu`, a sice v tom, že budeme lenivě a rekurzivně vytvářet iterátor. Zde je kód:
```coconut
def quick_sort(l):
    """Sort the input iterator, using the quick sort algorithm"""
	
    match [head] :: tail in l:
        tail = reiterable(tail)
        yield from (quick_sort((x for x in tail if x < head))
            :: (head,)
            :: quick_sort((x for x in tail_ if x >= head))
            )
    # We implicitly return an empty iterator here if the match falls through.			

# Test cases:
[] |> quick_sort |> list |> print # []
[3] |> quick_sort |> list |> print # [3]
[0,1,2,3,4] |> quick_sort |> list |> print # [0,1,2,3,4]
[4,3,2,1,0] |> quick_sort |> list |> print # [0,1,2,3,4]
[3,0,4,2,1] |> quick_sort |> list |> print # [0,1,2,3,4]
```
Copy, paste! Tento `quick_sort` algoritmus používá řadu nových konstruktů, takže hrr na ně.

Nejprve je to operátor `::`, který se zde objevuje jak v porovnávání shody (pattern-matching), tak samostatně. V podstatě to je líný operátor `+` pro iterátory, který spojuje nebo řetězí líně dva iterátory, nic nevyhodnocujíc, není-li žádáno; lze jej použít pro vytváření nekonečných iterátorů. V porovnání shody tuto operaci invertuje, rozkládaje (destructuring) počátek iterátoru na předlohu a zbytek, který váže k proměnné.

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
která eliminuje potřebu další úrovně identace při provedení pouze jednoho `match`.

Třetím novým konstruktem je [`reiterable`](DOCS.html#reiterable). Při realizaci neměnitelného funkcionálního programování s iterátory Pythonu se vyskytuje tento problém: kdykoliv se přistoupí k elementu iterátoru, je ztracen. Procedura `reiterable` umožňuje, aby byl volaný iterábl iterován opakovaně, poskytujíc pro stejné vstupy stejné výstupy.

Konečně, byť se nejedná o nový konstrukt, protože existuje v Python 3, naše použití `yield from` si zasluhuje zmínky. V Pythonu se příkaz `yield`, který pracuje podobně jako `return`, používá k vytváření iterátorů - s tou výjimkou, že se `yield` může vyskytnout vícekrát , pokaždé vraceje jiný element. Forma `yield from` je velmi podobná, až na to, že místo přidání jediného elementu do vytvářeného iterátoru přidává jiný celý iterátor.

Spojíme-li to všechno dohromady, máme zde opět naši funkci `quick_sort`:

```coconut
def quick_sort(l):
    """Sort the input iterator, using the quick sort algorithm."""
    match [head] :: tail in l:
        tail = reiterable(tail)
        yield from (quick_sort((x for x in tail if x < head))
            :: (head,)
            :: quick_sort((x for x in tail_ if x >= head))
            )
	# We implicitly return an empty iterator here if the match falls through.		
```

Funkce se nejprve pokouší rozdělit (split) seznam `l` na počáteční element a zbývající iterátor. Je-li `l` prázdným iterátorem, porovnání selže, poskytujíce prázdný iterátor (takto funkce ošetřuje základní případ). V opačném případě vytváříme kopii zbytku iterátoru a poskytujeme (yield) spojení: (quick-sort všech zbývajících elementů menších než počáteční element) + (počáteční element) + (quick-sort všech zbyvajících elementů větších než počáteční element).

Výhody zde použitého základního přístupu s četným použitím iterátorů a rekurzí, v porovnání s klasickým imperativním přístupem, jsou mnohé. Za prvé je náš přístup čistší a čitelnější, protože popisuje co **je** `quick_sort` místo **jak** by měl být použit. Za druhé je náš přístup _líný_ v tom, že náš `quick_sort` nic nevyhodnocuje bez vyžádání. A konečně, byť to není relevantní pro `quick_sort`, je to relevantní v mnoha jiných případech, jejichž příklady ještě v tomto tutoriálu uvidíme, náš přístup umožňuje pracovat s _nekonečnými_ řadami jako by byly skutečně nekonečné.

Coconut činí programování s takto výhodným funkcionálním přístupem výrazně snadnější. V tomto příkladě nám  `pattern-matching` Coconutu umožňuje snadné dělení daného iterátoru a jeho slučovací operátor `::` nám umožňuje jej vrátit zpět ve srovnaném pořadí.

## Případová studie 3: `vector` - část I 

V následující případové studii budeme provádět něco lehce odlišného - místo definování funkce budeme vytvářet objekt. Konkrétně se budeme pokoušet vytvořit neměnitelný n-vektor, který podporuje všechny základní vektorové operace.

Ve funkcionálním programování je často žádoucí definovat _neměnitelné_ objekty, jež nelze po vytvoření měnit, jako jsou řetězce a entice Pythonu. Stejně jako řetězce a entice (tuples) jsou neměnitelné objekty užitečné z celé řady důvodů:
- lze o nich snadněji uvažovat, protože víme že se nemění,
- jsou 'hashable and pickleable', takže je lze použít jako klíče a serializovat,
- jsou výrazně efektivnější, protože vyžadují mnohem méně doprovodných aktivit,
- při kombinaci s 'pattern-matching' mohou být použity jako takzvané **algebraické datové typy** ke snadnému vytváření velkých a složitých datových struktur.

### 2-vector 

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
vector2(1, 2) |> fmap$(x -> x*2) |> print  # vector2(x=2, y=4)
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

Další věcí, na kterou je zde zapotřebí upozornit, je použití funkce [`fmap`](DOCS.html#fmap). `fmap` umožňuje `mapovat` funkce po algebraických datových typech. Datové typy Coconut podporují iteraci, takže standardní `map` s nimi může pracovat ale nevrací jiný objekt téhož datového typu. Konstrukt `fmap` je jednoduše `map` plus volání konstruktoru objektu.


### Konstruktor pro n-Vector  

Nyní, když jsme vyřídili `2-vector`, vraťme se zpět k našemu původnímu, více komplikovanému problému s n-vektory, to jest s vektory libovolné délky. Pokusíme se, aby náš n-vektor podporoval všechny základní vektorové operace ale začneme pouze s definicí `data` a konstruktorem:

```coconut
data vector(*pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        match [v is vector] in pts:		
            return v  # vector(v) where v is a vector should return v
        else:
            return pts |*> makedata$(cls)  # accesses base constructor

# Test cases:
vector(1, 2, 3) |> print # vector(*pts=(1, 2, 3))
vector(4, 5) |> vector |> print # vector(*pts=(4, 5))
```

Copy, paste! Nově se zde dozvídáme, jak psát konstruktory `data`. Protože jsou typy `data` neměnitelné, nebude zde chodit konstrukce `__init__`. Místo toho je použita jiná specielní metoda `__new__`, která musí vrátit nově vytvořenou instanci a na rozdíl od většiny metod přijímá jako první argument class, nikoliv objekt. Protože `__new__` potřebuje vrátit úplnou instanci, bude ve většině případů nezbytný přístup k výchozímu konstruktoru `data`. Pro tento účel poskytuje Coconut vestavěnou funkci [`makedata`](DOCS.html/makedata), která přijímá datový typ a volá jeho výchozí konstruktor pro zbytek argumentů.

V tomto případě konstruktor kontroluje, zda nebylo zadáno nic jiného než další `vector`, v kterémžto případě jej vrací. Jinak vrací výsledek 
volání výchozího konstruktoru, jehož formou je `vector(pts)`, neboť takto jsme deklarovali datový typ. Používáme sekvenční p-m ke zjištění, zda jsme zadali jediný vektor, což je pouze seznam nebo entice vzorů, s nimiž je porovnáván obsah sekvence.

Dalším novým konstruktem zde použitým je operátor `|*>` neboli star-pipe, který funguje úplně stejně jako normální pojítko, kromě toho, že místo volání funkce s jedním argumentem, volá ji tolika argumenty, kolik je elementů v zadané sekvenci. Rozdíl mezi `|*>` a `|>` je analogický rozdílu mezi `f(args)` a `f(*args)`.

### Metody pro n-vector  

Nyní, když máme konstruktor pro náš n-vektor, je čas napsat jeho metody. První je metoda `__abs__`, která má počítat velikost vektoru. To bude mírně složitější než u 2-vektoru, protože musí chodit pro libovolný počet `pts`. Naštěstí můžeme použít pojítkový (pipeline) styl Coconutu a jeho částečnou aplikaci funkce:
```coconut
    def __abs__(self) =
        """Return the magnitude of the vector."""
        self.pts |> map$(pow$(?, 2)) |> sum |> pow$(?, 0.5)
```
Základním algoritmem zde je 'mapování' mocniny pro každý prvek, jejich celkový součet a druhá odmocnina výsledku. Novým konstruktem zde je znak `?` v částečné aplikaci, který jednoduše umožňuje přeskočení jednoho argumentu a odložení jeho použití na volání funkce. V tomto případě nám `?` umožňuje částečně aplikovat exponent místo základu ve funkci `pow` - mohli jsme rovněž ekvivalentně použít `(**)`.

Dále je sčítání vektorů. Cílem je sečíst dva vektory stejné délky sečtením jejich komponent. Za tím účelem využijeme schopnost Coconutu provést pattern-matching (nebo v tomto případě rozkladné přiřazení) pro datové typy a to takto:
```coconut
    def __add__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Add two vectors together."""
        map((+), self.pts, other_pts) |*> vector
```

Máme zde několik nových konstruktů ale nejvýznamnějším je  pattern-matching pro `vector(*other_pts)`, na němž vidíme skladbu pro porovnávání shody s datovými typy: přesně napodobuje originální deklaraci `data` pro daný datový typ. V tomto případě se `vector(*other_pts)` bude shodovat pouze s vektorem, přičemž přiřadí atribut `pts` vektoru proměnné `other_pts`. Pokud se nebude shodovat,  vyvolá chybu `MatchError`.

Další metodou je podíl vektorů, což je vlastně součet vektorů se znaménkem `(-)` místo `(+)`:
```coconut
    def __sub__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Subtract one vector from another."""
        map((-), self.pts, other_pts) |*> vector
```

Za povšimnutí zde stojí to, že na rozdíl od jiných operátorových funkcí, může `(-)` znamenat buď odečtení nebo negaci. Konkretní význam závisí na počtu poskytnutých argumentů - jeden pro negaci, dva pro odečtení. Abychom si to demonstrovali, použijeme stejnou funkci `(-)` k zavedení negace vektoru, což by mělo negovat každý jeho prvek:
```coconut
    def __neg__(self) =
        """Retrieve the negative of the vector."""
        self.pts |> map$(-) |*> vector
```



Poslední metodou, kterou zavedeme, je násobení vektorů. To je poněkud komplikované, neboť matematicky existuje více způsobů. Pro naše účely se soustředíme na dva: na (skalární) součin dvou vektorů stejné délky, což se součet součinů příslušných elementů a na násobení vektoru skalárem, což je násobení všech elementů stejným skalárem. Zde je naše implementace:
```coconut
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(*other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector # scalar multiple
    def __rmul__(self, other):
        """Necessary to make scalar multiplication commutative."""
        return self * other
```

Za pozornost zde stojí za prvé, že na rozdíl od součtu a podílu, kde jsme chtěli hlásit chybu při selhání shody vektoru, zde chceme při selhání shody provést násobení skalárem - takže místo použití rozloženého přiřazení použijeme příkaz `match`. 

Za druhé si povšimneme použití kombinace pojítkového (pipeline) stylu programování, částečné aplikace, operátorových funkcí a funkcí vyššího řádu pro výpočet skalárního součinu a pro násobení skalárem. U skalárového součinu mapujeme násobení na dva vektory a sečteme výsledky. U násobení skalárem vytváříme nový vektor násobením všech prvků původního vektoru stejným číslem.

Nakonec to vše dáme dohromady:
```coconut
data vector(*pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        match [v is vector] in pts:
            return v  # vector(v) where v is a vector should return v
        else:
            return pts |*> makedata$(cls)  # accesses base constructor
    def __abs__(self) =
        """Return the magnitude of the vector."""
        self.pts |> map$(pow$(?, 2)) |> sum |> pow$(?, 0.5)
    def __add__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Add two vectors together."""
        map((+), self.pts, other_pts) |*> vector
    def __sub__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Subtract one vector from another."""
        map((-), self.pts, other_pts) |*> vector
    def __neg__(self) =
        """Retrieve the negative of the vector."""
        self.pts |> map$(-) |*> vector
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(*other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum  # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector  # scalar multiplication
    def __rmul__(self, other) =
        """Necessary to make scalar multiplication commutative."""
        self * other

# Test cases:
vector(1, 2, 3) |> print  # vector(*pts=(1, 2, 3))
vector(4, 5) |> vector |> print  # vector(*pts=(4, 5))
vector(3, 4) |> abs |> print  # 5
vector(1, 2) + vector(2, 3) |> print  # vector(*pts=(3, 5))
vector(2, 2) - vector(0, 1) |> print  # vector(*pts=(2, 1))
-vector(1, 3) |> print  # vector(*pts=(-1, -3))
(vector(1, 2) == "string") |> print  # False
(vector(1, 2) == vector(3, 4)) |> print  # False
(vector(2, 4) == vector(2, 4)) |> print  # True
2*vector(1, 2) |> print  # vector(*pts=(2, 4))
vector(1, 2) * vector(1, 3) |> print  # 7
```

Copy, paste! Je to pěkná řádka řádků. Když si to však poučeně procházíme, je to čisté, čitelné a stručné a dělá to přesně to, co jsme chtěli aby to dělalo: vytvořit algebraický datový typ pro neměnitelný n-vektor, který podporuje základní vektorové operace. Celou záležitost jsme přitom provedli čistě funkcionálně bez potřeby imperativních konstruktů, jako jsou stavy nebo smyčky.

## Případová studie 4: `vector_field` 

V poslední případové studii nebudu kód psát já a vy přihlížet, ale budete jej psát vy a já vám posléze ukážu, jak bych to napsal sám.

Bonusovou výzvou u tohoto odstavce bude napsat každou definovanou funkci do jednoho řádku. Zkuste přitom použít přiřazovací funkce:

Nejprve si uveďme obecný cíl této případové studie. Chceme napsat program, který nám umožní vytvářet nekonečná pole vektorů, přes něž můžeme iterovat a s nimiž můžeme provádět různé operace. V tomto případě se budeme zajímat jenom o vektory s kladnými komponenty.

Naším prvním krokem tedy bude vytvoření pole všech bodů s pozitivními hodnotami `x` a `y`, to jest, nalézajících se v prvním kvadrantu roviny `x-y`, které vypadá nějak takto:
```
...

(0,2)   ...

(0,1)   (1,1)   ...

(0,0)   (1,0)   (2,0)   ...
```

Protože chceme být schopni přes tuto rovinu iterovat, potřebujeme ji nějakým způsobem linearizovat a nejjednoduším způsobem to učiníme tak, že ji rozdělíme do diagonál, načež můžeme traverzovat po první diagonále, potom po druhé a tak dále, nějak takto:
```
(0, 0), (1, 0), (0, 1), (2, 0), (1, 1), (0, 2), ...
```

### `diagonal_line` 

Naše první funkce `diagonal_line(n)` by tedy měla vytvořít iterátor všech bodů, reprezentovaných jako souřadnicové entice v `n-té` diagonále, počínaje v bodě `(0, 0)` jako `0th` diagonála. Jak jsme si řekli na počátku případové studie, o řešení se pokusíte nejdřív sami s použitím všech nástrojů funkcionálního programování, které Coconut poskytuje. Až budete hotovi, posuňte se dále.

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

### `linearized_plane` 

Nyní, když jsme vytvořili naše diagonální přímky, potřebujeme je spojit dohromady abychom sestavili plně linearizovanou rovinu a za tím účelem napíšeme funkci `linearized_plane()`. Funkce `linearized_plane` by měla vytvořit iterátor, který prochází všemi body roviny po diagonálách, počínaje nultou, prvou, atd. Tento iterátor musí být nezbytně nekonečný, protože musí procházet všemi body dané roviny. 

Nápovědou pro sestavování funkce budiž připomínka, že operátor `::` je líný a nevyhodnotí své operandy bez požádání, což znamená, že může být použit k vytvoření nekonečných iterátorů. Až budete hotovi, posuňte se v textu dále.

Testy:
```coconut
# Note: tyto testy používají označení $[], které jsme dosud neuvedli
#  ale bude uvedeno později ještě v této případové studii; prozatím proveďte 
#  testy a ujistěte se, že dostáváte stejný výsledek jako je v komentáři:
linearized_plane()$[0] |> print # (0, 0)
linearized_plane()$[:3] |> list |> print # [(0, 0), (0, 1), (1, 0)]
```

_Nápověda: místo definování funkce `linearized_plane()`, zkuste ji definovat jako `linearized_plane(n=0)`, kde `n` je označení počáteční diagonály a pro rozvinutí funkce použijte rekurzi._

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

### `vector_field` 

Nyní, když máme funkci, která vytvoří všechny potřebné body, je čas přeměnit je na vektory a za tím účelem si definujeme novou funkci `vector_field()`, která přemění všechny entice v `linearized_plane` na vektory s použitím třídy `n-vector`, kterou jsme definovali dříve.

Testy:
```coconut
# Budete potřebovat sem přenést třádu vektoru z předchozích textů aby vám chodilo následující:
vector_field()$[0] |> print # vector(*pts=(0, 0))
vector_field()$[2:3] |> list |> print # [vector(*pts=(1, 0))]
```

_Nápověda: Vzpomeňte si, že vektor, který jsme definovali, přijímá komponenty jako separátní argumenty, nikoliv jako jedinou entici._  Při řešení vám může být nápomocný text [Coconut built-in `starmap`](DOCS.html#starmap).

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

Děláme velký pokrok! Než pokročíme dál, srovnejte si řešení se mnou:
```coconut
def vector_field() = linearized_plane() |> starmap$(vector)

```
Vše, co jsme učinili, bylo to, že jsme mapovali `vector` přes funkci  `linearized_plane`, avšak s použitím `starmap` místo `map`, takže je `vector` volán s každým elementem entice jako separátním argumentem.

### Applikace 

Nyní, když máme všechny funkce, potřebné pro naše vektorové pole, dáme je všechny dohromady a otestujeme je. Nezdráhejte se dosadit vlastní verze funkcí:
```coconut
data vector(*pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        match [v is vector] in pts:
            return v  # vector(v) where v is a vector should return v
        else:
            return pts |*> makedata$(cls)  # accesses base constructor
    def __abs__(self) =
        """Return the magnitude of the vector."""
        self.pts |> map$(pow$(?, 2)) |> sum |> pow$(?, 0.5)
    def __add__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Add two vectors together."""
        map((+), self.pts, other_pts) |*> vector
    def __sub__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Subtract one vector from another."""
        map((-), self.pts, other_pts) |*> vector
    def __neg__(self) =
        """Retrieve the negative of the vector."""
        self.pts |> map$(-) |*> vector
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(*other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum  # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector  # scalar multiplication
    def __rmul__(self, other) =
        """Necessary to make scalar multiplication commutative."""
        self * other

def diagonal_line(n) = range(n+1) |> map$(i -> (i, n-i))
def linearized_plane(n=0) = diagonal_line(n) :: linearized_plane(n+1)
def vector_field() = linearized_plane() |> starmap$(vector)

# Test cases:
diagonal_line(0) `isinstance` (list, tuple) |> print  # False (should be an iterator)
diagonal_line(0) |> list |> print  # [(0, 0)]
diagonal_line(1) |> list |> print  # [(0, 1), (1, 0)]
linearized_plane()$[0] |> print  # (0, 0)
linearized_plane()$[:3] |> list |> print  # [(0, 0), (0, 1), (1, 0)]
vector_field()$[0] |> print  # vector(*pts=(0, 0))
vector_field()$[2:3] |> list |> print  # [vector(*pts=(1, 0))]
```

Copy, paste! Poté, co jste se ujistili, že po dosazení svých funkcí chodí vše jak má, zaměřte se na poslední čtyři testy. Zjistíte, že používají novou notaci, podobnou notaci pro částečnou aplikaci, již jsme viděli dříve - ale s hranatými závorkami místo kulatých. To je notace pro krájení (slicing) iterátoru. Podobně jako byla částečná aplikace líným voláním funkce, je dělení iterátoru _línym dělením sekvence_. Podobně jako u částečné aplikace, je užitečné považovat znak `$` za _zlenivějící_  (lazy-ify) operátor, v tomto případě přetvářející normální (ihned prováděné) krájení (slicing) Pythonu na líné krájení iterátoru, které se provádí jen tehdy, jsou-li prvky v řízcích (slice) potřebné.

Maje toto na mysli, nyní když jsme sestavili naše vektorové pole, je čas si s krájením iterátoru trochu pohrát. Zkuste něco smělého, jako například 
- vytvořit `magnitude-field`, kde každý bod reprezentuje délku příslušného vektoru
- zkombinovat celá vektorová pole aplikací funkce `match` na dříve vytvořené metody dělení a násobení

potom použít krájení iterátoru pro vynětí a přezkoušení úseků.

## Případová studie 5: `vector` - část II 

U některých aplikací, používajících naše `vector_fields`, může být žádoucí přidat k našemu `vektoru` nějaké užitečné metody. V této případové studii se zaměříme na metodu, zvanou `.angle`.

Metoda `.angle` přijme dva vektory a spočítá úhel mezi nimi. Matematicky je úhel dvou vektorů skalárním součinem jejich příslušných jednotkových vektorů. Takže před tím, než budeme moci použít metodu `.angle`, budeme potřebovat metodu `.unit`. Matematicky je výraz pro jednotkový vektor daného vektoru dán jako podíl tohoto vektoru a jeho velikosti. Tudíž, před použitím `.unit` a potažmo `.angle`, musíme začít zavedením dělení. 

### `__truediv__` 

Dělení vektorů je pouhé skalární dělení, pročež napíšeme metodu `__truediv__`, která přijímá `self` jako první argument a `other` jako druhý argument, vracejíc nový vektor téže velikosti jako `self`, s prvky dělenými vektorem `other`. Jako specielní výzvu, zkuste to zapsat v jediném řádku s použitím notace přiřazovací funkce.

Testy:
```coconut
vector(3, 4) / 1 |> print # vector(*pts=(3.0, 4.0))
vector(2, 4) / 2 |> print # vector(*pts=(1.0, 2.0))
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
    def __truediv__(self, other) = self.pts |> map$(x -> x/other) |*> vector
```

### `.unit` 

Další je `.unit`. Napíšeme metodu `unit`, která přijímá jako argument pouze `self` a vrací nový vektor téže velikosti jako `self`, s každým prvkem děleným velikostí `self`, jež můžeme získat pomocí funkce `abs`. To by měl být velmi jednoduchý jedořádkový zápis.

Testy:
```coconut
vector(0, 1).unit() |> print # vector(*pts=(0.0, 1.0))
vector(5, 0).unit() |> print # vector(*pts=(1.0, 0.0))
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

### `.angle` 

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

data vector(*pts):
    """Immutable n-vector."""
    def __new__(cls, *pts):
        """Create a new vector from the given pts."""
        match [v is vector] in pts:
            return v  # vector(v) where v is a vector should return v
        else:
            return pts |*> makedata$(cls)  # accesses base constructor
    def __abs__(self) =
        """Return the magnitude of the vector."""
        self.pts |> map$(pow$(?, 2)) |> sum |> pow$(?, 0.5)
    def __add__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Add two vectors together."""
        map((+), self.pts, other_pts) |*> vector
    def __sub__(self, vector(*other_pts)
                if len(other_pts) == len(self.pts)) =
        """Subtract one vector from another."""
        map((-), self.pts, other_pts) |*> vector
    def __neg__(self) =
        """Retrieve the negative of the vector."""
        self.pts |> map$(-) |*> vector
    def __mul__(self, other):
        """Scalar multiplication and dot product."""
        match vector(*other_pts) in other:
            assert len(other_pts) == len(self.pts)
            return map((*), self.pts, other_pts) |> sum  # dot product
        else:
            return self.pts |> map$((*)$(other)) |*> vector  # scalar multiplication
    def __rmul__(self, other) =
        """Necessary to make scalar multiplication commutative."""
        self * other
     # New one-line functions necessary for finding the angle between vectors:
    def __truediv__(self, other) = self.pts |> map$(x -> x/other) |*> vector
    def unit(self) = self / abs(self)
    def angle(self, other is vector) = math.acos(self.unit() * other.unit())

# Test cases:
vector(3, 4) / 1 |> print  # vector(*pts=(3.0, 4.0))
vector(2, 4) / 2 |> print  # vector(*pts=(1.0, 2.0))
vector(0, 1).unit() |> print  # vector(*pts=(0.0, 1.0))
vector(5, 0).unit() |> print  # vector(*pts=(1.0, 0.0))
vector(2, 0).angle(vector(3, 0)) |> print  # 0.0
print(vector(1, 0).angle(vector(0, 2)), math.pi/2)  # should be the same
vector(1, 2).angle(5)  # MatchError
```
_Jedna důležitá poznámka: dejte si pozor abyste nenechali prázdný řádek při dosazování vlastních metod, neboť v tom případě by interpret roztrhl kód. V normálním zápisu Coconut to není žádný problém, pouze zde, protože provádíme kopírování-vkládání do příkazového řádku_

Copy, paste! Jestliže všechno chodí jak má, doporučuji se vrátit ke hrátkám s [aplikacemi](#aplikace) `vector_field` s použitím našich nových metod.

## Vyplnění mezer 

Tímto vyčerpal tento tutoriál své případové studie, avšak to neznamená, že Coconut předvedl všechny své možnosti! V tomto posledním odstavci se dotkneme tří nejdůležitějších struktur, jež se nám podařilo opominout v případových studiích: líné seznamy, skladba funkcí a implicitní parciály (partials).

### Líné seznamy 

Líné seznamy jsou líně vyhodnocované iterátorové literály, podobné ve své lenosti operátoru `::` - a to v tom, že jakýkoli výraz uvnitř líného seznamu není vyhodnocen, dokud jej není zapotřebí. Syntaxe pro líné seznamy je přesně táž jako syntaxe pro normální seznamy, až na "banánové závorky" (`(|` and `|)`) místo normálních závorek, takto:
```coconut
abc = (| a, b, c |)
```
Jako u všech iterátorů Pythonu, lze volat `next` k získání následného objektu v iterátoru. S použitím líného seznamu je možné definovat hodnoty, použité ve výrazech dle potřeby bez vyvolání hlášení `NameError`:

```coconut
abcd = (| d(a), d(b), d(c) |)  # a, b, c, and d are not defined yet
def d(n) = n + 1

a = 1
next(abcd)  # 2
b = 2
next(abcd)  # 3
c = 3
next(abcd)  # 4
```

### Skladba funkcí 

Skladba funkcí v Coconut se zajišťuje operátorem `..`, který přijímá dvě funkce a spojí je do nové funkce, ekvivalentní zápisu `(*args, **kwargs) -> f1(f2(*args, **kwargs))`. To může být užitečné u částečné aplikace při spojování několika funkcí vyššího řádu, jako zde:
```coconut
zipsum = map$(sum)..zip
```
Jsou-li skládané funkce uzavřeny v závorkách, lze do nich vložit argumenty:
```coconut
def plus1(x) = x + 1
def square(x) = x * x

(plus1..square)(3) == 10  # True
```
Funkce s různými aritami lze skládat dohromady, pokud jsou uvedeny ve správném pořadí. Při nesprávném pořadí je vyvoláno hlášení `TypeError`. V tomto příkladu spojíme unární funkci s binární:
```coconut
def add(n, m) = n + m  # binary function
def square(n) = n * n  # unary function

(add..square)(3, 1)    # Raises TypeError: square() takes exactly 1 argument (2 given)
(square..add)(3, 1)    # 16
```

Jiný důležitý trik zahrnuje skládání funkce s funkcí vyššího řádu:
```coconut
def inc_or_dec(t):
    # Our higher-order function, which returns another function
    if t:
        return x -> x+1
    else:
        return x -> x-1

def square(n) = n * n

square_inc = square..inc_or_dec(True)
square_dec = square..inc_or_dec(False)
square_inc(4)  # 25
square_dec(4)  # 9

```
_Note: Coconut také podporuje skladebné pojítkové (pipe) operátory  `..>`, `<..`, `..*>` a `<*..`._

### Implicitní parciály 

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
Úplné vysvětlení co každý implicitní parciál dělá lze nalézt v části [implicit partials](DOCS.html#implicit-partial-application).


### Anotace typů

Pro mnoho lidí je velkou nevýhodou Pythonu skutečnost, že je to dynamicky typovaný jazyk. V Pythonu je tento problém osloven v [MyPy](http://mypy-lang.org/), což je analyzátor statických typů v Pythonu, který umí kontrolovat anotace typu, zavedené v Python 3, například:
```coconut_python
def plus1(x: int) -> int:
    return x + 1
a: int = plus1(10)
```

Bohužel, tyto anotace typu existují pouze v Python 3. Coconut ovšem kompiluje tyto anotace na univerzálně kompatibilní komentáře typu. Kromě toho má Coconut vestavěnou [MyPy integraci](DOCS.html#mypy-integration) pro automatické ověřování typu v kódu a vlastní [vylepšenou skladbu pro anotaci typu](DOCS.html#enhanced-type-annotations) pro snadnější vyjádření složitých typů.

### Další čtení 

Všechny vlastnosti popsané v tomto tutoriálu, stejně jako řada dalších, jsou podrobně dokumentovány v podrobné [dokumentaci](DOCS.html).

Also, if you have any other questions not covered in this tutorial, feel free to ask around at Coconut's [Gitter](https://gitter.im/evhub/coconut), a GitHub-integrated chat room for Coconut developers.

Finally, Coconut is a new, growing language, and if you'd like to get involved in the development of Coconut, all the code is available completely open-source on Coconut's [GitHub](https://github.com/evhub/coconut). Contributing is a simple as forking the code, making your changes, and proposing a pull request.  See Coconuts [contributing guidelines](CONTRIBUTING.html) for more information.

