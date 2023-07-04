# Lab - Class 16
## Project: capital-finder

Author: Sarah Glass for Python 401

Collaborated with Dan Quinn and Anthony Sinitsa on the code.

## Overview

Deploy a serverless function to the cloud.

- Sign up with Vercel.
- Create a repository on Github and link it to Vercel account.
- Use requests library to interact with REST Countries API
- Create a serverless function following Vercel’s get-started directions that handles two kinds of queries:

  - The serverless function should handle a GET http request with a given country name that responds with a string with the form The capital of X is Y
  - E.g./capital-finder?country=Chile should generate an http response of The capital of Chile is Santiago.
  - The serverless function should handle a GET http request with a given capital that responds with a string with the form The capital of X is Y
  - E.g./capital-finder?capital=Santiago should generate an http response of Santiago is the capital of Chile.

## Links and Resources

* TA and peer help.
* This API: [https://restcountries.com/#rest-countries](https://restcountries.com/#rest-countries)

## Setup
No .env requirements; gitignore invludes venv.

## How to initialize/run your application

* Deployed through Vercel: [https://capital-finder-teal-one.vercel.app/api/capital_finder](https://capital-finder-teal-one.vercel.app/api/capital_finder)

## How to use your library
The only library brought in was Requests