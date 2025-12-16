sql_queries = {

    # ======================================================
    # BASIC SELECT
    # ======================================================
    "SELECT_BASICS": {

        "SELECT * FROM Customers;":
            "Returns all columns and all rows from the Customers table.",

        "SELECT CustomerName, City FROM Customers;":
            "Returns only the CustomerName and City columns from the Customers table.",

        "SELECT DISTINCT Country FROM Customers;":
            "Returns a list of unique countries from the Customers table.",

        "SELECT Country FROM Customers;":
            "Returns the country column for all customers, including duplicates.",

        "SELECT COUNT(DISTINCT Country) FROM Customers;":
            "Counts how many unique countries exist in the Customers table."
    },

    # ======================================================
    # WHERE – CUSTOMERS (BASIC CONDITIONS)
    # ======================================================
    "WHERE_CUSTOMERS": {

        "SELECT * FROM Customers WHERE Country = 'Mexico';":
            "Returns all customers whose country is Mexico.",

        "SELECT * FROM Customers WHERE CustomerID = 1;":
            "Returns the customer with CustomerID equal to 1.",

        "SELECT * FROM Customers WHERE CustomerID > 80;":
            "Returns customers whose CustomerID is greater than 80.",

        "SELECT * FROM Customers WHERE City LIKE 's%';":
            "Returns customers whose city starts with the letter 's'.",

        "SELECT * FROM Customers WHERE City IN ('Paris','London');":
            "Returns customers located in Paris or London."
    },

    # ======================================================
    # WHERE – PRODUCTS (PRICE CONDITIONS)
    # ======================================================
    "WHERE_PRODUCTS_PRICE": {

        "SELECT * FROM Products WHERE Price = 18;":
            "Returns products priced exactly at 18.",

        "SELECT * FROM Products WHERE Price > 30;":
            "Returns products with a price greater than 30.",

        "SELECT * FROM Products WHERE Price < 30;":
            "Returns products with a price lower than 30.",

        "SELECT * FROM Products WHERE Price >= 30;":
            "Returns products with a price greater than or equal to 30.",

        "SELECT * FROM Products WHERE Price <= 30;":
            "Returns products with a price less than or equal to 30.",

        "SELECT * FROM Products WHERE Price <> 18;":
            "Returns products whose price is not equal to 18.",

        "SELECT * FROM Products WHERE Price BETWEEN 50 AND 60;":
            "Returns products with prices between 50 and 60."
    },

    # ======================================================
    # ORDER BY
    # ======================================================
    "ORDER_BY": {

        "SELECT * FROM Products ORDER BY Price;":
            "Orders products by price in ascending order.",

        "SELECT * FROM Products ORDER BY Price DESC;":
            "Orders products by price in descending order.",

        "SELECT * FROM Products ORDER BY ProductName;":
            "Orders products alphabetically by product name.",

        "SELECT * FROM Products ORDER BY ProductName DESC;":
            "Orders products alphabetically by product name in descending order.",

        "SELECT * FROM Customers ORDER BY Country, CustomerName;":
            "Orders customers by country first, then by customer name.",

        "SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;":
            "Orders customers by country ascending and customer name descending."
    },

    # ======================================================
    # LOGICAL OPERATORS (AND / OR / NOT)
    # ======================================================
    "LOGICAL_OPERATORS": {

        "SELECT * FROM Customers WHERE Country = 'Spain' AND CustomerName LIKE 'G%';":
            "Returns customers from Spain whose names start with the letter G.",

        "SELECT * FROM Customers WHERE Country = 'Brazil' AND City = 'Rio de Janeiro' AND CustomerID > 50;":
            "Returns customers from Brazil, in Rio de Janeiro, with an ID greater than 50.",

        "SELECT * FROM Customers WHERE Country = 'Spain' AND (CustomerName LIKE 'G%' OR CustomerName LIKE 'R%');":
            "Returns Spanish customers whose names start with G or R.",

        "SELECT * FROM Customers WHERE Country = 'Spain' AND CustomerName LIKE 'G%' OR CustomerName LIKE 'R%';":
            "Returns customers from Spain whose name starts with G, or any customer whose name starts with R due to operator precedence.",

        "SELECT * FROM Customers WHERE Country = 'Germany' OR Country = 'Spain';":
            "Returns customers from Germany or Spain.",

        "SELECT * FROM Customers WHERE City = 'Berlin' OR CustomerName LIKE 'G%' OR Country = 'Norway';":
            "Returns customers who live in Berlin, whose name starts with G, or who are from Norway.",

        "SELECT * FROM Customers WHERE NOT Country = 'Spain';":
            "Returns customers who are not from Spain.",

        "SELECT * FROM Customers WHERE CustomerName NOT LIKE 'A%';":
            "Returns customers whose names do not start with the letter A.",

        "SELECT * FROM Customers WHERE CustomerID NOT BETWEEN 10 AND 60;":
            "Returns customers whose ID is outside the range 10 to 60.",

        "SELECT * FROM Customers WHERE City NOT IN ('Paris', 'London');":
            "Returns customers who are not located in Paris or London.",

        "SELECT * FROM Customers WHERE NOT CustomerID > 50;":
            "Returns customers whose ID is less than or equal to 50.",

        "SELECT * FROM Customers WHERE NOT CustomerID < 50;":
            "Returns customers whose ID is greater than or equal to 50."
    },

    # ======================================================
    # DATA MODIFICATION (INSERT / UPDATE / DELETE / DROP)
    # ======================================================
    "DATA_MODIFICATION": {

        "INSERT INTO Customers (CustomerName, City, Country) VALUES ('Cardinal', 'Stavanger', 'Norway');":
            "Inserts a new customer with name, city, and country.",

        "UPDATE Customers SET ContactName = 'Alfred Schmidt', City = 'Frankfurt' WHERE CustomerID = 1;":
            "Updates the contact name and city for the customer with ID 1.",

        "DELETE FROM Customers WHERE CustomerName = 'Alfreds Futterkiste';":
            "Deletes the customer named Alfreds Futterkiste.",

        "DELETE FROM Customers;":
            "Deletes all records from the Customers table.",

        "DROP TABLE Customers;":
            "Deletes the Customers table completely, including its structure."
    },

    # ======================================================
    # AGGREGATE FUNCTIONS
    # ======================================================
    "AGGREGATES": {

        "SELECT MIN(Price) FROM Products;":
            "Returns the lowest price among all products.",

        "SELECT MAX(Price) FROM Products;":
            "Returns the highest price among all products.",

        "SELECT COUNT(*) FROM Products;":
            "Returns the total number of rows in the Products table.",

        "SELECT AVG(Price) FROM Products;":
            "Returns the average price of all products.",

        "SELECT * FROM Products WHERE Price > (SELECT AVG(Price) FROM Products);":
            "Returns products that are priced above the average price."
    }
}
