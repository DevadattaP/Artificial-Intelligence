american(west).
missile(m).
owns(nono, m).
enemy(nono,america).
weapon(X) :- missile(X).
sells(west,X,nono) :- missile(X), owns(nono,X).
hostile(X) :- enemy(X, america).
criminal(X) :- american(X), weapon(Y), sells(X, Y, Z), hostile(Z).
