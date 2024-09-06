% Facts
% By Gender
female(pallavi).
female(anasuya).
female(mugdha).
female(madhavi).
female(rujuta).
male(X) :- \+ female(X).
% By Hierarchy
parent(mahesh, devadatta).
parent(mahesh, mugdha).
parent(vinayak, mahesh).
parent(vinayak, madhavi).
parent(anil, pallavi).
parent(anil, avinash).
parent(avinash, chinmay).
parent(pallavi, devadatta).
parent(pallavi, mugdha).
parent(rujuta, chinmay).
parent(anasuya, avinash).
parent(anasuya, pallavi).
% Rules
mother(X,Y) :- parent(X, Y), female(X).
father(X, Y) :- parent(X, Y), male(X).
wife(X,Y) :- parent(X, Z), parent(Y, Z), female(X), male(Y).
husband(X, Y) :- wife(Y, X).
sibling(X, Y) :- parent(P, X), parent(P, Y).
aunt(X, Y) :- female(X), parent(P, Y), sibling(X, P).
uncle(X, Y) :- male(X), parent(P, Y), sibling(X, P).
grandparent(X, Y) :- parent(P, Y), parent(X, P).
cousin(X, Y) :- parent(P, Y), sibling(S, P), parent(S, X).