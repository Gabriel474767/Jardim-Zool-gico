'''
Jardim Zoológico do Garminho
'''
import random
import pickle
import os
animais = {}

print(''' ░░░░░██╗░█████╗░██████╗░██████╗░██╗███╗░░░███╗
          ░░░░░██║██╔══██╗██╔══██╗██╔══██╗██║████╗░████║
          ░░░░░██║███████║██████╔╝██║░░██║██║██╔████╔██║
          ██╗░░██║██╔══██║██╔══██╗██║░░██║██║██║╚██╔╝██║
          ╚█████╔╝██║░░██║██║░░██║██████╔╝██║██║░╚═╝░██║
          ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝╚═╝░░░░░╚═╝

        ███████╗░█████╗░░█████╗░██╗░░░░░░█████╗░░██████╗░██╗░█████╗░░█████╗░  ██████╗░░█████╗░
        ╚════██║██╔══██╗██╔══██╗██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗
        ░░███╔═╝██║░░██║██║░░██║██║░░░░░██║░░██║██║░░██╗░██║██║░░╚═╝██║░░██║  ██║░░██║██║░░██║
        ██╔══╝░░██║░░██║██║░░██║██║░░░░░██║░░██║██║░░╚██╗██║██║░░██╗██║░░██║  ██║░░██║██║░░██║
        ███████╗╚█████╔╝╚█████╔╝███████╗╚█████╔╝╚██████╔╝██║╚█████╔╝╚█████╔╝  ██████╔╝╚█████╔╝
        ╚══════╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░╚════╝░░╚════╝░  ╚═════╝░░╚════╝░

        ░██████╗░░█████╗░██████╗░███╗░░░███╗██╗███╗░░██╗██╗░░██╗░█████╗░
        ██╔════╝░██╔══██╗██╔══██╗████╗░████║██║████╗░██║██║░░██║██╔══██╗
        ██║░░██╗░███████║██████╔╝██╔████╔██║██║██╔██╗██║███████║██║░░██║
        ██║░░╚██╗██╔══██║██╔══██╗██║╚██╔╝██║██║██║╚████║██╔══██║██║░░██║
        ╚██████╔╝██║░░██║██║░░██║██║░╚═╝░██║██║██║░╚███║██║░░██║╚█████╔╝
        ░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚════╝░''')


# Menu Principal da Loja
def menu_geral():
    print('-'*10 + 'Menu' + '-'*10)
    print('1 - Espécimes Existentes no Zoológico')
    print('2 - Horários de Funcionamento')
    print('3 - Quizzes Educativos')
    print('4 - Consulta')
    print('0 - Sair')
    print('-'*26)

# Menus de Espécimes(Mamíferos,Aves,Répteis,Anfíbios,Peixes,Vida Marinha(Excluindo Peixes),Invertebrados)

def menu_especimes():
    print('-'*10 + 'Espécimes' + '-'*10)
    print('1 - Mamíferos')
    print('2 - Aves')
    print('3 - Répteis')
    print('4 - Anfíbios')
    print('5 - Peixes')
    print('6 - Vida Marinha')
    print('7 - Invertebrados')
    print('0 - Voltar ao Menu Principal')
    print('-'*29)

def menu_mamiferos():
    print('-'*10 + 'Mamíferos' + '-'*10)
    print('1 - Leão')
    print('2 - Elefante')
    print('3 - Cão')
    print('4 - Gato')
    print('5 - Baleia')
    print('6 - Morcego')
    print('0 - Voltar ao Menu Principal')
    print('-'*29)

def menu_aves():
    print('-'*10 + 'Aves' + '-'*10)
    print('1 - Águia')
    print('2 - Pinguim')
    print('3 - Papagaio')
    print('4 - Corvo')
    print('5 - Pavão')
    print('6 - Flamingo')
    print('0 - Voltar ao Menu Principal')
    print('-'*24)

def menu_repteis():
    print('-'*10 + 'Répteis' + '-'*10)
    print('1 - Crocodilo')
    print('2 - Lagarto')
    print('3 - Tartaruga')
    print('4 - Cobra')
    print('5 - Iguana')
    print('6 - Camaleão')
    print('0 - Voltar ao Menu Principal')
    print('-'*27)

def menu_anfibios():
    print('-'*10 + 'Anfíbios' + '-'*10)
    print('1 - Sapo')
    print('2 - Rã')
    print('3 - Salamandra')
    print('4 - Tritão')
    print('5 - Perereca')
    print('6 - Cecília')
    print('0 - Voltar ao Menu Principal')
    print('-'*28)

def menu_peixes():
    print('-'*10 + 'Peixes' + '-'*10)
    print('1 - Tubarão')
    print('2 - Salmão')
    print('3 - Atum')
    print('4 - Tilápia')
    print('5 - Dourada')
    print('6 - Cavala')
    print('0 - Voltar ao Menu Principal')
    print('-'*26)

def menu_vida_marinha():
    print('-'*10 + 'Vida Marinha' + '-'*10)
    print('1 - Polvo')
    print('2 - Lula')
    print('3 - Estrela-do-mar')
    print('4 - Alforreca')
    print('5 - Caranguejo')
    print('6 - Coral')
    print('0 - Voltar ao Menu Principal')
    print('-'*50)

def menu_invertebrados():
    print('-'*10 + 'Invertebrados' + '-'*10)
    print('1 - Borboleta')
    print('2 - Formiga')
    print('3 - Caracol')
    print('4 - Escaravelho')
    print('5 - Aranha')
    print('6 - Minhoca')
    print('0 - Sair')
    print('-'*33)

# Menus dos Horários em Diferentes Épocas(Primavera,Verão,Outono,Inverno)
def menu_horario():
    print('-'*10 + 'Horários de Funcionamento' + '-'*10)
    print('1 - Primavera')
    print('2 - Verão')
    print('3 - Outono')
    print('4 - Inverno')
    print('0 - Voltar ao Menu Principal')
    print('-'*32)

def menu_primavera():
    print('-'*10 + 'Horários de Primavera' + '-'*10)
    print('1 - Segunda-Feira - 07:00h-19:00h')
    print('2 - Terça-Feira - 07:00h-19:00h')
    print('3 - Quarta-Feira - 07:00h-16:00h')
    print('4 - Quinta-Feira - 07:00h-19:00h')
    print('5 - Sexta-Feira - 07:00h-19:00h')
    print('6 - Sábado - 07:00h-18:00h')
    print('7 - Domingo - Fechado')
    print('0 - Voltar ao Menu Principal')
    print('-'*41)

def menu_verao():
    print('-'*10 + 'Horários de Verão' + '-'*10)
    print('1 - Segunda-Feira - 08:00h-19:00h')
    print('2 - Terça-Feira - 08:00h-19:00h')
    print('3 - Quarta-Feira - 08:00h-16:00h')
    print('4 - Quinta-Feira - 08:00h-19:00h')
    print('5 - Sexta-Feira - 08:00h-19:00h')
    print('6 - Sábado - 08:00h-18:00h')
    print('7 - Domingo - Fechada')
    print('0 - Voltar ao Menu Principal')
    print('-'*37)

def menu_outono():
    print('-'*10 + 'Horários de Outono' + '-'*10)
    print('1 - Segunda-Feira - 08:00h-19:00h')
    print('2 - Terça-Feira - 08:00h-19:00h')
    print('3 - Quarta-Feira - 08:00h-19:00h')
    print('4 - Quinta-Feira - 08:00h-19:00h')
    print('5 - Sexta-Feira - 08:00h-19:00h')
    print('6 - Sábado - Fechado')
    print('7 - Domingo - 08:00h-18:00h')
    print('0 - Voltar ao Menu Principal')
    print('-'*38)

def menu_inverno():
    print('-'*10 + 'Horários de Inverno' + '-'*10)
    print('1 - Segunda-Feira - 08:00h-19:00h')
    print('2 - Terça-Feira - 08:00h-19:00h')
    print('3 - Quarta-Feira - 08:00h-19:00h')
    print('4 - Quinta-Feira - 08:00h-19:00h')
    print('5 - Sexta-Feira - 08:00h-19:00h')
    print('6 - Sábado - Fechado')
    print('7 - Domingo - Fechado')
    print('0 - Voltar ao Menu Principal')
    print('-'*39)
    
