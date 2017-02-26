# Dokumentace

<!-- MarkdownTOC -->

1. [Úvod](#uvod)
1. [Kompilace](#kompilace)
    1. [Instalace](#instalace)
    1. [Použití](#pouziti)
        1. [Poziční argumenty](#pozicni-argumenty)
        1. [Volitelné argumenty](#volitelne-argumenty)
    1. [Názvy zdrojových souborů](#nazvy-zdrojovych-souboru)
    1. [Kompilační režimy](#kompilacni-rezimy)
    1. [Kompatibilní verze Pythonu](#kompatibilni-verze-pythonu)
    1. [Přípustné cíle](#pripustne-cile)
    1. [Režim `strict`](#rezim-strict)
    1. [Podpora pro IPython-Jupyter](#podpora-pro-ipython-jupyter)
        1. [Extenze](#extenze)
        1. [Jádro](#jadro)
	1. [Integrace s MyPy](#integrace-s-mypy)
1. [Operátory](#operatory)
    1. [Lambda](#lambda)
    1. [Částečná aplikace](#castecna-aplikace)
    1. [Vedení pipeline](#vedeni-pipeline)
    1. [Skladba](#skladba)
    1. [Řetězení](#retezeni)
    1. [Krájení iterátoru](#krajeni-iteratoru)
    1. [Alternativy Unicode](#alternativy-unicode)
1. [Klíčová slova](#klicova-slova)
    1. [`data`](#data)
    1. [`match`](#match)
    1. [`case`](#case)
    1. [Backslash-Escaping](#backslash-escaping)
    1. [Vyhrazené proměnné](#vyhrazene-promenne)
1. [Výrazy](#vyrazy)
    1. [Příkaz lambda](#prikaz-lambda)
    1. [Líné seznamy](#line-seznamy)
    1. [Implicitní castecna aplikace](#implicitni-castecna-aplikace)
    1. [Literály setu](#literaly-setu)
    1. [Literály imaginárního čísla](#literaly-imaginarniho-cisla)
    1. [Podtržítkové separátory](#podtrzitkove-separatory)
1. [Definice funkce](#definice-funkce)
    1. [Optimalizace koncového volání ](#optimalizace-koncoveho-volani)
    1. [Operátorové funkce](#operatorove-funkce)
    1. [Přiřazovací funkce](#prirazovaci-funkce)
	1. [Porovnávací funkce](#pattern-matching)
	1. [Infixové funkce](#infixove-funkce)
1. [Příkazy](#prikazy)
    1. [Rozložené přiřazení](#rozlozene-prirazeni)
    1. [Dekorátory](#dekoratory)
    1. [Příkazy `else`](#prikazy-else)
    1. [Příkazy `except`](#prikazy-except)
    1. [Implicitní `pass`](#implicitni-pass)
    1. [Pokračování v závorkách](#pokracovani-v-zavorkach)
    1. [Zjednodušené určení `global` a `nonlocal`](#zjednodusene-urceni-global-a-nonlocal)
    1. [Průchod kódu](#pruchod-kodu)
1. [Vestavěné funkce](#vestavene-funkce)
    1. [`addpattern`](#addpattern)
    1. [`prepattern`](#prepattern)
    1. [`reduce`](#reduce)
    1. [`takewhile`](#takewhile)
    1. [`dropwhile`](#dropwhile)
    1. [`tee`](#tee)
    1. [`consume`](#consume)
    1. [`count`](#count)
    1. [`map` a `zip`](#map-a-zip)
    1. [`datamaker`](#datamaker)
    1. [`recursive iterator`](#recursive-iterator)
    1. [`parallel map`](#parallel-map)
    1. [`concurrent map`](#concurrent-map)
    1. [`MatchError`](#matcherror)
1. [Utilita Coconut](#utilita-coconut)
    1. [Zvýraznění skladby](#zvyrazneni-skladby)
        1. [SublimeText](#sublimetext)
        1. [Pygments](#pygments)
    1. [`coconut.coconut`](#coconutcoconut)
    1. [`coconut.convenience`](#coconutconvenience)
        1. [`parse`](#parse)
        1. [`setup`](#setup)
        1. [`cmd`](#cmd)
        1. [`version`](#version)
        1. [`CoconutException`](#coconutexception)

<!-- /MarkdownTOC -->

## Úvod

Tato dokumentace pokrývá všechny technické detaily programovacího jazyka [Coconut ](http://evhub.github.io/coconut/) a je zamýšlena spíš jako referenční příručka než edukativní úvod. Úplný úvod a tutoriál pro Coconut - viz [Tutoriál](http://coconut.readthedocs.io/cs/latest/HELP.html)

Coconut je varianta jazyka [Python](https://www.python.org/), vytvořená pro **jednoduché, elegantní a funkcionální programování v Pythonu**. Skladba Coconut je podmnožna skladby Pythonu 3. To znamená, že uživatel, obeznámený s Pythonem, bude již obeznámený s většinou obsahu Coconut.

Kompilátor jazyka Coconut převádí kód Coconut na kód Pythonu. Primární způsob přístupu ke kompilátoru Coconut je z příkazového řádku utility REPL, jež rovněž obsahuje překladač pro kompilaci v reálném čase. Kromě této konzoly podporuje Coconut také notebooky IPythonu a Jupiteru.

Zatímco většina kódu v Coconut vychází ze snahy umožnit a zjednodušit funkcionální programování v Pythonu, další inspirace pochází z [Haskellu](https://www.haskell.org/), [CoffeeScriptu](http://coffeescript.org/), [F#](http://fsharp.org/) a z extenze Pythonu  [patterns.py](https://github.com/Suor/patterns).

## Kompilace
 
### Instalace 

Protože je Coconut hostován v [Python Package Index](https://pypi.python.org/pypi/coconut), lze jej snadno instalovat s použitím `pip`. Jednoduše nainstalujte [Python](https://www.python.org/downloads/), otevřte příkazový řádek (cmd) a zadejte
```
pip install coconut
```
což nainstaluje Coconut a jeho požadované závislosti. Coconut sám má několik závislostí (dependencies), které lze instalovat zápisem 
```
pip install coconut[all]
```
což umožní používání flagů `--jobs`, `--watch` a `--jupyter`. Pro instalaci pouze vybraného flagu, napište místo `all` název příslušného flagu.

Případně, chcete-li si vyzkoušet poslední a nejlepší Coconut, zapište
```
pip install coconut-develop
```
což nainstaluje nejposlednější chodící [development build](https://github.com/evhub/coconut/tree/develop) (volitelná instalace závislostí je podporována stejným způsobem, jak popsáno výše). Více informací o aktuální vývojové sestavě najdete na [development version of this documentation](http://coconut.readthedocs.org/en/develop/DOCS.html). Buďte varováni: `coconut-develop` může být nestabilní — narazíte-li na chybu, prosím ohlašte ji [vytvořením nového issue](https://github.com/evhub/coconut/issues/new).

### Použití 

```
coconut [-h] [-v] [source] [dest] [-t version] [-s] [-l] [-k] [-p] [-a] [-w] [-d] [-r] [-n] [-m] [-i] [-q] [-f] [-c code] [-j processes] [--jupyter ...] [--tutorial] [--documentation] [--style name] [--recursion-limit limit] [--verbose]
```

#### Poziční argumenty 

```
source          cesta k souboru coconut, který má být kompilován
dest            cílová složka pro compilované soubory (implicitně jí je zdrojový adresář)
```

#### Volitelné argumenty 

```
-h, --help              show this help message and exit
-v, --version           print Coconut and Python version information
-t, --target            specify target Python version (defaults to universal)
-s, --strict            enforce code cleanliness standards
-l, --line-numbers      add line number comments for ease of debugging
-k, --keep-lines        include source code in comments for ease of debugging
-p, --package           compile source as part of a package (defaults to only if source is a directory)
-a, --standalone        compile source as standalone files (defaults to only if source is a single file)
-w, --watch           watch a directory and recompile on changes (requires watchdog)
-d, --display           print compiled Python
-r, --run               run compiled Python (often used with --nowrite)
-n, --nowrite           disable writing compiled Python
-m, --minify            compress compiled Python
-i, --interact          force the interpreter to start (otherwise starts if no other command is given)
-q, --quiet             suppress all informational output (combine with --display to write runnable code to stdout)
-f, --force             force overwriting of compiled Python (otherwise only overwrites when source code or compilation parameters change)
-c, --code code         run a line of Coconut passed in as a string (can also be passed into stdin)
-j, --jobs processes    number of additional processes to use (defaults to 0) (pass 'sys' to use machine default)
--jupyter, --ipython    run Jupyter/IPython with Coconut as the kernel (remaining args passed to Jupyter)
--tutorial              open the Coconut tutorial in the default web browser
--documentation         open the Coconut documentation in the default web browser
--style name            pygments syntax highlighting style (or 'none' to disable)
--recursion-limit       set maximum recursion depth in compiler (defaults to 2000)
--verbose               print verbose debug output
```

### Názvy zdrojových souborů 

Zdrojové soubory používají extenze `.coco` (upřednostněno), `.coc` nebo `.coconut`. Soubor `.coco` (či `.coc` / `.coconut`) je kompilován do souboru s příponou `.py`. Je-li požadována jiná extenze než `.py`, například `.pyde` pro [Python Processing](http://py.processing.org/), může být vložena před `.coco` a tato složená extenze bude použita místo `.py`. Například, `name.coco` bude kompilovat na `name.py`, zatímco `name.pyde.coco` bude kompilovat na `name.pyde`.

### Kompilační režimy 

Soubory, kompilované konzolou `coconut` se mohou lišit v závislosti na kompilačních parametrech. Je-li kompilována celá složka souborů (ve které bude kompilátor rekurzivně vyhledávat soubory s extenzí `.coco`, `.coc` nebo `.coconut`), vytvoří se soubor `__coconut__.py`, pro ukládání nezbytných funkcí (package mode), zatímco při kompilaci jediného souboru se nezbytné informace ukládají v záhlaví uvnitř souboru (standalone mode). Standalone mode je lepší pro jednotlivé soubory, protože se obejde bez nadbytečného importování `__coconut__.py`, avšak package mode je lepší pro velké pakety, protože se nemusí v každém souboru spouštět kód v záhlaví, jelikož může být jednoduše importován z `__coconut__.py`.
Je-li `zdrojovým` argumentem pro CLI konzolu soubor, provede se implicitně samostatná kompilace, zatímco je-li jím složka, provede se rekurzivní vyhledávání všech souborů `.coco` (nebo `.coc` či `.coconut`), pro něž se provede paketová kompilace. Coconut takto ve většině provede správnou volbu režimů. Je-li však důležité aby se nevytvářely žádné dodatečné soubory jako např. `__coconut__.py`, potom lze přinutit CLI konzolu aby použila určený režim použitím flagů `--package` (`-p`) a `--standalone` (`-a`).

### Kompatibilní verze Pythonu 

Protože je skladba Coconut založena na Python3, měl by kód Coconut, kompilovaný kompilátorem Coconut v univerzálním režimu (implicitní  `--target`) běžet v libovolné verzi Pythonu `>= 2.6` nebo `>= 3.2`.

_Poznámka: Vyzkoušené implementace jsou [CPython](https://www.python.org/) `2.6, 2.7, 3.2, 3.3, 3.4, 3.5` a [PyPy](http://pypy.org/) `2.7, 3.2`._

V rámci snahy o vzájemnou kompabilitu (cross-compatibility), přidává Coconut nové  Python 3 built-ins přepisuje Python 2 built-ins na Python 3 verze tam, kde je to možné. Navíc Coconut přepisuje některé Python 3 built-ins z optimalizačních důvodů. Je-li požadován přístup k verzím Pythonu, lze staré built-ins vydolovat s použitím předložky `py_`. Dostupné Python built-ins available jsou:
- `py_chr`
- `py_filter`
- `py_hex`
- `py_input`
- `py_raw_input`
- `py_int`
- `py_oct`
- `py_open`
- `py_print`
- `py_range`
- `py_xrange`
- `py_str`
- `py_map`
- `py_zip`

Konečně, zatímco se Coconut pokusí kompilovat skladbu Python3 na jeho univerzální ekvivalent, následující konstrukty nemají žádný ekvivalent v Python2 a vyžadují specifikaci alespoň `3` před svým použitím:
- destructuring assignment with `*`s (use Coconut pattern-matching instead),
- function type annotation,
- the `nonlocal` keyword,
- `exec` used in a context where it must be a function,
- keyword class definition,
- tuples and lists with `*` unpacking or dicts with `**` unpacking (requires `--target 3.5`),
- `@` as matrix multiplication (requires `--target 3.5`),
- `async` and `await` statements (requires `--target 3.5`), and
- formatting `f` strings (requires `--target 3.6`).

### Přípustné cíle 

Je-li verze Pythonu, v níž bude kompilovaný kód běžet, známa předem, měl by být cíl určen flagem `--target`. Daný cíl (target) ovlivní pouze kompilovaný kód a zda je určitá syntaxe Pythonu3 (viz níže) povolena. Tam, kde se standardy skladeb pro Python3 a Python2 liší, bude skladba Coconut vždy používat skladbu Python3 pro všechny cíle. Podporované cíle jsou:

- universal (default) (will work on _any_ of the below),
- `2`, `26` (will work on any Python `>= 2.6` but `< 3`),
- `27` (will work on any Python `>= 2.7` but `< 3`),
- `3`, `32` (will work on any Python `>= 3.2`),
- `33`, `34` (will work on any Python `>= 3.3`),
- `35` (will work on any Python `>= 3.5`),
- `36` (will work on any Python `>= 3.6`),
- `sys` (chooses the specific target corresponding to the current version).

_Poznámka: Čárky jsou ve specifikacích cíle ignorovány, takže cíl `2.7` je ekvivalentní cíli `27`._

### Režim `strict`  

Je-li povolen flag `--strict` (or `-s`), ohlásí Coconut chyby pro různé problémy stylu. Jsou jimi
- mixing of tabs and spaces (without `--strict` will show a Warning),
- missing new line at end of file (without `--strict` will show a Warning),
- use of `from __future__` imports (without `--strict` will show a Warning)
- trailing whitespace at end of lines,
- semicolons at end of lines,
- use of the Python-style `lambda` statement,
- use of `u` to denote Unicode strings, and
- use of backslash continuations (use [parenthetical continuation](#pokracovani-v-zavorkach) instead).

Doporučuje se při práci na novém projektu používat flag `--strict` (nebo `-s`) protože vám bude nápomocen při psaní čistšího kódu.

### Podpora pro IPython Jupyter 

Dáváte-li přednost prostředí [IPython](http://ipython.org/) (jádro Pythonu pro framework [Jupyter](http://jupyter.org/) framework) před normální konzolou Pythonu, lze použít Coconut jako extenzi IPythonu nebo jádro Jupyteru.

#### Extenze 

Je-li Coconut použit jako extenze, bude speciální "magic command" posílat útržky kódu k vyhodnocení s použitím Coconut místo IPythonu ale IPython bude stále použit jako implicitní aplikace. Řádkový magic `%load_ext coconut` načte Coconut jako extenzi, připojujíc magics `%coconut` a `%%coconut`. Řádkový magic `%coconut` spustí řádek Coconut s implicitními parametry a blokový magic `%%coconut` přijme CL (command line) argumenty z prvního řádku a vyhodnotí kód Coconut pro dané parametry ve zbytku buňky.


#### Jádro 

Je-li Coconut použit jako jádro (kernel), bude veškerý kód v konzoli nebo notebooku poslán k vyhodnocení do Coconut místo do Pythonu. Příkaz `coconut --jupyter notebook` (nebo `coconut --ipython notebook`) spustí notebook IPython/ Jupyter s použitím Coconut jako jádra a příkaz `coconut --jupyter console` (nebo `coconut --ipython console`) spustí konzoli IPython/ Jupyter s použitím Coconut jako jádra. Navíc, příkaz `coconut --jupyter` (nebo `coconut --ipython`) přidá Coconut jako jazykovou volbu uvnitř všech notebooků IPython/ Jupyter - i těch, které nejsou spouštěny aplikací Coconut. Tento příkaz musí být opakovaně proveden při instalaci nové verze Coconut.

### Integrace s MyPy

Coconut se umí integrovat s [MyPy](http://mypy-lang.org/) za účelem optimální statické kontroly typů, včetně všech vestavěných nástrojů Coconut.

Jednoduše zadejte `--mypy` (jako poslední argument), použijte [standardní skladbu anotace Python3](https://www.python.org/dev/peps/pep-0484/) a Coconut se o zbytek sám postará. Coconut implicitně kompiluje anotace typu na kompatibilní  `mypy --py2` komentáře typu. Chcete-li zachovat anotace typů z Python3, jednoduše zadejte `--target 3`.

Kromě anotace typu argumentu funkce podoporuje Coconut také anotace proměnných typů s použitím [nové syntaxe z Python 3.6](https://www.python.org/dev/peps/pep-0526/), jež kompiluje na kompatibilní komentáře `mypy --py2`, pokud není zadáno `--target 3.6`.

Coconut dokonce podporuje `--mypy` v překladači, jenž skenuje inteligentně každý nový řádek kódu v kontextu s předchozím řádkem zda neobjeví nově zavedené chyby MyPy. Na příklad:
```coconut
>>> a = count()[0]  # type: str
<string>:14: error: Incompatible types in assignment (expression has type "int", variable has type "str")
```

## Operátory 

### Lambda 

Coconut poskytuje jednoduchý, čistý operátor `->` jako alternativu k příkazu `lambda` v Pythonu. Skladba s operátorem `->` je `(arguments) -> expression`. Operátor má stejné pořadí důležitosti jako starý příkaz, což znamená, že bude často nezbytné uzavřít lambdu do závorek.

Navíc, Coconut také podporuje implicitní použití operátoru `->` ve formě `(-> expression)`, jež je ekvivalentní k `((_=None) -> expression)`, což umožňuje použití implicitní lambdy když nejsou vyžadovány žádné argumenty nebo když je vyžadován jen jeden argument (vyjádřený znakem `_`).

_Note: Je-li normální skladba lambdy nedostatečná, Coconut také podporuje rozšířenou skladbu lambdy ve formě  [příkazu lambda](#prikaz-lambda)._

##### Zdůvodnění

Použití funkce lambda je v Pythonu neúhledné a neohrabané, vyžadující vypsání celého slova `lambda` pokaždé, když je vytvářena. To je dobré tehdy, jsou-li in-line funkce používány zřidka ale ve funkcionálním programování jsou in-line funkce základním nástrojem.

##### Python Docs

Formy lambda mají totéž skladebné postavení jako obecné výrazy. Jsou zkratkou při vytváření anonymních funkcí; výraz `(arguments) -> expression` vytváří objekt funkce. Nepojmenovaný objekt se chová jako objekt funkce, definovaný:
```coconut
def <lambda>(arguments):
    return expression
```
Všimněte si, že funkce vytvořené formou lambda nemohou obsahovat příkazy nebo anotace.

##### Příklad

###### Coconut
```coconut
dubsums = map((x, y) -> 2*(x+y), range(0, 10), range(10, 20))
dubsums |> list |> print
```

###### Python
```coconut_python
dubsums = map(lambda x, y: 2*(x+y), range(0, 10), range(10, 20))
print(list(dubsums))
```

### Částečná aplikace 

K označení částečné aplikace používá Coconut znak `$` mezi názvem funkce a závorkou před argumenty. It has the same precedence as subscription.

##### Zdůvodnění

Částečná aplikace neboli currying je ústřední pilíř funkcionálního programování a to z dobrého důvodu: umožňuje dynamickou úpravu funkce pro potřebu v místě použití. Částečná aplikace umožňuje vytvoření nové funkce ze staré pro specifikované některé argumenty.

##### Python Docs

Má se vrátit nový objekt `partial`, který se při volání bude chovat jako _func_  volaná s pozičními argumenty _args_ a keyword-argumenty _keywords_. Jsou-li další argumenty zadány při volání, jsou připojeny k _args_. Jsou-li další keyword-argumenty zadány, rozšiřují a přepisují _keywords_. Zhruba ekvivalentní k:
```coconut_python
def partial(func, *args, **keywords):
    def newfunc(*fargs, **fkeywords):
        newkeywords = keywords.copy()
        newkeywords.update(fkeywords)
        return func(*(args + fargs), **newkeywords)
    newfunc.func = func
    newfunc.args = args
    newfunc.keywords = keywords
    return newfunc
```
Objekt `partial` je použit pro částečnou (partial) aplikaci funkce, která “zmrazí” (freezes) některé argumenty a/nebo keywords funkce, vytvářejíc tak nový objket se zjednodušenou signaturou. 

##### Příklad

###### Coconut
```coconut
expnums = map(pow$(2), range(5))
expnums |> list |> print
```

###### Python
```coconut_python
import functools
expnums = map(functools.partial(pow, 2), range(5))
print(list(expnums))
```

### Vedení pipeline 

Coconut používá vodící (pipe) operátory pro usměrnění průběhu aplikace funkcí. Všechny operátory mají precedenci infixových evokací a jsou levostranně asociativní. Všechny operátory také podporují 'in-place versions'. Těmito operátory jsou:
```coconut
(|>)    => pipe forward
(|*>)   => multiple-argument pipe forward
(<|)    => pipe backward
(<*|)   => multiple-argument pipe backward
```

##### Příklad

###### Coconut
```coconut
def sq(x) = x**2
(1, 2) |*> (+) |> sq |> print
```

###### Python
```coconut_python
import operator
def sq(x): return x**2
print(sq(operator.add(1, 2)))
```

### Skladba 

Coconut používá operátor `..` pro skládání funkcí. It has a precedence in-between subscription and exponentiation. The in-place operator is `..=`.

##### Example

###### Coconut
```coconut
fog = f..g
```

###### Python
```coconut_python
# unlike this simple lambda, .. produces a pickleable object
fog = lambda *args, **kwargs: f(g(*args, **kwargs))
```

### Řetězení 

Coconut používá operátor `::` pro řetězení iterátoru. Toto řetězení je prováděno líně - to jest tak, že argumenty se nevyhodnocují, pokud jich není zapotřebí. Tato forma má precedenci 'in-between bitwise or and infix calls'. 'In-place' operátorem je `::=`.

##### Zdůvodnění

Důležitým nástrojem pro práci s iterátory stejně snadno jako při práci se sekvencemi je schopnost líně kombinovat více iterátorů dohromady. Tato operace se nazývá řetěz (chain) a je ekvivalentní přidávání u sekvencí s tím rozdílem, že se nic nevyhodnocuje, pokud to není zapotřebí.

##### Python Docs

Vytvořte iterátor, který vyčerpá prvky z prvního a poté z druhého iteráblu (iterovatelného objektu). Používá se pro ošetření následných sekvencí jako jediné sekvence. Zřetězené vstupy jsou vyhodnocovány líně. Zhruba ekvivalentní k:
```coconut_python
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```

##### Příklad

###### Coconut
```coconut
def N(n=0) = (n,) :: N(n+1) # no infinite loop because :: is lazy

(range(-10, 0) :: N())$[5:15] |> list |> print
```

###### Python

_Nelze provést bez komplikované komprehence iterátoru namísto líného řetězení. Viz kompilovaný kód pro skladbu Pythonu._

### Krájení iterátoru 

K provedení iterátorového členění používá Coconut znak `$` mezi iterátorem a označením jeho úseku. Iterátorové členění pracuje stejně jako sekvenční členění v Pythonu a vypadá stejně jako částečná aplikace, avšak s hranatymi místo kulatých závorek. It has the same precedence as subscription.

Iterátorové členění pracuje stejně jako sekvenční členění, včetně podpory negativních indexů a úseků (slices) a podpory pro objekty `úseků` stejně jako u normálního členění. Iterátorové členění však nezaručuje, že bude zachován původní iterátor (pro jeho zachování použijte [funkci`tee`](#tee)).

Iterátorové členění v Coconut je velmi podobné `itertools.islice` v Pythonu, avšak na rozdíl od `itertools.islice`, podporuje iterátorové členění negativní index a přednostně použije  `__getitem__` objektu, pokud existuje. Iterátorové členění je také optimalizované pro práci s objekty `map`, `zip`, `range` a `count`, počítaje pouze ty prvky, které jsou nezbytné pro vynětí žádaného úseku.

##### Příklad

###### Coconut
```coconut
map((x)->x*2, range(10**100))$[-1] |> print
```

###### Python
_Nelze provést bez komplikované funkce pro iterátorové členění a inspekce uživatelských objektů. Nezbytné definice v Pythonu lze nalézt v záhlaví Coconut._

### Alternativy Unicode <a id="unicode-alternatives"></a>

Coconut podporuje alternativy Unicodu pro různé operátové symboly. Alternativy jsou poměrně nápovědné, se záměrem reflektovat vzhled nebo účel originálního symbolu. 

##### Full List

```
→ (\u2192)                  => "->"
↦ (\u21a6)                  => "|>"
*↦ (*\u21a6)                => "|*>"
↤ (\u21a4)                  => "<|"
↤* (\u21a4*)                => "<*|"
⋅ (\u22c5)                  => "*"
↑ (\u2191)                  => "**"
÷ (\xf7)                    => "/"
÷/ (\xf7/)                  => "//"
∘ (\u2218)                  => ".."
− (\u2212)                  => "-" (only subtraction)
⁻ (\u207b)                  => "-" (only negation)
¬ (\xac)                    => "~"
≠ (\u2260) or ¬= (\xac=)    => "!="
≤ (\u2264)                  => "<="
≥ (\u2265)                  => ">="
∧ (\u2227) or ∩ (\u2229)    => "&"
∨ (\u2228) or ∪ (\u222a)    => "|"
⊻ (\u22bb) or ⊕ (\u2295)    => "^"
« (\xab)                    => "<<"
» (\xbb)                    => ">>"
… (\u2026)                  => "..."
× (\xd7)                    => "@" (only matrix multiplication)
```

## Klíčová slova 

### `data` 

Syntaxe datového bloku `data` je něco mezi syntaxí pro funkce a syntaxí pro třídy. První řádek vypadá jako definice funkce, zatímco zbytek těla připomíná třídu, obvykle obsahující definice metod. Je to tak proto, že zatímco blok `data` vlastně v Pythonu končí jako třída, Coconut automatický vytváří specielní, neměnitelný konstruktor, založený na daných argumentech.

Bloky typu `data` vytvářejí v Coconut neměnitelné třídy pomocí parametru `__slots__` a odvozené z `collections.namedtuple`. Skladba deklarace datového bloku vypadá takto:
```coconut
data <name>(<args>):
    <body>
```
`<name>` je název nového datového typu, `<args>` jsou argumenty jeho konstruktoru stejně jako názvy jeho atributů a `<body>` obsahuje metody datového typu.

Subtřídy datových typů lze snadno vytvořit děděním do normální `třídy` Pythonu. Aby se stala nová subtřída neměnitelná, je nutné do ní vložit řádek
```coconut
__slots__ = ()
```
před definicemi metod nebo atributů.

##### Zdůvodnění

Hlavní část funkcionálního programování, které Coconut v Pythonu zlepšuje, je použití hodnot nebo neměnitelných datových typů. Neměnitelná data jsou velmi užitečná ale vytvoření takových typů v Pythonu je velice obtížné. Coconut vytváří neměnitelné datové typy velice snadno použitím bloků typu `data`.

##### Python Docs

Vrací novou subtřídu entice (tuple). Nová subtřída je použita k vytvoření entici podobných objektů, jejichž pole jsou přístupná přes vzhled (lookup) atributu a jsou indexovatelná a iterovatelná. Instance subtřídy mají také nápomocný docstring (se jménem typu a pole) a metodu  `__repr__()`, která uvádí obsah entice ve formátu `name=value`.

Pro název pole lze použít libovolný platný identifikátor Pythonu. Platné identifikátorý se skládají z písmen, číslic a podtržítek ale nezačínají číslicí nebo podtržítkem a nejsou klíčovým slovem jako _class, for, return, global, pass nebo raise_.

Pojmenované instance entic nemají individuální slovníky (dictionaries), takže jsou úsporné a nevyžadujíc více paměti než normální entice.

##### Příklady

###### Coconut
```coconut
data vector(x, y):
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5

v = vector(3, 4)
v |> print # all data types come with a built-in __repr__
v |> abs |> print
v.x = 2 # this will fail because data objects are immutable
```
_Demonstruje skladbu, vlastnosti a neměnitelnou povahu typů `data`._
```coconut
data Empty(): pass
data Leaf(n): pass
data Node(l, r): pass
Tree = (Empty, Leaf, Node)

def size(Tree()) = 0

@addpattern(size)
def size(Tree(n)) = 1

@addpattern(size)
def size(Tree(l, r)) = size(l) + size(r)

size(Node(Empty(), Leaf(10))) == 1
```
_Demonstruje algebraickou povahu typů `data` při kombinaci s pattern-matching._

###### Python
```coconut_python
import collections
class vector(collections.namedtuple("vector", "x, y")):
    __slots__ = ()
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5

v = vector(3, 4)
print(v)
print(abs(v))
v.x = 2
```
```coconut
import collections
class Empty(collections.namedtuple("Empty", "")):
    __slots__ = ()
class Leaf(collections.namedtuple("Leaf", "n")):
    __slots__ = ()
class Node(collections.namedtuple("Node", "l, r")):
    __slots__ = ()

def size(tree):
    if isinstance(tree, Empty):
        return 0
    elif isinstance(tree, Leaf):
        return 1
    elif isinstance(tree, Node):
        return size(tree[0]) + size(tree[1])
    else:
        raise MatchError()

size(Node(Empty(), Leaf(10))) == 1
```

### `match` 

Coconut poskytuje plnohodotné, funkcionální `pattern-matching` prostřednictvím svých příkazů `match`.

##### Úvod 

Příkazy `match` konvenují se základní skladbou `match <pattern> in <value>`. Příkaz match se pokusí porovnat hodnotu se vzorkem a v případě shody sváže proměnnou ve vzorku s odpovídající pozicí v hodnotě a provede následný kód za příkazem match. Příkazy match také ve své základní skladbě podporují podmínku `if <cond>`, která se vyhodnotí po nalezení shody před provedením následného kódu a příkaz `else`, který se provede, pokud ke shodě nedojde. Všechny možnosti příkazu match nemají ekvivalent v Pythonu a proto následuje vysvětlení jednotlivých specifikací.

##### Specifikace skladby

Skladba příkazu match v Coconut je
```coconut
match <pattern> in <value> [if <cond>]:
    <body>
[else:
    <body>]
```
kde `<value>` je položka, v níž se hledá shoda, `<cond>` je volitelná dodatečná podmínka a `<body>` je kód, který se provede při splnění výše uvedeného záhlaví. Vstup `<pattern>` má svoji vlastní specifickou skladbu, definovanou zhruba takto:

```coconut
pattern ::= (
    "(" pattern ")"                 # závorky
    | "None" | "True" | "False"     # konstanty 
    | "=" NAME                      # ověření (checks)
    | NUMBER                        # čísla
    | STRING                        # řetězce
    | [pattern "as"] NAME           # capture
    | NAME "(" patterns ")"         # datové typy
    | "(" patterns ")"              # sekvence mohou mít formu entice
    | "[" patterns "]"              #  nebo formu seznamu
    | "(|" patterns "|)"            # líné seznamy
    | "{" pattern_pairs "}"         # slovníky
    | ["s"] "{" pattern_consts "}"  # sety
    | ("(" | "[")                   # star splits
        patterns,
        "*" middle,
        patterns
      (")" | "]")                       # must both be parens or brackets
    | (                             # head-tail splits
        "(" patterns ")"
        | "[" patterns "]"
      ) "+" pattern
    | pattern "+" (                 # init-last splits
        "(" patterns ")"
        | "[" patterns "]"
      )
    | (                             # head-last splits
        "(" patterns ")"
        | "[" patterns "]"
      ) "+" pattern "+" (
        "(" patterns ")"                # this match must be the same
        | "[" patterns "]"              #  construct as the first match
      )
    | (                             # iterator splits
        "(" patterns ")"
        | "[" patterns "]"
        | "(|" patterns "|)"
      ) "::" pattern
    | pattern "is" exprs            # type-checking
    | pattern "and" pattern         # match all
    | pattern "or" pattern          # match any
    )
```

##### Specifikace významů

Příkaz `match` přijme vzorek a pokusí se k němu nalézt shodu v zadaných argumentech. Vzorek může obsahovat různé struktury:
- Konstanty, čísla a řetězce: se budou shodovat se stejnou konstantou, číslem či řetězcem na stejných pozicích argumentů.
- Proměnné: se budou shodovat a budou propojené s čímkoli - s několika výjimkami:
  * Je-li táž proměnná použita vícekrát, provede se kontrola, zda se každý výskyt shoduje se stejnou hodnotou.
  * Je-li názvem proměnné `_`, všechno se s ní bude shodovat ale nic nebude připojeno.
- Explicitní vazby (`<pattern> as <var>`): připojí `<var>` k `<pattern>`.
- Ověření (`=<var>`): ověří (checks), zda je kontrolovaná pozice rovna dříve definované proměnné `<var>`.
- Ověření typu (`<var> is <types>`): před připojením k proměnné `<var>` ověří, zda kontrolovaná pozice je typu `<types>`.
- Datové typy (`<name>(<args>)`): ověří, zda kontrolovaná pozice je typu `<name>` a spáruje atributy s `<args>`.
- Seznamy (`[<patterns>]`), entice (`(<patterns>)`) nebo líné seznamy (`(|<patterns>|)`): spáruje pouze sekvence (`collections.abc.Sequence`) stejné délky a porovná obsah vůči `<patterns>`.
- Dicts (`{<pairs>}`): spáruje pouze mapping (`collections.abc.Mapping`) stejné délky a porovná obsah vůči `<pairs>`.
- Sety (`{<constants>}`): spáruje pouze set (`collections.abc.Set`) se stejnou délkou a obsahem.
- Head-Tail Splits (`<list/tuple> + <var>`): porovná počátek sekvence vůči `<list/tuple>`, zbytek připojí k `<var>` a učiní jej typem použitého konstruktu.
- Init-Last Splits (`<var> + <list/tuple>`): přesně totéž jako head-tail splits ale vzhledem ke konci, nikoliv k počátku sekvence.
- Head-Last Splits (`<list/tuple> + <var> + <list/tuple>`): kombinace předchozích dvou operací.
- Iterator Splits (`<list/tuple/lazy list> :: <var>` nebo `<lazy list>`): porovná počátek iteráblu (`collections.abc.Iterable`) s `<list/tuple/lazy list>`, potom připojí zbytek k `<var>` nebo ověří, že je iteráble proveden.

_Poznámka: Podobně jako u [krájení iterátoru](#krajeni-iteratoru), porovnávání iterátoru a líného seznamu nezaručují, že původní porovnávaný iterátor zůstane zachovaný (pro zachování iterátoru použijte [funkci `tee`](#tee)._

Při ověřování zda může být objekt porovnáván určitým způsobem používá Coconut abstraktní bázové třídy Pythonu. Je tedy nutné registrovat uživatelský objekt jako příslušnou bázovou třídu.

##### Příklady

###### Coconut
```coconut
def factorial(value):
    match 0 in value:
        return 1
    else: match n is int in value if n > 0: # possible because of Coconut's
        return n * factorial(n-1)           #   enhanced else statements
    else:
        raise TypeError("invalid argument to factorial of: "+repr(value))

3 |> factorial |> print
```
_Demonstrace příkazů `else`, které pracují skoro stejně jako v Pythonu: kód pod příkazem `else` je proveden pouze tehdy, když selže příslušející srovnávání._
```coconut
data point(x, y):
    def transform(self, other):         # konstruktor
        match point(x, y) in other:
            return point(self.x + x, self.y + y)
        else:
            raise TypeError("arg to transform must be a point")
    def __eq__(self, other):            # konstruktor
        match point(=self.x, =self.y) in other:
            return True
        else:
            return False

point(1,2) |> point(3,4).transform |> print
point(1,2) |> point(1,2).__eq__ |> print
```
_Demonstrace porovnávání datových typů. Hodnoty, definované příkazem `data`, mohou být konfrontovány a jejich obsahy zpřístupněny s použitím konstruktorů datového typu `point`._
```coconut
data Empty(): pass
data Leaf(n): pass
data Node(l, r): pass
Tree = (Empty, Leaf, Node)

def depth(Tree()) = 0

@addpattern(depth)
def depth(Tree(n)) = 1

@addpattern(depth)
def depth(Tree(l, r)) = 1 + max([depth(l), depth(r)])

Empty() |> depth |> print                                  # 0
Leaf(5) |> depth |> print                                  # 1
Node(Leaf(2), Node(Empty(), Leaf(3))) |> depth |> print    # 3
```
_Ukázka kombinace datových typů a porovnávacích (match) příkazů při opakovaném použití algebraických datových typů v jiných funkcionálních programovacích jazycích._
```coconut
def duplicate_first(value):
    match [x] + xs as l in value:
        return [x] + l
    else:
        raise TypeError()

[1,2,3] |> duplicate_first |> print
```
_Ukázka head-tail krájení (splitting), jednoho z nejvíce používaného způsobu užití pattern-matching, kde `+ <var>` (nebo `:: <var>` pro jakýkoli iterábl) na konci seznamu nebo enticového literálu  může být použit k porovnání se zbytkem sekvence._
```
def sieve([head] :: tail) = [head] :: sieve(n for n in tail if n % head)

@addpattern(sieve)
def sieve((||)) = []
```
_Ukazuje, jak porovnávat vůči iterátorům, totiž že případ prázdného iterátoru (`(||)`) musí přijít jako poslední, jinak tento případ vyčerpá celý iterátor před tím, než přijde ke slovu porovnání s jakoukoli jinou předlohou._

###### Python

_Nelze provést bez dlouhé řady kontrol pro každý příkaz `match`. Viz kompilovaný kód pro skladbu Pythonu._

### `case` 

Příkaz `case` je rozšíření příkazu `match` pro potřebu opakovaného použití příkazů `match` vůči stejné hodnotě. Na rozdíl od osamělých příkazů `match` může uvnitř bloku `case` být úspěšný pouze jeden příkaz match. Obecnější shody (matches) mají být uvedeny pod konkretnějšími shodami.

Každý vzorek v bloku case je porovnáván, dokud není nalezena shoda. Poté se provede příslušné tělo a blok je ukončen. Skladba pro bloky case je
```coconut
case <value>:
    match <pattern> [if <cond>]:
        <body>
    match <pattern> [if <cond>]:
        <body>
    ...
[else:
    <body>]
```
kde `<pattern>` je jakýkoli vzorek pro hledání shody, `<value>` je porovnávaná položka, `<cond>` je volitelná kontrola a `<body>` je kód, který se provede při úspěchu záhlaví. Všimněte si nepřítomnosti `in` v příkazech `match`.

##### Příklad

###### Coconut
```coconut
def classify_sequence(value):
    out = ""        # unlike with normal matches, only one of the patterns
    case value:     #  will match, and out will only get appended to once
        match ():
            out += "empty"
        match (_,):
            out += "singleton"
        match (x,x):
            out += "duplicate pair of "+str(x)
        match (_,_):
            out += "pair"
        match _ is (tuple, list):
            out += "sequence"
    else:
        raise TypeError()
    return out

[] |> classify_sequence |> print
() |> classify_sequence |> print
[1] |> classify_sequence |> print
(1,1) |> classify_sequence |> print
(1,2) |> classify_sequence |> print
(1,1,1) |> classify_sequence |> print
```

###### Python

_Nelze provést bez dlouhé řady kontrol pro každý příkaz `match`. Viz kompilovaný kód pro skladbu Pythonu._

### Backslash-Escaping 

Klíčová slova `data`, `match`, `case`, `async` (keyword in Python 3.5) a `await` (keyword in Python 3.5) jsou v Coconut rovněž platná jména proměnných. I když Coconut umí tyto dva případy použití rozlišit, je možné pro zvýraznění použít před takovýmto názvem proměnné zpětné lomítko.

##### Příklad

###### Coconut
```coconut
\data = 5
print(\data)
```

###### Python
```coconut_python
data = 5
print(data)
```

### Vyhrazené proměnné 

Není povoleno aby název proměnné začínal `_coconut`, protože tyto proměnné jsou vyhrazeny pro kompilátor.

## Výrazy 

### Příkaz lambda 

Skladba příkazu lambda je rozšířením normální skladby [lambda](#lambda) pro podporu příkazů, nikoliv pouze výrazů.

Skadba pro příkaz lambda je:
```
def (arguments) -> statement; statement; ...
```
kde `statement` může být příkaz přiřazení nebo keyword statement. Je-li poslední `statement` (nenásledovaný středníkem) `výrazem`, je automaticky vrácen.

Příkazy lambda rovněž podporují implicitní skladbu lambda, u níž je při vypuštění argumentů, jako v `def -> _`, předpokládán výraz `def (_=None) -> _`.

##### Příklad

###### Coconut
```coconut
L |> map$(def (x) -> y = 1 / x; y*(1 - y))
```

###### Python
```coconut_python
def _lambda(x):
    y = 1 / x
    return y*(1 - y)
map(_lambda, L)
```

### Líné seznamy 

Coconut podporuje vytváření líných seznamů, jejichž obsah je považován za iterátor a není vyhodnocen, dokud není zapotřebí. Líné seznamy (lazy lists) se v Coconut vytvářejí jednoduše uzavřením čárkami odděleného výčtu do specielních závorek `(|` a `|)` (takzvaných "banana brackets") místo do `[` a `]` u seznamů nebo do `(` a `)` u entic.

Líné seznamy používají ke zlenivění stejný mechanizmus jako u iterátorového řetězení a tudíž je líný seznam `(| x, y |)` ekvivalentní výrazu iterátorového řetězení `(x,) :: (y,)`, byť líný seznam nevytváří mezilehlé entice.

##### Zdůvodnění

Líné seznamy, jejichž sekvence jsou vyhodnocovány jen v případě potřeby, jsou stěžejním útvarem funkcionálního programování, umožňujícím dynamické vyhodnocování jejich obsahu.

##### Příklad

###### Coconut
```coconut
(| print("hello,"), print("world!") |) |> consume
```

###### Python
_Nelze provést bez složité komprehence iterátoru. Viz kompilovaný kód pro skladbu Pythonu._

### Implicitní částečná aplikace 

Coconut podporuje řadu různých skladebných aliasů pro obecné případy částečné aplikace. Jsou to:
```coconut
.attr           =>      operator.attrgetter("attr")
.method(args)   =>      operator.methodcaller("method", args)
obj.            =>      getattr$(obj)
func$           =>      ($)$(func)
seq[]           =>      operator.getitem$(seq)
iter$[]         =>      # the equivalent of seq[] for iterators
.[a:b:c]        =>      operator.itemgetter(slice(a, b, c))
.$[a:b:c]       =>      # the equivalent of .[a:b:c] for iterators
```

##### Example

###### Coconut
```coconut
1 |> "123"[]
mod$ <| 5 <| 3
```

###### Python
```coconut_python
"123"[1]
mod(5, 3)
```

### Literály setu 

Coconut umožňuje předsadit písmeno `s` nebo `f` před deklaraci setu (množiny). Spojení `s{}` informuje Coconut, že jde o prázdný set a nikoli o prázdný slovník. Spojení `f{}` generuje `frozenset`.

##### Příklad

###### Coconut
```coconut
empty_frozen_set = f{}
```

###### Python
```coconut_python
empty_frozen_set = frozenset()
```

### Literály imaginárního čísla 

Jako doplněk k zápisu imaginárního čísla v Pythonu pomocí literálů `<num>j` nebo `<num>J` přidává Coconut ještě literály `<num>i` nebo `<num>I` pro zlepšení čitelnosti při použití v matematickém kontextu.

##### Python Docs

Literály imaginárního čísla (imaginární literály) jsou popsány následujícími lexikálními definicemi:
```coconut
imagnumber ::= (floatnumber | intpart) ("j" | "J" | "i" | "I")
```
Imaginární literál generuje komplexní číslo s hodnotou reálné části o velikosti 0.0. Komplexní čísla jsou prezentována jako dvojice desetinných čísel se stejným omezením jejich rozsahu. Komplexní číslo s nenulovou reálnou částí vytvoříte přidáním desetinného čísla, např. (3+4i). Několik příkladů imaginárních literálů (neboli imaginárních částí):
```coconut
3.14i   10.i    10i     .001i   1e100i  3.14e-10i
```

##### Příklad

###### Coconut
```coconut
3 + 4i |> abs |> print
```

###### Python
```coconut_python
print(abs(3 + 4j))
```

### Podtržítkové separátory 

Pro snadnější čitelnost umožňuje Coconut použití podtržítka pro optické rozdělení velkého čísla. Kompilátor tato podtržítka ignoruje.

##### Příklad

###### Coconut
```coconut
10_000_000.0
```

###### Python
```coconut_python
10000000.0
```

## Definice funkce 

### Optimalizace koncového volání 

Coconut provede automatickou optimalizaci koncovým voláním u každé funkce, která vyhoví následujícím kriteriím:

1. musí přímo vrátit (s použitím buď `return` nebo [přiřazovací funkce](#prirazovaci-funkce)) volání sama sebe (eliminace koncového volání - nejúčinnější optimalizace) nebo jiné funkce (optimalizace koncového volání).
2. nesmí to být generátor (používající `yield`) nebo asynchronní funkce (používající`async`).

_Poznámka: Optimalizace koncovým voláním pracuje i pro 1) vzájemnou rekurzi a 2) porovnávací (pattern-matching) funkce, rozdělené do několika definicí s pouožitím [`addpattern`](#addpattern) nebo [`prepattern`](#prepattern)._

Setkáte-li se s `RuntimeError` v souvislosti s maximální hloubkou rekurze, je velmi vhodné přepsat svou funkci aby vyhověla výše uvedenému kriteriu pro optimalizaci koncovým voláním nebo odpovídajícímu kriteriu pro [`recursive_iterator`](#recursive-iterator), obojí by mělo takové chybě zabránit.

##### Příklad

###### Coconut
```coconut
def factorial(n, acc=1):
    case n:
        match 0:
            return acc
        match _ is int if n > 0:
            return factorial(n-1, acc*n)
    else:
        raise TypeError("the argument to factorial must be an integer >= 0")
```

###### Python

_Nelze provést bez přepsání funkce._

### Operátorové funkce 

Coconut používá jednoduchou výrazovou zkratku: uzavření do závorek činí z operátoru funkci. Podobně jako u iterátorových komprehencí, je-li operátorová funkce jediný argument funkce, mohou závorky volání funkce sloužit jako závorky operátorové funkce.

##### Zdůvodnění

Velmi často prováděným úkonem ve funkcionálním programování je využití funkčních verzí vestavěných operátorů: 'currying them, composing them, and piping them'. Pro usnadnění těchto úkonů poskytuje Coconut zkrácenou syntaxi pro přístup k operátorovým funkcím.

##### Úplný seznam

```coconut
(|>)        => # pipe forward
(|*>)       => # multi-arg pipe forward
(<|)        => # pipe backward
(<*|)       => # multi-arg pipe backward
(..)        => # function composition
(.)         => (getattr)
(::)        => (itertools.chain) # will not evaluate its arguments lazily
($)         => (functools.partial)
(+)         => (operator.add)
(-)         => # 1 arg: operator.neg, 2 args: operator.sub
(*)         => (operator.mul)
(**)        => (operator.pow)
(/)         => (operator.truediv)
(//)        => (operator.floordiv)
(%)         => (operator.mod)
(&)         => (operator.and_)
(^)         => (operator.xor)
(|)         => (operator.or_)
(<<)        => (operator.lshift)
(>>)        => (operator.rshift)
(<)         => (operator.lt)
(>)         => (operator.gt)
(==)        => (operator.eq)
(<=)        => (operator.le)
(>=)        => (operator.ge)
(!=)        => (operator.ne)
(~)         => (operator.inv)
(@)         => (operator.matmul)
(not)       => (operator.not_)
(and)       => # boolean and
(or)        => # boolean or
(is)        => (operator.is_)
(in)        => (operator.contains)
```

##### Příklad

###### Coconut
```coconut
(range(0, 5), range(5, 10)) |*> map$(+) |> list |> print
```

###### Python
```coconut_python
import operator
print(list(map(operator.add, range(0, 5), range(5, 10))))
```

### Přiřazovací funkce 

Coconut umožňuje definování přiřazovací funkce tak, aby automaticky vrátila poslední řádek těla funkce. Přiřazovací funkce je vyjádřena náhradou `=` za `:`, takže složení přiřazovací funkce je buď 
```coconut
def <name>(<args>) = <expr>
```
pro jednořádkovou funkci nebo
```coconut
def <name>(<args>) =
    <stmts>
    <expr>
```
pro víceřádkovou funkci, kde `<name>` je název funkce, `<args>` jsou argumenty funkce, `<stmts>` jsou přípustné příkazy a `<expr>` je hodnota, kterou má funkce vrátit.

_Note: Definice přiřazovací funkce může být kombinována s definicí infixové a/nebo porovnávací (pattern-matching) funkce._

##### Zdůvodnění

Zápis definice přiřazovací funkce je stejně snadný jako přiřazení k funkci lambda a objeví se ve zpětných výpisech (tracebacks), protože kompiluje na normální definici funkce Pythonu.

##### Příklad

###### Coconut
```coconut
def binexp(x) = 2**x
5 |> binexp |> print
```

###### Python
```coconut_python
def binexp(x): return 2**x
print(binexp(5))
```

### Pattern matching 

Coconut podporuje vyhledávání shody s předlohou (pattern-matching), jíž jsou argumenty v definici funkce. Skladba definice porovnávací funkce je
```coconut
[match] def <name>(<pattern>, <pattern>, ... [if <cond>]):
    <body>
```
Kde `<name>` je název funkce, `<cond>` je nepovinná dodatečná kontrola, `<body>` je tělo funkce,  `<pattern>` je definován [příkazem `match`](#match) a  `<default>` je volitelná implicitní hodnota, není-li žádný argument zadán. Klíčové slovo `match` na začátku je nepovinné ale je někdy nezbytné pro odlišení definice porovnávací funkce od normální definice funkce, která má vždy přednost. 

Je-li `<pattern>` jméno proměnné (přímo nebo s `<as>`), podporuje výsledná porovnávací funkce klíčové argumenty stejného jména. Jestliže provedení porovnávací funkce selže, vyvolá objekt [`MatchError`](#matcherror), stejně jako [rozložené přiřazení](#rozlozene-prirazeni).

_Poznámka: Definice porovnávací funkce může být kombinována s definicí přiřazovací a/nebo infixové funkce._

##### Příklad

###### Coconut
```coconut
def last_two(_ + [a, b]):
    return a, b
def xydict_to_xytuple({"x":x is int, "y":y is int}):
    return x, y

range(5) |> last_two |> print
{"x":1, "y":2} |> xydict_to_xytuple |> print
```

###### Python

_Nelze provést bez dlouhé řady kontrol na počátku funkce. Viz kompilovaný kód pro skladbu Pythonu._


### Infixové funkce 

Coconut umožňuje infixové použití funkce, kde je název funkce umístěn mezi operandy a je obklopen zpětnými apostrofy. Volání se zpětným apostrofem (backtick calling) má prioritu mezi 'chaining and piping'.

Skladba definice infixové funkce je
```coconut
def <arg> `<name>` <arg>:  # asi má být `=` místo `:`
    <body>
```
kde `<name>` je název funkce, `<arg>` jsou parametry funkce a `<body>` je tělo funkce. Obsahuje-li `<arg>` ?? default ??, musí být parametry uvedeny v závorkách.

_Poznámka: Definici infixové funkce lze kombinovat s definicí přířazovací a/nebo porovnávací (pattern-matching) funkce._

##### Zdůvodnění

Infixové funkce jsou ve funkcionálním programování obvyklé.

##### Příklad

###### Coconut
```coconut
def a `mod` b = a % b
(x `mod` 2) `print`
```

###### Python
```coconut_python
def mod(a, b): return a % b
print(mod(x, 2))
```



## Příkazy

### Rozložené přiřazení 

Coconut podporuje výrazně zlepšené rozložené přiřazení (destructuring assignment), podobné rozkládání entice/seznamu v Pythonu. Skladba rozloženého přiřazení je
```coconut
[match] <pattern> = <value>
```
kde `<value>` je libovolný výraz a `<pattern>` je definován  [příkazem `match`](#match). Klíčové slovo `match` na začátku je nepovinné ale je někdy nezbytné pro odlišení rozloženého přiřazení od normálního přiřazení, které má vždy přednost. Rozložené přiřazení v Coconut je ekvivalentní příkazu `match`, jehož skladba je:
```coconut
match <pattern> in <value>:
    pass
else:
    err = MatchError(<error message>)
    err.pattern = "<pattern>"
    err.value = <value>
    raise err
```
Selže-li provádění rozloženého přiřazení, potom místo pokračování jako při selhání u bloku `match`, je evokován objekt [`MatchError`](#matcherror), popisující selhání.

##### Příklad

###### Coconut
```coconut
def last_two(l):
    _ + [a, b] = l
    return a, b

[0,1,2,3] |> last_two |> print
```

###### Python

_Nelze provést bez dlouhé řady kontrol místo příkazu rozloženého přiřazení. Viz kompilovaný kód pro skladbu Pythonu._

### Dekorátory 

Narozdíl od Pythonu, který v dekorátoru podporuje pouze jedinou proměnnou nebo volání funkce, podporuje Coconut libovolný výraz.

##### Příklad

###### Coconut
```coconut
@ wrapper1 .. wrapper2 $(arg)
def func(x) = x**2
```

###### Python
```coconut_python
def wrapper(func):
    return wrapper1(wrapper2(arg, func))
@wrapper
def func(x):
    return x**2
```

### Příkazy `else` 

Coconut podporuje složené příkazy `try`, `if` a `match` na konci příkazu `else` jako u každého jiného jednoduchého příkazu. To je nejvíce užitečné pro společné používání příkazů `match` a `if` a také umožňuje vytváření složených příkazů  `try`.

##### Příklad

###### Coconut
```coconut
try:
    unsafe_1()
except MyError:
    handle_1()
else: try:
    unsafe_2()
except MyError:
    handle_2()
```

###### Python
```coconut_python
try:
    unsafe_1()
except MyError:
    handle_1()
else:
    try:
        unsafe_2()
    except MyError:
        handle_2()
```

### Příkazy `except` 

Má-li být v Pythonu3 podchyceno více výjimek najednou, musejí být vloženy do závorek aby se v Pythonu2 zabránilo použití čárky místo `as`. Coconut umožňuje použití čárek ve výjimkových příkazech pro odchycení vícerých výjímek bez závorek.

##### Příklad

###### Coconut
```coconut
try:
    unsafe_func(arg)
except SyntaxError, ValueError as err:
    handle(err)
```

###### Python
```coconut_python
try:
    unsafe_func(arg)
except (SyntaxError, ValueError) as err:
    handle(err)
```

### Implicitní `pass` 

Coconut umožňuje zjednodušený zápis `class name(base)` a `data name(args)` místo `class name(base): pass` a `data name(args): pass`.

##### Příklad

###### Coconut
```coconut
data Empty
data Leaf(item)
data Node(left, right)
```

###### Python
```coconut_python
import collections

class Empty(collections.namedtuple("Empty", "")):
    __slots__ = ()
class Leaf(collections.namedtuple("Leaf", "n")):
    __slots__ = ()
class Node(collections.namedtuple("Node", "l, r")):
    __slots__ = ()
```

### Pokračování v závorkách 

Coconut umožňuje u příkazů `del`, `global`, `nonlocal` a `with` rozložení zápisu na více řádků s použitím závorek místo zpětných lomítek `\` jako u Pythonu.

##### Příklad

###### Coconut
```coconut
global (really_long_global_variable_name_the_first_one,
        really_long_global_variable_name_the_second_one)
```

###### Python
```coconut_python
global really_long_global_variable_name_the_first_one, \
        really_long_global_variable_name_the_second_one
```

### Zjednodušené určení `global` a `nonlocal` 

Coconut umožňuje deklaraci `global` či `nonlocal` v jednom řádku bez opakování názvu proměnné.

##### Příklad

###### Coconut
```coconut
global state_a, state_b = 10, 100
```

###### Python
```coconut_python
global state_a, state_b; state_a, state_b = 10, 100
```

### Průchod kódu 

Kvůli kompatibilitě s jinými variantami Pythonu, jako je [Cython](http://cython.org/) nebo [Mython](http://mython.org/),
podporuje Coconut schopnost protáhnout inertním způsobem libovolný kód kompilátorem. Cokoli umístěného mezi `\(` a `\)` projde netečně kompilátorem, stejně jako řádek, začínající `\\`.

##### Příklad

###### Coconut
```coconut
\\cdef f(x):
    return x |> g
```

###### Python
```coconut_python
cdef f(x):
    return g(x)
```

## Vestavěné funkce 

### `addpattern` 

Tato funkce přijímá argument, jenž je [pattern-matching funkcí](#porovnavaci-funkce) a vrací dekorátor, který přidává předlohy z existující funkce do nové dekorované funkce, v níž je existující předloha ověřována jako první. Její skladba je zhruba ekvivalentní k:
```
def addpattern(base_func):
    """Decorator to add a new case to a pattern-matching function, where the new case is checked last."""
    def pattern_adder(func):
        def add_pattern_func(*args, **kwargs):
            try:
                return base_func(*args, **kwargs)
            except MatchError:
                return func(*args, **kwargs)
        return add_pattern_func
    return pattern_adder
```

##### Příklad

###### Coconut
```
def factorial(0) = 1

@addpattern(factorial)
def factorial(n) = n * factorial(n - 1)
```

###### Python
_Nelze provést bez komplikované definice dekorátoru a dlouhé řady kontrol pro každé porovnávání. Viz kompilovaný kód pro skladbu Pythonu._

### `prepattern` 

Tato funkce přijímá argument, jenž je [pattern-matching funkcí](#porovnavaci-funkce) a vrací dekorátor, který přidává předlohy z existující funkce do nové dekorované funkce, v níž je existující předloha ověřována jako první. Je zhruba ekvivalentní k:
```
def prepattern(base_func):
    """Decorator to add a new case to a pattern-matching function, where the new case is checked first."""
    def pattern_prepender(func):
        return addpattern(func)(base_func)
    return pattern_prepender
```

##### Příklad

###### Coconut
```
def factorial(n) = n * factorial(n - 1)

@prepattern(factorial)
def factorial(0) = 1
```

###### Python
_Nelze provést bez komplikované definice dekorátoru a dlouhé řady kontrol pro každé porovnávání._

### `reduce` 

Coconut znovu uvádí funkci `reduce` z Python2, používaje verze `functools.reduce`.

##### Python Docs

**reduce**(_function, iterable_**[**_, initializer_**]**)

Funkce `reduce` použije opakovaně funkci se dvěmi proměnnými pro iterovatelný objekt, kumulujíc mezivýsledky do výsledné výstupní hodnoty. Například, `reduce((x, y) -> x+y, [1, 2, 3, 4, 5])` počítá `((((1+2)+3)+4)+5)`. Levý argument _x_  je akumulovaná hodnota a pravý argument _y_ je aktuální hodnota ze sekvence. Je-li přítomen nepovinný _iniciátor_, je umístěn před položky sekvence a slouží jako implicitní hodnota, je-li sekvence prázdná.

##### Příklad

###### Coconut
```coconut
prod = reduce$(*)
range(1, 10) |> prod |> print
```

###### Python
```coconut_python
import operator
import functools
prod = functools.partial(functools.reduce, operator.mul)
print(prod(range(1, 10)))
```

### `takewhile` 

Coconut poskytuje `itertools.takewhile` jako vestavěnou funkci pod názvem `takewhile`.

##### Python Docs

**takewhile**(_predicate, iterable_)

Vytvoří iterátor, který vrací prvky _iteráblu_, pokud je _predicate_ pravdivý. Ekvivalentní k:
```coconut_python
def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
```

##### Příklad

###### Coconut
```coconut
negatives = takewhile(numiter, (x) -> x<0)
```

###### Python
```coconut_python
import itertools
negatives = itertools.takewhile(numiter, lambda x: x<0)
```

### `dropwhile` 

Coconut poskytuje `itertools.dropwhile` jako vestavěnou funkci pod názvem `dropwhile`.

##### Python Docs

**dropwhile**(_predicate, iterable_)

Vytvoří iterátor, který vypouští prvky z _iteráblu_ pokud je _predicate_ pravdivý; poté vrací každý prvek. Poznámka: iterátor neprodukuje žádný výstup, dokud se predikát poprvé nestane nepravdivý. Ekvivalentní k:
```coconut_python
def dropwhile(predicate, iterable):
    # dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
    iterable = iter(iterable)
    for x in iterable:
        if not predicate(x):
            yield x
            break
    for x in iterable:
        yield x
```

##### Příklad

###### Coconut
```coconut
positives = dropwhile(numiter, (x) -> x<0)
```

###### Python
```coconut_python
import itertools
positives = itertools.dropwhile(numiter, lambda x: x<0)
```

### `tee` 

Coconut poskytuje optimalizovanou verzi `itertools.tee` jako vestavěnou funkci pod názvem `tee`.

##### Python Docs

**tee**(_iterable, n=2_)

Vrací _n_ nezávislých iterátorů z jediného iteráblu. Ekvivalentní k:
```coconut_python
def tee(iterable, n=2):
    it = iter(iterable)
    deques = [collections.deque() for i in range(n)]
    def gen(mydeque):
        while True:
            if not mydeque:             # when the local deque is empty
                newval = next(it)       # fetch a new value and
                for d in deques:        # load it to all the deques
                    d.append(newval)
            yield mydeque.popleft()
    return tuple(gen(d) for d in deques)
```
Jakmile `tee()` provede rozdělení, neměl by být původní  _iterábl_ jinde používán; otherwise, the _iterable_ could get advanced without the tee objects being informed.

Tento itertool může vyžadovat významý pomocný úložný prostor (v závisloti na tom, jak mnoho dočasných dat má být uloženo). Obecně lze říci, že když jeden iterátor použije většinu ze všech dat před tím, než spustí další iterátor, je rychlejší použít `list()` místo `tee()`.

##### Příklad

###### Coconut
```coconut
original, temp = tee(original)
sliced = temp$[5:]
```

###### Python
```coconut_python
import itertools
original, temp = itertools.tee(original)
sliced = itertools.islice(temp, 5, None)
```

### `consume` 

Coconut poskytuje funkci `consume` pro účinné vyčerpání iterátoru a pro provedení líného výpočtu. Funkce `consume` přijímá volitelný argument, `keep_last`, jehož implicitní hodnota je 0 a určuje kolik položek od konce vrátit jako iterábl (`None` zachová všechny prvky). Ekvivalentní k:
```coconut
def consume(iterable, keep_last=0):
    """Fully exhaust iterable and return the last keep_last elements."""
    return collections.deque(iterable, maxlen=keep_last) # fastest way to exhaust an iterator
```

##### Zdůvodnění

V procesu líného provádění operací na iterátorech je posléze dosaženo místa, kde je vyhodnocení iterátoru nezbytné. Aby to mohlo být provedeno efektivně, poskytuje Coconut funkci `consume`, která zcela vyčerpá poskytnutý iterátor.

##### Příklad

###### Coconut
```coconut
range(10) |> map$((x) -> x**2) |> map$(print) |> consume
```

###### Python
```coconut_python
collections.deque(map(print, map(lambda x: x**2, range(10))), maxlen=0)
```

### `count` 

Coconut poskytuje modifikovanou verzi `itertools.count`, která podporuje `in`, normální členění (slicing), optimalizoané členění iterátoru, sekvenční metody `count` a `index`, atributy `repr`, `_start` a `_step` jako vestavěnou funkci jménem `count`.

##### Python Docs

**count**(_start=0, step=1_)

Vytvoří iterátor, který vráti rovnoměrně rozmístěné  hodnoty, počínajíc číslem _start_. Používá se často jako argument funkci `map()` ke generování postupných datových bodů. Také se používá s funkcí `zip()` pro připojení pořadových čísel. Zhruba ekvivalentní k:
```coconut_python
def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step
```

##### Příklad

###### Coconut
```coconut
count()$[10**100] |> print
```

###### Python
_Nelze provést rychle bez iterátorového členění Coconutu, jež vyžaduje mnoho složitých částí. Nezbytné definice v Pythonu lze nalézt v záhlaví Coconut._

### `map` a `zip` 

Objekty `map` a `zip` v Coconut jsou vylepšené ekvivalenty Pythonu, které podporují optimalizované normální (a iterátorové) členění, postupy `reversed`, `len`, `repr` a mají přidané atributy, jež mohou použít subtřídy k přístupu k původním argumentům objektu (`map` podporuje `_func` a atributy `_iters` a `zip` podporuje atributy `_iters`).

##### Příklad

###### Coconut
```coconut
map((+), range(5), range(6)) |> len |> print
```

###### Python
_Nelze provést bez definování uživatelského typu  `map`. Úplnou definici `map` lze nalézt v záhlaví Coconut._

### `datamaker` 

Coconut poskytuje funkci `datamaker` pro přímý přístup k bázovému konstruktoru datových typů, vytvořenému příkazem  `data`. Toto je zejména užitečné při psaní alternativních konstruktorů pro datové typy přepsáním metody `__new__`. Ekvivalentní k:
```coconut
def datamaker(data_type):
    """Returns base data constructor of data_type."""
    return super(data_type, data_type).__new__$(data_type)
```

##### Příklad

###### Coconut
```coconut
data trilen(h):
    def __new__(cls, a, b):
        return (a**2 + b**2)**0.5 |> datamaker(cls)
```

###### Python
```coconut_python
import collections
class trilen(collections.namedtuple("trilen", "h")):
    __slots__ = ()
    def __new__(cls, a, b):
        return super(cls, cls).__new__(cls, (a**2 + b**2)**0.5)
```

### `recursive iterator` 

Coconut poskytuje dekorátor `recursive_iterator`, který poskytuje výraznou optimalizaci pro každou bezstavovou (stateless) rekurzivní funkci, která vrací iterátor. Pro použití `recursive_iterator` u funkce musí být splněna následující kritéria:

1. vaše funkce buď vždy `vrací` iterátor nebo generuje iterátor pomocí `yield`,
2. při opakovaném volání pro tytéž argumenty produkuje vaše funkce tentýž iterátor (vaše funkce je bezestavová),
3. vaše funkce volá samu sebe pro tytéž argumenty,
4. všechny argumenty, zadávané funkci jsou serializovatelné (pickleable).

Setkáte-li se s `RuntimeError` následkem maximální hloubky rekurze, je vhodné přepsat funkci tak, aby vyhověla buď výše uvedenému požadavku na `recursive_iterator`nebo odpovídajícím kritériím pro [optimalizaci koncového volání](#optimalizace-koncoveho-volani), jež obojí by mělo takovým chybám zabránit.

Nadto, `recursive_iterator` také umožňuje řešení [of nasty segmentation fault in Python's iterator logic that has never been fixed](http://bugs.python.org/issue14010). Konkrétně, místo zápisu
```coconut
seq = get_elem() :: seq
```
které havaruje v důsledku výše uvedeného problému, pište
```coconut
@recursive_iterator
def seq() = get_elem() :: seq()
```
které poběží uspokojivě.

##### Příklad

###### Coconut
```coconut
@recursive_iterator
def fib() = (1, 2) :: map((+), fib(), fib()$[1:])
```

###### Python

_Nelze provést bez dlouhé definice dekorátoru._

### `parallel map` 

Coconut poskytuje paralelní verzi `map` pod názvem `parallel_map`. `parallel_map` využívá více procesů a je proto mnohem rychlejší než `map` pro úlohy, svázané s CPU. Použití `parallel_map` vyžaduje `concurrent.futures`, jež existují ve standardní knihovně Python 3, avšak v Python 2 bude zapotřebí provést `pip install futures`.

Protože `parallel_map` používá ke svému provedení více procesů, je nezbytné aby všechny její argumenty byly serializovatelné. Serializovatelné (pickleable) jsou pouze objekty definované na úrovni modulu, uvnitř funkce nebo uvnitř interpreta. Navíc, ve Windows je nezbytné aby se všechna volání `parallel_map` vyskytla uvnitř dozoru `if __name__ == "__main__"`.

##### Python Docs

**parallel_map**(_func, \*iterables_)

Ekvivalentní k `map(func, *iterables)` až nato, že _func_ je provedena asynchronně a několik volání _func_ může být provedeno současně. Vyvolá-li volání výjimku, je tato výjimka zvednuta při vyzvedávání jeho hodnoty z iterátoru.

##### Příklad

###### Coconut
```coconut
parallel_map(pow$(2), range(100)) |> list |> print
```

###### Python
```coconut_python
import functools
import concurrent.futures
with concurrent.futures.ProcessPoolExecutor() as executor:
    print(list(executor.map(functools.partial(pow, 2), range(100))))
```

### `concurrent map` 

Coconut poskytuje concurrentní verzi `map` pod názvem `concurrent_map`. `concurrent_map` využívá více vláken a je proto mnohem rychlejší než `map` u úloh související s IO. Použití `concurrent_map` vyžaduje `concurrent.futures`, jež existuje ve standardní knihovně Python 3, avšak v Python 2 bude zapotřebí provést `pip install futures`.

##### Python Docs

**concurrent_map**(_func, \*iterables_)

Ekvivalentní k `map(func, *iterables)` až nato, že _func_ je provedena asynchronně a několik volání _func_ může být provedeno současně. Vyvolá-li volání výjimku, je tato výjimka zvednuta při vyzvedávání jeho hodnoty z iterátoru.

##### Příklad

###### Coconut
```coconut
concurrent_map(get_data_for_user, get_all_users()) |> list |> print
```

###### Python
```coconut_python
import functools
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    print(list(executor.map(get_data_for_user, get_all_users())))
```

### `MatchError` 

Objekt `MatchError` je vyvolán, když selže [destructuring assignment](#rozlozene-prirazeni), načež je `MatchError` poskytnut jako vestavěná procedura pro odchycení takovýchto chyb. Objekty `MatchError` podporují dva atributy, `pattern`, což je řetězec, popisující selhávající předlohu a `value`, což je objekt, který selhal při porovnávání s předlohou.

## Utilita Coconut 

### Zvýraznění skladby 

Současné možnosti pro zvýraznění skladby v Coconut jsou tyto:

1. use **[SublimeText](https://www.sublimetext.com/)** (instructions below),
2. use an editor that supports **[Pygments](http://pygments.org/)** (instructions below),
3. use [`coconut.vim`](https://github.com/manicmaniac/coconut.vim), a third-party **[Vim](http://www.vim.org/)** highlighter,
4. use [`coconut-mode`](https://github.com/NickSeagull/coconut-mode), a third-party **[Emacs](https://www.gnu.org/software/emacs/)** highlighter, or
4. just treat Coconut as Python.

Pokyny pro nastavení skladby zvýrazňování pro SublimeText a Pygments jsou uvedeny níže. Pokud některý z výše uvedených zvýrazňovačů nechodí, potom by mělo stačit nastavit editor tak, aby interpretoval všechny soubory `.coco` (také `.coc` a `.coconut`, byť `.coco` je preferovaná přípona) jako kód Pythonu, neboť se tak dostatečně zvýrazní většina vašeho kódu.

#### SublimeText 

Zvýrazňování skladby Coconut v editoru SublimeText vyžaduje aby byl instalován standardní správce paketů [Package Control](https://packagecontrol.io/installation). Pokud tomu tak je, potom:

1. otevřte příkazovou paletu SublimeTextu stisknutím  `Ctrl+Shift+P`,
2. potvrďte a zvolte `Package Control: Install Package`,
3. potvrďte a zvolte `Coconut`.

Abyste se přesvědčili, že všechno chodí jak má, otevřte soubor `.coco` file a ujistěte se, že se `Coconut` objeví v pravém dolním rohu. Objeví-li se něco jiného, jako třeba `Plain Text`, klikněte na to, zvolte `Open all with current extension as...` a potom vyberte `Coconut`.

#### Pygments 

Tentýž příkaz `pip install coconut`, který instaluje interaktivní utilitu Coconut, instaluje také `coconut` lexer aplikace Pygments. Jak tento lexer použít záleží na použité 'Pygments-enabled' aplikaci, ale obecně se zvolí `coconut` jako zvýrazňovaný jazyk a/nebo použije se platná extenze souboru Coconut (`.coco`, `.coc` nebo `.coconut`) a Pygments by se v tom měl vyznat. Tato dokumentace je například generována pomocí [Sphinx](http://www.sphinx-doc.org/en/stable/). Zvýraznění, které vidíme, bylo vytvořeno přidáním řádku
```coconut_python
highlight_language = "coconut"
```
v souboru `conf.py` Coconutu.

### `coconut.coconut` 

Toto je občas užitečné pro přístup k vestavěným objektům Coconutu z čistého Pythonu. Za tím účelem Coconut poskytuje `coconut.__coconut__`, jenž se chová přesně jako hlavičkový soubor `__coconut__.py`, připojený když je Coconut kompilován v režimu 'package'.

Všechny nativní objekty Coconutu jsou přístupné z `coconut.__coconut__`. Doporučený způsob jejich importu je použití `from coconut.__coconut__ import`. 

##### Example

###### Python
```coconut_python
from coconut.__coconut__ import parallel_map
```

### `coconut.convenience` 

Někdy je užitečné mít možnost použít kompilátor Coconutu z kódu místo z příkazového řádku. Doporučuje se použít `from coconut.convenience import` a importovat potřebnou užitečnou (convenience) funkci. Specifikace různých 'convenience' funkcí jsou uvedeny dále.

#### `parse` <a id="parse"></a>

**coconut.convenience.parse**(_code,_ **[**_mode_**]**)

Patrně nejužitečnější z 'výhodných' funkcí je `parse`, která přijme kód Coconut a vrací ekvivalentní kompilovaný kód Pythonu. Druhý argument, _mode_, se použije k indikaci kontextu pro parsing.

Každý _mode_ má dvě komponenty: jaký parser používá a jaké záhlaví předesílá (prepends). Parser určuje, jaký kód Coconutu je přípustný jako vstup a záhlaví určuje, jak může být kompilovaný Python použit. Možné hodnoty _mode_ jsou:

- `"exec"`: (the default)
    + parser: file
        The file parser can parse any Coconut code.
    + header: exec
        When passed to `exec` at the global level, this header will create all the necessary Coconut objects.
- `"file"`:
    + parser: file
    + header: file
        This header is meant to be written to a `--standalone` file and should not be passed to `exec`.
- `"module"`:
    + parser: file
    + header: module
        This header is meant to be written to a `--package` file and should not be passed to `exec`.
- `"block"`:
    + parser: file
    + header: none
        No header is included, thus this can only be passed to `exec` if the exec header has already been executed at the global level.
- `"single"`:
    + parser: single
        Can only parse one line of Coconut code.
    + header: none
- `"eval"`:
    + parser: eval
        Can only parse a Coconut expression, not a statement.
    + header: none
- `"debug"`:
    + parser: debug
        Can parse any Coconut code and allows leading whitespace.
    + header: none

#### `setup` 

**coconut.convenience.setup**(_target, strict, minify, line\_numbers, keep\_lines_**)**

`setup` lze použít k zadání flagů příkazového řádku, použitých v akci `parse`. Možné hodnoty flagů jsou:

- _target_: `None` (default), or any [allowable target](#pripustne-cile)
- _strict_: `False` (default) or `True`
- _minify_: `False` (default) or `True`
- _line\_numbers_: `False` (default) or `True`
- _keep\_lines_: `False` (default) or `True`

#### `cmd` 

**coconut.convenience.cmd**(_args_, **[**_interact_**]**)

Zpracuje dané _args_, jakoby byly zadáný z příkazového řádku, s tou výjimkou, že pokud _interact_ není `true` nebo nebylo-li zadáno `-i`, interpret se nespustí. Navíc, protože `parse` a `cmd` sdílejí tentýž 'convenience parsing' objekt, 
jakékoli změny pro parsing zadané přes `cmd`, budou pracovat stejně, jakoby byly zavedeny přes `setup`.

#### `version` 

**coconut.convenience.version**(**[**_which_**]**)


Vyhledá řetězec obsahující informaci o verzi Coconut. Nepovinný argument _which_ upřesňuje požadovanou verzi informace. Možné hodnoty _which_ jsou:

- `"num"`: číselná verze (implicitní)
- `"name"`: kódové označení verze
- `"spec"`: číselná verze s připojeným kódovým označením
- `"tag"`: tag verze, použitý v GitHub a v URL dokumentace
- `"-v"`: výstup příkazu `coconut -v` (úplný řetězec)

#### `CoconutException` 

Je-li v 'convenience' funkci detekována chyba, je aktivováno hlášení `CoconutException`. `coconut.convenience.CoconutException` umožňuje odchycení takových chyb.
