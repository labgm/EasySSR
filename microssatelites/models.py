from django.db import models, connection, transaction
from django.contrib.auth import get_user_model
import django_tables2 as tables

# Create your models here.

# class Microssatelites(models.Model):
#     # owner = models.ForeignKey
#     name = models.CharField('Nome', max_length=100)
#     slug = models.SlugField('Atalho')
#     created_at = models.DateTimeField(
#         'Criado em', auto_now_add=True
#     )
#     file = models.FileField(upload_to='files')
#     # update_at = models.DateTimeField(
#     #     'Atualizado em', auto_now=True
#     # )
# class Project(models.Model):

    # cepa = models.CharField('Cepa'),
    #  file = models.FileField(upload_to='files'

class User(models.Model):
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email')

    def __str__(self):
        return self.name

class Project(models.Model):
    # headline = models.CharField(max_length=100)
    created_at = models.DateTimeField(
            'Criado em', auto_now_add=True
        )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ProjectData(models.Model):
    cepa = models.CharField('Cepa', max_length=200)
    motif = models.CharField('Motif', max_length=200)
    lflanking = models.CharField('LFlanking', max_length=200)
    rflanking = models.CharField('RFlanking', max_length=200)
    iterations = models.IntegerField('Iterations')
    tractlength = models.IntegerField('Tractlength')
    consensus = models.CharField('Consensus', max_length=200)
    pos_start = models.IntegerField('Start')
    pos_end = models.IntegerField('End')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def my_custom_sql(project):
        cursor = connection.cursor()
        # Operação de modificação de dado - commit obrigatório
        # cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        # transaction.commit_unless_managed()

        # Operação de recebimento de dado - não é necessário o commit
        # cursor.execute(f"SELECT * FROM microssatelites_projectdata WHERE project_id = {project} GROUP BY motif ORDER BY motif")
        cursor.execute(f"SELECT motif, iterations, cepa FROM microssatelites_projectdata WHERE project_id = {project} GROUP BY motif, iterations, cepa  ORDER BY motif")
        rows = cursor.fetchall()
        return rows

    def get_cepas_by_motif(project):
        cursor = connection.cursor()
        cursor.execute(f"SELECT cepa, motif FROM microssatelites_projectdata WHERE project_id = {project} GROUP BY cepa")
        # cursor.execute(f"SELECT cepa FROM microssatelites_projectdata WHERE motif = '{motif}' GROUP BY cepa")
        rows_cepas = cursor.fetchall()
        return rows_cepas
    
    def get_data(project):
        cursor = connection.cursor()
        cursor.execute(f"SELECT COUNT(*) as total, motif, iterations, cepa, lflanking, rflanking, pos_start, pos_end FROM microssatelites_projectdata WHERE project_id = {project} GROUP BY motif, iterations, cepa, lflanking, rflanking, pos_start, pos_end  ORDER BY motif")
        rows_cepas = cursor.fetchall()
        return rows_cepas

    def get_motifs(project):
        cursor = connection.cursor()
        cursor.execute(f"SELECT motif, COUNT(*) as total, iterations FROM microssatelites_projectdata WHERE project_id = {project} GROUP BY motif, iterations ORDER BY total DESC LIMIT 10")
        rows_cepas = cursor.fetchall()
        return rows_cepas
    
    def get_motifs2(project):
        cursor = connection.cursor()
        cursor.execute(f"SELECT motif, COUNT(*) as total FROM microssatelites_projectdata WHERE project_id = {project} GROUP BY motif ORDER BY total DESC LIMIT 10")
        rows_cepas = cursor.fetchall()
        return rows_cepas

    def get_cepas(motif, project, iteration):
        cursor = connection.cursor()
        cursor.execute(f"SELECT motif, cepa, COUNT(*) FROM microssatelites_projectdata WHERE motif = '{motif}' AND project_id = {project} AND iterations = {iteration} GROUP BY cepa")
        rows_cepas = cursor.fetchall()
        return rows_cepas
    
    def get_cepas2(motif, project):
        cursor = connection.cursor()
        cursor.execute(f"SELECT motif, cepa, COUNT(*) FROM microssatelites_projectdata WHERE motif = '{motif}' AND project_id = {project} GROUP BY cepa")
        rows_cepas = cursor.fetchall()
        return rows_cepas

