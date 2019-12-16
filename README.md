# mail-sender

## setup

- Create `template.html` with HTML version of email content
- Create `template.txt` with plain text email content (for the clients that does not allow HTML)
- Replace `<your_email>` and `<your_password>` variables in `mail.py` file with proper ones 
- Start db
  ```
  $ docker-compose up -d
  ```
- Create `receivers` table
  ```
  create table receivers
  (
    email text not null
      constraint receivers_pk
        primary key,
    sent boolean default false
  );

  alter table receivers owner to postgres;

  create unique index receivers_email_uindex
    on receivers (email);

  ```
- Fill the db with receivers emails
- Install dependencies
  ```
  $ pip install psycopg2-binary
  ```
- Run
  ```
  $ python sender.py
  ```

### Note

Gmail will block mails after sending 150+ at one. Wait 1-24h and try again.