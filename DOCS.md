# Dokumentace

```eval_rst
.. contents::
    :local:
	:depth: 2
```



## Úvod

Tato dokumentace pokrývá všechny technické detaily programovacího jazyka [Coconut ](http://evhub.github.io/coconut/) a je zamýšlena spíš jako referenční příručka než podrobný úvod. Úplný úvod a tutoriál pro Coconut - viz [Tutoriál](HELP.html).

Coconut je varianta jazyka [Python](https://www.python.org/), vytvořená pro **jednoduché, elegantní a funkcionální programování v Pythonu**. Skladba Coconut je podmnožna skladby Pythonu 3. To znamená, že uživatel, obeznámený s Pythonem, bude již obeznámený s většinou obsahu Coconut.

Kompilátor jazyka Coconut převádí kód Coconut na kód Pythonu. Primární způsob přístupu ke kompilátoru Coconut je z příkazového řádku utility REPL, jež rovněž obsahuje překladač pro kompilaci v reálném čase. Kromě této konzoly podporuje Coconut také notebooky IPythonu a Jupiteru.

Zatímco většina kódu v Coconut vychází ze snahy umožnit a zjednodušit funkcionální programování v Pythonu, další inspirace pochází z [Haskellu](https://www.haskell.org/), [CoffeeScriptu](http://coffeescript.org/), [F#](http://fsharp.org/) a z extenze Pythonu  [patterns.py](https://github.com/Suor/patterns).

## Kompilace bez instalace

Chcete-li vyzkoušet Coconut ve svém webovém prohlížeči, můžete použít [online interpreter](https://cs121-team-panda.github.io/coconut-interpreter).
 
### Instalace

#### Použití Pip 

Protože je Coconut hostován v [Python Package Index](https://pypi.python.org/pypi/coconut), lze jej snadno instalovat s použitím `pip`. Jednoduše nainstalujte [Python](https://www.python.org/downloads/), otevřte příkazový řádek (cmd) a zadejte
```
pip install coconut
```
což nainstaluje Coconut a jeho požadované závislosti. 

_Note: Máte-li nainstalovanou starou verzi Coconut a chcete ji aktualizovat, zadejte `pip install --upgrade coconut`._

Když při spuštění `pip install coconut` narazíte na chybu, spusťte příkaz znovu s volbou `--user`. Když `pip install coconut` chodí ale nemáte přístup k příkazu `coconut`, ujistěte se, že umístění vaší instalace Coconut je uvedeno v proměnné prostředí `PATH`. V UNIXu to je `/usr/local/bin` (bez `--user`) nebo `${HOME}/.local/bin/` (s `--user`).
 
#### Použití Conda

Preferujete-li pro správu vašich paketů pro Python použití [`conda`](https://conda.ioo/docs/) místo systému `pip` , můžete instalovat Coconut s použitím  nástroje `conda`. Pouze [install `conda`](https://conda.io/miniconda.html), otevřte terminál a zadejte
```
conda config --add channels conda-forge
conda install coconut
```
což řádně vytvoří a sestaví `conda recipe` z [`conda-forge` feedstock] (https://github.com/conda-forge/coconut-feedstock).

_Note: Pro použití `conda` k instalaci alternativního `coconut-develop`,   
 nahraďte slovo `coconut` souslovím `coconut-develop` v posledních třech příkazech nahoře._

### Volitelné závislosti

Coconut má také volitelné dependence, instalovatelné zadáním
```
pip install coconut [název volitelné závislosti]
```
nebo pro instalaci více dependencí,
```
pip install coconut [opt_dep_1, opt_dep_2]
```
Úplný seznam volitelných depencencí:

- `all`: alias pro `jupyter, watch, jobs, mypy` (doporučný způsob  
   instalace úplné verze Coconut) 
- `jupyter/ipython`: umožňuje použití flagu `--jupyter` / `--ipython`
- `watch`: umožňuje flag `--watch`
- `jobs`: umožňuje flag `--jobs`
- `mypy`: umožňuje flag `mypy`
- `cPyparsing`: výrazně urychluje kompilaci (pokud to vaše platforma     
   podporuje) použitím [`cPyparsing`](https://github.com/evhub/ 
   cpyparsing)                
- `tests`: všechno nezbytné pro používání sestovací soupravy Coconutu
- `docs`: všechno nezbytné pro vytváření dokumentace Coconutu
- `dev`: všechno nezbytné pro vyvíjení Coconutu, včetně všech výše
   uvedených dependencí

### Vývojářská verze

Případně, chcete-li si vyzkoušet poslední a nejlepší Coconut, zapište
```
pip install coconut-develop
```
což nainstaluje nejposlednější chodící verzi Coconutu z [`develop` branch](https://github.com/evhub/coconut/tree/develop). Volitelná instalace závislostí je podporována stejným způsobem, jak popsáno výše. Více informací o aktuální vývojové sestavě najdete na [development version of this documentation](http://coconut.readthedocs.io/en/develop/DOCS.html). Buďte varováni: `coconut-develop` může být nestabilní — narazíte-li na chybu, prosím ohlašte ji [vytvořením nového issue](https://github.com/evhub/coconut/issues/new).

## Kompilace

### Použití 

```
coconut [-h] [-v] [-t version] [-i] [-l] [-k] [-p] [-a] [-w] [-r] [-n]
        [-d] [-q] [-s] [-f] [-c code] [-j processes] [--no-tco]
        [--minify] [--jupyter ...] [--mypy ...] [--argv ...] 
        [--tutorial] [--documentation] [--style name] 
        [--recursion-limit limit] [--verbose] [--trace]
        [source] [dest]
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
-t version, --target version
                        specify target Python version (defaults to
                        universal)
-i, --interact			force the interpreter to start (otherwise starts if no
                        other command is given) (implies --run)
-p, --package           compile source as part of a package (defaults to only
                        if source is a directory)
-a, --standalone        compile source as standalone files (defaults to only
                        if source is a single file)
-l, --line-numbers      add line number comments for ease of debugging
-k, --keep-lines        include source code in comments for ease of debugging
-w, --watch             watch a directory and recompile on changes 
-r, --run               run compiled Python (often used with --nowrite)
-n, --no-write          disable writing compiled Python
-d, --display           print compiled Python
-q, --quiet             suppress all informational output (combine with 
                        --display to write runnable code to stdout)
-s, --strict            enforce code cleanliness standards
--no-tco, --notco       disable tail call optimization                       
-c code, --code code    run Coconut passed in as a string (can also be piped
                        into stdin)
-j, --jobs processes    number of additional processes to use (defaults to 
                        0) (pass 'sys' to use machine default)
-f, --force             force overwriting of compiled Python (otherwise only
                        overwrites when source code or compilation
                        parameters change)
--minify                compress compiled Python						
--jupyter, --ipython    run Jupyter/IPython with Coconut as the kernel (
                        remaining args passed to Jupyter)
--mypy ...              run MyPy on compiled Python (remaining args passe to
                        MyPy) (implies --package--no-tco)
--argv ...              set sys.argv to source plus remaining args for use
                        in Coconut script being run						
--tutorial              open the Coconut tutorial in the default web browser

--style name            Pygments syntax highlighting style (or 'none' to
                        disable) (defaults to COCONUT_STYLE environment
                        variable, if it exists, otherwise 'default')
--recursion-limit limit
                        set maximum recursion depth in compiler (defaults to
                        2000)
--verbose               print verbose debug output
--trace                 print verbose parsing data (only available in
                        coconut-develop)
```

### Skripty Coconutu
```
Ke spuštění souboru Coconut jako skriptu poskytuje Coconut příkaz
```
coconut-run <source> <args>
```
jako alias pro
```
coconut --run --quiet --target sys <source> --argv <args>
```
který se potichu zkompiluje a spustí `<source>`, předávajíc skriptu jakýkoliv dodatečný argument, napodobujíc tak práci příkazu pythonu.

`coconut-run` může být použit v řádku s shebangem Unixu pro vytvoření skriptu Coconut přidáním následujícího řádku na začátek skriptu:
```bash
#!/usr/bin/env coconut-run
```


### Názvy zdrojových souborů 

Zdrojové soubory používají extenze `.coco` (upřednostněno), `.coc` nebo `.coconut`. Soubor `.coco` (či `.coc`/`.coconut`) je kompilován do souboru s příponou `.py`. Je-li požadována jiná extenze než `.py`, například `.pyde` pro [Python Processing](http://py.processing.org/), může být vložena před `.coco` a tato složená extenze bude použita místo `.py`. Například, `name.coco` bude kompilovat na `name.py`, zatímco `name.pyde.coco` bude kompilovat na `name.pyde`.

### Kompilační režimy 

Soubory, kompilované konzolou `coconut` se mohou lišit v závislosti na kompilačních parametrech. Je-li kompilována celá složka souborů (ve které bude kompilátor rekurzivně vyhledávat soubory s extenzí `.coco`, `.coc` nebo `.coconut`), vytvoří se soubor `__coconut__.py`, pro ukládání nezbytných funkcí (package mode), zatímco při kompilaci jediného souboru se nezbytné informace ukládají v záhlaví uvnitř souboru (standalone mode). Standalone mode je lepší pro jednotlivé soubory, protože se obejde bez nadbytečného importování `__coconut__.py`, avšak package mode je lepší pro velké pakety, protože se nemusí v každém souboru spouštět kód v záhlaví, jelikož může být jednoduše importován z `__coconut__.py`.

Je-li `zdrojovým` argumentem pro CLI konzolu soubor, provede se implicitně samostatná kompilace, zatímco je-li jím složka, provede se rekurzivní vyhledávání všech souborů `.coco` (nebo `.coc` či `.coconut`), pro něž se provede paketová kompilace. Coconut takto ve většině provede správnou volbu režimů. Je-li však důležité aby se nevytvářely žádné dodatečné soubory jako např. `__coconut__.py`, potom lze přinutit CLI konzolu aby použila určený režim použitím flagů `--package` (`-p`) a `--standalone` (`-a`).

### Kompatibilní verze Pythonu 

Protože je skladba Coconut založena na Python3, měl by kód Coconut, kompilovaný kompilátorem Coconut v univerzálním režimu (implicitní  `--target`) běžet v libovolné verzi Pythonu `>= 2.6` nebo `>= 3.2`.

_Poznámka: Vyzkoušené implementace jsou [CPython](https://www.python.org/) `2.6, 2.7, 3.2, 3.3, 3.4, 3.5, 3.6` a [PyPy](http://pypy.org/) `2.7, 3.2`._

Aby byly nativní objekty (built-ins) Coconut univerzálně přístupné pro různé verze Pythonu, přepisuje **Coconut automaticky built-iny Pythonu 2 na příslušné protějšky Pythonu3**. Navíc, Coconut také přepisuje některé built-iny Pythonu3 z optimalizačních důvodů. Je-li žádán přístup k původním verzím přepsaných built-inů, lze je získat s použitím prefixu `py_`.

Pro kompatibilitu se standardní knihovnou **mapuje Coconut automaticky importy pod názvy Python3 s importy pod názvy Python2**. Takto se Coconut automaticky postará o všechny moduly standardní knihovny, které byly přejmenovány z Python2 na Python3, pokud je použit pouze Python3. Ovšem, pro moduly nebo objekty, které existují pouze v Python3, neumí Coconut kompatibilitu zajistit.

Konečně, zatímco se Coconut pokusí kompilovat skladbu Python3 na jeho univerzální ekvivalent, následující konstrukty nemají žádný ekvivalent v Python2 a vyžadují specifikaci alespoň `3` před svým použitím:
- destructuring assignment with `*`s (use Coconut pattern-matching instead),
- the `nonlocal` keyword,
- `exec` used in a context where it must be a function,
- keyword class definition,
- tuples and lists with `*` unpacking or dicts with `**` unpacking (requires `--target 3.5`),
- `@` as matrix multiplication (requires `--target 3.5`),
- `async` and `await` statements (requires `--target 3.5`), and
- formatting `f` strings  by prefixing them with `f`(requires `--target 3.6`).

### Přípustné cíle 

Je-li verze Pythonu, v níž bude kompilovaný kód běžet, známa předem, měl by být cíl určen flagem `--target`. Daný cíl (target) ovlivní pouze kompilovaný kód a zda je určitá syntaxe Pythonu3 (viz výše) povolena. Tam, kde se standardy skladeb pro Python3 a Python2 liší, bude skladba Coconut vždy používat skladbu Python3 pro všechny cíle. Podporované cíle jsou:

- universal (default) (will work on _any_ of the below),
- `2`, `2.6` (will work on any Python `>= 2.6` but `< 3`),
- `2.7` (will work on any Python `>= 2.7` but `< 3`),
- `3`, `32` (will work on any Python `>= 3.2`),
- `3.3`, `34` (will work on any Python `>= 3.3`),
- `3.5` (will work on any Python `>= 3.5`),
- `3.6` (will work on any Python `>= 3.6`),
- `sys` (chooses the specific target corresponding to the current version).

_Note: Tečky jsou ve specifikacích cíle ignorovány, takže cíl `2.7` je ekvivalentní cíli `27`._

### Režim `strict`  

Je-li povolen flag `--strict` (or `-s`), ohlásí Coconut chyby pro různé problémy stylu. Jsou jimi
- mixing of tabs and spaces (without `--strict` will show a Warning),
- use of `from __future__` imports (without `--strict` will show a Warning)
- missing new line at end of file ),
- trailing whitespace at end of lines,
- semicolons at end of lines,
- use of the Python-style `lambda` statement,
- inheriting from `object` in classes (Coconut does this automatically)
- use of `u` to denote Unicode strings (all Coconut strings aru Unicode
  strings)
- use of backslash continuations (use [parenthetical continuation](#
  pokracovani-v-zavorkach) instead).

Navíc, `--strict` zneplatňuje (disables) zavrhnuté vlastnosti, činíce je zcela nedostupnými při kompilaci s flagem `--strict`. Doporučuje se při práci na novém projektu používat flag `--strict` (nebo `-s`) protože vám bude nápomocen při psaní čistšího kódu.

## Integrace

### Zvýraznění syntaxe

Textové editory, které podporují zvýraznění syntaxe Coconut, jsou tyto:

- **SublimeText**: Viz sekci SublimeText níže.
- **Vim**: Viz [`coconut.vim`](https://github.com/manicmaniac/coconut.vim).
- **Emacs**: Viz [`coconut-mode`](https://github.com/NickSeagull/coconut-mode).
- **Atom**: Viz [`language-coconut`](https://github.com/enilsen16/language-coconut).
- Každý editor, který podporuje Pygments (např. **Spyder**): Viz sekci Pygments níže.

Případně, pokud žádný z výše uvedený editorů vám nevyhovuje, můžete v Coconut pracovat jako v Pythonu. Jednoduše nastavte svůj editor tak, aby interpretoval všechny souboury `.coco` jako soubory Pythonu, čímž by mělo být zvýraznění vašeho kódu vyhovující.

#### SublimeText

Zvýraznění syntaxe Coconutu v editoru SublimeText vyžaduje, aby byl instalován standardní manažer [Package Control](https://packagecontrol.io/installation). Je-li tak učiněno, potom:

1. otevřte příkazovou paletu SublimeTextu stiskem `Ctrl+Shift+P` (nebo `Cmd+Shift+P` v Mac)
2. zadejte `Package Controll: Install Package`
3. zadejte `Coconut`.

Abyste se ujistili, že je všechno OK, otevřte soubor `.coco` a ujistěte se, že se v pravém spodním rohu objeví `Coconut`. Objeví-li se něco jiného, třeba `Plain Text`, klikněte na to, vyberte `Open all with current extension as...` na vrchu výsledného menu a vyberte `Coconut`.

_Note: Zvýraznění syntaxe Coconutu je poskytnuto paketem [sublime-coconut](https://github.com/evhub/sublime-coconut)._

#### Pygments

Tentýž příkaz `pip install coconut`, který instaluje utilitu příkazového řádku Coconutu, instaluje také lexer `coconut` Pygments. Způsob použití závisí na použité `Pygments-enabled` aplikaci ale normálně zadejte `coconut` jako zvýrazňovaný jazyk a/nebo použijte platnou extenzi souboru Coconut (`.coco`, `.coc` nebo `.coconut`) a Pygment by se měl umět zorientovat.

Na příklad, tato dokumentace je generována [Sphinx](http://www.sphinx-doc.org/en/stable/) se zvýrazněním syntaxe vytvořené přidáním řádku
```coconut_python
highlight_language = "coconut"
```
do souboru `conf.py` v distribuci Coconut.

### Podpora pro IPython Jupyter 

Dáváte-li přednost prostředí [IPython](http://ipython.org/) (jádro Pythonu pro framework [Jupyter](http://jupyter.org/) ) před normální konzolou Pythonu, lze použít Coconut jako extenzi IPythonu nebo jádro Jupyteru.

#### Jádro 

Je-li Coconut použit jako jádro (kernel), bude veškerý kód v konzoli nebo notebooku poslán k vyhodnocení do Coconut místo do Pythonu. Jinak se jádro Coconut chová stejně jako jádro iPythonu, včetně podpory pro příkazy `%magic`. 

Příkaz `coconut --jupyter notebook` (nebo `coconut --ipython notebook`) spustí notebook IPython/ Jupyter s použitím Coconut jako jádra a příkaz `coconut --jupyter console` (nebo `coconut --ipython console`) spustí konzoli IPython/ Jupyter s použitím Coconut jako jádra. Navíc, příkaz `coconut --jupyter` (nebo `coconut --ipython`) přidá Coconut jako jazykovou volbu uvnitř všech notebooků IPython/ Jupyter - i těch, které nejsou spouštěny aplikací Coconut. Tento příkaz musí být opakovaně proveden při instalaci nové verze Coconut.

_Note: Coconut také podporuje příkaz `coconut --jupyter lab` pro použití s [JupyterLab](https://github.com/jupyterlab/jupyterlab) místo standardního notebooku Jupyter.

#### Extenze 

Je-li Coconut použit jako extenze, bude speciální "magic command" posílat útržky kódu k vyhodnocení s použitím Coconut místo IPythonu ale IPython bude stále použit jako implicitní aplikace.

Řádkový magic `%load_ext coconut` načte Coconut jako extenzi, připojujíc magics `%coconut` a `%%coconut`. Řádkový magic `%coconut` spustí řádek Coconut s implicitními parametry a blokový magic `%%coconut` přijme CL (command line) argumenty z prvního řádku a vyhodnotí kód Coconut pro dané parametry ve zbytku buňky.


### Integrace s MyPy

Coconut se umí integrovat s [MyPy](http://mypy-lang.org/) za účelem optimální statické kontroly typů, včetně všech vestavěných nástrojů Coconut. Jednoduše zadejte `--mypy` abyste umožnili integraci s MyPy, ale dejte si pozor abyste to zadali jako poslední argument, protože všechny argumenty po `--mypy` jsou poslány do `mypy`, nikoliv do Coconut.

_Note: Protože [optimalizace koncového volání](#tail-call-optimization) vylučuje řádnou typovou kontrolu, `--mypy` ji implicitně vypíná.

Pro explicitní typovou kontrolu kódu v MyPy podporuje Coconut anotace typu funkcí v [Python 3](https://www.python.org/dev/peps/pep-0484/), anotace typu proměnných v [Python 3.6](https://www.python.org/dev/peps/pep-0526/) a dokonce vlastní [vylepšenou skladbu](#enhanced-type-annotations) anotace typů. Implicintě jsou všechny anotace typu kompilovány na signaturu typu, kompatibilní s Python 2, což znamená že všechny anotace chodí ve všech verzích Pythonu.

Coconut dokonce podporuje `--mypy` v interpretu, který inteligentně skenuje každý nový řádek kódu, číhaje na nově zavedené chyby MyPy. Na příklad:

Coconut dokonce podporuje `--mypy` v překladači, jenž skenuje inteligentně každý nový řádek kódu v kontextu s předchozím řádkem zda neobjeví nově zavedené chyby MyPy. Na příklad:
```coconut
>>> a: str = count()[0]
<string>:14: error: Incompatible types in assignment (expression has type "int", variable has type "str")
```

:Note: Někdy si MyPy nebude vědět rady s jistými konstrukty Coconut, např. s `adaptern`. V tom případě jednoduše zadejte `# type: ignore` na řádek Coconut, na jehož kompilaci si MyPy stěžuje (o který řádek se jedná, zjistíte použitím flagu `--line-numbers`).

## Operátory 

Toto jsou operátory Coconut, uvedené v pořadí podle precedencí (nejvyšší nahoře):
```
===================== ==========================
Symbol                 Asociativita
===================== ==========================
..                    n/a wont´t capture call
**                    right
+, -, ~               unary
*, /, //, %, @        left
+, -                  left
<<, >>                left
&                     left
^                     left
|                     left
::                    n/a lazy
a `b` c               left captures lambda
??                    left short-circuit
..>, <.., ..*>, <*..  n/a captures lambda
|>, <|, |*>, <*|      left captures lambda
==, !=, <, >,
    <=, >=,
	in, not in,
	is, is not        n/a
not                   unary
and                   left short-circuit
or                    left short-circuit
a if b else c         ternary left short-circuit
->	                  right
===================== ==========================
```


### Lambdy 

Coconut poskytuje jednoduchý, čistý operátor `->` jako alternativu k příkazu `lambda` v Pythonu. Skladba s operátorem `->` je `(parameters) -> expression` (nebo `parameter -> expression` pro lambdy s jedním argumentem). Operátor má stejné pořadí důležitosti jako starý příkaz, což znamená, že bude často nezbytné uzavřít lambdu do závorek a je asociativní vpravo.

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

**Coconut**
```coconut
dubsums = map((x, y) -> 2*(x+y), range(0, 10), range(10, 20))
dubsums |> list |> print
```

**Python**
```coconut_python
dubsums = map(lambda x, y: 2*(x+y), range(0, 10), range(10, 20))
print(list(dubsums))
```

### Částečná aplikace 

Coconut používá znak `$` hned za názvem funkce, však před závorkou, použitou k volání funkce.

Částečná aplikace Coconutu také podporuje použití `?` a by se přeskočilo částečné použití argumentu, odkládajíc použití tohoto argumentu až na volání částečtě aplikované funkce. To je důležité, chcete-li částečně aplikovat argumenty, které nejsou první v pořadí argumentů.

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

**Coconut**
```coconut
expnums = range(5) |> map$(pow$(?, 2))
expnums |> list |> print
```

**Python**
```coconut_python
# unlike this simple lambda, $ produces a pickleable object
expnums = map(lambda x: pow(x, 2), range(5))
print(list(expnums))
```

### Spojovník (pipeline) 

Coconut používá spojovníky (|) pro usměrnění průběhu aplikace funkcí. Všechny operátory mají precedenci infixových evokací a jsou levostranně asociativní. Všechny operátory také podporují 'in-place versions'. Těmito operátory jsou:
```coconut
(|>)    => pipe forward
(|*>)   => multiple-argument pipe forward
(<|)    => pipe backward
(<*|)   => multiple-argument pipe backward
```
Navíc, všechny spojovníkové operátory podporují lambdu jako poslední argument, přesto že má lambda nižší precedenci. Takže, `a |> x -> b |> c` je ekvivalentní s `a |> (x -> b |> c)`, nikoliv s `a |> (x -> b) |> c`.

_Note: Pro vizuální rozložení operací přes několik řádek použijte [parenthetical continuation](#enhanced-parenthetical-continuation)._

##### Optimalizace

V Coconut je obvyklé psát kód, který používá spojovníky pro zadávaní objektu řadou [partials](#partial-application) a/nebo [implicit partials](#immplicit-partial-application), jako v
```coconut
obj |> .attribute |> .method(args) |> func$(args) |> .[index]
```
což je často mnohem čitelnější, protože to umožňuje aby byly operace psány v pořadí, v němž jsou vykonávány, místo jako v
```coconut_python
func(args, obj.attribute.method(args))[index]
```
kde musí `func` přijít jako první.

Kdyby Coconut kompiloval každou část ve spojovníkové syntaxi jako skutečný objekt částečné aplikace, stala by se skladba ve stylu Coconut do té míry pomalejší než skladba ve stylu Python, že by byla téměř nepoužitelná. Coconut tento problém obchází tím, že `partials` i `implicit partials` jsou kompilovány na skladbu ve stylu Python, nevytvářejíc tak žádné mezilehlé objekty.

##### Příklad

**Coconut**
```coconut
def sq(x) = x**2
(1, 2) |*> (+) |> sq |> print
```

**Python**
```coconut_python
import operator
def sq(x): return x**2
print(sq(operator.add(1, 2)))
```

### Skladba funkcí 

Coconut má tři základní operátory pro skladbu funkcí: `..`, `..>` a `<..`. Jak `..`, tak  `<..` používají "zpětnou" skladbu funkcí, kdy je první funkce volána jako poslední, zatímco `..>` používá "dopřednou"  skladbu funkcí, kde je první funkce volaná jako první.

Spojovníkové operátory `..>` a `<..` mají také formu `..*>` a `<*..`, která je ekvivalentní k operátorům `|*>` a `<*|`. Zpětné a dopředné spojovníkové operátory nemohou být použitý společně v jednom výrazu (na rozdíl od normálních spojovníků) a jeich precedence je mezi spojovníkem `None` a normálním spojovníkem.

Operátor `..` má nižší precedenci než přístup k atributu (`.`), slicing (`[]`), atd, kromě volání funkce, vůči níž má precedenci vyšší. Takže je `a.b..c.d` ekvivalentní k `(a.b)..(c.d)`, zatímco `f..g(x)` je ekvivalentní k `(f.g)(x)`.

'In-place' operátory pro skladbu funkcí jsou `..=`, `..>=`, `<..=`, `..*>=` a `<*..=`.

##### Příklad

**Coconut**
```coconut
fog = f..g
f_into_g = f ..> g
```

**Python**
```coconut_python
# unlike this simple lambda, Coconut produces a pickleable object
fog = lambda *args, **kwargs: f(g(*args, **kwargs))
f_into_g = lambda *args, **kwargs: g(f(*args, **kwargs))
```

### Řetězení 

Coconut používá operátor `::` pro řetězení iterátoru. Toto řetězení je prováděno líně - to jest tak, že argumenty se nevyhodnocují, pokud jich není zapotřebí. Tato forma má precedenci 'in-between bitwise or and infix calls'. 'In-place' operátorem je `::=`.

##### Zdůvodnění

Důležitým nástrojem pro práci s iterátory stejně snadno jako při práci se sekvencemi je schopnost líně kombinovat více iterátorů dohromady. Tato operace se nazývá řetěz (chain) a je ekvivalentní přidávání u sekvencí s tím rozdílem, že se nic nevyhodnocuje, pokud to není zapotřebí.

##### Python Docs

Vytvořte iterátor, který vrací prvky z prvního iteráblu (iterovatelného objektu) dokud je nevyčerpá, potom přejde do dalšího iteráblu až projde všemi iterábly. Používá se pro ošetření následných sekvencí jako jediné sekvence. Zřetězené vstupy jsou vyhodnocovány líně. Zhruba ekvivalentní k:
```coconut_python
def chain(*iterables):
    # chain('ABC', 'DEF') --> A B C D E F
    for it in iterables:
        for element in it:
            yield element
```

##### Příklad

**Coconut**
```coconut
def N(n=0) = (n,) :: N(n+1) # no infinite loop because :: is lazy

(range(-10, 0) :: N())$[5:15] |> list |> print
```

**Python:**

_Nelze provést bez komplikované komprehence iterátoru namísto líného řetězení. Viz kompilovaný kód pro skladbu Pythonu._

### Krájení (slicing) iterátoru 

K provedení iterátorového členění používá Coconut znak `$` mezi iterátorem a označením jeho úseku. Iterátorové členění pracuje stejně jako sekvenční členění v Pythonu a vypadá stejně jako částečná aplikace, avšak s hranatymi místo kulatých závorek. 

Iterátorové členění pracuje stejně jako sekvenční členění, včetně podpory negativních indexů a úseků (slices) a podpory pro objekty `úseků` stejně jako u normálního členění. Iterátorové členění však nezaručuje, že bude zachován původní iterátor (pro jeho zachování použijte [funkci`tee`](#tee) nebo [`reiterable`](#reiterable)).

Iterátorové členění v Coconut je velmi podobné `itertools.islice` v Pythonu, avšak na rozdíl od `itertools.islice`, podporuje iterátorové členění negativní index a přednostně použije  `__getitem__` objektu, pokud existuje. Iterátorové členění je také optimalizované pro práci s objekty `map`, `zip`, `range` a `count`, počítaje pouze ty prvky, které jsou nezbytné pro vynětí žádaného úseku.

##### Příklad

**Coconut**
```coconut
map((x)->x*2, range(10**100))$[-1] |> print
```

**Python**
_Nelze provést bez komplikované funkce pro iterátorové členění a inspekce uživatelských objektů. Nezbytné definice v Pythonu lze nalézt v záhlaví Coconut._

### None Coalescing

Coconut poskytuje označení `??` pro operátor `none-coalescing` (none-sloučení), podobný operátoru null-coalescing `??` v C#. Operátor  `none-coalescing` vyhodnocuje svůj levý operand, nemá-li hodnotu `None`, v opačném případě svůj pravý operand. Tento operátor také vyjadřuje zkratku, spočívající v tom, že když jeho levý operand není `None`, nevyhodnocuje pravý operand. `None-coalescing` má precedenci mezi voláním infixové funkce a spojovníkem a je asociativní vlevo. Operátor `in-place` má označení `??=`.

Coconut také umožňuje použití jediného znaku `?` před přístupem k atributu, při volání funkce, částečné aplikaci a při (iterátorovém) indexování pro (zkratkovité) upuštění od vyhodnocení zbytku, pokud dosavadní vyhodnocení má hodnotu `None`. Tudíž, `a?.b` je ekvivalentní k `a.b if a is not None else a`.

##### Příklad

**Coconut:**
```coconut
could_be_none() ?? calculate_default_value()
could_be_none()?.attr[index].method()
```

**Python**
```coconut_python
(lambda result: result if result is not None else
 calculate_default_value())(could_be_none())
(lambda result: None if result is None else
 result.attr[index].method())(could_be_none())

### Alternativy Unicode

Coconut podporuje alternativy Unicodu pro různé operátové symboly. Alternativy jsou poměrně nápovědné, se záměrem reflektovat vzhled nebo účel originálního symbolu. 

##### Úplný seznam

```
→ (\u2192)                  => "->"
↦ (\u21a6)                  => "|>"
*↦ (*\u21a6)                => "|*>"
↤ (\u21a4)                  => "<|"
↤* (\u21a4*)                => "<*|"
× (\xd7)                    => "*"
↑ (\u2191)                  => "**"
÷ (\xf7)                    => "/"
÷/ (\xf7/)                  => "//"
∘ (\u2218)                  => ".."
∘> (\u2218>)                => "..>"
<∘ (<\u2218)                => "<.."
∘*> (\u2218*>)              => "..*>"
<*∘ (<*\u2218)              => "<*.."
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
⋅ (\u22c5)                  => "@" (only matrix multiplication)
```

## Klíčová slova 

### `data`

Klíčové slovo `data` se používá k vytvoření neměnitelných algebraických datových typů s nativní podporou pro rozkladný (destructuring) [pattern-matching](#match) a [`fmap`](#fmap). 

Syntaxe datového bloku `data` je něco mezi syntaxí pro funkce a syntaxí pro třídy. První řádek vypadá jako definice funkce, zatímco zbytek těla připomíná třídu, obvykle obsahující definice metod. Je to tak proto, že zatímco blok `data` vlastně v Pythonu končí jako třída, Coconut automatický vytváří specielní, neměnitelný konstruktor, založený na daných argumentech.

Deklarace datového typu vypadá takto:
```coconut
data <name>(<args>) [from <inherits>]:
    <body>
```

`<name>` je název nového datového typu, `<args>` jsou argumenty jeho konstruktoru stejně jako názvy jeho atributů, `<body>` obsahuje metody datového typu a <inherits> nepovinně obsahuje libovolnou bázovou třídu.

Coconut připouští aby datová pole v `<args>` měla přiřazené implicitní hodnoty a [anotace typu](#enhanced-type-annotations) a podporuje hvězdičkové parametry na konci, pro posbírání extra argumentů.

Konstruktory pro `datové` typy musí být vytvářeny s použitím metody `__new__` místo `__init__`. Pro snadnější psaní metod `__new__` poskytuje Coconut vestavěnou funkci [makedata](#makedata).

Subtřídy datových typů lze snadno vytvořit jejich děděním v jiné deklaraci `datového` typu nebo v normální `třídě` Pythonu. Použije-li se normální příkaz `class`, vytvoření nové neměnitelné subtřídy vyžaduje přidání řádku
```coconut
__slots__ = ()
```
do těla subtřídy před definicemi metod nebo atributů.

##### Zdůvodnění

Hlavní část funkcionálního programování, které Coconut v Pythonu zlepšuje, je použití hodnot nebo neměnitelných datových typů. Neměnitelná data jsou velmi užitečná ale vytvoření takových typů v Pythonu je velice obtížné. Coconut vytváří neměnitelné datové typy velice snadno použitím bloků typu `data`.

##### Python Docs

Vrací novou subtřídu entice (tuple). Nová subtřída je použita k vytvoření entici podobných objektů, jejichž pole jsou přístupná přes vzhled (lookup) atributu a jsou indexovatelná a iterovatelná. Instance subtřídy mají také nápomocný docstring (se jménem typu a pole) a metodu  `__repr__()`, která uvádí obsah entice ve formátu `name=value`.

Pro název pole lze použít libovolný platný identifikátor Pythonu. Platné identifikátorý se skládají z písmen, číslic a podtržítek ale nezačínají číslicí nebo podtržítkem a nejsou klíčovým slovem jako _class, for, return, global, pass nebo raise_.

Pojmenované instance entic nemají individuální slovníky (dictionaries), takže jsou úsporné a nevyžadujíc více paměti než normální entice.

##### Příklady

**Coconut**
```coconut
data vector2(x:int=0, y:int=0):
    def __abs__(self):
        return (self.x**2 + self.y**2)**.5

v = vector2(3, 4)
v |> print  # all data types come with a built-in __repr__
v |> abs |> print
v.x = 2  # this will fail because data objects are immutable
vector2() |> print
```
_Demonstruje skladbu, vlastnosti a neměnitelnou povahu typů `data`, stejně jako použití implicitních argumentů a anotací typů._
```coconut
data Empty()
data Leaf(n)
data Node(l, r)

def size(Empty()) = 0

@addpattern(size)
def size(Leaf(n)) = 1

@addpattern(size)
def size(Node(l, r)) = size(l) + size(r)

size(Node(Empty(), Leaf(10))) == 1
```
_Demonstruje algebraickou povahu typů `data` při kombinaci s pattern-matching._

```coconut
data vector(*pts):
    """Immutable arbitrary-length vector."""

    def __abs__(self) =
        self.pts |> map$(pow$(?, 2)) |> sum |> pow$(?, 0.5)

    def __add__(self, other) =
        vector(*other_pts) = other
        assert len(other_pts) == len(self.pts)
        map((+), self.pts, other_pts) |*> vector

    def __neg__(self) =
        self.pts |> map$((-)) |*> vector

    def __sub__(self, other) =
        self + -other
```
_Demonstruje `hvězdičkovou` deklaraci typu `data`._		

**Python**
_Nelze provést bez definování řady metod pro každý datový typ. Viz kompilovaný kód pro syntaxi Pythonu._

### `match` 

Coconut poskytuje plnohodotné, funkcionální `pattern-matching` prostřednictvím svých příkazů `match`.

##### Přehled 

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
    | pattern "is" exprs            # type-checking
    | pattern "and" pattern         # match all
    | pattern "or" pattern          # match any
    | "{" pattern_pairs             # dictionaries
        ["," "**" NAME] "}"
    | ["s"] "{" pattern_consts "}"  # sets	
    | "(" patterns ")"              # sekvence mohou mít formu entice
    | "[" patterns "]"              #  nebo formu seznamu
    | "(|" patterns "|)"            # líné seznamy
    | "{" pattern_pairs "}"         # slovníky
    | ["s"] "{" pattern_consts "}"  # sety
    | ("(" | "[")                   # star splits
        patterns,
        "*" middle,
        patterns
      (")" | "]")                   
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
    | ([STRING "+"] NAME            # complex string matching
        ["+" STRING]) 
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
- Líné seznamy (`(|<patterns>|)`): totéž jako při hledání shody (matching) u seznamů nebo entic, ale místo sekvencí kontroluje iterovatelné objekty - `iterábly` (`collections.abc.Iterable`).
- Fixed-Length Dicts (`{<pairs>}`): porovná pouze `mapování` (`collections.abc.Mapping`) stejné délky a obsahy porovná s `<pairs>`.
- Dicts With Rest (`{<pairs>, **<rest>}`): porovná `mapování` (`collections.abc.Mapping`) obsahující všechny `<pairs>` a vloží `dict` všeho ostatního do `<rest>`.
- Sety (`{<constants>}`): spáruje pouze set (`collections.abc.Set`) se stejnou délkou a obsahem.
- Head-Tail Splits (`<list/tuple> + <var>`): porovná počátek sekvence vůči `<list/tuple>`, zbytek připojí k `<var>` a učiní jej typem použitého konstruktu.
- Init-Last Splits (`<var> + <list/tuple>`): přesně totéž jako head-tail splits ale vzhledem ke konci, nikoliv k počátku sekvence.
- Head-Last Splits (`<list/tuple> + <var> + <list/tuple>`): kombinace předchozích dvou operací.
- Iterator Splits (`<list/tuple/lazy list> :: <var>` nebo `<lazy list>`): porovná počátek iteráblu (`collections.abc.Iterable`) s `<list/tuple/lazy list>`, potom připojí zbytek k `<var>` nebo ověří, že je iteráble proveden.
- Complex String Matching (`<string> + <var> + <string>`): porovná stringy, které začínají a končí danými substringy, přiřazujíce prostředek k <`var`>.

_Poznámka: Podobně jako u [krájení iterátoru](#krajeni-iteratoru), porovnávání iterátoru a líného seznamu nezaručují, že původní porovnávaný iterátor zůstane zachovaný (pro zachování iterátoru použijte funkci [`tee`](#tee) nebo [`reitarable`](#reiterable))._

Při ověřování zda může být objekt porovnáván určitým způsobem používá Coconut abstraktní bázové třídy Pythonu. Je tedy nutné registrovat uživatelský objekt jako příslušnou bázovou třídu.

##### Příklady

**Coconut**
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
_Demonstrace porovnávání datových typů. Hodnoty, definované příkazem `data` mohou být konfrontovány a jejich obsahy zpřístupněny s použitím konstruktorů datového typu `point`._
```coconut
data Empty()
data Leaf(n)
data Node(l, r)
Tree = (Empty, Leaf, Node)  # type union

def depth(Tree()) = 0

@addpattern(depth)
def depth(Tree(n)) = 1

@addpattern(depth)
def depth(Tree(l, r)) = 1 + max([depth(l), depth(r)])

Empty() |> depth |> print                                 
Leaf(5) |> depth |> print                                 
Node(Leaf(2), Node(Empty(), Leaf(3))) |> depth |> print   
```
_Ukázka kombinace datových typů a porovnávacích (match) příkazů při opakovaném použití algebraických datových typů v jiných funkcionálních programovacích jazycích._
```coconut
def duplicate_first([x] + xs as l) =
    [x] + l

[1,2,3] |> duplicate_first |> print
```
_Ukázka head-tail krájení (splitting), jednoho z nejvíce používaného způsobu užití pattern-matching, kde `+ <var>` (nebo `:: <var>` pro jakýkoli iterábl) na konci seznamu nebo enticového literálu  může být použit k porovnání se zbytkem sekvence._
```
def sieve([head] :: tail) = 
    [head] :: sieve(n for n in tail if n % head)

@addpattern(sieve)
def sieve((||)) = []
```
_Ukazuje, jak porovnávat vůči iterátorům, totiž že případ prázdného iterátoru (`(||)`) musí přijít jako poslední, jinak tento případ vyčerpá celý iterátor před tím, než přijde ke slovu porovnání s jakoukoli jinou předlohou._

**Python**

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

**Coconut**
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

**Python**

_Nelze provést bez dlouhé řady kontrol pro každý příkaz `match`. Viz kompilovaný kód pro skladbu Pythonu._

### `where`

Příkaz `where` je velmi přímočarý s touto syntaxí:
```
<stmt> where:
    <body>
```
kde `<body>` se skládá pouze z příkazů přiřazení. Příkaz `where` 
pouze provede zadaná přiřazení v `<body>` a potom vyhodnotí výchozí `<stmt>`.

##### Example

**Coconut:**
```coconut
c = a + b where:
    a = 1
    b = 2
```

**Python:**
```coconut_python
a = 1
b = 2
c = a + b
```

### Backslash-Escaping 

Klíčová slova `data`, `match`, `case`, `async` (keyword in Python 3.5) a `await` (keyword in Python 3.5) jsou v Coconut rovněž platná jména proměnných. I když Coconut umí tyto dva případy použití rozlišit, je možné pro zvýraznění použít před takovýmto názvem proměnné zpětné lomítko.

##### Příklad

**Coconut:**
```coconut
\data = 5
print(\data)
```

**Python:**
```coconut_python
data = 5
print(data)
```

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

**Coconut:**
```coconut
L |> map$(def (x) -> y = 1 / x; y*(1 - y))
```

**Python:**
```coconut_python
def _lambda(x):
    y = 1 / x
    return y*(1 - y)
map(_lambda, L)
```

### Líné seznamy 

Coconut podporuje vytváření líných seznamů (lazy lists), jejichž obsah je považován za iterátor a není vyhodnocen, dokud není zapotřebí. Líné seznamy (lazy lists) se v Coconut vytvářejí jednoduše uzavřením čárkami odděleného výčtu do specielních závorek `(|` a `|)` (takzvaných "banana brackets") místo do `[` a `]` u seznamů nebo do `(` a `)` u entic.

Líné seznamy používají ke zlenivění stejný mechanizmus jako u iterátorového řetězení a tudíž je líný seznam `(| x, y |)` ekvivalentní výrazu iterátorového řetězení `(x,) :: (y,)`, byť líný seznam nevytváří mezilehlé entice.

##### Zdůvodnění

Líné seznamy, jejichž sekvence jsou vyhodnocovány jen v případě potřeby, jsou stěžejním útvarem funkcionálního programování, umožňujícím dynamické vyhodnocování jejich obsahu.

##### Příklad

**Coconut:**
```coconut
(| print("hello,"), print("world!") |) |> consume
```

**Python:**
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

##### Příklad

**Coconut:**
```coconut
1 |> "123"[]
mod$ <| 5 <| 3
```

**Python:**
```coconut_python
"123"[1]
mod(5, 3)
```
### Operátorové funkce

Coconut používá jednoduchou zkratku pro vyjádření operátorové funkce: obklopení operátoru kulatými závorkami. Podobně jako u [komprehencí iterátoru](http://howto.py.cz/cap13.htm), je-li operátorová funkce jediným argumentem funkce, mohou závorky pro volání funkce sloužit také jako závorky operátorové funkce.

##### Zdůvodnění

Obvyklou věcí při funkcionálním programování je využití funkčních verzí vestavěných operátorů: jejich 'currying', `composing` a `piping`. Coconut nabízí zjednodušenou syntaxi pro přístup k operátorovým funkcím.

##### Úplný seznam

```coconut
(|>)        => # pipe forward
(|*>)       => # multi-arg pipe forward
(<|)        => # pipe backward
(<*|)       => # multi-arg pipe backward
(..), (<..) => # backward function composition
(..>)       => # forward function composition
(<*..)      => # multi-arg backward function composition
(..*>)      => # multi-arg forward function composition
(.)         => (getattr)
(::)        => (itertools.chain)  # will not evaluate its arguments lazily
($)         => (functools.partial)
($[])       => # iterator slicing operator
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

**Coconut:**
```coconut
(range(0, 5), range(5, 10)) |*> map$(+) |> list |> print
```

**Python:**
```coconut_python
import operator
print(list(map(operator.add, range(0, 5), range(5, 10))))
```


### Vylepšené anotace typu

Protože je syntaxe Coconutu nadmnožinou syntaxe Python3, podporuje sladbu [anotace typu Pythonu 3](https://www.python.org/dev/peps/pep-0484) a skladbu [anotace proměnné typu Pythonu 3.6](https://www.python.org/dev/peps/pep-0526/). Implicitně kompiluje Coconut všechny anotace typu na typové komentáře, kompatibilní s Python 2. Chcete-li zachovat anotace typu, zadejte flag --target, který je podporuje.

Protože ne všechny podporované verze Pyhonu podporují modul [`typing`](https://docs.python.org/3/library/typing.html), poskytuje Coconut vestavěnou proceduru [`TYPE_CHECKING`](#type-checking) pro zakrytí importů `typing` a definicí `TypeVar` před vyhodnocením při runtime. Kromě toho při kompilaci anotace typů do syntaxe Python3, zabalí Coconut tyto anotace do řetězců aby je uchráníl před vyhodnocením při runtime.

Navíc, Coconut přidává speciální syntaxi pro zjednodušení zápisu anotací. Uvnitř anotace typu zachází Coconut s některými konstrukty odlišně, kompilujíc je na anotaci typu místo na to, co by normálně představovaly. Konkrétně, Coconat používá následující transformace:

```coconut
<type>?
    => typing.Optional[<type>]
<type>[]
    => typing.Sequence[<type>]
<type>$[]
    => typing.Iterable[<type>]
() -> <ret>
    => typing.Callable[[], <ret>]
<arg> -> <ret>
    => typing.Callable[[<arg>], <ret>]
(<args>) -> <ret>
    => typing.Callable[[<args>], <ret>]
-> <ret>
    => typing.Callable[..., <ret>]
```
kde [`typing`](https://docs.python.org/3/library/typing.html) je standardní modul Pythonu 3.5.

##### Příklad

**Coconut:**
```coconut
def int_map(
    f: int -> int,
    xs: int[],
) -> int[] =
    xs |> map$(f) |> list
```

**Python:**
```coconut_python
import typing  # unlike this typing import, Coconut produces universal code
def int_map(
    f,  # type: typing.Callable[[int], int]
    xs,  # type: typing.Sequence[int]
):
    # type: (...) -> typing.Sequence[int]
    return list(map(f, xs))
```

### Literály setu 

Coconut umožňuje předsadit písmeno `s` před literály setu. Byť to ve většině případů nedělá nic, v případě prázdného setu to indikuje, že se jedná o `set` a nikoliv o `dictionary`. Spojení `s{}` informuje Coconut, že jde o prázdný set a nikoli o prázdný slovník. Spojení `f{}` generuje `frozenset`.

##### Příklad

**Coconut**
```coconut
empty_frozen_set = f{}
```

**Python**
```coconut_python
empty_frozen_set = frozenset()
```

### Imaginární literály 

Jako doplněk k notaci imaginárních literálů`<num>j` nebo `<num>J` v Pythonu, podporuje Coconut také notace `<num>i` nebo `<num>I` pro zlepšení čitelnosti imaginárních literálů při použití v matematickém kontextu.

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

**Coconut**
```coconut
3 + 4i |> abs |> print
```

**Python**
```coconut_python
print(abs(3 + 4j))
```



## Definice funkce 

### Optimalizace koncového volání 

Coconut provede automatickou optimalizaci a eliminaci koncové rekurze u každé funkce, která vyhoví následujícím kriteriím:

1. musí přímo vrátit (s použitím buď `return` nebo [přiřazovací funkce](#prirazovaci-funkce)) volání sama sebe (eliminace koncového volání - nejúčinnější optimalizace) nebo jiné funkce (optimalizace koncového volání).
2. nesmí to být generátor (používající `yield`) nebo asynchronní funkce (používající`async`).

_Note: Optimalizace koncového voláníí (byť ne eliminace koncové rekurze) pracuje i pro 1) vzájemnou rekurzi a 2) porovnávací (pattern-matching) funkce, rozdělené do několika definicí s pouožitím [`addpattern`](#addpattern)._

Setkáte-li se s `RuntimeError` v souvislosti s maximální hloubkou rekurze, je velmi vhodné přepsat svou funkci aby vyhověla výše uvedenému kriteriu pro optimalizaci koncovým voláním nebo odpovídajícímu kriteriu pro [`recursive_iterator`](#recursive-iterator), obojí by mělo takové chybě zabránit.

_Note: Optimalizace koncového volání (byť ne eliminace koncové rekurze) se vypne, zadáte-li flag `--no-tco`, což je užitečné, máte-li potíže se čtením svých `tracebacks` a potřebujete maximální výkon._


##### Příklad

**Coconut**
```coconut
# na rozdíl od Pythonu, tato funkce nikdy nedospěje k chybě maximální hloubky rekurze
def factorial(n, acc=1):
    case n:
        match 0:
            return acc
        match _ is int if n > 0:
            return factorial(n-1, acc*n)
```

_Demonstruje eliminaci koncové rekurze._
```coconut
# unlike in Python, neither of these functions will ever hit a maximum recursion depth error
def is_even(0) = True
@addpattern(is_even)
def is_even(n is int if n > 0) = is_odd(n-1)

def is_odd(0) = False
@addpattern(is_odd)
def is_odd(n is int if n > 0) = is_even(n-1)
```
_Demonstruje optimalizaci koncové rekurze._

**Python**

_Nelze provést bez přepsání funkce._


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

**Coconut**
```coconut
def binexp(x) = 2**x
5 |> binexp |> print
```

**Python**
```coconut_python
def binexp(x): return 2**x
print(binexp(5))
```

### Funkce pro pattern matching 

Tyto funkce Coconutu jsou normální funkce, kde argumenty jsou vzory k porovnávání, místo proměnných pro přiřazení hodnot.  Skladba definice porovnávací (pattern-matching) funkce je
```coconut
[match] def <name>(<arg>, <arg>, ... [if <cond>]):
    <body>
```
where `<arg>` je definován jako
```coconut
[*|**] <pattern> [= <default>]
```
kde `<name>` je název funkce, `<cond>` je nepovinná dodatečná kontrola, `<body>` je tělo funkce,  `<pattern>` je definován [příkazem `match`](#match) a  `<default>` je volitelná implicitní hodnota, není-li žádný argument zadán. Klíčové slovo `match` na začátku je nepovinné ale je někdy nezbytné pro odlišení definice porovnávací funkce od normální definice funkce, která má vždy přednost. 

Je-li `<pattern>` jméno proměnné (přímo nebo s `<as>`), podporuje výsledná porovnávací funkce klíčové argumenty stejného jména. Jestliže provedení porovnávací funkce selže, vyvolá objekt [`MatchError`](#matcherror), stejně jako [rozložené přiřazení](#rozlozene-prirazeni).

_Note: Definice porovnávací funkce může být kombinována s definicí přiřazovací a/nebo infixové funkce._

##### Příklad

**Coconut**
```coconut
def last_two(_ + [a, b]):
    return a, b
def xydict_to_xytuple({"x":x is int, "y":y is int}):
    return x, y

range(5) |> last_two |> print
{"x":1, "y":2} |> xydict_to_xytuple |> print
```

**Python**

_Nelze provést bez dlouhé řady kontrol na počátku funkce. Viz kompilovaný kód pro skladbu Pythonu._


### Infixové funkce 

Coconut umožňuje infixové volání funkce, kde je výraz, vyhodnocovaný na funkci, obklopen zpětnými apostrofy; argumenty mohou být uvedeny před nebo za funkcí. Infixové volání má prioritu mezi 'chaining and None-coalescing' (řetězením a sloučením) a je asociativní vlevo.

Coconut také podporuje definování jednodušší infixové funkce:
```coconut
def <arg> `<name>` <arg>:
    <body>
```
kde `<name>` je název funkce, `<arg>` jsou parametry funkce a `<body>` je tělo funkce. Obsahuje-li `<arg>` implicitní hodnotu, musí být uvedena v závorkách.

_Note: Definici infixové funkce lze kombinovat s definicí přířazovací a/nebo porovnávací (pattern-matching) funkce._

##### Zdůvodnění

Obvyklým idiomem ve funkcionálním programování je psaní funkcí, zamýšlených jako operátory a volat je i definovat vložením mezi své argumenty. Infixová syntaxe Coconutu to umožňuje.

##### Příklad

**Coconut**
```coconut
def a `mod` b = a % b
(x `mod` 2) `print`
```

**Python**
```coconut_python
def mod(a, b): return a % b
print(mod(x, 2))
```

### Definice funkce s tečkami

Coconut umožňuje definovat funkci s použitím vytečkovaného jména pro přiřazení funkce jako methody objektu, jak je specifikováno v [PEP 542](https://www.python.org/dev/peps/pep-0542/).

##### Příklad

**Coconut:**
```coconut
def MyClass.my_method(self):
    ...
```

**Python:**
```coconut_python
def my_method(self):
    ...
MyClass.my_method = my_method
```


## Příkazy

### Rozkladné přiřazení 

Coconut podporuje výrazně zlepšené rozkladné přiřazení (destructuring assignment), podobné rozkládání entice/seznamu v Pythonu. Skladba rozkladného přiřazení je
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
Selže-li provádění rozkladného přiřazení, potom místo pokračování jako při selhání u bloku `match`, je evokován objekt [`MatchError`](#matcherror), popisující selhání.

##### Příklad

**Coconut**
```coconut
def last_two(l):
    _ + [a, b] = l
    return a, b

[0,1,2,3] |> last_two |> print
```

**Python**

_Nelze provést bez dlouhé řady kontrol místo příkazu rozkladného přiřazení. Viz kompilovaný kód pro skladbu Pythonu._

### Dekorátory 

Narozdíl od Pythonu, který v dekorátoru podporuje pouze jedinou proměnnou nebo volání funkce, podporuje Coconut libovolný výraz.

##### Příklad

**Coconut**
```coconut
@ wrapper1 .. wrapper2 $(arg)
def func(x) = x**2
```

**Python**
```coconut_python
def wrapper(func):
    return wrapper1(wrapper2(arg, func))
@wrapper
def func(x):
    return x**2
```
### Zanořování příkazů

Coconut podporuje vnořování složených příkazů na témže řádku. To umožňuje spojování příkazů `match` a `if`, stejně jako složené příkazy `try`.

##### Příklad

**Coconut:**
```coconut
if invalid(input_list):
    raise Exception()
else: match [head] + tail in input_list:
    print(head, tail)
else:
    print(input_list)
```

**Python:**
```coconut_python
from collections.abc import Sequence
if invalid(input_list):
    raise Exception()
elif isinstance(input_list, Sequence):
    head, tail = inputlist[0], inputlist[1:]
    print(head, tail)
else:
    print(input_list)
```

### Příkazy `except`

Python 3 vyžaduje, že mají-li být odchyceny víceré výjimky, musí být umístěny v uvozovkách aby se znemožnilo použití čárky místo `as` v Python 2. Coconut umožňuje čárky ve výjimkových příkazech za účelem odchycení vícerých výjimek bez použití uvozovek, protože - stejně jako v Python3 - od `as` se vždy požaduje připojit výjimku ke jménu.

##### Example

**Coconut:**
```coconut
try:
    unsafe_func(arg)
except SyntaxError, ValueError as err:
    handle(err)
```

**Python:**
```coconut_python
try:
    unsafe_func(arg)
except (SyntaxError, ValueError) as err:
    handle(err)
```
### Implicitní `pass` 

Coconut umožňuje jednoduchý zápis `class name(base)` a `data name(args)` jako aliasy pro `class name(base): pass` a `data name(args): pass`.

##### Příklad

**Coconut**
```coconut
class Tree
data Empty from Tree
data Leaf(item) from Tree
data Node(left, right) from Tree
```

**Python:**
_Can't be done without a series of method definitions for each data type. See the compiled code for the Python syntax._
```

### In-line `global` a `nonlocal` přiřazení

Coconut umožňuje použití slov `global` nebo `nonlocal` před přiřazením k proměnné nebo k seznamu proměnných, činíce tak přiřazení `globální` případně `nelokální`.

##### Příklad

**Coconut:**
```coconut
global state_a, state_b = 10, 100
```

**Python:**
```coconut_python
global state_a, state_b; state_a, state_b = 10, 100
```
### Průchod kódu 

Kvůli kompatibilitě s jinými variantami Pythonu, jako je [Cython](http://cython.org/) nebo [Mython](http://mython.org/),
podporuje Coconut schopnost protáhnout inertním způsobem libovolný kód kompilátorem. Cokoli umístěného mezi `\(` a `\)` projde netečně kompilátorem, stejně jako řádek, začínající `\\`, umožňující navíc následnou indentaci.

##### Příklad

**Coconut**
```coconut
\\cdef f(x):
    return x |> g
```

**Python**
```coconut_python
cdef f(x):
    return g(x)
```


### Vylepšené závorkové pokračování 

Protože je syntaxe Coconut nadmnožinou syntaxe Python 3, podporuje Cooconut stejnou formu pokračování řádku jako Python. To znamená, že lze použít jak pokračování se zpětným lomítkem nebo implikované pokračování uvnitř kulatých, hranatých či složených závorek.

V Pythonu je ovšem několik případů (např. víceré příkazy `with`), kde lze použít pouze pokračování se zpětným lomítkem. Ve všech těchto případech podporuje Coconut i závorkové pokračování.

Podporu univerzálního použití závorkového pokračování povoluje konvence [PEP 8](https://www.python.org/dev/peps/pep-0008/) :

>Upřednostňovaný způsob ukončování dlouhých řádků je implikované pokračování uvnitř kulatých, hranatých či složených závorek. Dlouhé řádky mohou být uvnitř závorek rozděleny do více kratších řádků. Tento způsob má přednost před používáním zpětných lomítek pro pokračování řádků.

_Note: Použití flagu `--strict` vyloučí použití zpětných lomítek._

##### Příklad

**Coconut:**
```coconut
with (open('/path/to/some/file/you/want/to/read') as file_1,
      open('/path/to/some/file/being/written', 'w') as file_2):
    file_2.write(file_1.read())
```

**Python:**
```coconut_python
# split into two with statements for Python 2.6 compatibility
with open('/path/to/some/file/you/want/to/read') as file_1:
    with open('/path/to/some/file/being/written', 'w') as file_2:
        file_2.write(file_1.read())
```


## Vestavěné funkce

### Vylepšené vestavěné funkce

Objekty `map`, `zip`, `filter`, `reversed` a `enumerate` 
jsou vylepšené verze svých ekvivalentů v Pythonu, které podporují procedury `reversed`, `repr`, optimalizované (a iterátorové) `krájení` (slicing), `len` (vše až na `filter`) a mají přidané atributy, jež mohou subtříty použít pro přístup původním argumentům objektu:

- `map`: `_func`, `_iters`
- `zip`: `_iters`
- `filter`: `_func`, `_iter`
- `reversed`: `_iter`
- `enumerate`: `_iter`, `_start`

##### Příklad

**Coconut:**
```coconut
map((+), range(5), range(6)) |> len |> print
range(10) |> filter$((x) -> x < 5) |> reversed |> tuple |> print
```

**Python:**
_Nelze provést bez definování uživatelskéko typu `map`. Úplnou definici `map` lze nalézt v záhlaví Coconut._
 

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
Mějte na paměti, že funkce, převzatá dekorátorem `addpattern`, musí být 'pattern-matchingová' funkce. Obdrží-li `addpattern` 'non-pattern-matchingovou' funkci, nevyvolá původní funkce hlášení `MatchError`. Tudíž, při volání této funkce nebude `addpattern` vědět, že první shoda selhala a správné cesty nebude nikdy dosaženo.

Například, následující kód vyvolá `TypeError`:
```coconut
def print_type():
    print("Received no arguments.")

@addpattern(print_type)
def print_type(x is int):
    print("Received an int.")

print_type()  # appears to work
print_type(1) # TypeError: print_type() takes 0 positional arguments but 1 was given
```

Toto může být napraveno použitím klíčového slova `match`, činíce tak z funkce `print_type()` funkci pattern-matchingovou. V důsledku toho se všechna hlášení `TypeErrors` přemění na `MatchErrors`. Tato hlášení mohou být potom ošetřena dle potřeby novými `addpattern` dekorovanými funkcemi.

```coconut
match def print_type():
    print("Received no arguments.")

@addpattern(print_type)
def print_type(x is int):
    print("Received an int.")

print_type(1)  # Works as expected
print_type("This is a string.") # Raises MatchError
```

`addpattern` může být použit bez klíčového slova `match`, pokud je příjímaná funkce [přiřazovací funkcí](#assignment-functions), jak ukázáno v následujícím příkladu:


##### Příklad

**Coconut**
```
def factorial(0) = 1

@addpattern(factorial)
def factorial(n) = n * factorial(n - 1)
```

**Python**
_Nelze provést bez komplikované definice dekorátoru a dlouhé řady kontrol pro každé porovnávání. Viz kompilovaný kód pro skladbu Pythonu._

##### `prepattern`

**DEPRECATED:** Coconut also has a `prepattern` built-in, which adds patterns in the opposite order of `addpattern`; `prepattern` is defined as:

```coconut_python
def prepattern(base_func):
    """Decorator to add a new case to a pattern-matching function,
    where the new case is checked first."""
    def pattern_prepender(func):
        return addpattern(func)(base_func)
    return pattern_prepender
```
_Note: Passing `--strict` disables deprecated features._

### `reduce` 

Coconut znovu uvádí funkci `reduce` z Python2, používaje verze `functools.reduce`.

##### Python Docs

**reduce**(_function, iterable_**[**_, initializer_**]**)

Funkce `reduce` použije opakovaně funkci se dvěmi proměnnými pro iterovatelný objekt, kumulujíc mezivýsledky do výsledné výstupní hodnoty. Například, `reduce((x, y) -> x+y, [1, 2, 3, 4, 5])` počítá `((((1+2)+3)+4)+5)`. Levý argument _x_  je akumulovaná hodnota a pravý argument _y_ je aktuální hodnota ze sekvence. Je-li přítomen nepovinný _iniciátor_, je umístěn před položky sekvence a slouží jako implicitní hodnota, je-li sekvence prázdná.

##### Příklad

**Coconut**
```coconut
product = reduce$(*)
range(1, 10) |> product |> print
```

**Python**
```coconut_python
import operator
import functools
product = functools.partial(functools.reduce, operator.mul)
print(product(range(1, 10)))
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

**Coconut**
```coconut
negatives = takewhile(numiter, (x) -> x<0)
```

**Python**
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

**Coconut**
```coconut
positives = dropwhile(numiter, (x) -> x<0)
```

**Python**
```coconut_python
import itertools
positives = itertools.dropwhile(numiter, lambda x: x<0)
```
### `memoize`

Coconut poskytuje `functools.lru_cache` jako 'built-in' pod jménem `memoize`, s tou úpravou, že parametr _maxsize_ je nastaven implicitně na `None`. Procedura `memoize` usnadňuje optimalizaci rekurzivních funkcí, neboť _maxsize_ argumentu `None` je obvykle to, co se žádá.

Použití `memoize` vyžaduje `functools.lru_cache`, jež existuje ve standardní knihovně v Python 3 ale v Python 2 bude požadovat `pip install backports.functools_lru_cache`. Navíc, při přítomnosti `backports.functools_lru_cache` v Python2, bude Coconut 'patch' `functools` tak, že `functools.lru_cache = backports.functools_lru_cache.lru_cache`.

##### Python Docs

**memoize**(_maxsize=None, typed=False_)

Dekorátor pro spojení funkce s memoizačním volatelným objektem (memoizing callable), který ukládá poslední volání v počtu až _maxsize_. Může šetřit čas, je-li opakovaně volána náročná I/O funkce pro stejné argumenty.

Protože se pro ukládání výsledků používá slovník, musejí být poziční a klíčově slovní (KW) argumenty hešovatelné.

Je-li parametr _maxsize_ nastaven na `None`, je LRU vlastnost vypnuta (disabled) a cache může růst bez omezení. LRU feature pracuje nejlépe, je-li _maxsize_ rovno druhé mocnině (power-of-two).

Je-li parametr _typed_ nastaven na `true`, jsou argumenty funkce různých typů ukládány odděleně. Například, `f(3)` a `f(3.0)` jsou šetřeny jako odlišná volání s odlišnými výsledky.

Za účelem měření účinnosti cache a pro vyladění parametru _maxsize_ je obalová funkce vybavena funkcí `cache_info()`, která vrací pojmenovanou entici, ukazující _hits_, _misses_, _maxsize_ a _currsize_. Ve vícevláknovém prostředí jsou hodnoty 'hits' a 'mises' přibližné.

Dekorátor také poskytuje funkci `cache_clear()` pro mazání nebo zneplatnění cache.

Základní funkce je přístupná přes atribut `__wrapped__`. Ten je užitečný pro introspekci, pro obejití cache nebo pro překrytí funkce (rewrapping) jinou cache.

Cache LRU (least recently used) pracuje nejlépe, když poslední volání jsou prediktory nadcházejících volání (například, nejpopulárnější články na serveru se mění každý den). Limit pro velikost této paměti zajišťuje, že cache neroste bez omezení u dlouho běžících procesů, jako jsou webové servery.

Příklad obsahu cache LRU cache pro statický webový obsah:
```coconut_python
@memoize(maxsize=32)
def get_pep(num):
    'Retrieve text of a Python Enhancement Proposal'
    resource = 'http://www.python.org/dev/peps/pep-%04d/' % num
    try:
        with urllib.request.urlopen(resource) as s:
            return s.read()
    except urllib.error.HTTPError:
        return 'Not Found'

>>> for n in 8, 290, 308, 320, 8, 218, 320, 279, 289, 320, 9991:
...     pep = get_pep(n)
...     print(n, len(pep))

>>> get_pep.cache_info()
CacheInfo(hits=3, misses=8, maxsize=32, currsize=8)
```

##### Example

**Coconut:**
```coconut
def fib(n if n < 2) = n

@memoize()
@addpattern(fib)
def fib(n) = fib(n-1) + fib(n-2)
```

**Python:**
```coconut_python
try:
    from functools import lru_cache
except ImportError:
    from backports.functools_lru_cache import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)
```



### `groupsof`

Coconut poskytuje funkci `groupsof` pro rozdělení (splitting) iterovatelného objektu do skupin určiné délky. Konkretně, `groupsof(n, iterable)` rozdělí `iterábl` to entic délky `n`, případně u poslední entice délky `< n`, není-li délka `iteráblu` dělitelná `n`.

##### Příklad

**Coconut:**
```coconut
pairs = range(1, 11) |> groupsof$(2)
```

**Python:**
```coconut_python
pairs = []
group = []
for item in range(1, 11):
    group.append(item)
    if len(group) == 2:
        pairs.append(tuple(group))
        group = []
if group:
    pairs.append(tuple(group))
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
Jakmile `tee()` provede rozdělení, neměl by být původní  _iterábl_ jinde používáný, neboť by se mohl _iterable_ přesunout bez uvědomění objektu tee.

Tento itertool může vyžadovat významý pomocný úložný prostor (v závisloti na tom, jak mnoho dočasných dat má být uloženo). Obecně lze říci, že když jeden iterátor použije většinu ze všech dat před tím, než spustí další iterátor, je rychlejší použít `list()` místo `tee()`.

##### Příklad

**Coconut**
```coconut
original, temp = tee(original)
sliced = temp$[5:]
```

**Python**
```coconut_python
import itertools
original, temp = itertools.tee(original)
sliced = itertools.islice(temp, 5, None)
```

### `reiterable`

Někdy, kdy je zapotřebí aby byl iterátor opakovaně iterován, může být použití `tee` nešikovné. Pro takový případ poskytuje Coconut proceduru `reiterable`, která zabalí daný iterátor tak, že iterace se provádí po objektu `tee` místo po původním iterátoru.

##### Příklad

**Coconut:**
```coconut
def list_type(xs):
    case reiterable(xs):
        match [fst, snd] :: tail:
            return "at least 2"
        match [fst] :: tail:
            return "at least 1"
        match (| |):
            return "empty"
```

**Python:** _Nelze provést bez dlouhé řady kontrol pro každý příkaz `match`. Viz kompilovaný kód pro skladbu Pythonu._

### `consume` 

Coconut poskytuje funkci `consume` pro účinné vyčerpání iterátoru a pro provedení líného výpočtu. Funkce `consume` přijímá volitelný argument, `keep_last`, jehož implicitní hodnota je 0 a určuje kolik položek od konce vrátit jako iterábl (`None` zachová všechny prvky). 

Ekvivalentní k:
```coconut
def consume(iterable, keep_last=0):
    """Fully exhaust iterable and return the last keep_last elements."""
    return collections.deque(iterable, maxlen=keep_last) # fastest way to exhaust an iterator
```

##### Zdůvodnění

V procesu líného provádění operací na iterátorech je posléze dosaženo místa, kde je vyhodnocení iterátoru nezbytné. Aby to mohlo být provedeno efektivně, poskytuje Coconut funkci `consume`, která zcela vyčerpá poskytnutý iterátor.

##### Příklad

**Coconut**
```coconut
range(10) |> map$((x) -> x**2) |> map$(print) |> consume
```

**Python**
```coconut_python
collections.deque(map(print, map(lambda x: x**2, range(10))), maxlen=0)
```

### `count` 

Coconut poskytuje modifikovanou verzi `itertools.count`, která podporuje `in`, normální členění (slicing), optimalizoané členění iterátoru, sekvenční metody `count` a `index`, atributy `repr`, `_start` a `_step` jako vestavěnou funkci jménem `count`.

##### Python Docs

**count**(_start=0, step=1_)

Vytvoří iterátor, který vrátí rovnoměrně rozmístěné  hodnoty, počínajíc číslem _start_. Používá se často jako argument funkci `map()` ke generování postupných datových bodů. Také se používá s funkcí `zip()` pro připojení pořadových čísel. Zhruba ekvivalentní k:
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

**Coconut**
```coconut
count()$[10**100] |> print
```

**Python**
_Nelze provést rychle bez iterátorového členění Coconutu, jež vyžaduje mnoho složitých částí. Nezbytné definice v Pythonu lze nalézt v záhlaví Coconut._

### `makedata`

Funkce `makedata` poskytuje přímý přístup k bázovému konstruktoru datových typů, vytvořenému příkazem `data`. To je zejména užitečné při psaní alternativních konstruktorů pro datové typy přepisem `__new__`.

Funkce `makedata` přijímá datový typ jako první argument, následovaný potřebnými argumenty pro vytvoření datového typu. Pro objekty `data` se funkce `makedata` chová jako konstruktor výchozího datového typu, přesně jak byl datový typ deklarován. Pro `nedatové` objekty je `makedata` ekvivalentní k:
```coconut
def makedata(data_type, *args, **kwargs):
    """Returns base data constructor of data_type."""
    return super(data_type, data_type).__new__(data_type, *args, **kwargs)
```

**DEPRECATED:** Coconut má také vestavěný `datamaker`, který částečně aplikuje `makedata`; `datamaker` je definován jako:
```coconut
def datamaker(data_type):
    """Get the original constructor of the given data type or class."""
    return makedata$(data_type)
```
_Note: Passing `--strict` disables deprecated features._

##### Příklad

**Coconut:**
```coconut
data Tuple(elems):
    def __new__(cls, *elems):
        return elems |> makedata$(cls)
```

**Python:**
_Can't be done without a series of method definitions for each data type. See the compiled code for the Python syntax._


### `fmap`

Ve funkcionálním programování přijímá funkce `fmap(func, obj)` datový typ `obj` a vrací nový datový typ s mapovanou `func` pro celý obsah. Funkce `fmap` v Coconut provádí totéž.

Funkce `fmap` může být rovněž použita pro objekty `str`, `list`, `set` a `dict` jako varianta `map`, vracejíc objekt téhož typu. Chování `fmap` může být pro daný objekt změněno definováním metody `__fmap__(self, func)`, jež bude volána při každé invokaci funkce `fmap`.

Pro `dict` nebo každé `collections.abc.Mapping` je `fmap` voláno pro `.items()` mappingu namísto implicitní iterace po jeho klíčích (`.keys()`).

##### Příklad

**Coconut:**
```coconut
[1, 2, 3] |> fmap$(x -> x+1) == [2, 3, 4]

data Nothing()
data Just(n)

Just(3) |> fmap$(x -> x*2) == Just(6)
Nothing() |> fmap$(x -> x*2) == Nothing()
```

**Python:**
_Can't be done without a series of method definitions for each data type. See the compiled code for the Python syntax._

### `starmap`

Coconut poskytuje modifikovanou verzi `itertools.starmap` která podporuje procedury `reversed`, `repr`, optimized normal (and iterator) slicing, `len` a `_func` a atributy `_iter`.

##### Python Docs

**starmap**(_function, iterable_)

Vytvoří iterátor, který počítá funkci s použitím argumentů, získaných z iteráblu. Používá se místo `map()`, jsou-li argumenty parametrů již seskupeny do entic z jednoho iteráblu (the data has been "pre-zipped"). Rozdíl mezi `map()` a `starmap()` je obdobný rozdílu mezi `function(a,b)` a `function(*c)`. Je zhruba ekvivalentní k:

```coconut_python
def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)
```

##### Příklad

**Coconut:**
```coconut
range(1, 5) |> map$(range) |> starmap$(print) |> consume
```

**Python:**
```coconut_python
import itertools, collections
collections.deque(itertools.starmap(print, map(range, range(1, 5))), maxlen=0)
```

### `scan`

Coconut poskytuje modifikovanou verzi `itertools.accumulate` s opačným pořadím argumentů než má `scan`, který rovněž podporuje `repr`, `len` a `func` a atributy `iter`. `scan` pracuje stejně jako
 [`reduce`](#reduce), kromě toho, že místo vracení poslední akumulované hodnoty, vrací iterátor se všemi mezilehlými hodnotami.

##### Python Docs

**scan**(_func, iterable_)

Vytvoří iterátor, který vrací akumulované výsledky některých funkcí pro dva argumenty. Typy elementů vstupního iteráblu musí být akceptovatelné u argumentů funkce. Například pro sčítání mohou být elementy jakéhokoli sčítatelného typu včetně Decimal nebo Fraction. Je-li vstupní iterábl prázdný, je výstupní iterábl rovněž prázdný.

Jest to zhruba ekvivalentní k:
```coconut_python
def scan(func, iterable):
    'Return running totals'
    # scan(operator.add, [1,2,3,4,5]) --> 1 3 6 10 15
    # scan(operator.mul, [1,2,3,4,5]) --> 1 2 6 24 120
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total
```

##### Příklad

**Coconut:**
```coconut
input_data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
running_max = input_data |> scan$(max) |> list
```

**Python:**
```coconut_python
input_data = [3, 4, 6, 2, 1, 9, 0, 7, 5, 8]
running_max = []
max_so_far = input_data[0]
for x in input_data:
    if x > max_so_far:
        max_so_far = x
    running_max.append(x)
```

### `TYPE_CHECKING`

Proměnná `TYPE_CHECKING` je nastavena na `False` při runtime a na `True` v průběhu ověřování typu (type-checking), umožňujíc zabránit při runtmie vyhodnocení importů `typing` a definicí `TypeVar`. Při zahrnování vašich importů `typing` do bloku `if TYPE_CHECKING:`, můžete dokonce použít modul [`typing`](https://docs.python.org/3/library/typing.html) i v těch verzích Pythonu, které jej nativně nepodporují.

##### Python Docs

Speciální konstanta, u níž aplikace třetích stran pro ověřování typu předpokládají hodnotu `True`. Při runtime má hodotu `False`. Použití:
```coconut_python
if TYPE_CHECKING:
    import expensive_mod

def fun(arg: expensive_mod.SomeType) -> None:
    local_var: expensive_mod.AnotherType = other_fun()
```

##### Příklad

**Coconut:**
```coconut
if TYPE_CHECKING:
    from typing import List
x: List[str] = ["a", "b"]
```

**Python:**
```coconut_python
try:
    from typing import TYPE_CHECKING
except ImportError:
    TYPE_CHECKING = False

if TYPE_CHECKING:
    from typing import List
x: List[str] = ["a", "b"]
```



### `recursive_iterator` 

Coconut poskytuje dekorátor `recursive_iterator`, který poskytuje výraznou optimalizaci pro každou bezstavovou (stateless) rekurzivní funkci, která vrací iterátor. Pro použití `recursive_iterator` u funkce musí být splněna následující kritéria:

1. vaše funkce buď vždy `vrací` iterátor nebo generuje iterátor pomocí `yield`,
2. při opakovaném volání pro tytéž argumenty produkuje vaše funkce tentýž iterátor (vaše funkce je bezestavová),
3. vaše funkce je volána (obvykle volá samu sebe) několikrát pro tytéž argumenty.


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

**Coconut**
```coconut
@recursive_iterator
def fib() = (1, 2) :: map((+), fib(), fib()$[1:])
```

**Python**
_Can't be done without a long decorator definition. The full definition of the decorator in Python can be found in the Coconut header._


### `parallel map` 

Coconut poskytuje paralelní verzi `map` pod názvem `parallel_map`. `parallel_map` využívá více procesů a je proto mnohem rychlejší než `map` pro úlohy, svázané s CPU. 

Použití `parallel_map` vyžaduje `concurrent.futures`, jež existují ve standardní knihovně Python 3, avšak v Python 2 bude zapotřebí provést `pip install futures`.

Protože `parallel_map` používá ke svému provedení více procesů, je nezbytné aby všechny její argumenty byly serializovatelné. Serializovatelné (pickleable) jsou pouze objekty definované na úrovni modulu, uvnitř funkce nebo uvnitř interpreta. Navíc, ve Windows je nezbytné aby se všechna volání `parallel_map` vyskytla uvnitř dozoru `if __name__ == "__main__"`.

##### Python Docs

**parallel_map**(_func, \*iterables_)

Ekvivalentní k `map(func, *iterables)` až nato, že _func_ je provedena asynchronně a několik volání _func_ může být provedeno současně. Vyvolá-li volání výjimku, je tato výjimka zvednuta při vyzvedávání jeho hodnoty z iterátoru.

##### Příklad

**Coconut**
```coconut
parallel_map(pow$(2), range(100)) |> list |> print
```

**Python**
```coconut_python
import functools
import concurrent.futures
with concurrent.futures.ProcessPoolExecutor() as executor:
    print(list(executor.map(functools.partial(pow, 2), range(100))))
```

### `concurrent_map` 

Coconut poskytuje concurentní verzi `map` pod názvem `concurrent_map`. `concurrent_map` využívá více vláken a je proto mnohem rychlejší než `map` u úloh související s IO. Použití `concurrent_map` vyžaduje `concurrent.futures`, jež existuje ve standardní knihovně Python 3, avšak v Python 2 bude zapotřebí provést `pip install futures`.

##### Python Docs

**concurrent_map**(_func, \*iterables_)

Ekvivalentní k `map(func, *iterables)` až nato, že _func_ je provedena asynchronně a několik volání _func_ může být provedeno současně. Vyvolá-li volání výjimku, je tato výjimka zvednuta při vyzvedávání jeho hodnoty z iterátoru.

##### Příklad

**Coconut**
```coconut
concurrent_map(get_data_for_user, get_all_users()) |> list |> print
```

**Python**
```coconut_python
import functools
import concurrent.futures
with concurrent.futures.ThreadPoolExecutor() as executor:
    print(list(executor.map(get_data_for_user, get_all_users())))
```

### `MatchError` 

Objekt `MatchError` je vyvolán, když selže [destructuring assignment](#rozlozene-prirazeni), načež je `MatchError` poskytnut jako vestavěná procedura pro odchycení takovýchto chyb. Objekty `MatchError` podporují dva atributy, `pattern`, což je řetězec, popisující selhávající předlohu a `value`, což je objekt, který selhal při porovnávání s předlohou.


## Moduly Coconut

### Automatická kompilace

Pokud nemáte speciení požadavky ohledně parametrů kompilace, můžete použít automatickou kompilaci, která se vám postará o všechno potřebné. Pokud před čímkoli ostatním importujete [`coconut.convenience`](#coconut-convenience), Coconut prověří každý váš import a zjistí-li, že importujete soubor ` ~.coco`, automaticky jej kompiluje. Pamatujte, že aby Coconut věděl, jaký soubor importujete, musí být dostupný via `sys.path`, stejně jako normální import.

Automatická kompilace vždycky kompiluje moduly a pakety v místě a vždy používá `--target sys`. Automatická kompilace je vždy dostupná v interpretu Coconut, stejně jako vestavěná funkce `reload` pro snadné znovunačtení importovaných modulů.

### `coconut.convenience`

Kromě automatické kompilace lze také použít volání kompilátoru z kódu místo z příkazového řádku. Specifikace různých 'convenience functions' je uvedena níže.

#### `parse`

**coconut.convenience.parse**(**[**_code,_ **[**_mode_**]]**)

Patrně nejužitečnější z 'convenience functions' je funkce `parse`, která jako vstup přijímá kód Coconut a vrací ekvivalentní kompilovaný kód v Pythonu. Druhý argument _mode_ se používá k označení kontextu pro parsování.

Pokud není _code_ zadán, vrací `parse` pouze záhlaví argumentu  _mode_, jež může být vyhodnoceno pro nastavení prostředí, v němž může být budoucí kód parsován a vyhodnocen bez záhlaví.

Každý argument _mode_ má dvě komponenty: jaký používá parser a jaké jaké záhlaví připojuje. Parser určuje přípustný kód a záhlaví (header) určuje jak má být kompilovaný kód použit. Možné hodnoty _mode_ jsou:

- `"sys"`: (the default)
    + parser: file
        * The file parser can parse any Coconut code.
    + header: sys
        * This header imports [`coconut.__coconut__`](#coconut-coconut) to access the necessary Coconut objects.
- `"exec"`:
    + parser: file
    + header: exec
        * When passed to `exec` at the global level, this header will create all the necessary Coconut objects itself instead of importing them.
- `"file"`:
    + parser: file
    + header: file
        * This header is meant to be written to a `--standalone` file and should not be passed to `exec`.
- `"package"`:
    + parser: file
    + header: package
        * This header is meant to be written to a `--package` file and should not be passed to `exec`.
- `"block"`:
    + parser: file
    + header: none
        * No header is included, thus this can only be passed to `exec` if code with a header has already been executed at the global level.
- `"single"`:
    + parser: single
        * Can only parse one line of Coconut code.
    + header: none
- `"eval"`:
    + parser: eval
        * Can only parse a Coconut expression, not a statement.
    + header: none
- `"debug"`:
    + parser: debug
        * Can parse any Coconut code, allows leading whitespace, and has no trailing newline.
    + header: none

##### Příklad

```coconut_python
from coconut.convenience import parse
exec(parse())
while True:
    exec(parse(input(), mode="block"))
```

#### `setup`

**coconut.convenience.setup**(_target, strict, minify, line\_numbers, keep\_lines, no\_tco_)

`setup` lze použít pro zadání flagů příkazového řádku, použitých funkcí `parse`. Možné hodnoty flagů jsou:

- _target_: `None` (default), or any [allowable target](#allowable-targets)
- _strict_: `False` (default) or `True`
- _minify_: `False` (default) or `True`
- _line\_numbers_: `False` (default) or `True`
- _keep\_lines_: `False` (default) or `True`
- _no\_tco_: `False` (default) or `True`

#### `cmd`

**coconut.convenience.cmd**(_args_, **[**_interact_**]**)

Vyhodnotí dané _args_ jakoby byly zadané interpretu `coconut` z příkazového řádku. Pokud však _interact_ má hodnotu True nebo je zadáno `-i`, interpret se nespustí. Navíc, protože `parse` a `cmd` sdílejí tentýž 'convenience parsing' objekt, všechny změny provedené při parsování přes `cmd` budou působit jako by byly zavedené přes `setup`.

#### `version`

**coconut.convenience.version**(**[**_which_**]**)

Přináší řetězec, obsahující informaci o verzi Coconutu. Volitelný argument _which_ je typ verze požadované informace. Možné hodnoty argumentu _which_ jsou:

- `"num"`: the numerical version (the default)
- `"name"`: the version codename
- `"spec"`: the numerical version with the codename attached
- `"tag"`: the version tag used in GitHub and documentation URLs
- `"-v"`: the full string printed by `coconut -v`

#### `auto_compilation`

**coconut.convenience.auto_compilation**(**[**_on_**]**)

Zapíná či vypíná [automatickou  compilaci](#automatic-compilation) (implicitně je zapnuta). Tato funkce je volána automaticky při importu `coconut.convenience`.

#### `CoconutException`

Vyskytne-li se při vyhodnocení 'convenience function' chyba, vyvolá se instance `CoconutException`. Pomocná funkce `coconut.convenience.CoconutException` slouží k odchycení těchto chyb.
 

### `coconut.__coconut__` 

Toto je občas užitečné pro přístup k vestavěným objektům Coconutu z čistého Pythonu. Za tím účelem Coconut poskytuje `coconut.__coconut__`, jenž se chová přesně jako hlavičkový soubor `__coconut__.py`, připojený když je Coconut kompilován v režimu 'package'.

Všechny nativní objekty Coconutu jsou přístupné z `coconut.__coconut__`. Doporučený způsob jejich importu je použití `from coconut.__coconut__ import`.

##### Příklad

**Python**
```coconut_python
from coconut.__coconut__ import parallel_map
```



