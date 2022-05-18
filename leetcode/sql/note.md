# note

Union is a bit faster than OR
Suppose we are searching population and area,
Given that MySQL usually uses one one index per table in a given query,
so when it uses the 1st index rather than 2nd index,
it would still have to do a table-scan to find rows that fit the 2nd index.

select if nothing found Null will be returned
