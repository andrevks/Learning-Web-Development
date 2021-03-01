#  :beginner: Testing Login and Register Endpoints

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

## Short statement about the project:

- On the tutorial was asked to use Mlab, but I couldn't connect there. Then a mistake was because I just allowed the currently IP address on my machine. 

- I came across an error regading CORS policy and learned the basic about Cross-Origin, read a bit about it and found out the faster way was to download Postman for desktop, because I didn't wan't to create a proxy.

- In all attempts on testing everything work as expected. However, in another project should be great to use unit test :D