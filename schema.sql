DROP TABLE IF EXISTS temperature;


CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  exterior TEXT NOT NULL,
  bedroom TEXT NOT NULL,
  livingroom TEXT NOT NULL,
  FOREIGN KEY (author_id) REFERENCES user (id)
);