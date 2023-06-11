Video de apresentação do programa:
https://youtu.be/yXJDQYMBlew

BANCO: 
    matriz_sod

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

    MATRIZ_SOD
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


Possíveis simulações para cadastro na MatrizSoD

Não permita que o mesmo usuário tenha acesso à:

1. Módulo Financeiro:

    Emissão de Pagamentos e Aprovação de Pagamentos.
    Cadastro de Fornecedores e à Alteração de Informações Bancárias.

2. Módulo de Vendas:

    Emissão de Pedidos e à Aprovação de Pedidos.
    Cadastro de Clientes e à Alteração de Preços.
    
3.  Módulo de Estoque:

    Recebimento de Mercadorias e à Saída de Mercadorias.
    Cadastro de Produtos e ao Ajuste de Estoque.

4. Módulo de Recursos Humanos:

    Cadastro de Funcionários e à Alteração de Salários.
    Folha de Pagamento e à Alteração de Benefícios.