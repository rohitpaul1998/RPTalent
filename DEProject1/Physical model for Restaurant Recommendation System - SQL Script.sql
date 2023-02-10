CREATE TABLE Restaurants (
  Restaurant_ID INT PRIMARY key not null,
  Restaurant_Name VARCHAR(390) NOT NULL,
  Restaurant_Number VARCHAR(50) NOT NULL,
  Restaurant_Address VARCHAR(100) NOT NULL,
  City VARCHAR(50) NOT NULL,
  State VARCHAR(50) NOT NULL,
  ZipCode VARCHAR(40) NOT NULL
);

CREATE TABLE Tripadvisor_Ratings (
  Tripadvisor_ID INT PRIMARY key not null,
  TripAdvisor_Rating VARCHAR(50) NOT NULL,
  TripAdvisor_Rating_Count VARCHAR(50) NOT NULL,
  Restaurant_ID INT NOT null,
  foreign key (Restaurant_ID) references Restaurants(Restaurant_ID)
);

CREATE TABLE Foursquare_Ratings (
  Foursquare_ID INT PRIMARY key not null,
  Foursquare_Rating VARCHAR(50) NOT NULL,
  Restaurant_ID INT NOT null,
  foreign key (Restaurant_ID) references Restaurants(Restaurant_ID)
);


