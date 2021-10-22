-- Example 1 LIKE -- Vamos dizer que você quer encontrar uma pessoa no banco de dados que você sabe que o nome dela era ovi... alguma coisa.
-- Exemplo 1 LIKE -- Let's say you want to find a person in the database that you know their name was ovi... something.

SELECT *
FROM person.person
WHERE FirstName LIKE 'ovi%'

-- Example 2
-- Exemplo 2

SELECT *
FROM person.person
WHERE FirstName LIKE '%to'

-- Example 3
-- Exemplo 3

SELECT *
FROM person.person
WHERE FirstName LIKE '%essa%'

