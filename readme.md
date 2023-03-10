# How to use the script.

## Signup for an account in OpenAI
[Signup here](https://auth0.openai.com/u/signup/identifier?state=hKFo2SB3V1E1ZjlWcWk0eVdsUXdqcFphLW93bm5XdVNyRW5Ta6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIHJ2ZDk0SUJtU25SX3Izb3BrUzhFeG4wV1I2UXFsRHE3o2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q)

## Create an API Key
- Navigate to your account managment and look for "View API Keys" section
- Create a new secret key
- Copy the key and paste it in a file called "key.txt"

## Install OpenAI python module
- *Beforehand make sure you have Python software installed in your computer*
- Open a command window and paste this 
  - **pip install openai** *or* **pip3 install openai**

## Clone the repository
- git clone https://github.com/lopeben/gpt_models.git
- and copy the "key.txt" file into this repository

## Run the script
- python -u davinci003.py "Hello DaVinci"
- python -u gpt35_turbo.py "<anything you want to talk about>"

## GPT Models
- davinci003.py uses text-davinci-003
- gpt35_turbo.py uses gpt-3.5-turbo
- read [Documentation](https://platform.openai.com/docs/models/gpt-3-5)
