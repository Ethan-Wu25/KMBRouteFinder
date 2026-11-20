# KMBRouteFinder
A Java-based KMB route finder project focused on exploring route optimization using travel time and fares. The project is currently in early development.



### Fare Data Disclaimer
Currently, the KMB API does not provide route fare information. Therefore, this project uses fare data published by the Hong Kong Government.

However, KMB and the Hong Kong Government use different route identification systems. As a result, this project matches fare data using route names rather than unique route IDs.

Please note:This matching method may lead to inaccuracies, particularly when multiple routes share the same name. Fare information should therefore be treated as reference data rather than guaranteed accurate pricing.


# DataBase Set up
use scripts/setup_dp.py to set up SQlite DataBase.