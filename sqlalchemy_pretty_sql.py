# -*- coding: utf-8 -*-
import sqlparse
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter, Terminal256Formatter
from IPython import get_ipython
from IPython.display import display, HTML


def pretty_term(query, *args):
    pretty_sql(query, formatter="terminal")


def pretty_sql(query, formatter="html"):
    engine = query.session.get_bind()
    dialect = type(engine.dialect).__name__.lower()

    sql = str(query.statement.compile(dialect=engine.dialect, compile_kwargs={"literal_binds": True}))
    formatted_sql = sqlparse.format(sql, reindent=True, keyword_case="upper")

    if dialect.startswith("mysql"):
        lexer = get_lexer_by_name("mysql")
    elif dialect.startswith("pg"):
        lexer = get_lexer_by_name("postgres")
    else:
        lexer = get_lexer_by_name("sql")

    if formatter == "html":
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
    elif formatter == "terminal":
        formatter = Terminal256Formatter()
        print(highlight(formatted_sql, lexer, formatter))


html_formatter = get_ipython().display_formatter.formatters['text/html']
html_formatter.for_type_by_name('sqlalchemy.orm.query', 'Query', pretty_sql)

plain_formatter = get_ipython().display_formatter.formatters['text/plain']
plain_formatter.for_type_by_name('sqlalchemy.orm.query', 'Query', pretty_term)


