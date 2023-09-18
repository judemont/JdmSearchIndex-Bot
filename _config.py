MAX_PAGE_TEXT_LENGTH = 500*1000

SQL_CREATE_TABLE_QUERY = f"""
CREATE TABLE IF NOT EXISTS pages (
    ID int,
    URL varchar(2000),
    title varchar(255),
    description varchar(255),
    text varchar({MAX_PAGE_TEXT_LENGTH}),
    domain varchar(255),
    IP varchar(255),
    PRIMARY KEY (ID)
);
"""