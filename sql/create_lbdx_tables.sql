drop table if EXISTS book_table

create TABLE book_table(
    id SERIAL PRIMARY KEY ,
    libridex_id INT,
    author text,
    genre text, 
    bk_desc text, 
    bk_lang text, 
    copyright_year int, 
    lib_book_url text, 
    img_url text, 
)