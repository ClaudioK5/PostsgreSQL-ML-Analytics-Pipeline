# PostsgreSQL-ML-Analytics-Pipeline
This pipeline integrates with the **FastAPI PostgreSQL client-orders handler pipeline**, analyzes the orders stored in the postsgreSQL database and **creates for each ordered product a demand statistics graph, a prediction demand graph using machine learning models, and finally a combined graph**. All of the plots are then uploaded on a desired AWS bucket in a graphs folder.
These **graphs** are crucial for **extracting insights into company operations, helping identify demand trends, optimize inventory, and support data-driven decision-making.**
