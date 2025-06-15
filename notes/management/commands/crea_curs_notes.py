from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from faker import Faker
from datetime import timedelta
from random import randint, uniform
 
from notes.models import *
 
faker = Faker(["es_CA","es_ES"])

assignatures_per_grau_nivell = {
    'ASIX': {
        '1r': [
            ('Implantació de Sistemes Operatius', 'ISO'),
            ('Gestió de Bases de Dades', 'BBDD'),
            ('Programació Bàsica', 'PROG'),
            ('Llenguatge de Marques i Sistemes de Gestió d’Informació', 'LM'),
            ('Fonaments de Maquinari', 'HARD'),
            ('Formació i Orientació Laboral', 'FOL'),
        ],
        '2n': [
            ('Administració de Sistemes Operatius', 'ASO'),
            ('Planificació i Administració de Xarxes', 'PAX'),
            ('Serveis de Xarxa i Internet', 'SXR'),
            ('Implantació d’Aplicacions Web', 'IAW'),
            ('Administració de Sistemes Gestors de Bases de Dades', 'ASGBD'),
            ('Seguretat i Alta Disponibilitat', 'SEGAD'),
            ('Projecte de Sistemes Informàtics en Xarxa', 'PRJ'),
            ('Empresa i Iniciativa Emprenedora', 'EIE'),
            ('Formació en Centres de Treball', 'FCT'),
        ]
    },
    'DAM': {
        '1r': [
            ('Sistemes Informàtics', 'SI'),
            ('Bases de Dades', 'BBDD'),
            ('Programació', 'PROG'),
            ('Llenguatges de Marques i Sistemes de Gestió d’Informació', 'LM'),
            ('Entorns de Desenvolupament', 'ED'),
            ('Formació i Orientació Laboral', 'FOL'),
        ],
        '2n': [
            ('Accés a Dades', 'AD'),
            ('Desenvolupament d’Interfícies', 'DI'),
            ('Programació Multimèdia i Dispositius Mòbils', 'PMDM'),
            ('Programació de Serveis i Processos', 'PSP'),
            ('Sistemes de Gestió Empresarial', 'SGE'),
            ('Projecte de Desenvolupament d’Aplicacions Multiplataforma', 'PRJ'),
            ('Empresa i Iniciativa Emprenedora', 'EIE'),
            ('Formació en Centres de Treball', 'FCT'),
        ]
    },
    'DAW': {
        '1r': [
            ('Sistemes Informàtics', 'SI'),
            ('Bases de Dades', 'BBDD'),
            ('Programació', 'PROG'),
            ('Llenguatges de Marques i Sistemes de Gestió d’Informació', 'LM'),
            ('Entorns de Desenvolupament', 'ED'),
            ('Formació i Orientació Laboral', 'FOL'),
        ],
        '2n': [
            ('Desenvolupament Web en Entorn Client', 'DWEC'),
            ('Desenvolupament Web en Entorn Servidor', 'DWES'),
            ('Desplegament d’Aplicacions Web', 'DAW'),
            ('Disseny d’Interfícies Web', 'DIW'),
            ('Projecte de Desenvolupament d’Aplicacions Web', 'PRJ'),
            ('Empresa i Iniciativa Emprenedora', 'EIE'),
            ('Formació en Centres de Treball', 'FCT'),
        ]
    }
}
 
class Command(BaseCommand):
    help = 'Crea un campus amb grups, assignatures alumnes i notes'
 
    def add_arguments(self, parser):
        parser.add_argument('curs_academic', nargs=1, type=str)
 
    def handle(self, *args, **options):
        any_academic = options['curs_academic'][0]
        

        for grau,_ in Grup._meta.get_field('grau').choices:
            for nivell,_ in Grup._meta.get_field('nivell').choices:
                grup = Grup(any_academic = any_academic,grau=grau,nivell=nivell)
                grup.save()

                print("S'ha creat al grup")
                llista_assignatures = []
                for nom, nom_curt in assignatures_per_grau_nivell[grau][nivell]:
                    assignatura = Assignatura.objects.create(nom=nom, nom_curt=nom_curt, grup=grup)
                    llista_assignatures.append(assignatura)

                for _ in range(randint(25,30)):  # 25-30 alumnes per grup
                    nom=faker.first_name()
                    cognom=faker.last_name()
                    #grup=grup

                    alumne = Alumne(nom=nom, cognoms=cognom, grup=grup)
                    alumne.save()

                    print(f"S'ha agregat {nom} {cognom} a {nivell} de {grau}")
                    
                    for assignatura in llista_assignatures: #es podria haver fet més random

                        matricula = Matricula(alumne=alumne, assignatura=assignatura)
                        matricula.save()
                        nota_random = round(uniform(0, 10), 2)
                        nota = Nota(matricula=matricula, nota=nota_random)
                        nota.save()
                print(f"S'han matriculat i posat les notes als alumnes del grup : {nivell} de {grau}")