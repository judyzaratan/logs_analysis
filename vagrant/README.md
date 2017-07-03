# Logs Analysis

## Description


##How to run application

1) Run a virtual machine
⋅⋅⋅Vagrantfile is included in repository. Please run following commands in Terminal:

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
