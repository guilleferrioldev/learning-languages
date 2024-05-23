what_grade(5) :- 
    write('Go to kindergarden').

what_grade(6) :- 
    write('Go to 1st Grade').

what_grade(Other) :- 
    Grade is Other - 5,
    format('Go to grade ~w', [Grade]).

customer(tom, smith, 20.55).
customer(sally, smith, 120.55).

get_cust_bal(FName, LName) :- 
    customer(FName, LName, Bal),
    write(FName), tab(1),
    format('~w owes us $~2f ~n', [LName, Bal]).

vertical(line(point(X, Y), point(X, Y2))).