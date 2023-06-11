Video de apresentação do programa:
    https://youtu.be/yXJDQYMBlew

Bibliotecas necessárias:
    tkinter
    sys
    pathlib
    sqlite3

Descrição do Projeto:

    Nós desenvolvemos uma solução para a regra de negócio pré-estabelecida, que consiste em fornecer um controle de perfis de acesso visando a segurança e a prevenção de fraudes.
    Um diferencial que acreditamos ter em nosso sistema, e que vocês verão com mais detalhes ao falarmos sobre a arquitetura, é a capacidade de registrar perfis de um único sistema na matriz de perfis. Diferentemente de outras abordagens, o nosso sistema não requer o cadastro de mais de um sistema para registrar perfis na matriz, oferecendo flexibilidade e adaptabilidade aos requisitos de cada cenário.
    
    Adotamos o padrão MVC (Model-View-Controller), amplamente utilizado no desenvolvimento de aplicações web. Esse padrão divide a aplicação em três componentes principais: Model, View e Controller.

    No nosso projeto, a lógica de negócio foi implementada principalmente no Controller, que desempenha um papel central no sistema. Ele é responsável por receber as requisições do usuário, validar os dados inseridos e direcionar as informações corretas para o Model. O Controller também realiza a interação com a lógica da matriz SoD, garantindo o controle adequado da permissão de dois perfis para um mesmo usuário.
    O Model, por sua vez, concentra-se na manipulação dos dados e na comunicação com o banco de dados relacional. Ele inclui as classes que representam as entidades principais do sistema, como Sistemas, Perfis, Matriz SoD, Usuários e Usuários-Perfis. O Model é responsável por realizar operações de consulta, inserção, atualização e exclusão no banco de dados, de acordo com as necessidades da aplicação.
    Essa abordagem, em que a lógica de negócio é distribuída entre o Controller e o Model, proporciona uma separação clara de responsabilidades e promove a reutilização de código. O Controller gerencia as interações do usuário e coordena as ações necessárias, enquanto o Model lida com a persistência dos dados e as operações de banco de dados.

    Além da arquitetura MVC e da divisão de responsabilidades entre o Controller e o Model, nosso sistema utiliza o SQLite como banco de dados relacional para armazenar e buscar as informações. A escolha pelo SQLite foi motivada pela sua facilidade de integração com o projeto em Python e pelo fato de ser um banco de dados embutido, dispensando a necessidade de um servidor separado.
    Com uma arquitetura sólida e uma distribuição adequada da lógica de negócio, nosso sistema oferece uma solução eficiente e segura para o controle de perfis de acesso e prevenção de fraudes. 
    
    A parte principal da regra de negócio foi garantir que um determinado usuário não possa ter a permissão de dois perfis cadastrados na MatrizSoD. Essa foi a nossa principal preocupação e desafio durante o desenvolvimento do sistema. Para resolver essa questão, implementamos uma lógica específica no Controller.    
    Quando há a tentavida de cadastro de um segundo perfil para um determinado usuário, o sistema concatena o código desse perfil com cada código previamente cadastrado para aquele usuário e realiza uma busca na tabela da MatrizSoD. Caso haja algum registro correspondente, a ação de cadastrar o segundo perfil é bloqueada, evitando assim a violação das restrições impostas pela MatrizSoD.
    Essa lógica de verificação da permissão de dois perfis para um mesmo usuário é fundamental para garantir a segurança e a consistência do sistema. Ao implementar essa funcionalidade, pudemos assegurar que cada usuário tenha apenas um perfil registrado na MatrizSoD, evitando assim possíveis brechas de segurança.

    Vale ressaltar que consideramos implementar um registro dessas tentativas de cadastro para uma possível auditoria interna. Embora essa implementação seja viável, decidimos priorizar nosso foco nas requisições da regra de negócio e deixar a funcionalidade de registro para uma etapa futura do projeto.
    Com essa solução implementada, estamos confiantes de que o nosso sistema atende às necessidades de controle de perfis de acesso e prevenção de fraudes de forma eficaz.

    Um dos aspectos-chave do nosso sistema é a lógica da matriz e sua flexibilidade na validação dos perfis de acesso. Essa lógica é implementada no método valida_matriz_sod do arquivo usuario_perfil_controller.py.
    A matriz de separação de deveres (SoD - Separation of Duties) é uma técnica utilizada para evitar possíveis fraudes ou conflitos de interesse, garantindo que determinados perfis não sejam atribuídos ao mesmo usuário. No nosso sistema, essa lógica é aplicada para evitar a permissão de dois perfis para um mesmo usuário, desde que esses perfis estejam previamente cadastrados na MatrizSoD.
    No método valida_matriz_sod, realizamos uma série de verificações para determinar se o perfil pode ser adicionado ou alterado para um usuário específico. Vamos analisar brevemente a lógica por trás disso:

        1 - Primeiramente, buscamos todos os usuários-perfis relacionados ao usuário em questão e todas as matrizes SoD cadastradas.

        2 - Em seguida, verificamos se existem registros tanto na lista de usuários-perfis quanto na lista de matrizes SoD. Essa verificação é importante para garantir que as consultas tenham retornado resultados válidos.

        3 - Caso existam registros nas duas listas, prosseguimos com a validação da matriz SoD. Se o método for de alteração e houver apenas um perfil associado ao usuário, a validação é ignorada, permitindo a alteração.

        4 - Caso contrário, concatenamos o código do perfil atual com cada código de perfil previamente cadastrado para o usuário. Em seguida, geramos uma matriz no formato perfil1_perfil2 ou perfil2_perfil1, dependendo da ordem dos perfis.

        5 - Iteramos sobre as matrizes SoD buscadas e verificamos se alguma delas corresponde à matriz gerada. Se encontrarmos uma correspondência, significa que há uma restrição na matriz SoD que proíbe a associação desses dois perfis ao mesmo usuário.

        6 - Se encontrarmos uma matriz correspondente, retornamos um resultado de sucesso com uma mensagem indicando a detecção da MatrizSoD.

        7 - Caso contrário, retornamos um resultado de falha, indicando que a validação foi bem-sucedida e que o perfil pode ser adicionado ou alterado.

    Essa lógica de validação da matriz SoD é fundamental para garantir a segurança e a integridade do sistema. Ao implementar essa lógica no controlador de usuários-perfis, podemos evitar conflitos e violações das restrições impostas pela MatrizSoD, fornecendo um controle efetivo dos perfis de acesso.        

    A flexibilidade da matriz reside no fato de que ela pode ser configurada e atualizada conforme as necessidades específicas do sistema. Os perfis e as restrições da matriz SoD podem ser definidos de acordo com as políticas de segurança e os requisitos da organização. Isso permite uma adaptação fácil do sistema a diferentes cenários e requisitos específicos de cada cliente.
    Com a lógica da matriz e sua flexibilidade, o nosso sistema oferece um controle robusto e personalizável dos perfis de acesso, garantindo a segurança e a prevenção de fraudes em diversos contextos organizacionais.

