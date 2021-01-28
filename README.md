# Dog-vs-cat-classifier

# About the project :
#### This is a simple project which takes a picture of cat or dog and outputs the probability of each of them. 

#### The model has been built using the pre-trained Mobilenet model for better accuracy.

#### You can visit the app at https://dog-vs-cat-classifier.herokuapp.com

# The working flow of the project :

#### The backend has been built using flask. When you first visit the app it takes you to the home.html where you will see two buttons one is for choosing the image and one for classification. After you select the image from your device and click on the predict button it sends the image to flask which takes the image choosen by the user and then loads the whole preprocessing pipeline. The whole preprocessing logic is in the predict.py file in the form of class. After getting the prediction result flask renders the predict.html page which shows the probability of the cat and dog.

# Requirements for this project to run on your local machine :

#### Flask==1.1.2
#### matplotlib==3.3.3
#### numpy==1.19.4
#### pandas==1.1.5
#### Pillow==8.0.1
#### tensorflow==2.3.1

# A side note :

### If you find any bug feel free to modify, and you can add new features too.

# Catch me :

#### Instagram :- https://www.instagram.com/noor_coder/
#### Linkedin :- https://www.linkedin.com/in/noor-mohammad-0a28a21a3/
