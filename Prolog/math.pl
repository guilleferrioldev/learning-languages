% Sum
sum(X, Y, Result) :-
    Result is X + Y.

% Subtraction
subtract(X, Y, Result) :-
    Result is X - Y.

% Multiplication
multiply(X, Y, Result) :-
    Result is X * Y.

% Division
divide(X, Y, Result) :-
    Y = 0,
    Result is X / Y.

% Power
:- discontiguous power/3.

power(Base, Exponent, Result) :-
    base_zero(Base, Exponent, Result).

base_zero(0, Exponent, Result) :-
    Exponent < 0,
    Result is 0.

base_zero(Base, Exponent, Result) :-
    Exponent > 0,
    Result is 1 / power(Base, -Exponent).

power(Base, Exponent, Result) :-
    Exponent mod 2 =:= 0,
    Root is power(Base, Exponent / 2),
    Result is Root * Root.

power(Base, Exponent, Result) :-
    Exponent mod 2 =:= 1,
    Root is power(Base, (Exponent - 1) / 2),
    Result is Base * Root * Root.

/* 
random(Start, End, Result).
between(Start, End, Result).
succ(Number, Result).
abs(Number, Result).
max(Number, Result).
min(Number, Result).
round(Number, Result).
Result is truncate(Number).
*/
