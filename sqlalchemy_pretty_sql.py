# -*- coding: utf-8 -*-
import sqlparse
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from IPython.display import display, HTML


def pretty_sql(query):
    engine = query.session.get_bind()
    dialect = type(engine.dialect).__name__.lower()

    sql = str(query.statement.compile(dialect=engine.dialect))
    formatted_sql = sqlparse.format(sql, reindent=True, keyword_case="upper")

    if dialect.startswith("mysql"):
        lexer = get_lexer_by_name("mysql")
    elif dialect.startswith("pg"):
        lexer = get_lexer_by_name("postgres")
    else:
        lexer = get_lexer_by_name("sql")

    formatter = HtmlFormatter()
    pygments_css = formatter.get_style_defs(".highlight")

    display(
        HTML(
            f"""
            <style>
            {pygments_css}
            </style>
            """
        )
    )
    display(HTML(highlight(formatted_sql, lexer, formatter)))
