# EasierClass

## Descrição
O EasierClass é um aplicativo de auxílio à ministração de disciplinas no regime EAD, semi-presencial ou remotas onde professor e alunos podem se comunicar entre si, elaborar e responder atividades, além de estimular o engajamento por parte dos alunos através de técnicas de gamificação baseadas em experiência de usuário.

## Público alvo
Alunos e professores usuários de plataformas para aulas a distância.

## Problema a ser resolvido
Aumentar o engajamento em aulas online, através de um sistema de notificações inteligentes, interação com outros alunos e gamificação da plataforma.

## Funcionalidades básicas que o projeto deve contemplar
- Feed de atividades;
- Criação de salas para agrupamento de estudantes;
- Lembretes em formas de notificações personalizadas;
- Criação de atividades por parte dos professores;
- Possibilidade de anexar resposta por parte dos alunos;
- Ranking comparativo de desempenho dos estudantes baseado na pontuação do app;
- Alocação de títulos baseados no uso de funcionalidades do app de determinadas formas (achievements);

## Casos de uso
![Casos de uso](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_UseCases.png)

Até o dia 06/09/2020 dois atores foram identificados para o sistema, sendo eles Professor e Aluno. Para cada ator foram identificados os casos de uso listados abaixo:

# Professor:
1. Verificar suas conquistas dentro do portal:
    O professor poderá visualizar suas conquistas referêntes a prazos, métricas gerais de uso do app e comprometimento com as disciplinas em forma de achievements (conquistas).
2. Criar salas no portal:
    O professor deve ser capaz de criar um ambiente virtual chamado de "sala", para então, conseguir agrupar usuários do tipo 'Aluno' dentro de salas separadas.
3. Visualizar posts por turma:
    Nas telas de navegação, o professor deve ser capaz de ter uma view separada para cada uma de suas turmas, facilitando o agrupamento de posts por cada uma delas.
4. Realizar posts no portal:
    O professor deve ser capaz de criar posts, sendo eles de natureza puramente informativa ou em forma de atividade com atribuição de pontos relacionados a entrega.
5. Atribuir notas a atividades:
    Dentro da categoria de posts, se um deles for uma atividade com uma pontuação cadastrada pelo professor no momento da criação, ele também poderá atribuir uma nota a cada aluno que tenha realizado a entrega daquela atividade.
6. Gerenciar alunos das salas no portal:
    Mesmo com as salas criadas, o professor deve ser capaz de excluir, inserir novos membros, ou definir permissões de postagens para alunos participantes das salas criadas por aquele professor.

# Aluno:
1. Verificar suas conquistas dentro do portal:
    O aluno poderá visualizar suas conquistas referêntes a prazos, métricas gerais de uso do app e comprometimento com as disciplinas em forma de achievements (conquistas), como forma de aumentar o engajamento e promover uma espécie de gamificação na experiência de usuário.
2. Visualizar posts por turma:
    Nas telas de navegação, o aluno deve ser capaz de ter uma view separada para cada uma das turmas em que está cadastrado, facilitando o agrupamento de posts por cada uma delas e organização de prazos por parte do aluno.
3. Realizar download de arquivos anexados aos posts:
    O aluno deve ser capaz de visualizar arquivos disponibilizados pelo professor ou por outros alunos com permissão de post, e realizar o download local destes arquivos.
4. Acessar feed geral com posts ordenados por data:
    O aluno deve ser capaz de acessar uma view geral, onde cada post será mostrado por ordem cronológica de inclusão por parte do professor.
5. Visualizar tarefas por calendário:
    O aluno deve ser capaz de visualizar as atividades pendentes por ordem de data.
6. Se inscrever em salas criadas por professores:
    O aluno deve ser capaz de, com um link ou código de acesso fornecido pelo professor, entrar nas salas criadas para participar das atividades daquela turma.


