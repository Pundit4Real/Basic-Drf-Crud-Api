# HNGx Backend Stage 2 Task: API Documentation

### Introduction

A warm welcome to the documentation for **my awesome API**. This API allows you to perform *CRUD (Create, Read, Update, Delete) operations* on user profiles.

## API Endpoints
#### Create a Person Profile
Endpoint: POST /api

##### Request Format:
`{
    "name": "Tulasi Joshua"
}`

##### Response Format:
    {
        "status": 200 ok,
       
         {
            "id": 2,
            "name": "Tulasi Joshua",
            "country": "CHAD",
            "stack": "Backend",
            "added": "2023-09-15T16:32:29.220209Z"
        }

    }

#### Get Person Profile
Endpoint: GET /api/{user_id}

##### Request Format: 
`No request body required.`

##### Response Format:
    {
        {
            "id": 3,
            "name": "MOHAMMED ALI",
            "country": "GHANA",
            "stack": "Backend",
            "added": "2023-09-15T17:00:45.115412Z"
        }
    }

#### Update Person Profile
Endpoint: PATCH /api/{user_id}/

##### Request Format:
    {
        "name": "Updated Name"
    }

##### Response Format:
    {
        "status": 200 ok,
       
    }

#### Delete Person Profile
Endpoint: DELETE /api/{user_id}/

##### Request Format: 
    No request body required.

##### Response Format:
    {
        "status": 204 No Content,
       
    }

## Sample Usage

### Creating a Person Profile
##### Request:

###### POST /api
    Content-Type: application/json

    {
        "name": "MOHAMMED ALI"
    }

#### Response:
    HTTP/1.1 201 Created
    {
        "status": true,
       
        {
            "id": 3,
            "name": "MOHAMMED ALI",
            "country": "GHANA",
            "stack": "Backend",
            "added": "2023-09-15T17:00:45.115412Z"
        }
    }

### Getting Personal Profile
#### Request:
`GET /api/2`
#### Response:
    HTTP/1.1 200 OK
    {
        "status": 200 OK,
        {
            "id": 3,
            "name": "MOHAMMED ALI",
            "country": "GHANA",
            "stack": "Backend",
            "added": "2023-09-15T17:00:45.115412Z"
        }
    }


# Limitations and Assumptions
*The API assumes that person profiles are identified by unique numeric IDs.
This documentation covers the basic functionality of the API and does not include advanced features like authentication and authorization as the project does not require that.*

## Local Setup

*To set up and run the API locally:*

- Clone the repository from GitHub.
- Install the required dependencies using `pip install -r requirements.txt`.
- Create and apply the database migrations using `python manage.py makemigrations` and `python manage.py migrate`.
- Run the development server with `python manage.py runserver`.

good luck!!!
