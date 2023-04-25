from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_connection_string']

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem",
                       }})

# def load_jobs_from_db():
#   with engine.connect() as conn:
#     result = conn.execute(text("SELECT * FROM jobs"))

#     jobs = []
#     for row in result.all():
#       jobs.append(row._mapping)
#     return jobs


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(
      text(
        "SELECT  title, location, salary, currency, responsibilities, requirments FROM jobs"
      ))
    jobs = []
    for row in result.fetchall():
      job = {
        'title': row[0],
        'location': row[1],
        'salary': row[2],
        'currency': row[3],
        'responsibilities': row[4],
        'requirments': row[5]
      }
      jobs.append(job)
    return jobs
