/*I have created a new database called Wollastons*/
CREATE DATABASE WollastonsStore;

/*I am trying to search if my database is created is in schema*/
SHOW databases;	

/*I am accessing my database*/
USE WollastonsStore;

/*Creating a table in my database "WollastonsStore"*/
CREATE TABLE Wollastons (SlNo INTEGER PRIMARY KEY, Aisle INTEGER, Items TEXT, Price REAL, Quantity REAL);

/*Now I am inserting data into my table*/
INSERT INTO Wollastons VALUES (1, 2, "Turkey Suasage", 3.12, 3);

INSERT INTO Wollastons VALUES (2, 3, "Chicken Nuggets", 10.12, 5);

INSERT INTO Wollastons VALUES (3, 8, "Fruit Packs", 12.12, 4);

INSERT INTO Wollastons VALUES (4, 1, "Vegetable Goodies", 11.12, 2);

INSERT INTO Wollastons VALUES (5, 7, "Ice Cream and Desert", 9.12, 2);

INSERT INTO Wollastons VALUES (6, 3, "Pastries", 13.12, 9);

INSERT INTO Wollastons VALUES (7, 6, "Winery", 23.12, 30);

INSERT INTO Wollastons VALUES (8, 11, "Cheese Sweeze", 27.12, 5);

INSERT INTO Wollastons VALUES (9, 4, "Jellies and Jam", 15.12, 2);

INSERT INTO Wollastons VALUES (10, 2, "Curd", 3.12, 10);

INSERT INTO Wollastons VALUES (11, 3, "Raw Meat", 14.12, 11);

INSERT INTO Wollastons VALUES (12, 3, "Hummus", 3.12, 4);

INSERT INTO Wollastons VALUES (13, 1, "Broccoli Packs", 10.00, 3);

INSERT INTO Wollastons VALUES (14, 1, "Potatoes", 4.12, 6);

INSERT INTO Wollastons VALUES (15, 1, "Carrots and Onions", 5.12, 10);

/*I am trying to fetch my table that is now filled with data*/
SELECT * FROM Wollastons;

/*Trying to get the total sum ot the quatities of my items in the Wollastons table*/
SELECT SUM(Quantity) FROM Wollastons;

/*Trying to check how many items are there in each Aisle*/
SELECT Aisle, COUNT(Items) FROM Wollastons GROUP BY Aisle;

/*To get all Items in each Aisle starting from their cheapest price*/
SELECT Aisle, Items, Price FROM Wollastons ORDER BY Aisle ASC, Price ASC;



