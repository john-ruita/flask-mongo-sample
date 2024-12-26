# SAT Sample Questions API

## Demo
You can access the online demo at [https://sat-sample.writers.ke](https://sat-sample.writers.ke)

## Setting Up

### Prerequisites
- Docker
- Docker Compose

### Steps
1. Clone the repository:
    ```sh
    git clone git@github.com:john-ruita/flask-mongo-sample.git
    ```
2. Navigate to the project directory:
    ```sh
    cd flask-mongo-sample
    ```
3. Copy the `.env.example` file to `.env` and update the values as needed:
    ```sh
    cp .env.example .env
    ```
4. Build and start the Docker containers:
    ```sh
    docker-compose up
    ```

Your application should now be running and accessible at `http://localhost:5000`.

## CRUD operations and JSON List
****
If your are using Pycharm open the file api.http and run the requests.
```
api
 └── server
  └── questions
    └── api.http
```
Or download the [postman collection](https://sat-sample.writers.ke/postman) and use postman.
Base url for online demo is https://sat-sample.writers.ke/api.
****
You can also use any other API testing tool and use the following endpoints.

### Create
- POST /api/question
```json
{
  "Question": "The function f(d) = -0.05d + 13.2 models the volume of fuel (in gallons) left in a truck's fuel tank after driving d miles. Based on this model, approximately how many gallons of fuel are consumed for every mile driven?",
  "Solution": "<color=green>Choice A is correct.</color> The function given is:\n<b><color=black>f(d) = -0.05d + 13.2</color></b>\n\nHere, the coefficient of d (which is -0.05) represents the change in the volume of fuel for each additional mile driven. \n\nSince it's negative, it indicates that the truck uses 0.05 gallons for each mile.\n",
  "CorrectAnswer": "0.05",
  "Options": [
    "0.05",
    "13.2",
    "21",
    "264"
  ],
  "Steps": [
    {
      "Title": "Step Title 1",
      "Result": "Result Title 1"
    },
    {
      "Title": "Step Title 2",
      "Result": "Result Title 2"
    }
  ]
}
```
### Read
- GET /api/question/{id}

### Update
- PUT /api/question/{id}
```json
{
  "Question": "The function f(d) = -0.05d + 13.2 models the volume of fuel (in gallons) left in a truck's fuel tank after driving d miles. Based on this model, approximately how many gallons of fuel are consumed for every mile driven?",
  "Solution": "<color=green>Choice A is correct.</color> The function given is:\n<b><color=black>f(d) = -0.05d + 13.2</color></b>\n\nHere, the coefficient of d (which is -0.05) represents the change in the volume of fuel for each additional mile driven. \n\nSince it's negative, it indicates that the truck uses 0.05 gallons for each mile.\n",
  "CorrectAnswer": 0,
  "Options": [
    "0.05",
    "13.2",
    "21",
    "264"
  ],
  "Steps": [
    {
      "Title": "Step Title 1",
      "Result": "Result Title 1",
      "ImageUrl": "https://picsum.photos/id/28/200/300"
    },
    {
      "Title": "Step Title 2",
      "Result": "Result Title 2",
      "ImageUrl": "https://picsum.photos/id/29/200/300"
    }
  ],
  "ImageUrl": "https://picsum.photos/id/237/200/300"
}
```

### Delete
- DELETE /api/question/{id}

### List
- GET /api/questions
