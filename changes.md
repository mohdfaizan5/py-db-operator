# Insert.py

- [x] Update the SQL query by making placeholders and data dynamic
- [x] make it universal \<table_name> and take parameter names from the csv header
- [ ] Dealing with null values
  - [ ] 1048 (23000): Column 'dob' cannot be null

# Show tables



# WEBSITE

## Navbar 
1. "Data science" -> "Data warehouse" 
2. "Training" -> "Learing's and Training's" 
3. Add one more link "Big Data" 

https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.mynrma.com.au%2Ftravel%2Froad-trips%2Fmelbourne-to-great-ocean-road&psig=AOvVaw3jgR8JQqRh_A0TQSJtgRUZ&ust=1710214193387000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCJCA372i64QDFQAAAAAdAAAAABAJ

https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FSydney_Opera_House&psig=AOvVaw2oisjvdI4hqd-aEXa5oYnA&ust=1710214239890000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCIDrhtSi64QDFQAAAAAdAAAAABAE

https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.britannica.com%2Ftopic%2FSydney-Harbour-Bridge&psig=AOvVaw1HCqLWdS6x_Py-zbf28T46&ust=1710214271618000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCNC6mOOi64QDFQAAAAAdAAAAABAI


## Test cases

## Insert.csv
✅Extra spaces, `list out of range`
```
table_name,name,phone_no,address,dob
employees,mq,aslfd,Gujrath,1999-12-10







```

Mising column value:

- ❌ We can't set `NULL` to date datatype or int can be set to `NULL`
- ❌ Option is you have to either enter `0` or `1000-01-10` -> junk data
```
table_name,name,phone_no,address,dob
employees,mq,,Gujrath,1999-12-10
```


✅Wrong data format

`Invalid date format: '12-10-1999'. Please use YYYY-MM-DD.`
```
table_name,name,phone_no,address,dob
employees,mq,93424341,Gujrath,12-10-1999
```

## delete.csv

✅Case insensitive target_value/column_value bug

```
table,name
USERS,SACHIN
<!-- It was deleting by name `sachin` -->
```

## Show tables

✅ If no tables were mentioned then 
```
table_name,

```