# GS2026.1_PCAP

O software foi desenvolvido com o objetivo de auxiliar uma missão espacial em seu decorrer, garantindo o registro de dados e análise de risco em tempo real.


O sistema simula níveis de 5 áreas: temperatura, comunicação, energia, oxigênio e estabilidade operacional de um veículo espacial em seus 6 principais ciclos: Lançamento, Ascenção, Inserção Orbital, Operação Espacial e Retorno ou Desativação.

São considerados apenas valores que permitam uma missão completa, não considerando valores que causem fracasso inevitável. Além disso, foram estabelecidos valores mínimos e máximos plausíveis para cada ciclo.


O sistema analisa o nível de cada área categorizando como Normal, Atenção ou Critico. A partir dessa análise é calculado o nível de criticidade do ciclo, e são emitidos alertas condizentes com o estado atual.


Ao final da missão é gerado um relatório contendo:

Análise de ciclos: quantidade de ciclos analisados, quantidade de ciclo críticos, ciclo mais crítico e tendência da missão. Essa análise seria importante para um programa espacial pois a partir dela é possível estimar a saúde geral do sistema.


Análise por área: pontuações médias de risco de temperatura, comunicação, energia, oxigênio e estabilidade. É dada também a área que foi mais afetada, e sua pontuação. Essa análise é importante para que a equipe direcione os esforços aos pontos que demandaram maior atenção durante a missão.


Em seguida, o relatório apresenta uma matriz contendo a pontuação das áreas em cada ciclo, oferecendo um panorama completo da missão.

Por fim, o sistema classifica a missão como estável, alerta ou critica, e emite a conclusão do relatório.
