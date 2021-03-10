# SIMPLE MERN AUTH using JWT

## Description

 The web app consists in a Login/Register which has basic validation.
 Once the user registered and logs in, a screen confirms that the user
 successfuly logged into the website.

 This web app gives a foundation to implement a robust one.

 The app will allow users to 

    Register
    Log in
    Access protected pages only accessible to logged in users
    Stay logged in when they close the app or refresh the page
    Log out

## Demo - Screenshots

<img src="https://media.giphy.com/media/n6EzPgdhL0MWiwhWeH/giphy.gif" width="300">


## Problems faced on the project:

- On the tutorial was asked to use Mlab, but I couldn't connect there. Then a mistake was because I just allowed the currently IP address on my machine. 

- I came across an error regading CORS policy and learned the basic about Cross-Origin, read a bit about it and found out the faster way was to download Postman for desktop, because I didn't wan't to create a proxy.

- In all attempts on testing everything work as expected. However, in another project should be great to use unit test :D

## Installation

npm install && npm run client-install 

npm run dev 

# Testing Login and Register Endpoints

## Endpoints:

> Register: POST http://localhost:5000/api/users/register 

Navigate to the Body tab, select x-www-form-urlencoded, fill in your registration parameters (name, email,password,password2) and hit Send

> Login: POST http://localhost:5000/api/users/login same thing as register, instead just fill login parameters (email,password).

## Manual Test Made:

*1 - Checked invalid email formats*

  * If they don't have "@"
  * If they don't have at least 2 characters after the "."

*2 - Checked invalid passwords*

  * If they don't match
  * If they are shorter than 6 characters