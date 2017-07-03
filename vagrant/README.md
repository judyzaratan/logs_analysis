# Logs Analysis

## Description
This application reports the following queries from a sample SQL news database.  
1) Reports the 3 most popular articles
2) Reports the 3 most popular authors
3) Report the days where more than 1% of requests on news website lead to errors

## How to run application

1) Run a virtual machine
Vagrantfile is included in repository. Please run following commands in Terminal:

```
vagrant up
vagrant ssh
```

2) When virtual machine is up and running, change directory containing files
```
cd /vagrant
```

3) Create database and import database schemas, by typing in Terminal:
```
psql -d news -f newsdata.sql
```

4) Run test file to run database queries.
```
python3 news_query.py
```

A sample of Terminal output can be viewed in `report_sample.txt`
