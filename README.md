[![Build Status](https://travis-ci.com/vmuthabuku/Questioner-api-v1.svg?branch=develop)]
[![Coverage Status](https://coveralls.io/repos/github/vmuthabuku/Questioner-api-v1/badge.svg?branch=develop)](https://coveralls.io/github/vmuthabuku/Questioner-api-v1?branch=ch-addition-of-coveralls-163084088)
[![Maintainability](https://api.codeclimate.com/v1/badges/aa526901c2bdce291ab8/maintainability)](https://codeclimate.com/github/vmuthabuku/Questioner-api-v1/maintainability)
[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/15026be3425422d57a74)

# Questioner-api-v1
Questioner-api-v1 is a platform where someone can crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered.

### The Questioner api should manage to:

    - An admin should be able to create a meetup
    - A user should be able to get all meetups
    - A user should be able to get a specific meetup
    - A user should be able to create a question
    - A user should be able to get all questions
    - A user should be able to get a specific question
    - A user should be able to rsvp for a specific meetup
    - A user should be able to upvote or downvote a question


### Running the app
1. git clone the repo `https://github.com/vmuthabuku/Questioner-api-v1.git`
2. Switch to `develop` branch \
`$ git checkout develop`
3. install requirements
`$ pip install -r requirements.txt`
4. in the terminal 
`$ export FLASK_APP=run.py`
5. run the app
`$ flask run`

### Run tests

1. git clone the repo `https://github.com/vmuthabuku/Questioner-api-v1.git`
2. cd into the folder `Questioner-api-v1`
3. move the root directory of the folder 
4. run `pytest`

### Pivotal tracker stories 
[Pivotal tracker](https://www.pivotaltracker.com/n/projects/2235282)

### Heroku link

 https://questioner-api-v1.herokuapp.com/

## Endpoints

The api endpoints are

| Endpoint | Description |
| --- | --- |
| GET /meetups/incoming | Fetch all icoming meetups |
| GET /meetups/meetupid | Fetch a single meetup record |
| POST /meetups | create a meetup |
| POST /questions | create a question |
| GET /questions | get all questions |
| GET /questions/questionid | get a specific questions |
| POST /meetups/meetupid/rsvp | rsvp for a specific event |
| PATCH/questions/questionid/upvote | upvote a question |
| PATCH/questions/questionid/downvote | downvote a question |

### Author
[vmuthabuku](vthamara96@gmail.com)
