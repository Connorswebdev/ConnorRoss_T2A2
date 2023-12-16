# Flask App Installation Guide

## Prerequisites
Make sure you have the following installed on your system:
- [Python](https://www.python.org/) (version 3.6 or higher)
- [pip](https://pip.pypa.io/en/stable/installation/) (Python package installer)

## Instructions on how to set up application:

Provided is a sample .env file, but a personal postgresql uri and jwt secret key must be provided for the application to work.

Change directory to /src folder, then run commands in terminal below:

`python3 -m venv .venv`

`source .venv/bin/activate`

`pip install -r requirements.txt`

In order to create tables, run:

`flask db create`

Populate the tables with:

`flask db seed`

Run server with in /src folder:

`flask run`

### Requirement 1 - Identify the problem you are trying to solve with this app
Creating this app aims to tackle a range of challenges faced by people with allergies. For those with specific dietary restrictions, finding restaurants that cater to their needs can be a real struggle, occassionally even leading to health risks from accidental allergen consumption. The app comes as a solution, making it easier for users to discover restaurants offering allergen-free or allergy-friendly options. Beyond just health concerns, it aims to simplify the often time-consuming process of researching and contacting restaurants for allergy information, providing a user-friendly experience. It also supports allergy-friendly restaurants by increasing their visibility and fostering a sense of community among users with similar dietary restrictions. In essence, this app not only addresses health-related challenges but also seeks to improve accessibility, convenience, and community engagement for individuals with dietary restrictions.

### Requirement 2 - Why is it a problem that needs solving
The need to address the challenges faced by individuals with allergies is paramount due to the severity and prevalence of allergic reactions, which can lead to hospitalizations and, in extreme cases, fatalities. According to the Centers for Disease Control and Prevention (CDC), food allergies result in over 200,000 emergency room visits annually in the United States alone. Additionally, a study published in the Journal of Allergy and Clinical Immunology estimates that food allergies affect approximately 32 million Americans, including 5.6 million children, with an increasing trend observed over the years. 

[Source] Available at: (https://matsui.house.gov/media/press-releases/matsui-gallagher-lead-effort-highlight-benefits-early-introduction-food#:~:text=Food%20allergies%20impact%20an%20estimated,requiring%20emergency%20medical%20treatment%20annually) [Accessed 16 Dec. 2023].

The consequences of accidental allergen exposure can range from mild discomfort to life-threatening anaphylaxis. Anaphylaxis is a severe allergic reaction that can cause a rapid drop in blood pressure, difficulty breathing, and, if not treated promptly, can be fatal. The Asthma and Allergy Foundation of America reports that anaphylaxis results in an estimated 1,500 deaths in the United States annually.

Given the substantial impact of allergies on public health and the potential for severe consequences, a dedicated app that helps users easily identify allergy-friendly restaurants is essential. By providing accurate and accessible information about allergen-free menu options, the app contributes to reducing the risk of allergic reactions and related hospitalizations. The ultimate goal is to enhance the safety, well-being, and overall quality of life for individuals managing allergies.

### Requirement 3 - Why Choose PostgreSQL? What are the drawbacks compared to others?

Selecting PostgreSQL as the go-to database system brings with it some notable benefits, but like any choice, it isn't without its drawbacks. On the positive side, PostgreSQL is an open-source platform, making it not only cost-effective but also customizable to suit project needs. Renowned for its robustness, this system ensures data integrity even in the face of system failures, thanks to its adherence to ACID principles. PostgreSQL is highly extensible, allowing developers the freedom to create tailored functions, data types, and operators. Its support for diverse data types, scalability, and an active community further contribute to its popularity. However, navigating PostgreSQL may pose a steeper learning curve for those accustomed to other databases. Performance, particularly in comparison to databases like MySQL or NoSQL options, can be subjective to the use case. Additionally, while PostgreSQL offers replication features, some databases provide more straightforward built-in tools for replication setup. In essence, the choice between PostgreSQL and other systems hinges on the unique requirements of a project, considering factors such as performance, ease of use, database knowledge and available features.

### Requirement 4 - Identify and discuss the key functionalities and benefits of an ORM

Object-Relational Mapping (ORM) serves as a crucial facilitator in bridging the gap between databases and applications by abstracting the intricacies of database operations into a more intuitive, object-oriented model. With ORM, developers can interact with databases using the paradigm of classes and objects, simplifying the code and aligning it closely with the logic of the application. This abstraction also offers portability, enabling developers to switch between different database systems with minimal code adjustments. ORM significantly enhances productivity and accelerates development cycles by simplifying CRUD operations and reducing boilerplate code. The framework promotes code reusability, maintains clean separation between business logic and database interactions, and often automates query generation, minimizing the risk of SQL injection vulnerabilities. Additionally, ORM contributes to maintainability, providing tools for managing database schemas, handling concurrency control, and seamlessly integrating the database with the application's business logic. While ORM introduces some performance overhead, its advantages in terms of productivity and code organization make it a valuable asset in modern application development.

### Requiremtn 5 - Document all Endpoints

#### User Routes (/users)

1. /users/

Method: GET

Description: Retrieve a list of all users, excluding passwords (admin access only).

Authorization: Requires a valid JWT token with admin privileges.

Response:

200 OK: Returns a list of user objects excluding their passwords.
401 Unauthorized: If the request is not authorized as an admin.

2. /users/{user_id}

Methods: PUT, PATCH

Description: Update a user's information.

Authorization: Requires a valid JWT token with admin privileges or the user themselves.

Request: Accepts JSON data with optional fields for updating user information.

Response:

200 OK: Returns the updated user object excluding the password.

404 Not Found: If the specified user ID does not exist.

401 Unauthorized: If the request is not authorized as an admin or the user themselves.

3. /users/{user_id}

Method: DELETE

Description: Delete a user.

Authorization: Requires a valid JWT token with admin privileges or the user themselves.

Response:

200 OK: If the user is successfully deleted.

404 Not Found: If the specified user ID does not exist.

401 Unauthorized: If the request is not authorized as an admin or the user themselves.


#### Restaurants Routes

1. /restaurants/

Method: GET

Description: Retrieve a list of all restaurants.

Response:

200 OK: Returns a list of restaurant objects excluding the location ID.

404 Not Found: If no restaurants are found.


2. /restaurants/{restaurant_id}

Method: GET

Description: Retrieve information for a specific restaurant.

Response:

200 OK: Returns the restaurant object excluding the ID and location ID.

404 Not Found: If the specified restaurant ID does not exist.

3. /restaurants/

Method: POST

Description: Create a new restaurant.

Authorization: Requires a valid JWT token.

Request: Accepts JSON data with required fields for creating a new restaurant.

Response:

201 Created: Returns the created restaurant object excluding the location ID.

400 Bad Request: If there are issues with the request body.

401 Unauthorized: If the request is not authorized.


4. /restaurants/{restaurant_id}

Method: PUT, PATCH

Description: Update a restaurant's information.

Authorization: Requires a valid JWT token.

Request: Accepts JSON data with optional fields for updating restaurant information.

Response:

200 OK: Returns the updated restaurant object excluding the location ID.

404 Not Found: If the specified restaurant ID does not exist.

400 Bad Request: If there are issues with the request body.

401 Unauthorized: If the request is not authorized.


5. /restaurants/{restaurant_id}

Method: DELETE

Description: Delete a restaurant.

Authorization: Requires a valid JWT token.

Response:

200 OK: If the restaurant is successfully deleted.

404 Not Found: If the specified restaurant ID does not exist.

401 Unauthorized: If the request is not authorized.


#### Authentication Routes:

1. /auth/sign_up

Method: POST

Description: Register a new user.

Request: Accepts JSON data with required fields for user registration.

Response:

201 Created: Returns the created user object excluding the password.

400 Bad Request: If there are issues with the request body.

409 Conflict: If the email address is already in use.

2. /auth/login

Method: POST

Description: Login with email and password.

Request: Accepts JSON data with email and password for user login.

Response:

200 OK: Returns a JWT token and user object excluding the password.

401 Unauthorized: If the email or password is invalid.

400 Bad Request: If the email and password are not provided.


#### Allergy Routes

1. /allergies/

Method: GET

Description: Retrieve a list of all allergies.

Response:

200 OK: Returns a list of allergy objects excluding the location ID.

404 Not Found: If no allergies are found.


2. /allergies/{allergy_id}

Method: GET

Description: Retrieve information for a specific allergy.

Response:

200 OK: Returns the allergy object excluding the ID and location ID.

404 Not Found: If the specified allergy ID does not exist.


3. /allergies/

Method: POST

Description: Create a new allergy.

Authorization: Requires a valid JWT token.

Request: Accepts JSON data with required fields for creating a new allergy.

Response:

201 Created: Returns the created allergy object excluding the location ID.

400 Bad Request: If there are issues with the request body.

401 Unauthorized: If the request is not authorized.


4. /allergies/{allergy_id}

Method: PUT/PATCH

Description: Update an allergy's information.

Authorization: Requires a valid JWT token.

Request: Accepts JSON data with optional fields for updating allergy information.

Response:

200 OK: Returns the updated allergy object excluding the location ID.

404 Not Found: If the specified allergy ID does not exist.

400 Bad Request: If there are issues with the request body.

401 Unauthorized: If the request is not authorized.


5. /allergies/{allergy_id}

Method: DELETE

Description: Delete an allergy.

Authorization: Requires a valid JWT token.

Response:

200 OK: If the allergy is successfully deleted.

404 Not Found: If the specified allergy ID does not exist.

401 Unauthorized: If the request is not authorized.

#### Error Handling

The Flask application incorporates a robust error handling system to provide informative and user-friendly responses in various exceptional scenarios. For instance, when attempting to access or modify resources such as users, restaurants, or allergies that do not exist, the application responds with a clear "Not Found" message and a corresponding HTTP 404 status code. Additionally, the system handles scenarios like attempting to create a new user with an email address already in use or creating a restaurant with an invalid location ID, delivering appropriate responses with distinct HTTP status codes such as 409 Conflict or 400 Bad Request, respectively. Furthermore, when user login attempts fail due to incorrect credentials or missing email/password information, the application issues a concise and accurate error message alongside a 401 Unauthorized status code. Lastly, to ensure secure data access, the system requires the appropriate privileges (admin or user ownership) and responds with a 401 Unauthorized status if those conditions are not met. This comprehensive approach to error handling enhances the API's usability by guiding users through potential issues and facilitating effective issue resolution. Images are linked below which provide examples of how error handling was used in the app.

![Local Image](docs/errorhandling.JPG.jpg)
![Local Image](docs/errorhandling2.JPG.jpg)