# Criar Ficheiro Binário
def criar_ficheiro_binário():
    global animais
    # Estrutura de Dados Dinâmica
    animais = {
        'Espécimes': {
            'Mamiferos': {
                'Leão': {
                    'Nome Científico e Classificação Taxonômica':['Panthera leo', 'Família: Felidae', 'Ordem: Carnivora.'],
                        'Habitat e Distribuição Geográfica':['Savanas da África Subsaariana.'],
                        'Dieta e Hábitos Alimentares':['Carnívoro, caça grandes herbívoros em grupo.'],
                        'Comportamento Social':['Vivem em grupos sociais chamados de "coalizões".'],
                        'Ciclo de Vida e Reprodução':['Gestação de cerca de 110 dias, fêmeas cuidam dos filhotes.'],
                        'Adaptações Fisiológicas e Comportamentais':['Força física, mandíbulas poderosas, excelente visão e audição.'],
                        'Papel no Ecossistema':['Topo da cadeia alimentar, essencial para o equilíbrio dos ecossistemas.'],
                        'Estado de Conservação':['Vulnerável, devido à perda de habitat e caça ilegal.']},
                'Elefante': {
                    'Nome Científico e Classificação Taxonômica':['Loxodonta africana (Elefante africano) ou Elephas maximus (Elefante asiático)', 'Família: Elephantidae', 'Ordem: Proboscidea.'],
                        'Habitat e Distribuição Geográfica':['Diversos habitats, desde florestas tropicais a desertos, África e Ásia.'],
                        'Dieta e Hábitos Alimentares':['Herbívoro, consome grandes quantidades de vegetação.'],
                        'Comportamento Social':['Vivem em grupos matriarcais altamente organizados.'],
                        'Ciclo de Vida e Reprodução':['Gestação de 18 a 22 meses, os filhotes são cuidados por toda a manada.'],
                        'Adaptações Fisiológicas e Comportamentais':['Probóscide para alimentação e manipulação de objetos, excelente memória.'],
                        'Papel no Ecossistema':['Desempenham um papel fundamental na abertura de clareiras nas florestas e na dispersão de sementes.'],
                        'Estado de Conservação':['Em perigo de extinção devido à caça ilegal e perda de habitat.']},
                'Cão': {
                    'Nome Científico e Classificação Taxonômica':['Canis lupus familiaris', 'Família: Canidae', 'Ordem: Carnivora.'],
                        'Habitat e Distribuição Geográfica':['Presente em todos os continentes, geralmente associado a habitats modificados pelo homem.'],
                        'Dieta e Hábitos Alimentares':['Carnívoro, com variações na dieta dependendo da domesticação.'],
                        'Comportamento Social':['Altamente sociáveis, têm comportamento de matilha.'],
                        'Ciclo de Vida e Reprodução':['Gestação de cerca de 2 meses, filhotes nascem cegos e surdos.'],
                        'Adaptações Fisiológicas e Comportamentais':['Olfato e audição altamente desenvolvidos, adaptados à vida em grupo e ao convívio com humanos.'],
                        'Papel no Ecossistema':['Doméstico, mas pode desempenhar papéis de caça e guarda em certas comunidades humanas.'],
                        'Estado de Conservação':['Não aplicável, pois é uma espécie domesticada.']},
                'Gato': {
                    'Nome Científico e Classificação Taxonômica':['Felis catus', 'Família: Felidae', 'Ordem: Carnivora.'],
                        'Habitat e Distribuição Geográfica':['Doméstico, mas originário de regiões selvagens, atualmente global.'],
                        'Dieta e Hábitos Alimentares':['Carnívoro, consome pequenos animais como presas.'],
                        'Comportamento Social':['Solitário, mas capaz de viver em grupos sociais em determinadas condições.'],
                        'Ciclo de Vida e Reprodução':['Gestação de cerca de 2 meses, filhotes nascem cegos e dependentes.'],
                        'Adaptações Fisiológicas e Comportamentais':['Agilidade, visão noturna e audição aguçada.'],
                        'Papel no Ecossistema':['Doméstico, mas pode controlar populações de roedores em áreas urbanas.'],
                        'Estado de Conservação':['Não aplicável, pois é uma espécie domesticada.']},
                'Baleia': {
                    'Nome Científico e Classificação Taxonômica':['Várias espécies, como a baleia-azul (Balaenoptera musculus)', 'Família: Balaenopteridae', 'Ordem: Cetacea.'],
                        'Habitat e Distribuição Geográfica':['Oceanos de todo o mundo, em diferentes profundidades e latitudes.'],
                        'Dieta e Hábitos Alimentares':['Principalmente planctívora, algumas espécies consomem krill, peixes e lulas.'],
                        'Comportamento Social':['Podem ser solitárias ou viver em grupos, dependendo da espécie.'],
                        'Ciclo de Vida e Reprodução':['Gestação de 10 a 18 meses, cuidado materno altamente desenvolvido.'],
                        'Adaptações Fisiológicas e Comportamentais':['Grande tamanho, respiração por meio de espiráculos, capacidade de mergulhar por longos períodos.'],
                        'Papel no Ecossistema':['Desempenham um papel importante no equilíbrio dos ecossistemas marinhos, controlando populações de presas.'],
                        'Estado de Conservação':['Variável, algumas espécies estão ameaçadas de extinção devido à caça e à poluição dos oceanos.']},
                'Morcego': {
                    'Nome Científico e Classificação Taxonômica':['Diversas espécies, como o morcego-vampiro (Desmodus rotundus)', 'Ordem: Chiroptera.'],
                        'Habitat e Distribuição Geográfica':['Diversos habitats, desde florestas a áreas urbanas, global.'],
                        'Dieta e Hábitos Alimentares':['Variada, incluindo insetos, frutas, néctar e até pequenos vertebrados, dependendo da espécie.'],
                        'Comportamento Social':['Varia de solitário a altamente gregário, dependendo da espécie.'],
                        'Ciclo de Vida e Reprodução':['Gestação de cerca de 2 a 6 meses, as crias são amamentadas e cuidadas pelas mães.'],
                        'Adaptações Fisiológicas e Comportamentais':['Voo ativo, ecolocalização, capacidade de dormir de cabeça para baixo.'],
                        'Papel no Ecossistema':['Importante para o controle de insetos, polinização de plantas e dispersão de sementes.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas ameaçadas devido à perda de habitat e doenças.']}
            },
            'Aves': {
                'Águia': {
                    'Nome Científico e Classificação Taxonômica':['Diversas espécies, como a águia-real (Aquila chrysaetos)', 'Família: Accipitridae', 'Ordem: Accipitriformes.'],
                        'Habitat e Distribuição Geográfica':['Diversos habitats, desde montanhas a planícies, global.'],
                        'Dieta e Hábitos Alimentares':['Carnívora, alimenta-se de presas como mamíferos, aves e peixes.'],
                        'Comportamento Social':['Geralmente solitárias, exceto na época de reprodução'],
                        'Ciclo de Vida e Reprodução':['Gestação de cerca de 2 meses, filhotes são cuidados pelos pais até a independência.'],
                        'Adaptações Fisiológicas e Comportamentais':['Visão aguçada, voo potente, garras afiadas.'],
                        'Papel no Ecossistema':['Importante para o controle de populações de presas, equilíbrio dos ecossistemas.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas ameaçadas devido à perda de habitat e poluição.']},
                'Pinguim': {
                    'Nome Científico e Classificação Taxonômica':['Diversas espécies, como o pinguim-imperador (Aptenodytes forsteri)', 'Ordem: Sphenisciformes.'],
                        'Habitat e Distribuição Geográfica':['Principalmente regiões polares e áreas costeiras, Hemisfério Sul.'],
                        'Dieta e Hábitos Alimentares':['Principalmente carnívora, alimenta-se de peixes e krill.'],
                        'Comportamento Social':['Altamente gregária, vive em colônias'],
                        'Ciclo de Vida e Reprodução':['Incubação dos ovos por cerca de 1 a 2 meses, cuidado parental compartilhado.'],
                        'Adaptações Fisiológicas e Comportamentais':['Adaptações para natação rápida, impermeabilização das penas.'],
                        'Papel no Ecossistema':['Importante para o controle de populações de peixes e krill, parte integrante dos ecossistemas marinhos.'],
                        'Estado de Conservação':['Algumas espécies ameaçadas devido à perda de habitat, pesca predatória e mudanças climáticas.']},
                'Papagaio': {
                    'Nome Científico e Classificação Taxonômica':['Diversas espécies, como o papagaio-verdadeiro (Amazona aestiva)', 'Família: Psittacidae', 'Ordem: Psittaciformes.'],
                        'Habitat e Distribuição Geográfica':['Principalmente florestas tropicais e subtropicais, América do Sul, África, Ásia e Oceania.'],
                        'Dieta e Hábitos Alimentares':['Frugívora, consome sementes, frutas, flores e néctar.'],
                        'Comportamento Social':['Sociável, vive em bandos ou pares'],
                        'Ciclo de Vida e Reprodução':['Incubação dos ovos por cerca de 3 semanas, cuidado parental compartilhado.'],
                        'Adaptações Fisiológicas e Comportamentais':['Bico forte para quebrar sementes, capacidade de imitar sons.'],
                        'Papel no Ecossistema':['Importante para a dispersão de sementes, polinização de flores e controle de insetos.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas ameaçadas devido à perda de habitat e tráfico ilegal.']},
                'Corvo': {
                    'Nome Científico e Classificação Taxonômica':['Diversas espécies, como o corvo-comum (Corvus corax)', 'Família: Corvidae', 'Ordem: Passeriformes.'],
                        'Habitat e Distribuição Geográfica':['Diversos habitats, desde florestas a áreas urbanas, global.'],
                        'Dieta e Hábitos Alimentares':['Omnívoro, consome frutas, insetos, pequenos vertebrados e restos de animais.'],
                        'Comportamento Social':['Altamente gregário, vive em grupos familiares'],
                        'Ciclo de Vida e Reprodução':['Incubação dos ovos por cerca de 2 semanas, cuidado parental compartilhado.'],
                        'Adaptações Fisiológicas e Comportamentais':['Inteligência, capacidade de aprendizado, vocalização complexa.'],
                        'Papel no Ecossistema':['Importante para a limpeza de carcaças, controle de populações de insetos e pequenos vertebrados.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas estão adaptadas a viverem próximas aos humanos, enquanto outras sofrem com perda de habitat e envenenamento por pesticidas.']},
                'Pavão': {
                    'Nome Científico e Classificação Taxonômica':['Pavo cristatus (pavão-indiano)', 'Família: Phasianidae', 'Ordem: Galliformes.'],
                        'Habitat e Distribuição Geográfica':['Florestas tropicais e áreas adjacentes, Sul da Ásia.'],
                        'Dieta e Hábitos Alimentares':['Omnívoro, alimenta-se de sementes, insetos, frutas e pequenos vertebrados.'],
                        'Comportamento Social':['Os machos exibem plumagem colorida durante a época de acasalamento para atrair as fêmeas.'],
                        'Ciclo de Vida e Reprodução':['Os ovos são incubados por cerca de 28 dias, os filhotes são precoces e nidífugos.'],
                        'Adaptações Fisiológicas e Comportamentais':['Plumagem colorida usada para cortejar parceiros, vocalizações altas.'],
                        'Papel no Ecossistema':['Seu comportamento de cortejo e exibição pode afetar a seleção sexual e a diversidade genética.'],
                        'Estado de Conservação':['Pavões selvagens estão listados como "Pouco preocupante", mas a destruição do habitat é uma ameaça.']},
                'Flamingo': {
                    'Nome Científico e Classificação Taxonômica':['Diversas espécies, como Phoenicopterus roseus (flamingo-comum)', 'Família: Phoenicopteridae', 'Ordem: Phoenicopteriformes.'],
                        'Habitat e Distribuição Geográfica':['Habitats aquáticos costeiros e de água doce, presente em todos os continentes, exceto na Antártida.'],
                        'Dieta e Hábitos Alimentares':['Filtradores de alimentação, consomem pequenos crustáceos, algas e larvas de insetos na água.'],
                        'Comportamento Social':['Geralmente vivem em grandes colônias'],
                        'Ciclo de Vida e Reprodução':['Incubação dos ovos por cerca de 28 dias, cuidado parental compartilhado.'],
                        'Adaptações Fisiológicas e Comportamentais':['Longas pernas e pescoço adaptados para alimentação na água, filtragem de alimentos com bico especializado.'],
                        'Papel no Ecossistema':['Importante para a manutenção de ecossistemas aquáticos saudáveis, controle de populações de organismos aquáticos.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas ameaçadas devido à perda de habitat, poluição e perturbação humana.']}
            },
            'Répteis': {
                'Crocodilo': {
                    'Nome Científico e Classificação Taxonômica':['Crocodylidae', 'Ordem: Crocodylia'],
                        'Habitat e Distribuição Geográfica':['Habitam principalmente regiões tropicais e subtropicais, como África, Ásia, América e Austrália.'],
                        'Dieta e Hábitos Alimentares':['Carnívoros, alimentam-se de uma variedade de presas, incluindo peixes, mamíferos e aves.'],
                        'Comportamento Social':['São geralmente solitários, exceto na época de acasalamento e quando cuidam dos filhotes.'],
                        'Ciclo de Vida e Reprodução':['Depende da espécie, geralmente poe ovos em ninhos feitos de vegetação próxima à água.'],
                        'Adaptações Fisiológicas e Comportamentais':['Corpo robusto e musculoso, mandíbulas poderosas, excelente capacidade de natação e visão noturna.'],
                        'Papel no Ecossistema':['São predadores de topo, desempenhando um papel importante no controle populacional de várias espécies.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas estão ameaçadas devido à caça ilegal e perda de habitat.']},
                'Lagarto': {
                    'Nome Científico e Classificação Taxonômica':['Varia de acordo com a espécie, como Lagartos Monitores (Família: Varanidae) e Lagartos Geckos (Família: Gekkonidae).'],
                        'Habitat e Distribuição Geográfica':['Ampla distribuição geográfica, habitando desde florestas tropicais até desertos e ambientes urbanos.'],
                        'Dieta e Hábitos Alimentares':['Varia de acordo com a espécie, alguns são carnívoros, outros são herbívoros e alguns são onívoros.'],
                        'Comportamento Social':['Varia de acordo com a espécie, alguns são solitários, outros são territoriais e alguns são gregários.'],
                        'Ciclo de Vida e Reprodução':['Depende da espécie, algumas colocam ovos em ninhos no solo, enquanto outras dão à luz filhotes vivos.'],
                        'Adaptações Fisiológicas e Comportamentais':['Depende da espécie, alguns possuem línguas bifurcadas para ajudar na percepção de presas, outros têm capacidade de regeneração de caudas.'],
                        'Papel no Ecossistema':['Como predadores de diferentes níveis tróficos, ajudam a controlar populações de presas e desempenham um papel na cadeia alimentar.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas são ameaçadas devido à perda de habitat e caça ilegal.']},
                'Tartaruga': {
                    'Nome Científico e Classificação Taxonômica':['Varia de acordo com a espécie, como a Tartaruga-de-pente (Eretmochelys imbricata) e a Tartaruga-de-couro (Dermochelys coriacea).'],
                        'Habitat e Distribuição Geográfica':['Varia de acordo com a espécie, algumas habitam oceanos, outras vivem em água doce e algumas são terrestres.'],
                        'Dieta e Hábitos Alimentares':['Varia de acordo com a espécie, algumas são herbívoras, outras são carnívoras e algumas são onívoras.'],
                        'Comportamento Social':['Varia de acordo com a espécie, algumas são solitárias, outras vivem em grupos e algumas migram em grandes grupos para desovar.'],
                        'Ciclo de Vida e Reprodução':['Depende da espécie, algumas tartarugas colocam ovos em praias, outras fazem ninhos em terra firme e algumas dão à luz filhotes vivos.'],
                        'Adaptações Fisiológicas e Comportamentais':['Carapaça protetora, capacidade de mergulho prolongado, termorregulação.'],
                        'Papel no Ecossistema':['Como presas e predadores, as tartarugas desempenham um papel importante na manutenção do equilíbrio ecológico.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, algumas estão ameaçadas devido à pesca predatória, poluição e destruição de habitats.']},
                'Cobra': {
                    'Nome Científico e Classificação Taxonômica':['Varia de acordo com a espécie, como a Naja naja (Cobra-rei).'],
                        'Habitat e Distribuição Geográfica':['Habitam uma variedade de habitats, incluindo florestas, savanas, desertos e áreas urbanas, distribuídas globalmente, exceto na Antártida.'],
                        'Dieta e Hábitos Alimentares':['Carnívoras, alimentam-se principalmente de pequenos mamíferos, aves, anfíbios e outros répteis.'],
                        'Comportamento Social':['São geralmente solitárias, exceto durante a época de acasalamento ou em áreas de reprodução abundante de presas.'],
                        'Ciclo de Vida e Reprodução':['Depende da espécie, algumas põem ovos, enquanto outras dão à luz filhotes vivos; o período de gestação varia de algumas semanas a vários meses.'],
                        'Adaptações Fisiológicas e Comportamentais':['Produzem veneno neurotóxico para caça e autodefesa, possuem órgão de Jacobson para detectar odores.'],
                        'Papel no Ecossistema':['Como predadoras, ajudam a controlar as populações de pequenos animais, influenciando indiretamente a estrutura e a dinâmica dos ecossistemas.'],
                        'Estado de Conservação':['Varia de acordo com a espécie e a região geográfica; algumas estão ameaçadas devido à perda de habitat, caça ilegal e conflitos com humanos.']},
                'Iguana': {
                    'Nome Científico e Classificação Taxonômica':['Varia de acordo com a espécie, como a Iguana iguana (Iguana-verde).'],
                        'Habitat e Distribuição Geográfica':['Habitam principalmente florestas tropicais, áreas rochosas e desertos em regiões da América Central e do Sul.'],
                        'Dieta e Hábitos Alimentares':['São herbívoras, alimentam-se principalmente de folhas, frutas e flores.'],
                        'Comportamento Social':['Podem ser solitárias ou viver em pequenos grupos, principalmente durante a estação reprodutiva.'],
                        'Ciclo de Vida e Reprodução':['Põem ovos, com o período de incubação variando de algumas semanas a vários meses, dependendo da espécie.'],
                        'Adaptações Fisiológicas e Comportamentais':['Possuem uma pele escamosa que oferece proteção contra predadores e ajuda na regulação térmica.'],
                        'Papel no Ecossistema':['Como herbívoras, desempenham um papel importante na dispersão de sementes e na estruturação da vegetação em seus habitats.'],
                        'Estado de Conservação':['Varia de acordo com a espécie, com algumas enfrentando ameaças devido à perda de habitat e à caça para o comércio de animais de estimação.']},
                'Camaleão': {
                    'Nome Científico e Classificação Taxonômica':['Varia de acordo com a espécie, como o Chamaeleo chamaeleon (Camaleão-comum).'],
                        'Habitat e Distribuição Geográfica':['Habitam principalmente florestas tropicais, savanas, desertos e áreas montanhosas em regiões da África, Madagascar, sul da Europa e Ásia.'],
                        'Dieta e Hábitos Alimentares':['São carnívoros, alimentam-se principalmente de insetos e outros pequenos invertebrados, capturando suas presas com a língua pegajosa e os olhos móveis.'],
                        'Comportamento Social':['São geralmente solitários, exceto durante a época de acasalamento ou quando interagem com outros camaleões em seus territórios.'],
                        'Ciclo de Vida e Reprodução':['Depende da espécie, algumas põem ovos, enquanto outras dão à luz filhotes vivos; o período de gestação varia de algumas semanas a vários meses.'],
                        'Adaptações Fisiológicas e Comportamentais':['Possuem olhos independentes que lhes permitem olhar em direções diferentes simultaneamente, além de capacidade de mudar de cor para camuflagem e comunicação.'],
                        'Papel no Ecossistema':['Como predadores de insetos, ajudam a controlar as populações de pragas e contribuem para o equilíbrio dos ecossistemas onde habitam.'],
                        'Estado de Conservação':['Varia de acordo com a espécie e a região geográfica; algumas enfrentam ameaças devido à perda de habitat, exploração ilegal para o comércio de animais de estimação e mudanças climáticas.']}
            },
            'Anfíbios': {
                'Sapo': {
                        'Nome Científico e Classificação Taxonômica': ['Varia de acordo com a espécie, como o Bufo bufo (Sapo-comum).'],
                        'Habitat e Distribuição Geográfica': ['Podem ser encontrados em uma variedade de habitats, incluindo florestas, campos, zonas úmidas e áreas urbanas, distribuídos em todos os continentes, exceto a Antártica.'],
                        'Dieta e Hábitos Alimentares': ['São carnívoros e se alimentam de insetos, vermes e pequenos invertebrados, capturando suas presas com a língua pegajosa.'],
                        'Comportamento Social': ['São geralmente solitários, exceto durante a época de acasalamento'],
                        'Ciclo de Vida e Reprodução': ["A reprodução geralmente envolve a postura de ovos em corpos d'água, onde as larvas se desenvolvem até se transformarem em sapos adultos."],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem glândulas parotoides que secretam substâncias tóxicas como defesa contra predadores.'],
                        'Papel no Ecossistema': ['Como predadores de insetos, ajudam a controlar as populações de pragas e contribuem para o equilíbrio dos ecossistemas onde habitam.'],
                        'Estado de Conservação': ['Varia de acordo com a espécie e a região geográfica; algumas enfrentam ameaças devido à perda de habitat, poluição e mudanças climáticas.']},
                'Rã': {
                        'Nome Científico e Classificação Taxonômica': ['Varia de acordo com a espécie, como a Lithobates catesbeianus (Rã-touro).'],
                        'Habitat e Distribuição Geográfica': ['Podem ser encontradas em uma variedade de habitats aquáticos e terrestres, como lagos, lagoas, riachos, florestas e áreas úmidas, distribuídas em todos os continentes, exceto a Antártica.'],
                        'Dieta e Hábitos Alimentares': ['São carnívoras e se alimentam de uma variedade de presas, incluindo insetos, vermes, peixes e pequenos vertebrados.'],
                        'Comportamento Social': ['Podem ser solitárias ou viver em grupos, dependendo da espécie e das condições do habitat.'],
                        'Ciclo de Vida e Reprodução': ["A reprodução geralmente envolve a postura de ovos em corpos d'água, onde as larvas se desenvolvem até se transformarem em rãs adultas."],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem pele fina e úmida, que facilita a respiração cutânea e ajuda na regulação térmica.'],
                        'Papel no Ecossistema': ['Como predadores de uma variedade de presas, desempenham um papel importante na cadeia alimentar e no equilíbrio dos ecossistemas onde habitam.'],
                        'Estado de Conservação': ['Varia de acordo com a espécie e a região geográfica; algumas enfrentam ameaças devido à perda de habitat, poluição e introdução de espécies invasoras.']},
                'Salamandra': {
                        'Nome Científico e Classificação Taxonômica': ['Varia de acordo com a espécie, como a Salamandra salamandra (Salamandra-comum).'],
                        'Habitat e Distribuição Geográfica': ["Habitam principalmente florestas úmidas, áreas montanhosas e regiões próximas a corpos d'água em diversos continentes, incluindo Europa, Ásia e América do Norte."],
                        'Dieta e Hábitos Alimentares': ['São carnívoras e se alimentam de uma variedade de presas, incluindo insetos, vermes, moluscos e pequenos vertebrados.'],
                        'Comportamento Social': ['São geralmente solitárias e ativas durante a noite, procurando por presas e parceiros reprodutivos.'],
                        'Ciclo de Vida e Reprodução': ["A reprodução geralmente envolve a postura de ovos em corpos d'água, onde as larvas se desenvolvem até se transformarem em salamandras adultas."],
                        'Adaptações Fisiológicas e Comportamentais': ['Podem regenerar partes do corpo, incluindo membros e órgãos internos, em caso de lesões ou amputações.'],
                        'Papel no Ecossistema': ['Como predadores de uma variedade de presas e presas para predadores, desempenham um papel importante na cadeia alimentar e no equilíbrio dos ecossistemas onde habitam.'],
                        'Estado de Conservação': ['Varia de acordo com a espécie e a região geográfica; algumas enfrentam ameaças devido à perda de habitat, poluição e mudanças climáticas.']},
                'Tritão': {
                    'Nome Científico e Classificação Taxonômica':['Varia de acordo com a espécie, como o Lissotriton vulgaris (Tritão-palmado).'],
                        'Habitat e Distribuição Geográfica':['Podem ser encontrados em uma variedade de habitats aquáticos, incluindo lagos, lagoas, riachos e charcos, distribuídos principalmente na Europa e Ásia.'],
                        'Dieta e Hábitos Alimentares':['São carnívoros e se alimentam de uma variedade de presas, incluindo insetos, vermes e pequenos crustáceos.'],
                        'Comportamento Social':["São geralmente solitários, exceto durante a época de acasalamento, quando se reúnem em corpos d\'água para reproduzir."],
                        'Ciclo de Vida e Reprodução':["A reprodução envolve a postura de ovos em corpos d\'água, onde as larvas se desenvolvem até se transformarem em tritões adultos."],
                        'Adaptações Fisiológicas e Comportamentais':['Podem regenerar partes do corpo, incluindo membros, cauda e até partes dos órgãos internos.'],
                        'Papel no Ecossistema':['Como predadores de pequenos invertebrados, ajudam a controlar as populações de suas presas e contribuem para o equilíbrio ecológico dos habitats aquáticos onde vivem.'],
                        'Estado de Conservação':['Varia de acordo com a espécie; algumas estão ameaçadas devido à destruição de habitats, poluição e mudanças climáticas.']},
                'Perereca': {
                        'Nome Científico e Classificação Taxonômica': ['Varia de acordo com a espécie, como a Hyla cinerea (Perereca-verde).'],
                        'Habitat e Distribuição Geográfica': ["Habitam principalmente áreas próximas a corpos d\'água, como rios, lagos e lagoas, além de florestas tropicais e subtropicais, encontradas em diversas partes do mundo, especialmente nas Américas."],
                        'Dieta e Hábitos Alimentares': ['São carnívoras e se alimentam principalmente de insetos e outros pequenos invertebrados.'],
                        'Comportamento Social': ['São geralmente solitárias, mas podem ser encontradas em grandes números durante a época de acasalamento, quando machos vocalizam para atrair fêmeas.'],
                        'Ciclo de Vida e Reprodução': ["A reprodução envolve a postura de ovos em corpos d\'água, onde as larvas se desenvolvem até se transformarem em pererecas adultas."],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem discos adesivos nas pontas dos dedos, que permitem escalar superfícies verticais e folhas.'],
                        'Papel no Ecossistema': ['Como predadores de insetos, ajudam a controlar as populações de pragas e contribuem para o equilíbrio dos ecossistemas onde habitam.'],
                        'Estado de Conservação': ['Varia de acordo com a espécie e a região; algumas enfrentam ameaças devido à destruição de habitats, poluição e mudanças climáticas.']},
                'Cecília': {
                        'Nome Científico e Classificação Taxonômica': ['Pertencem à ordem Gymnophiona, como a Ichthyophis glutinosus.'],
                        'Habitat e Distribuição Geográfica': ['Habitam principalmente solos úmidos de florestas tropicais e subtropicais, encontradas em regiões tropicais da América Central e do Sul, África e Sudeste Asiático.'],
                        'Dieta e Hábitos Alimentares': ['São carnívoras e se alimentam de insetos, vermes, pequenos invertebrados e, ocasionalmente, pequenos vertebrados.'],
                        'Comportamento Social': ['São geralmente solitárias e passam a maior parte do tempo enterradas no solo, saindo apenas para procurar comida e parceiros reprodutivos.'],
                        'Ciclo de Vida e Reprodução': ['A reprodução varia entre as espécies; algumas são ovíparas e outras são vivíparas, com algumas espécies exibindo cuidado parental.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem corpos longos e segmentados, sem membros, adaptados para uma vida subterrânea, com pele que secreta muco para facilitar a movimentação através do solo.'],
                        'Papel no Ecossistema': ['Como predadores de pequenos invertebrados do solo, ajudam a controlar suas populações e contribuem para a aeração e mistura do solo.'],
                        'Estado de Conservação': ['Varia de acordo com a espécie; muitas cecílias estão ameaçadas devido à destruição de habitats e mudanças climáticas.']}
            },
            'Peixes': {
                'Tubarão': {
                        'Nome Científico e Classificação Taxonômica': ['Varia de acordo com a espécie, como o Carcharodon carcharias (Tubarão-branco).'],
                        'Habitat e Distribuição Geográfica': ['Habitam todos os oceanos do mundo, desde águas costeiras rasas até profundezas oceânicas.'],
                        'Dieta e Hábitos Alimentares': ['São carnívoros e se alimentam de peixes, lulas, crustáceos e mamíferos marinhos, dependendo da espécie.'],
                        'Comportamento Social': ['Geralmente solitários, mas algumas espécies podem formar cardumes temporários.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução varia entre espécies; pode ser ovípara, ovovivípara ou vivípara. A maioria tem um longo período de gestação e produz poucos filhotes.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem dentes afiados que são constantemente substituídos, sentidos aguçados como olfato e eletrorrecepção, e uma estrutura corporal adaptada para natação eficiente.'],
                        'Papel no Ecossistema': ['Predadores de topo, ajudam a manter o equilíbrio das populações de presas marinhas, controlando a saúde dos ecossistemas marinhos.'],
                        'Estado de Conservação': ['Muitas espécies estão ameaçadas devido à pesca excessiva, perda de habitat e mudanças climáticas.']},
                'Salmão': {
                        'Nome Científico e Classificação Taxonômica': ['Gênero Oncorhynchus (Pacífico) e Salmo (Atlântico), como o Oncorhynchus tshawytscha (Salmão-rei).'],
                        'Habitat e Distribuição Geográfica': ['Encontrados em oceanos e rios do Hemisfério Norte; salmões do Pacífico e do Atlântico têm diferentes áreas de distribuição.'],
                        'Dieta e Hábitos Alimentares': ['Se alimentam de zooplâncton, insetos, pequenos peixes e crustáceos durante suas fases de vida marinha e de água doce.'],
                        'Comportamento Social': ['Podem ser solitários ou formar cardumes durante migrações reprodutivas.'],
                        'Ciclo de Vida e Reprodução': ['Anádromos; nascem em água doce, migram para o oceano e retornam aos rios de origem para desovar. Muitas espécies morrem após a reprodução.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Adaptados para migração de longas distâncias, com mudanças fisiológicas para transitar entre água doce e salgada.'],
                        'Papel no Ecossistema': ['Importantes para ecossistemas aquáticos; suas migrações trazem nutrientes do oceano para rios e florestas.'],
                        'Estado de Conservação': ['Algumas populações estão ameaçadas devido à sobrepesca, barragens, destruição de habitats de desova e mudanças climáticas.']},
                'Atum': {
                        'Nome Científico e Classificação Taxonômica': ['Gênero Thunnus, como o Thunnus thynnus (Atum-azul).'],
                        'Habitat e Distribuição Geográfica': ['Habitam oceanos tropicais e temperados, migrando grandes distâncias.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoros, alimentando-se de peixes menores, lulas e crustáceos.'],
                        'Comportamento Social': ['Formam grandes cardumes, especialmente durante a migração e alimentação.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução ovípara; desovam em áreas específicas, onde liberam milhões de ovos que flutuam na superfície.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Corpos hidrodinâmicos para natação rápida, termorregulação que permite manter temperaturas corporais acima da água ao redor.'],
                        'Papel no Ecossistema': ['Predadores rápidos, ajudam a controlar as populações de suas presas e são importantes para a pesca comercial.'],
                        'Estado de Conservação': ['Muitas espécies estão ameaçadas devido à sobrepesca e perda de habitat.']},
                'Tilápia': {
                        'Nome Científico e Classificação Taxonômica': ['Família Cichlidae, com várias espécies como a Oreochromis niloticus (Tilápia-do-Nilo).'],
                        'Habitat e Distribuição Geográfica': ['Nativa da África, mas introduzida em águas doces tropicais e subtropicais ao redor do mundo.'],
                        'Dieta e Hábitos Alimentares': ['Omnívoras; alimentam-se de plantas, algas, pequenos invertebrados e detritos.'],
                        'Comportamento Social': ['Podem formar grupos, especialmente em áreas com abundância de alimentos.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução ovípara; muitas espécies exibem cuidado parental, com os pais protegendo os ovos e alevinos.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Adaptadas para viver em uma variedade de condições ambientais, incluindo águas pobres em oxigênio.'],
                        'Papel no Ecossistema': ['Importantes em aquicultura devido ao crescimento rápido e dieta variada, mas podem ser invasoras em alguns ecossistemas.'],
                        'Estado de Conservação': ['Geralmente não ameaçadas, mas algumas populações nativas podem estar em declínio devido à competição com espécies introduzidas.']},
                'Dourada': {
                        'Nome Científico e Classificação Taxonômica': ['Sparus aurata.'],
                        'Habitat e Distribuição Geográfica': ['Encontrada no Atlântico Leste e no Mediterrâneo, habitando áreas costeiras e estuários.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoras, alimentando-se de crustáceos, moluscos e pequenos peixes.'],
                        'Comportamento Social': ['Geralmente solitárias ou em pequenos grupos.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução ovípara; desovam em áreas específicas e exibem dimorfismo sexual.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem mandíbulas fortes e dentes adaptados para esmagar conchas.'],
                        'Papel no Ecossistema': ['Importantes predadores em seus habitats naturais e populares na pesca comercial e recreativa.'],
                        'Estado de Conservação': ['Não estão ameaçadas, mas populações podem ser afetadas por sobrepesca e destruição de habitats costeiros.']},
                'Cavala': {
                        'Nome Científico e Classificação Taxonômica': ['Scomber scombrus.'],
                        'Habitat e Distribuição Geográfica': ['Encontrada no Atlântico Norte e no Mar Mediterrâneo, em águas costeiras e oceânicas.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoras, alimentando-se de zooplâncton, pequenos peixes e crustáceos.'],
                        'Comportamento Social': ['Formam grandes cardumes, especialmente durante migrações e alimentação.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução ovípara; desovam em águas abertas, liberando ovos que flutuam na superfície.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Corpos hidrodinâmicos para natação rápida e migratória.'],
                        'Papel no Ecossistema': ['Importantes como predadores e presas em ecossistemas marinhos, também valiosas para a pesca comercial.'],
                        'Estado de Conservação': ['Populações são monitoradas, mas não estão atualmente ameaçadas; sobrepesca pode ser uma preocupação em algumas áreas.']}
            },
            'Vida marinha': {
                'Polvo': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Cephalopoda, Ordem Octopoda, como o Octopus vulgaris.'],
                        'Habitat e Distribuição Geográfica': ['Habitam todos os oceanos, geralmente em recifes de corais, águas costeiras e fundos arenosos.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoros, alimentam-se de crustáceos, moluscos e pequenos peixes, utilizando suas habilidades de camuflagem e inteligência para caçar.'],
                        'Comportamento Social': ['Geralmente solitários, mas alguns podem exibir comportamentos sociais complexos em cativeiro.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada, com fêmeas depositando ovos que são protegidos até a eclosão. A maioria das espécies tem um ciclo de vida curto, morrendo após a reprodução.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Notáveis por sua capacidade de camuflagem, regeneração de membros, inteligência avançada e uso de ferramentas.'],
                        'Papel no Ecossistema': ['Predadores importantes em ecossistemas marinhos, regulando populações de presas.'],
                        'Estado de Conservação': ['Variado; algumas espécies estão em declínio devido à pesca excessiva e destruição de habitat.']},
                'Lula': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Cephalopoda, Ordem Teuthida, como o Loligo vulgaris.'],
                        'Habitat e Distribuição Geográfica': ['Encontradas em todos os oceanos, desde águas superficiais até grandes profundidades.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoras, alimentam-se de peixes, crustáceos e outros invertebrados, capturando presas com seus tentáculos.'],
                        'Comportamento Social': ['Algumas espécies formam grandes cardumes, especialmente durante a migração e desova.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada; muitas espécies desovam em massa, com a maioria dos adultos morrendo após a reprodução.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Possuem corpos hidrodinâmicos para natação rápida, habilidades de camuflagem e comunicação complexa através de mudanças de cor.'],
                        'Papel no Ecossistema': ['Predadores e presas importantes em cadeias alimentares marinhas.'],
                        'Estado de Conservação': ['Populações geralmente estáveis, mas podem ser afetadas pela pesca excessiva e mudanças ambientais.']},
                'Estrela-do-mar': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Asteroidea, como o Asterias rubens.'],
                        'Habitat e Distribuição Geográfica': ['Habitam todos os oceanos, em diversas profundidades, desde zonas intertidais até profundezas abissais.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoras, alimentam-se de moluscos, crustáceos e detritos marinhos, utilizando seus pés ambulacrários para capturar e ingerir presas.'],
                        'Comportamento Social': ['Geralmente solitárias, mas podem ser encontradas em agregações durante a alimentação ou reprodução.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução tanto sexuada quanto assexuada; muitas espécies podem regenerar membros perdidos e algumas podem se reproduzir por fragmentação.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Capacidade de regeneração, sistema vascular único que utiliza água para locomoção e alimentação.'],
                        'Papel no Ecossistema': ['Predadores e decompositores, desempenham papel crucial na reciclagem de nutrientes e controle de populações de presas.'],
                        'Estado de Conservação': ['Algumas populações estão ameaçadas devido à perda de habitat e doenças, mas muitas espécies são abundantes.']},
                'Alforreca': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Scyphozoa, como a Aurelia aurita.'],
                        'Habitat e Distribuição Geográfica': ['Encontradas em todos os oceanos, desde águas superficiais até profundas, incluindo algumas áreas de água doce.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoras, alimentam-se de zooplâncton, peixes pequenos e outros invertebrados, capturando presas com tentáculos urticantes.'],
                        'Comportamento Social': ['Geralmente solitárias, mas algumas espécies formam grandes enxames em certas condições.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada e assexuada, com ciclos de vida que incluem estágios de pólipo e medusa.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Tentáculos urticantes para captura de presas e defesa, capacidade de pulsação para locomoção'],
                        'Papel no Ecossistema': ['Predadores e presas, influenciam populações de zooplâncton e peixes pequenos.'],
                        'Estado de Conservação': ['Geralmente abundantes, mas populações podem ser influenciadas por mudanças ambientais e poluição.']},
                'Caranguejo': {
                        'Nome Científico e Classificação Taxonômica': ['Ordem Decapoda, como o Carcinus maenas.'],
                        'Habitat e Distribuição Geográfica': ['Habitam diversos ambientes marinhos, de águas costeiras a profundezas abissais, e também em água doce e terrestre.'],
                        'Dieta e Hábitos Alimentares': ['Omnívoros, alimentam-se de detritos, algas, moluscos, crustáceos e pequenos peixes.'],
                        'Comportamento Social': ['Podem ser solitários ou formar agregações, especialmente durante a muda e reprodução.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada, com fêmeas carregando ovos até a eclosão; muitos passam por estágios larvais planctônicos antes de se estabelecerem como juvenis.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Exoesqueleto duro para proteção, capacidade de regenerar membros perdidos, comportamento de muda para crescimento.'],
                        'Papel no Ecossistema': ['Importantes como decompositores e predadores, influenciando a estrutura das comunidades bentônicas.'],
                        'Estado de Conservação': ['Populações variam, algumas espécies são ameaçadas por sobrepesca e destruição de habitat, enquanto outras são invasoras e prósperas.']},
                'Coral': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Anthozoa, como o Acropora cervicornis.'],
                        'Habitat e Distribuição Geográfica': ['Habitam águas tropicais e subtropicais, formando recifes de corais em águas rasas e claras.'],
                        'Dieta e Hábitos Alimentares': ['Autotróficos e heterotróficos, obtendo nutrientes através de simbiose com zooxantelas (algas) e capturando plâncton com tentáculos.'],
                        'Comportamento Social': ['Formam colônias massivas que são fundamentais para a construção de recifes de corais.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada e assexuada; muitos corais liberam gametas em sincronização durante a desova em massa.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Capacidade de formar esqueletos de carbonato de cálcio, simbiose com algas para obtenção de energia.'],
                        'Papel no Ecossistema': ['Criam habitats complexos que abrigam uma vasta diversidade de vida marinha, protegem costas contra erosão.'],
                        'Estado de Conservação': ['Muitas espécies estão ameaçadas devido ao branqueamento de corais, acidificação dos oceanos, poluição e pesca destrutiva.']}
            },
            'Invertebrados': {
                'Borboleta': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Insecta, Ordem Lepidoptera, como a Danaus plexippus (Borboleta-monarca).'],
                        'Habitat e Distribuição Geográfica': ['Encontradas em quase todos os continentes, exceto na Antártida, habitando florestas, campos, jardins e áreas urbanas.'],
                        'Dieta e Hábitos Alimentares': ['Larvas (lagartas) alimentam-se de folhas de plantas hospedeiras específicas; adultos se alimentam de néctar de flores.'],
                        'Comportamento Social': ['Geralmente solitárias, mas algumas espécies migram em grandes grupos.'],
                        'Ciclo de Vida e Reprodução': ['Passam por metamorfose completa: ovo, larva, pupa e adulto. A reprodução é sexuada, com fêmeas depositando ovos em plantas hospedeiras.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Asas coloridas para camuflagem e comunicação, mecanismos de defesa química nas lagartas.'],
                        'Papel no Ecossistema': ['Polinizadoras importantes e uma fonte de alimento para muitos predadores.'],
                        'Estado de Conservação': ['Algumas espécies estão ameaçadas devido à perda de habitat e uso de pesticidas.']},
                'Formiga': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Insecta, Ordem Hymenoptera, como a Formica rufa (Formiga-vermelha).'],
                        'Habitat e Distribuição Geográfica': ['Habitam praticamente todos os continentes, exceto a Antártida, em diversos ambientes, desde florestas até áreas urbanas.'],
                        'Dieta e Hábitos Alimentares': ['Omnívoras, alimentam-se de néctar, sementes, fungos, insetos e outros pequenos animais.'],
                        'Comportamento Social': ['Altamente sociais, vivem em colônias com uma divisão complexa de trabalho.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada, com rainhas produzindo ovos fertilizados e não fertilizados; colônias podem ter uma ou várias rainhas.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Comunicação através de feromônios, mandíbulas fortes para defesa e construção.'],
                        'Papel no Ecossistema': ['Ajudam na dispersão de sementes, controle de pragas e aeração do solo.'],
                        'Estado de Conservação': ['Geralmente abundantes, mas algumas espécies estão ameaçadas por perda de habitat.']},
                'Caracol': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Gastropoda, como o Helix pomatia (Caracol-de-jardim).'],
                        'Habitat e Distribuição Geográfica': ['Encontrados em habitats terrestres, de água doce e marinhos em todo o mundo.'],
                        'Dieta e Hábitos Alimentares': ['Herbívoros, alimentam-se de folhas, frutos, fungos e matéria orgânica em decomposição.'],
                        'Comportamento Social': ['Geralmente solitários, mas podem ser encontrados em grupos durante a alimentação ou reprodução.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada e hermafrodita; muitos depositam ovos em solo úmido ou água.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Concha calcária para proteção, produção de muco para locomoção e defesa.'],
                        'Papel no Ecossistema': ['Decompositores importantes, reciclando nutrientes no ecossistema.'],
                        'Estado de Conservação': ['Algumas espécies estão ameaçadas devido à destruição de habitat e poluição.']},
                'Escaravelho': {
                        'Nome Científico e Classificação Taxonômica': ['Ordem Coleoptera, como o Scarabaeus sacer (Escaravelho-sagrado).'],
                        'Habitat e Distribuição Geográfica': ['Encontrados em quase todos os ambientes terrestres, desde florestas tropicais até desertos.'],
                        'Dieta e Hábitos Alimentares': ['Variedade de dietas; alguns são herbívoros, outros detritívoros ou predadores.'],
                        'Comportamento Social': ['Geralmente solitários, mas algumas espécies exibem comportamento social complexo.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada, com muitos passando por metamorfose completa: ovo, larva, pupa e adulto.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Exoesqueleto duro para proteção, asas rígidas (élitros) para voo.'],
                        'Papel no Ecossistema': ['Decompositores, polinizadores e controladores de pragas.'],
                        'Estado de Conservação': ['Populações geralmente estáveis, mas algumas espécies estão ameaçadas por perda de habitat e poluição.']},
                'Aranha': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Arachnida, Ordem Araneae, como a Latrodectus mactans (Viúva-negra).'],
                        'Habitat e Distribuição Geográfica': ['Encontradas em todos os continentes, exceto a Antártida, em habitats variados, desde florestas até áreas urbanas.'],
                        'Dieta e Hábitos Alimentares': ['Carnívoras, alimentam-se principalmente de insetos e outros pequenos artrópodes, utilizando teias para capturar presas.'],
                        'Comportamento Social': ['Geralmente solitárias, mas algumas espécies exibem comportamento social ou colonial.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada, com fêmeas depositando ovos em sacos de seda; algumas exibem cuidado parental.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Produção de seda para construção de teias, comunicação e reprodução, veneno para captura de presas.'],
                        'Papel no Ecossistema': ['Controladores de populações de insetos e outros artrópodes.'],
                        'Estado de Conservação': ['Geralmente abundantes, mas algumas espécies estão ameaçadas por perda de habitat.']},
                'Minhoca': {
                        'Nome Científico e Classificação Taxonômica': ['Classe Clitellata, como a Lumbricus terrestris (Minhoca-comum).'],
                        'Habitat e Distribuição Geográfica': ['Encontradas em solos úmidos em todo o mundo, especialmente em áreas ricas em matéria orgânica.'],
                        'Dieta e Hábitos Alimentares': ['Detritívoras, alimentam-se de matéria orgânica em decomposição, contribuindo para a formação de húmus.'],
                        'Comportamento Social': ['Geralmente solitárias, mas podem ser encontradas em alta densidade em solos ricos.'],
                        'Ciclo de Vida e Reprodução': ['Reprodução sexuada e hermafrodita; trocam esperma com outros indivíduos e depositam ovos em casulos.'],
                        'Adaptações Fisiológicas e Comportamentais': ['Corpos segmentados para movimentação eficiente no solo, capacidade de regeneração de segmentos perdidos.'],
                        'Papel no Ecossistema': ['Aeração e fertilização do solo, decomposição de matéria orgânica, reciclagem de nutrientes.'],
                        'Estado de Conservação': ['Geralmente abundantes, mas populações podem ser afetadas por poluição e práticas agrícolas.']
                }
            }
        }
    }

