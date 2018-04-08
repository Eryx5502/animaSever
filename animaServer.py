from api import create_app
from api.database import (db, Arma, Armadura, Hechizo, Objeto,
                          PoderPsiquico, Ventaja)

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {'db': db,
            'Arma': Arma,
            'Armadura': Armadura,
            'Hechizo': Hechizo,
            'Objeto': Objeto,
            "PoderPsiquico": PoderPsiquico,
            "Ventaja": Ventaja}


# if __name__ == '__main__':
#     app.run(debug=True)
