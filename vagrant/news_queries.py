#!/usr/bin/env python
#
# news_query.py -- reports results from a news article database
#

import psycopg2


query1 = """select articles.title, count(*) as total from log, articles
    where log.path like concat('%', articles.slug, '%')
    group by articles.slug, articles.title
    order by total desc
    limit 3;"""

report1_title = "Report 3 top accessed articles"

query2 = """select count(articles.author) as total, authors.name
    from log, articles, authors
    where log.path like concat('%', articles.slug, '%')
    and articles.author= authors.id
    group by authors.name
    order by total desc
    limit 3;"""

report2_title = "Report 3 top viewed authors"

query3 = """select (round((cast(a.tally as decimal)/b.tally)*100, 2)) as percent,
    a.tally, b.tally, a.d, b.d
    from
        (select count(status) as tally, date(time) as d from log
            where status = '404 NOT FOUND'
            group by d) as a,
        (select count(status) as tally, date(time) as d from log
            group by d) as b
    where a.d = b.d and
    (round((cast(a.tally as decimal)/b.tally)*100, 2)) > 1;"""

report3_title = "Report day when over 1% resulted in error"

reports = [
    (report1_title, query1),
    (report2_title, query2),
    (report3_title, query3)
]


def connect(database_name="news"):
    try:
        """Connect to the PostgreSQL database.
        Returns a database connection."""
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        print ('Connected to the database')
        return db, cursor
    except:
        print("<error message>")


def query(query_list):
    for report in query_list:
        db, c = connect()
        print (report[0])
        c.execute(report[1])
        q = c.fetchall()
        c.close()
        for result in q:
            print ('"', result[0], '" —', result[1], "views")
    print ("Queries complete")
    return


query(reports)