class DataStatistic(models.Model):
    cepa = models.CharField('Cepa', max_length=200)
    totalSSR = models.IntegerField('Total SSR')
    totalCodificante = models.IntegerField('Total Codificante')
    totalNaoCodificante = models.IntegerField('Total não Codificante')
    mono = models.IntegerField('Mono')
    di = models.IntegerField('Di')
    tri = models.IntegerField('Tri')
    tetra = models.IntegerField('Tetra')
    penta = models.IntegerField('Penta')
    hexa = models.IntegerField('Hexa')
    totalPerfeitos = models.IntegerField('Total Perfeitos')
    totalPerfeitosCodificantes = models.IntegerField('Total Perfeitos Codificantes')
    totalPerfeitosNaoCodificantes = models.IntegerField('Toral Perfeitos Não Codificantes')
    perfeitoMono = models.IntegerField('Perfeito Mono')
    perfeitoDi = models.IntegerField('Perfeito Di')
    perfeitoTri = models.IntegerField('Perfeito Tri')
    perfeitoTetra = models.IntegerField('Perfeito Tetra')
    perfeitoPenta = models.IntegerField('Perfeito Penta')
    perfeitoHexa = models.IntegerField('Perfeito Hexa')
    totalImperfeitos = models.IntegerField('Total Imperfeitos')
    totalImperfeitosCodificantes = models.IntegerField('Total Imperfeitos Codificantes')
    totalImperfeitosNaoCodificantes = models.IntegerField('Total Imperfeitos Não Codificantes')
    imperfeitoMono = models.IntegerField('Imperfeito Mono')
    imperfeitoDi = models.IntegerField('Imperfeito Di')
    imperfeitoTri = models.IntegerField('Imperfeito Tri')
    imperfeitoTetra = models.IntegerField('Imperfeito Tetra')
    imperfeitoPenta = models.IntegerField('Imperfeito Penta')
    imperfeitoHexa = models.IntegerField('Imperfeito Hexa')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def get_total_data_statistic(project):
        cursor = connection.cursor()
        cursor.execute(f"""
        SELECT
        -- Totais de Padrões
            SUM( mono ),
            SUM( di ),
            SUM( tri ),
            SUM( tetra ),
            SUM( penta ),
            SUM( hexa ),
        -- Perfeitos x Imperfeitos
            SUM( totalPerfeitos ),
            SUM( totalImperfeitos ),
        -- Totais Perfeitos
            SUM( perfeitoMono ), 
            SUM( perfeitoDi ), 
            SUM( perfeitoTri ), 
            SUM( perfeitoTetra ), 
            SUM( perfeitoPenta ), 
            SUM( perfeitoHexa ),
        -- Totais Imperfeitos
            SUM( imperfeitoMono ), 
            SUM( imperfeitoDi ), 
            SUM( imperfeitoTri ), 
            SUM( imperfeitoTetra ), 
            SUM( imperfeitoPenta ), 
            SUM( imperfeitoHexa ),
        -- Perfeitos Codificantes x Perfeitos Não-Codificantes
            SUM(totalPerfeitosCodificantes), 
            SUM(totalPerfeitosNaoCodificantes),
        -- Imperfeitos Codificantes x Imperfeitos Não-Codificantes
            SUM(totalImperfeitosCodificantes),
            SUM(totalImperfeitosNaoCodificantes),
        -- Codificantes x Não-Codificantes
            SUM(totalCodificante),
            SUM(totalNaoCodificante)
        FROM
        microssatelites_datastatistic
        WHERE project_id = {project} """)
        rows_cepas = cursor.fetchall()
        return rows_cepas