# Gravar o ficheiro binário
def gravar_ficheiro_binário():
    global animais
    f = open(r"C:\Users\Gabriel\Desktop\Python\mod7\Jardim Zoológico.bin", "wb")
    pickle.dump(animais,f)
    f.close()

# Carregar o ficheiro binário
def carregar_ficheiro_binário():
    global animais
    f = open(r"C:\Users\Gabriel\Desktop\Python\mod7\Jardim Zoológico.bin", "rb")
    animais=pickle.load(f)
    f.close()

criar_ficheiro_binário()
gravar_ficheiro_binário()
carregar_ficheiro_binário()
while True:
        # Mostrar o Menu Geral Do Jardim Zoológico
        menu_geral()
        # Escolher a Opção Geral Para Ir Para Um Menu Específico..
        opcao_geral=int(input('Opção:'))
        if opcao_geral == 1:
            menu_especimes()

            opcao_2= int(input('Opção:'))
            if opcao_2 == 1:
                # Mostrar o Menu dos Mamíferos
                menu_mamiferos()

                opcao_3=int(input('Opção:'))
            
                if opcao_3==1:
                    for dados in animais['Espécimes']["Mamiferos"]["Leão"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Mamiferos"]["Leão"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==2:
                    for dados in animais['Espécimes']["Mamiferos"]["Elefante"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Mamiferos"]["Elefante"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==3:
                    for dados in animais['Espécimes']["Mamiferos"]["Cão"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Mamiferos"]["Cão"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==4:
                    for dados in animais['Espécimes']["Mamiferos"]["Gato"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Mamiferos"]["Gato"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==5:
                    for dados in animais['Espécimes']["Mamiferos"]["Baleia"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Mamiferos"]["Baleia"][dados]:
                     print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==6:
                    for dados in animais['Espécimes']["Mamiferos"]["Morcego"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Mamiferos"]["Morcego"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==0:
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break

            if opcao_2 == 2:
                # Mostrar o Menu das Aves
                menu_aves()

                opcao_3=int(input('Opção:'))
                if opcao_3==1:
                    for dados in animais['Espécimes']["Aves"]["Águia"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Aves"]["Águia"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                
                if opcao_3==2:
                    for dados in animais['Espécimes']["Aves"]["Pinguim"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Aves"]["Pinguim"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==3:
                    for dados in animais['Espécimes']["Aves"]["Papagaio"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Aves"]["Papagaio"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==4:
                    for dados in animais['Espécimes']["Aves"]["Corvo"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Aves"]["Corvo"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==5:
                    for dados in animais['Espécimes']["Aves"]["Pavão"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Aves"]["Pavão"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==6:
                    for dados in animais['Espécimes']["Aves"]["Flamingo"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Aves"]["Flamingo"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==0:
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break

            if opcao_2 == 3:
                # Mostrar o Menu dos Reptéis
                menu_repteis()
                
                opcao_3=int(input('Opção:'))
                if opcao_3==1:
                    for dados in animais['Espécimes']["Répteis"]["Crocodilo"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Répteis"]["Crocodilo"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==2:
                    for dados in animais['Espécimes']["Répteis"]["Lagarto"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Répteis"]["Lagarto"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==3:
                    for dados in animais['Espécimes']["Répteis"]["Tartaruga"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Répteis"]["Tartaruga"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==4:
                    for dados in animais['Espécimes']["Répteis"]["Cobra"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Répteis"]["Cobra"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==5:
                    for dados in animais['Espécimes']["Répteis"][" Iguana"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Répteis"]["Iguana"][dados]:
                     print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==6:
                    for dados in animais['Espécimes']["Répteis"]["Camaleão"]:
                        print(dados)
                    for informacoes in animais['Espécimes']["Répteis"]["Camaleão"][dados]:
                        print(informacoes)
                    print()
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')

                if opcao_3==0:
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break

            if opcao_2 == 4:
                # Mostrar o Menu de Anfíbios
                menu_anfibios()

                opcao_3=int(input('Opção:'))
                if opcao_3==1:
                    for dados in animais['Espécimes']["Anfíbios"]["Sapo"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Anfíbios"]["Sapo"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                
                if opcao_3==2:
                    for dados in animais['Espécimes']["Anfíbios"]["Rã"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Anfíbios"]["Rã"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==3:
                    for dados in animais['Espécimes']["Anfíbios"]["Salamandra"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Anfíbios"]["Salamandra"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==4:
                    for dados in animais['Espécimes']["Anfíbios"]["Tritão"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Anfíbios"]["Tritão"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==5:
                    for dados in animais['Espécimes']["Anfíbios"]["Perereca"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Anfíbios"]["Perereca"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==6:
                    for dados in animais['Espécimes']["Anfíbios"]["Cecília"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Anfíbios"]["Cecília"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==0:
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break

            if opcao_2 == 5:
                # Mostrar o Menu de Peixes
                menu_peixes()

                opcao_3=int(input('Opção:'))
                if opcao_3==1:
                    for dados in animais['Espécimes']["Peixes"]["Tubarão"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Peixes"]["Tubarão"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                
                if opcao_3==2:
                    for dados in animais['Espécimes']["Peixes"]["Salmão"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Peixes"]["Salmão"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==3:
                    for dados in animais['Espécimes']["Peixes"]["Atum"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Peixes"]["Atum"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==4:
                    for dados in animais['Espécimes']["Peixes"]["Tilápia"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Peixes"]["Tilápia"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==5:
                    for dados in animais['Espécimes']["Peixes"]["Dourada"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Peixe"]["Dourada"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==6:
                    for dados in animais['Espécimes']["Peixe"]["Cavala"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Peixe"]["Cavala"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==0:
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break

            if opcao_2 == 6:
               # Mostrar Menu de Vida Marinha
                menu_vida_marinha()

                opcao_3 = input('Opção:')
                if opcao_3=='1':
                    for dados in animais['Espécimes']["Vida marinha"]["Polvo"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Vida aarinha"]["Polvo"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                
                if opcao_3=='2':
                    for dados in animais['Espécimes']["Vida marinha"]["Lula"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Vida marinha"]["Lula"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3=='3':
                    for dados in animais['Espécimes']["Vida marinha"]["Estrela-do-mar"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Vida marinha"]["Estrela-do-mar"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3=='4':
                    for dados in animais['Espécimes']["Vida marinha"]["Alforreca"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Vida marinha"]["Alforreca"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3=='5':
                    for dados in animais['Espécimes']["Vida marinha"]["Caranguejo"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Vida marinha"]["Caranguejo"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3=='6':
                    for dados in animais['Espécimes']["Vida marinha"]["Coral"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Vida marinha"]["Coral"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3=='0':
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break
                
            if opcao_2 == 7:
                # Mostrar Menu de Invertebrados
                menu_invertebrados()

                opcao_3=int(input('Opção:'))
                if opcao_3==1:
                    for dados in animais['Espécimes']["Invertebrados"]["Borboleta"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Invertebrados"]["Borboleta"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                
                if opcao_3==2:
                    for dados in animais['Espécimes']["Invertebrados"]["Formiga"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Invertebrados"]["Formiga"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==3:
                    for dados in animais['Espécimes']["Invertebrados"]["Caracol"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Invertebrados"]["Caracol"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==4:
                    for dados in animais['Espécimes']["Invertebrados"]["Escaravelho"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Invertebrados"]["Escaravelho"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==5:
                    for dados in animais['Espécimes']["Invertebrados"]["Aranha"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Invertebrados"]["Aranha"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==6:
                    for dados in animais['Espécimes']["Invertebrados"]["Minhoca"]:
                        print(dados)
                for informacoes in animais['Espécimes']["Invertebrados"]["Minhoca"][dados]:
                    print(informacoes)
                print()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

                if opcao_3==0:
                    input('Pressione Enter Para Continuar...')
                    os.system('cls')
                    break

            if opcao_2 == 0:
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                break
                
        if opcao_geral == 2:
            menu_horario()
            
            opcao_3=int(input('Opção:'))
            if opcao_3==1:
                menu_primavera()
                input('Pressione Enter Para Continuar...')
                os.system('cls')
                
            if opcao_3==2:
                menu_verao()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

            if opcao_3==3:
                menu_outono()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

            if opcao_3==4:
                menu_inverno()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

            if opcao_3==0: 
                menu_inverno()
                input('Pressione Enter Para Continuar...')
                os.system('cls')

        if opcao_geral==3:
            certas = 0
            perguntas = [
            {
                "pergunta": "Qual é o maior mamífero terrestre?\n",
                "respostas": ("a) Elefante Africano", "b) Hipopótamo", "c) Rinoceronte", "d) Búfalo"),
                "resposta_correta": "a",
            },
            {
                "pergunta": "Quantas espécies de pinguins existem no mundo?\n",
                "respostas": ("a) 5", "b) 10", "c) 18", "d) 25"),
                "resposta_correta": "c",
            },
            {
                "pergunta": "Qual é a única espécie de urso encontrada na América do Sul?\n",
                "respostas": ("a) Urso Polar", "b) Urso Pardo", "c) Urso-de-óculos", "d) Panda Gigante"),
                "resposta_correta": "c",
            },
            {
                "pergunta": "Qual destes animais é um marsupial?\n",
                "respostas": ("a) Canguru", "b) Elefante", "c) Girafa", "d) Zebra"),
                "resposta_correta": "a",
            },
            {
                "pergunta": "Qual é a principal dieta de um panda gigante?\n",
                "respostas": ("a) Frutas", "b) Bambus", "c) Carne", "d) Insetos"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Qual é o nome do maior réptil do mundo?\n",
                "respostas": ("a) Crocodilo-de-água-salgada", "b) Anaconda", "c) Dragão-de-komodo", "d) Tartaruga-gigante"),
                "resposta_correta": "a",
            },
            {
                "pergunta": "Quanto tempo pode viver uma tartaruga-gigante das Galápagos?\n",
                "respostas": ("a) 50 anos", "b) 100 anos", "c) 150 anos", "d) 200 anos"),
                "resposta_correta": "c",
            },
            {
                "pergunta": "Qual é a ave com a maior envergadura de asas?\n",
                "respostas": ("a) Condor-dos-Andes", "b) Albatroz", "c) Águia-americana", "d) Falcão-peregrino"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Quantas espécies de grandes felinos existem?\n",
                "respostas": ("a) 3", "b) 5", "c) 7", "d) 9"),
                "resposta_correta": "c",
            },
            {
                "pergunta": "Qual destes animais é conhecido por mudar de cor?\n",
                "respostas": ("a) Iguana", "b) Camaleão", "c) Lagarto", "d) Cobra"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Qual animal é conhecido como o 'Rei da Selva'?\n",
                "respostas": ("a) Tigre", "b) Leão", "c) Leopardo", "d) Gorila"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Qual mamífero marinho é conhecido por suas acrobacias e inteligência?\n",
                "respostas": ("a) Baleia", "b) Foca", "c) Golfinho", "d) Tubarão"),
                "resposta_correta": "c",
            },
            {
                "pergunta": "Qual é a maior espécie de papagaio do mundo?\n",
                "respostas": ("a) Papagaio-do-mangue", "b) Arara-azul", "c) Papagaio-do-congo", "d) Calopsita"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Qual animal é conhecido por ser o mais rápido em terra?\n",
                "respostas": ("a) Gazela", "b) Tigre", "c) Cavalo", "d) Guepardo"),
                "resposta_correta": "d",
            },
            {
                "pergunta": "Qual animal é famoso por ter uma longa língua que pode alcançar até 50 cm de comprimento?\n",
                "respostas": ("a) Girafa", "b) Tamanduá-bandeira", "c) Cavalo-marinho", "d) Orangotango"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Qual ave é conhecida por sua capacidade de imitar sons humanos?\n",
                "respostas": ("a) Cobra", "b) Crocodilo", "c) Tartaruga", "d) Camaleão"),
                "resposta_correta": "a",
            },
            {
                "pergunta": "Qual anfíbio é famoso por suas cores vibrantes e veneno potente?\n",
                "respostas": ("a) Sapo-comum", "b) Rã-dardo-venenosa", "c) Salamandra-tigre", "d) Tritão-de-crista"),
                "resposta_correta": "b",
            },
            {
                "pergunta": "Qual é o maior invertebrado do mundo?\n",
                "respostas": ("a) Lula-colossal", "b) Caranguejo-aranha-gigante", "c) Polvo-gigante-do-pacífico", "d) Besouro-golias"),
                "resposta_correta": "a",
            },
            {
                "pergunta": "Qual animal é conhecido por dormir em pé?\n",
                "respostas": ("a) Cavalo", "b) Elefante", "c) Girafa", "d) Búfalo"),
                "resposta_correta": "a",
            },
            {
                "pergunta": "Qual destes animais é conhecido por ser um excelente construtor de represas?\n",
                "respostas": ("a) Lontra", "b) Ornitorrinco", "c) Rato-almiscarado", "d) Castor"),
                "resposta_correta": "d",
            }]
            def verificar(pergunta):
                global certas
                print(pergunta["pergunta"])
                print(pergunta["respostas"])
                opção=(str(input("Resposta (a até d): "))).lower()
                if opção == pergunta["resposta_correta"]:
                    print("➥ Acertou ✅\n")
                    certas += 1
                else:
                    print("➥ Errou ⛔\n")
                    certas -= 0
            
                    for i in range(20):
                        pergunta = random.choice(perguntas)
                        perguntas.remove(pergunta)
                        verificar(pergunta)
            
                    if certas <= 7:
                        print("Acertaste",certas,"de 20")
                        print("Precisa de treinar mais :(")
                    elif certas > 7 and certas <= 15:
                        print("Acertaste",certas,"de 200")
                        print("Continua com o bom trabalho :)")
                    elif certas > 15 and certas <= 20:
                        print("Acertaste",certas,"de 20")
                        print("Excelente trabalho ★")
            
            verificar()
            if opcao_geral == 4:
                
                especie,animal=input("Qual a especie e animal que pretende consultar (separe por espaço):").split()
                if especie not in animais['Espécimes'].keys():
                    print("Essa especie não está registada")
                elif(animal in animais['Espécimes'][especie].values()):
                    print("Esse animal não se encontra registado")
                else:
                    for dados in animais['Espécimes'][especie][animal]:
                        print(dados)
                        for informacoes in animais['Espécimes']["Mamiferos"]["Leão"][dados]:
                            print(informacoes)
                        print()

            if opcao_geral == 0:
                break




'''
menu_geral()
O = 1
O = int(input("Opção:"))
if(O == 0):
'''