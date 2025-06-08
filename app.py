from flask import Flask, render_template_string
import psycopg2
import pandas as pd
import os

app = Flask(__name__)

def get_data():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432"),
        dbname=os.getenv("DB_NAME", "cropwise_database"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "123")
    )
    query = "SELECT * FROM trial_report"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

@app.route("/")
def home():
    df = get_data()
    html_table = df.to_html(index=False, border=1)
    html_template = f"""
    <html>
        <head>
            <meta charset="UTF-8">
            <title>Cropwise Report</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }}
                table {{
                    border-collapse: collapse;
                    width: 100%;
                    table-layout: fixed;
                }}
                th, td {{
                    border: 1px solid #ccc;
                    padding: 8px;
                    text-align: left;
                    font-size: 14px;
                }}
                th {{
                    background-color: #f0f0f0;
                    font-weight: bold;
                }}
            </style>
            <script>
                function refreshTable() {{
                    fetch("/table")
                        .then(response => response.text())
                        .then(html => {{
                            document.getElementById("live-table").innerHTML = html;
                        }});
                }}
                setInterval(refreshTable, 30000); // обновление каждые 30 сек
                window.onload = refreshTable;
            </script>
        </head>
        <body>
            <h2>Cropwise Report: trial_report</h2>
            <div id="live-table">{html_table}</div>
        </body>
    </html>
    """
    return render_template_string(html_template)

@app.route("/table")
def get_table_only():
    df = get_data()
    return df.to_html(index=False, border=1)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
