# wikiquotes_serverless

Random tweet from Wikiquotes using Serverless (AWS Lambda)

Pre-steps:

 1. Create an AWS account.

Steps to install:

 1. Clone this repo.
 2. Install the `serverless` tool.
 
`sudo npm install -g serverless`
    
 3. `cd wikiquotes_serverless`

 4. Execute the following commands (be sure to use Python 3.x):

`virtualenv env`

`source env/bin/activate`

`pip install tweepy requests wikiquotes`

`pip freeze > requirements.txt`

`npm init `

`npm install --save serverless-python-requirements`

5. `sls deploy`

