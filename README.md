# EasierClass

## Descrição
O EasierClass é um aplicativo de auxílio à ministração de disciplinas no regime EAD, semi-presencial ou remotas onde professor e alunos podem se comunicar entre si, elaborar e responder atividades, além de estimular o engajamento por parte dos alunos através de técnicas de gamificação baseadas em experiência de usuário.

## Justificativa
O engajamento de alunos na modalidade EAD nem sempre é algo plenamente mensurável, e ferramentas que auxiliem nessa proposta tendem a ajudar cada vez mais a educação. Com o aumento do número de casos onde aulas presicam ser transmitidas de forma remota ou semi-presencial, faz-se necessária uma aplicação capaz de trazer uma solução moderna, de fácil utilização e que consiga aumentar engajamento dos usuários, melhorando o resultado geral de um processo de aprendizado.

## Fundamentação teórica
Formas inovadores de ensinar têm sido discutidas a partir da popularização das tecnologias, capazes de proporcionar flexibilidade relativas ao tempo e ao formato desses métodos de ensino. A aprendizagem de qualidade constitui um desafio, sendo que a motivação e o engajamento dos alunos são tópicos que merecem atenção. O relacionamento entre gamificação e engajamento tem sido um tópico constantemente pesquisado. 
O engajamento em nível superficial através da gamificação pode ser alcançado através de vídeos bem humorados, recompensas e rankings, mas com o planejamento ideal e uma boa forma de apresentar isso ao usuário, o engajamento pode ser sustentado a longo prazo, até que se torne um hábito fazer as atividades que contribuam para o desenvolvimento educacional do aluno. Diversos estudos mostram que o nível de engajamento da modalidade EAD ainda é baixo.

## Objetivos Gerais
O trabalho tem como principal objetivo fornecer uma plataforma de fácil uso e que estimule os alunos e professores a utilizá-la através de conteúdos gamificados.

## Objetivos Específicos
O trabalho tem como objetivos específicos a criação de uma plataforma de estudos, utilizando a metodologia de gamificação do usuário, para facilitar a aprendizagem e a interação professor-aluno.

## Metodologia de execução
O projeto deve executar de forma linear e intuitiva, o usuário seja professor ou aluno deve realizar um login no sistema - caso tenha já realizado o cadastro - informando nome do usuário e senha.Logo após essa ação, o mesmo será redirecionado para uma aba de escolha da sala na qual deseja ver as postagem, se for um professor será capaz de cadastrar novas salas , e se for um aluno será capaz de entrar em uma sala. Dentro da sala escolhida as funções serão especificas para cada tipo de usuário, ao professor será dada as ações: cadastrar atividade, cadastrar assunto e ver desempenho da sala. Ao aluno, será possível , responder as questões postadas por um professor e ver seu rendimento na matéria. Ambos terão funções idênticas de ver o calendário com as atividades para cada dia, fazer postagens com ou sem anexos e ver suas conquistas pessoais.

## Resultados Esperados e Disseminação dos Resultados
Com esse projeto, espera-se desenvolver uma plataforma intuitiva e com boas ferramentas de gamificação para aumentar o engajamento de modalidades remotas de aprendizado. A plataforma poderá ser utilizada por faculdades, escolas ou qualquer instituição de ensino que necessite de uma comunicação aluno-professor em modalidade de turmas.

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

## Telas de protótipo

# Login
![Login](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_login.jpeg)

# Calendario
![Calendario](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_Calendario.jpeg)

# Nova postagem
![Nova Postagem](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_nova_postagem.jpeg)

# Post
![Post](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_post.jpeg)

# Salas - visão professor
![Visão Professor](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_prof_salas.jpeg)

# Salas - visão aluno
![Visão Aluno](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_alunos_salas.jpeg)

# Timeline Aluno
![Timeline Aluno](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_timeline.jpeg)

# Timeline Professor
![Timeline Professor](https://github.com/magnoazneto/easierclass/blob/master/files/EasierClass_timeline.jpeg)

## Referências
- FREIRE, C. D. C. (2015). Gamificaçao e ead: Importância e possibilidades para uma educaçao com foco no aluno. Trabalho de Final de Curso. Instituto de Matemática e Estatıstica. LANTE–Laboratório de Novas Tecnologias de Ensino. Universidade Federal Fluminense (RJ).

- Sanches, L. R. J., Dos Santos, A. C., & Hardagh, C. C. (2018). A GAMIFICAÇÃO COMO FERRAMENTA NA CRIAÇÃO DE OBJETOS DE APRENDIZAGEM EAD. CIET: EnPED.

- http://www.scielo.mec.pt/scielo.php?script=sci_arttext&pid=S2182-13722019000200003&lang=pt

- https://blog.elos.vc/7-dicas-para-engajar-seus-alunos-atraves-da-gamificacao/amp/

- https://viddia.com.br/gamificacao-engajamento-ead/
