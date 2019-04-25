# setUp
* virtualenv
> create virtual environment for this project
* source cs_project3/bin/activate
> get in virtual env
* pip install -r requirements.txt
> install requirements from freeze version
* python manage.py migrate
> create table for app
* python manage.py runserver localhosst:10043
> run server
* open website with url http://mac1xa3.ca/u/muw2/project3.html
> use my bill app
* register to have an account 
* login to add bill and look previous bill
* if not login, the website shows ** instead of bill

* feature
> use django's built-in session to control user log in and log out
> The session informmmation is written when thee euser logs in and registers
> when the bill is created and the bill is read, the user is first checked according to the session
> use the bootstrap, mmodal, form etc. css classes, to make the webpage rendering
> base on jquery processing data selection and rendering, using ajax to commplete the situation that the page does not refresh data submission
> did research during code editing, sometime go to chinese website to find how to resolve problem
#commend
* virtualenv
> install virtualenv
> virtualenv project3_env
> source bin/activate
>deactivate
* branch
> use branch project03 to edit
> merge after completing the program
* check the url set up
> go to the virtual environment
> run server at localhost 10043
* session cookie
> session cookies enable the website you are visiting to keep track of your movement from page to page
> do not need to get asked for the same information customer has already given to the site
> cookies allow costumer to proceed through many pages of a site quickly and easily without having to authenticate or reprocess each new area costumer visit
> reference https://www.allaboutcookies.org/cookies/session-cookies-used-for.html
* resetful api
> an api uses http to get put post and delete data
> reference https://linuxhint.com/rest_api_python/
* bootstrap
> reference https://www.w3schools.com/bootstrap/default.asp
* modal (bootstrap)
> mmodal.js
> reference http://v3.bootcss.com/javascript/#modals
* cors
> Cross-origin resource sharing, which can fix the problem of ajax limitation

