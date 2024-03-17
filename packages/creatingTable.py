
        cursor.execute("""CREATE TABLE users (
  id INT NOT NULL PRIMARY KEY,  -- Primary key, not auto-increment
  name VARCHAR(255) DEFAULT NULL,  -- Name allows NULL values
  phone_no INT DEFAULT NULL,  -- Phone number allows NULL values
  address TEXT DEFAULT NULL,  -- Address allows text data and NULL values
  dob DATE DEFAULT NULL  -- Date of birth allows date format and NULL values
);
""")
        return      