Estrutura do Banco de Dados:

BANCO: 
    matriz_sod

TABELAS:
    SISTEMAS
        codigo INTEGER PRIMARY KEY,
        nome VARCHAR(40) NOT NULL COLLATE NOCASE,
        UNIQUE (nome)

    PERFIS
        codigo INTEGER PRIMARY KEY,
        nome VARCHAR(40) NOT NULL,
        descricao VARCHAR(100),
        cod_sistema INTEGER NOT NULL,
        UNIQUE (cod_sistema, nome),
        FOREIGN KEY(cod_sistema) REFERENCES sistemas(codigo) ON DELETE CASCADE

    MATRIZ_SOD
        codigo INTEGER PRIMARY KEY,
        cod_perfil1 INTEGER NOT NULL,
        cod_perfil2 INTEGER NOT NULL,
        concat INTEGER NOT NULL,
        UNIQUE (concat),
        FOREIGN KEY(cod_perfil1) REFERENCES perfis(codigo) ON DELETE CASCADE,
        FOREIGN KEY(cod_perfil2) REFERENCES perfis(codigo) ON DELETE CASCADE

    USUARIOS
        codigo INTEGER PRIMARY KEY,
        nome VARCHAR(40) NOT NULL,
        cpf VARCHAR(11) NOT NULL,
        UNIQUE (cpf)

    USUARIOS_PERFIS
        codigo INTEGER PRIMARY KEY,
        cod_usuario INTEGER NOT NULL,
        cod_perfil INTEGER NOT NULL,
        UNIQUE (cod_usuario, cod_perfil),
        FOREIGN KEY(cod_usuario) REFERENCES usuarios(codigo) ON DELETE CASCADE,
        FOREIGN KEY(cod_perfil) REFERENCES perfis(codigo) ON DELETE CASCADE            


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