# flask-mongo-sample

## How to set up locally
1. Install docker and docker-compose
2. Clone the repository
3. cd into the repository
4. Run `docker-compose up`

## CRUD operations and JSON List
If your are using Pycharm open the file api.http and run the requests.
```
api
 └── server
  └── questions
    └── api.http
```

You can also use Postman or any other API testing tool and use the following endpoints.
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
      "Result": "Result Title 1"
    },
    {
      "Title": "Step Title 2",
      "Result": "Result Title 2"
    }
  ]
}
```

### Delete
- DELETE /api/question/{id}

### List
- GET /api/questions
