likes(mary,food).
likes(mary,wine).
likes(mary,john).
likes(joseph,joseph).
likes(john, Something) :- likes(mary, Something).
likes(john, Someone) :- likes(Someone, wine).
likes(john, Someone) :- likes(Someone, Someone).