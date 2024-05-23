parent(albert, bob).
parent(albert, betsy).
parent(albert, bill).

parent(alice, bob).
parent(alice, betsy).
parent(alice, bill).

parent(bob, carl).
parent(bob, charlie).

grandchild(X) :- 
    parent(X, Z),
    parent(Z, Y),
    format('~s`s grandchild is ~s~n', [X, Y]).

grandparent(X) :- 
    parent(Z, X), 
    parent(Y, Z), 
    format('~s`s grandparent is ~s~n', [X, Y]).

blushes(X) :- human(X).
human(derek).

stabs(tybalt, mercurio, sword).
hates(romeo, X) :- stabs(X, mercurio, sword).



