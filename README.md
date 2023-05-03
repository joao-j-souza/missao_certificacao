BANCO: 
    matriz_sod

FUNÇÕES SQL:
    # UNIQUE_PERFIS retorna a concatenação entre perfil1 e perfil2, normalizando por ordem crescente e acrescentado o símbolo de underline entre os valores.
    unique_perfis(a INT, b INT) RETURNS TEXT
                AS 
                '''
                return f"{min(a, b)}_{max(a, b)}"
                '''

Matriz
TABELAS:
    SISTEMAS
        codigo INTEGER NOT NULL AUTOINCREMENT,
        nome VARCHAR(40) UNIQUE NOT NULL,
        PRIMARY KEY(codigo)

    PERFIS
        codigo INTEGER NOT NULL AUTOINCREMENT,
        nome VARCHAR(40) NOT NULL
        descricao VARCHAR(100)
        cod_sistema INTEGER NOT NULL
        UNIQUE unique_sistema (cod_sistema, nome)
        PRIMARY KEY(codigo)
        FOREIGN KEY(cod_sistema) REFERENCES sistemas(codigo)

    MATRIZ_SoD
        codigo INTEGER NOT NULL AUTOINCREMENT
        cod_perfil1 INTEGER NOT NULL
        cod_perfil2 INTEGER NOT NULL
        UNIQUE unique_perfis (unique_perfis(cod_perfil1, cod_perfil2))
        PRIMARY KEY(codigo)
        FOREIGN KEY(cod_perfil1) REFERENCES perfis(codigo)
        FOREIGN KEY(cod_perfil2) REFERENCES perfis(codigo)

    USUARIOS
        codigo INTEGER NOT NULL AUTOINCREMENT
        cpf VARCHAR(11) UNIQUE NOT NULL
        cod_perfil INTEGER NOT NULL
        UNIQUE unique_perfil (cpf, cod_perfil)
        PRIMARY KEY(codigo)
        FOREIGN KEY(cod_perfil) REFERENCES perfis(codigo)

