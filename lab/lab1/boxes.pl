initial_state([0,0]).

goal_state([2,0]).

operator([B1, B2], [4,B2], 4-B1) :-
    B1 < 4.

