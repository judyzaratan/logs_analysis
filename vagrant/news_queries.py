#!/usr/bin/env python
#
# news_query.py -- reports results from a news article database
#

import psycopg2


def connect(database_name="news"):
    try:
        """Connect to the PostgreSQL database.
        Returns a database connection."""
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")


def reportPopularArticles():
    """Reports 3 most popular articles"""
    query = """select articles.title, count(*) as total from log, articles
        where log.path like concat('%', articles.slug, '%')
        group by articles.slug, articles.title
        order by total desc
        limit 3;"""

    report_title = "Report 3 top accessed articles"

    db, c = connect()
    print (report_title)
    c.execute(query)
    q = c.fetchall()
    c.close()
    for report in q:
        print (report[0], '-', report[1], 'views')
    return


def reportPopularAuthors():
    """Reports 3 most popular authors"""
    query = """select authors.name, count(articles.author) as total
        from log, articles, authors
        where log.path like concat('%', articles.slug, '%')
        and articles.author= authors.id
        group by authors.name
        order by total desc
        limit 3;"""

    report_title = "Report 3 top viewed authors"

    db, c = connect()
    print (report_title)
    c.execute(query)
    q = c.fetchall()
    c.close()
    for report in q:
        print (report[0], '-', report[1], 'views')
    return


def reportErrorDays():
    """Reports days where more than 1% of requests led to errors"""
    query = """select a.d, (round((cast(a.tally as decimal)/b.tally)*100, 2)),
        a.d
        from
            (select count(status) as tally, date(time) as d from log
                where status = '404 NOT FOUND'
                group by d) as a,
            (select count(status) as tally, date(time) as d from log
                group by d) as b
        where a.d = b.d and
        (round((cast(a.tally as decimal)/b.tally)*100, 2)) > 1;"""

    report_title = "Report day when over 1% resulted in error"

    db, c = connect()
    print (report_title)
    c.execute(query)
    q = c.fetchall()
    c.close()

    for report in q:
        print (report[0], '-', report[1], '%')
    return


reportPopularArticles()
print ("---")
reportPopularAuthors()
print ("---")
reportErrorDays()
