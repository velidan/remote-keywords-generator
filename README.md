# URL Keywords generator
A REST service that allows you to parse the title of the remote web-page and generate all possible keywords combination based on it

Based on Python 3.6, Django 2, Django Rest Framework, urllib3, beautifysoup4

How to install & run:

Easiest way is to do it via Docker

download the image:  url_keys
1) docker pull velidan/url_keys
2) docker-compose up


it should run the dev server at the http://0.0.0.0:8000/ host

URL model structure
{
    id: int <Primary Key. AutoInremented>;
    title: string <optional>;
    address: string;
    keywords: string;
}

REST API works under /api/urls entrypoint  

1) You can see all previously saved urls, their ids, titles and keywords.
   To do it you should do a GET request to: http://127.0.0.1:8000/api/urls

2) You can create a keywords for a new URL by executing a POST request
   to http://127.0.0.1:8000/api/urls 
   Payload should be: url='http://urladdress'
   Payload should be a plain text.

   If this URL doesn't exist you'll receive the 404 err with the human readable message

   If the URL had been already handled when you executed the POST request it will be just updated. Duplicates won't be created

   In case of success you'll receive 201 status and the URL data.

   In case of error you'll receive 400 status and an error msg

3) You can see a particular URL detail by going a GET request to
   http://127.0.0.1:8000/api/urls/<int:url_id>
   url_id - the id of the url what you can examine.

4) You can update the keywords etc. in a particular URL manually by     executing a PUT request to:
http://127.0.0.1:8000/api/urls/<int:url_id>
payload should be a stringified json that contains model fields that you want to update
In case of error you'll receive status 400 and an error msg

5) You can delete a particulr URL data bu executing a DELETE request to
http://127.0.0.1:8000/api/urls/<int:url_id>
In case of success you will receive 204


