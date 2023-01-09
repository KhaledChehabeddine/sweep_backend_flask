from flask import Flask

app = Flask(__name__)


def wrap_html(message: str) -> str:
    return """
        <html>
            <body>
                <div style='font-size:120px;'>
                    <center>
                        <br>
                        {0}
                        <br>
                    </center>
                </div>
            </body>
        </html>""".format(message)


@app.route('/')
def hello_world() -> str:
    return wrap_html("Welcome to Sweep!")


if __name__ == '__main__':
    app.run()
