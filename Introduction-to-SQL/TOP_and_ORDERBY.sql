-- TOP (Número de linhas).
-- TOP (number of lines).

SELECT TOP 10 *
FROM Production.Product

-- ORDER BY
SELECT FirstName, LastName
FROM Person.Person
ORDER BY FirstName ASC, LastName DESC

-- Desafio!, Challenge!
-- Obter o productId dos 10 produtos mais caros cadastrados no sistema, listado do mais caro para o mais barato.
-- Get the productId of the 10 most expensive products registered in the system, listed from the most expensive to the cheapest.

SELECT ProductID, ListPrice
FROM Production.Product
ORDER BY ListPrice DESC

SELECT TOP 10 ProductID
FROM Production.Product
ORDER BY ListPrice DESC