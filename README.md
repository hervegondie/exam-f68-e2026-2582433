# Data-Science-API-FastAPI-Docker
 
This project demonstrates a simple yet powerful API built using FastAPI for serving machine learning predictions. The API is containerized using Docker and is ready for deployment in any environment.

# Features

   FastAPI: High-performance API framework with built-in support for automatic documentation (Swagger UI & ReDoc).
   
   Dockerized: Fully containerized for easy deployment and scalability.
   
   Machine Learning Integration: Handles input data and returns predictions using a custom ML model.
   
   Customizable: Extendable architecture to integrate more models and features.
   
   Interactive Docs: Automatically generated API documentation available at /docs.
   

# Endpoints

  ### Health Check:

        URL: GET /
        Description: Verifies that the API is running.
        
  ### Response: 
      { 
      "message": "API is up and running!" 
      }

  ### Prediction:
        URL: POST /predict
        Description: Accepts a JSON payload with features and returns predictions.
    
 ### Request Body:
        {
        "features": [1.0, 2.0, 3.0]
        }

### Response:

        {
          "predictions": [2.0, 4.0, 6.0]
        }

# How to Run

### Clone the repository:
```
git clone https://github.com/AlexandruEmil/Data-Science-API-FastAPI-Docker
```
```
cd Data-Science-API-FastAPI-Docker
```
### Build and run the Docker container:
```
   docker-compose up --build
```
### Access the API:
   
        Swagger UI: http://localhost:8000/docs
        API Root: http://localhost:8000

Technologies Used

    Python: Version 3.10
    FastAPI: API framework
    Docker: Containerization
    Uvicorn: ASGI server

> [!NOTE]
> The endpoint ```/predict``` is configured for the POST method. \
> From browser you can use ```RESTer``` extention and use POST method

> [!WARNING]
>For ```/favicon.ico```, browsers automatically request the ```favicon.ico``` file when accessing a URL.\
> If you don't have a favicon configured, the server will return a ```404```.


![CI](https://github.com/jao81/TD-CI-DS-API-FastAPI-Docker/actions/workflows/CI.yml/badge.svg)