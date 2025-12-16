sql_queries = {
    "SELECT_basico": {
        "seleccionar_todo_customers": "SELECT * FROM Customers;",
        "seleccionar_columnas": "SELECT CustomerName, City FROM Customers;",
        "seleccionar_paises_distintos": "SELECT DISTINCT Country FROM Customers;",
        "seleccionar_paises": "SELECT Country FROM Customers;",
        "contar_paises_distintos": "SELECT COUNT(DISTINCT Country) FROM Customers;"
    },

    "WHERE_customers": {
        "customers_mexico": "SELECT * FROM Customers WHERE Country='Mexico';",
        "customer_id_1": "SELECT * FROM Customers WHERE CustomerID=1;",
        "customer_id_mayor_80": "SELECT * FROM Customers WHERE CustomerID > 80;",
        "city_empieza_con_s": "SELECT * FROM Customers WHERE City LIKE 's%';",
        "city_paris_london": "SELECT * FROM Customers WHERE City IN ('Paris','London');"
    },

    "WHERE_products_precios": {
        "precio_igual_18": "SELECT * FROM Products WHERE Price = 18;",
        "precio_mayor_30": "SELECT * FROM Products WHERE Price > 30;",
        "precio_menor_30": "SELECT * FROM Products WHERE Price < 30;",
        "precio_mayor_igual_30": "SELECT * FROM Products WHERE Price >= 30;",
        "precio_menor_igual_30": "SELECT * FROM Products WHERE Price <= 30;",
        "precio_distinto_18": "SELECT * FROM Products WHERE Price <> 18;",
        "precio_entre_50_60": "SELECT * FROM Products WHERE Price BETWEEN 50 AND 60;"
    },

    "ORDER_BY_products": {
        "ordenar_precio_asc": "SELECT * FROM Products ORDER BY Price;",
        "ordenar_precio_desc": "SELECT * FROM Products ORDER BY Price DESC;",
        "ordenar_nombre_asc": "SELECT * FROM Products ORDER BY ProductName;",
        "ordenar_nombre_desc": "SELECT * FROM Products ORDER BY ProductName DESC;"
    },

    "ORDER_BY_customers": {
        "ordenar_pais_nombre": "SELECT * FROM Customers ORDER BY Country, CustomerName;",
        "ordenar_pais_asc_nombre_desc": "SELECT * FROM Customers ORDER BY Country ASC, CustomerName DESC;"
    }
}
