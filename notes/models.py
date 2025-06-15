from django.db import models
import datetime

def default_any_academic():
    any_actual = datetime.date.today().year
    return f'{any_actual}-{any_actual+1}'

class Grup(models.Model):
    any_academic = models.CharField(max_length=20, default=default_any_academic)  # Ex: "2024-2025"
    grau = models.CharField(max_length=50, choices=[('ASIX', 'ASIX'),('DAM', 'DAM'),('DAW', 'DAW'),])
    nivell = models.CharField(max_length=10, choices=[('1r', 'Primer'),('2n', 'Segon'),])

    class Meta:
        unique_together = ('any_academic', 'grau', 'nivell')

    def __str__(self):
        return f"{self.grau} {self.nivell} ({self.any_academic})"

class Assignatura(models.Model):
    nom = models.CharField(max_length=100)
    nom_curt = models.CharField(max_length=5,default=' ')
    grup = models.ForeignKey(Grup, on_delete=models.CASCADE, related_name='assignatures',null=True)
    
    def __str__(self):
        return f"{self.nom_curt} - {self.nom} ({self.grup.nivell}, {self.grup.grau})"

class Alumne(models.Model):
    nom = models.CharField(max_length=100)
    cognoms = models.CharField(max_length=150)
    grup = models.ForeignKey(Grup, on_delete=models.CASCADE, related_name='alumnes_curs',null=True)
    assignatures = models.ManyToManyField(Assignatura, through='Matricula', related_name='alumnes_assignatura')

    def __str__(self):
        return f"{self.nom} {self.cognoms}"

class Matricula(models.Model):
    alumne = models.ForeignKey(Alumne, on_delete=models.CASCADE)
    assignatura = models.ForeignKey(Assignatura, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('alumne', 'assignatura')

    def __str__(self):
        return f"{self.alumne} - {self.assignatura}"

class Nota(models.Model):
    matricula = models.ForeignKey(Matricula, on_delete=models.CASCADE, related_name='notes_matricula',null=True)
    nota = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)  # Ex: 8.75

    class Meta:
        unique_together = ('matricula',)

    def __str__(self):
        return f"{self.matricula}: {self.nota}"
