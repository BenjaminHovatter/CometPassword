# CometPassword


Instructions to run backend:

In runner.py, call the function store_credentials() by passing the credentials (username and password) along with the hosts information to it.
This will create (if it does not already exist) a file under the directory "./Hosts/" with the name of the host provided. 
This file will contain the encrypted credentials of the user for that host.

To decrypt the user's credentials on a particular host, call get_credentials() by passing the host's name to it. This will decrypt and return the username and password of the user for that host.
