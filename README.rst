Coconut
=======

.. toctree::
   :maxdepth: 3

   FAQ
   HELP
   DOCS

`Coconut <http://coconut-lang.org/>`_ je varianta jazyka `Python <https://www.python.org/>`_ vytvořená pro jednoduché a elegantní Pythonické **funkcionální programování**.

Coconut je vyvíjen na `GitHub <https://github.com/evhub/coconut>`_ a hostován na `PyPI <https://pypi.python.org/pypi/coconut>`_.


Instalace
---------

Instalace Coconut je stejně snadná jako otevření konzoly s promptem a zadání::

    pip install coconut

načež máte celý svět Coconut u svých nohou.

Ukázky kódu
-----------

**Usměrnění programu** (pipeline-style programming):

.. code-block:: coconut

    "hello, world!" |> print

**Pohlednější lambda**:

.. code-block:: coconut

    (x) -> x ** 2

**Částečná aplikace** (partial application):

.. code-block:: coconut

    range(10) |> map$((x) -> x ** 2) |> list


**Porovnání předlohy** (pattern-matching):

.. code-block:: coconut

    match [head] + tail in [0, 1, 2, 3]:
        print(head, tail)


**Rozložené přiřazení** (destructuring assignment):

.. code-block:: coconut

    {"list": [0] + rest} = {"list": [0, 1, 2, 3]}


**Infixová notace**:

.. code-block:: coconut

    5 `mod` 3 == 2


**Operátorové funkce**:

.. code-block:: coconut

    range(15) |> map$((*)$(2)) |> list


**Kompozice funkcí**:

.. code-block:: coconut

    (f .. g .. h)(x, y, z)


**Líné seznamy**:

.. code-block:: coconut

    (| first_elem() |) :: rest_elems()


**Paralelní programování**:

.. code-block:: coconut

    range(100) |> parallel_map$((**)$(2)) |> list


**Optimalizace koncové rekurze**:

.. code-block:: coconut

    def factorial(n, acc=1):
        case n:
            match 0:
                return acc
            match _ is int if n > 0:
                return factorial(n-1, acc*n)
        else:
            raise TypeError("the argument to factorial must be an integer >= 0")

**Algebraické datové typy**:

.. code-block:: coconut

    data Empty()
    data Leaf(n)
    data Node(l, r)

    def size(Empty()) = 0

    @addpattern(size)
    def size(Leaf(n)) = 1

    @addpattern(size)
    def size(Node(l, r)) = size(l) + size(r)

    size(Node(Empty(), Leaf(10))) == 1


Užitečné odkazy
---------------

Podporu pro své první kroky v prostředí Coconut naleznete na těchto odkazech:

* `Tutoriál <http://coconut.readthedocs.io/cs/master/HELP.html>`_: Dobrým výchozím bodem pro začátečníka v Coconut je jeho tutorial s případovými studiemi.
* `Documentace <http://coconut.readthedocs.io/cs/master/DOCS.html>`_: Hledáte-li informaci o konkretní entitě, zkuste referenční dokumentaci jazyka Coconut.
* `FAQ <http://coconut.readthedocs.io/cs/master/FAQ.html>`_: Chcete-li se zeptat, pro koho je Coconut určen a zda byste jej měl používat, navštivte Frequently Asked Questions .
* `Create a New Issue <https://github.com/evhub/coconut/issues/new>`_: If you're having a problem with Coconut, creating a new issue detailing the problem will allow it to be addressed as soon as possible.
* `Gitter <https://gitter.im/evhub/coconut>`_: For any questions, concerns, or comments about anything Coconut-related, ask around at Coconut's Gitter, a GitHub-integrated chat room for Coconut developers.

Poznámka: Pokud výše uvedené linky nechodí, zkuste `mirror <http://pythonhosted.org/coconut/>`_.

