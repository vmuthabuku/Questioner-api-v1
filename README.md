[![Build Status](https://travis-ci.com/vmuthabuku/Questioner-api-v1.svg?branch=ft-post-a-meetup-163052418)]

[![Coverage Status](https://coveralls.io/repos/github/vmuthabuku/Questioner-api-v1/badge.svg?branch=ch-addition-of-coveralls-163084088)](https://coveralls.io/github/vmuthabuku/Questioner-api-v1?branch=ch-addition-of-coveralls-163084088)

# Questioner-api-v1
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered.

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

in the terminal in the root directory of the folder run `pytest`

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
| POST /meetups/meetupid/rsvp | rsvp for a specific event |
| PATCH/questions/questionid/upvote | upvote a question |
| PATCH/questions/questionid/downvote | downvote a question |

### Author
[vmuthabuku](vthamara96@gmail.com)
