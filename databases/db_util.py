"""A collection of database utility methods."""


def setup_table(cursor, table_name, data, **options):
    """Create table table_name and add data to columns.

    options represents columns and the respective data type, e.g.
    Age="INT"
    """
    cursor.execute("DROP TABLE IF EXISTS " + table_name)
    options = options.items()
    sql_statement = "CREATE TABLE " + table_name + "("
    for index, columns in enumerate(options):
        if columns == options[-1]:
            sql_statement += columns[0] + " " + columns[1].upper()
        else:
            sql_statement += columns[0] + " " + columns[1] + ", "
    sql_statement += ")"
    print sql_statement
    cursor.execute(sql_statement)
    cursor.executemany(
        "INSERT INTO " + table_name + " VALUES(?, ?, ?)", data)
    return cursor.lastrowid
