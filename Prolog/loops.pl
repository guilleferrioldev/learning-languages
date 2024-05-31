count_to_10(10) :- write(10), nl.

count_to_10(X) :- 
    write(X), nl, 
    Y is X + 1, 
    count_to_10(Y).

count_down(Low, High) :- 
    between(Low, High, Y),
    Z is High - Y,
    write(Z), nl.

count_up(Low, High) :- 
    between(Low, High, Y),
    Z is  Low + Y,
    write(Z), nl.

% Another loop
guess_number :- loop(start).
loop(15) :- write('You guessed it').

loop(X) :-
    X \=15,
    write('Guess Number '),
    read(Guess),
    write(Guess),
    write(' is not the number'), nl,
    loop(Guess).