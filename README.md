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