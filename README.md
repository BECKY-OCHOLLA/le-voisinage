# le-voisinage

## Author

#### Becky Ocholla

## Description

A Django application that allows users know about their Neighborhood, businesses around and keeps them updated on events taking place around them.

## Live Link



## User Story

* Signup & signin to use the application
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Leave My neighborhood when I decide to move out.
* View details of a single neighborhood.
* User is able to search for different businesses in the area
* Only the admin can create a new neighborhood with by signing into the app with the credentials



## Prerequisites

You need the following to start working on this project: On your local system; 

1. Python3.8
2. Django
3. Pip
4. Virtual Environment(venv)
5. A text editor

## Development Installation

To get the code..

1. Clone the repository:
 `git clone https://github.com/BECKY-OCHOLLA/le-voisinage `

2. Move to the folder and install requirements
 ` cd Ujirani`

3. In the projects root directory, install the virtualenv library using pip and create a virtual environment. Run the following commands respectively:
    - **`pip install virtualenv`**
    - **`virtualenv venv`**
    - **`. venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
4. Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
5. Launch the application locally by running the command **`python manage.py runserver`** and copying the link given on the termnal on your browser.
    - To upload photos as admin, run the command  **`python manage.py createsuperuser`** to create an admin account in order to post. Access to the admin panel is by adding the path /admin to the address bar.
6. Run tests by running the command **`python3.8 manage.py test hood`**

## Technology used

* [Python3.8](https://www.python.org/)
* [Django](https://docs.djangoproject.com)
* [Heroku](https://heroku.com)
* Git
* Bootstrap 4.3.1

## Known Bugs

* There are no known bugs currently but pull requests are allowed incase you spot a bug

## Contact Information 

If you have any question or contributions, please email me at [ochollabecky0@gmail.com]

## License
Copyright (c) 2022 Becky Ocholla

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
