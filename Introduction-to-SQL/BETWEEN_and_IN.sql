-- Example 1 BETWEEN
-- Exemplo 1 BETWEEN

SELECT *
FROM Production.product
WHERE Listprice BETWEEN 1000 AND 1500

-- Example 2 BETWEEN
-- Exemplo 2 BETWEEN

SELECT *
FROM HumanResources.employees
WHERE HireDate BETWEEN '2009/01/01' AND '2010/01/01'
ORDER BY HireDate

-- Exemplo 1 IN
-- Example 1 IN

SELECT *
FROM Person.Person
WHERE BusinessEntityID IN (2,7,13)