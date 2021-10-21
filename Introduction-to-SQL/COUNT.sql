-- 1 - Quantos produtos cadastrados nas tabelas de produtos.
-- 1 - How many products are registered in the product tables.

SELECT COUNT(*)
FROM Production.Product

-- 2 - Quantos tamanhos de produtos cadastrados nas tabelas.
-- 2 - How many sizes of products registered in the tables.

SELECT COUNT(size)
FROM Production.Product