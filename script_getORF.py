#Importando as bibliotecas do módulo sys e das expressões regulares:
import sys
import re

#Abrindo, lendo e salvando na variável "FASTA" o arquivo contendo o DNA em arquivo FASTA:
FASTA=open("multifasta2","r")
FASTA=FASTA.read()

#Criando a expessão regular para cortar os ORFs da variável "FASTA.obj":
pattern = '(?<=ATG).*(?=TAA)|(?=TGA)|(?=TAG)' 
result = re.findall(pattern, FASTA)

#Criando a variável "len.ORF" onde o comando sorted irá permitir a contagem e identificação da maior cadeia de ORF:
len_ORF=sorted(result, key=len)[-1]
print("Cadeia encontrada de maior tamanho:",len_ORF)
KK=len(len_ORF)
print("A quantidade de bases nitrogenadas entre o codon de início e o de parada é:",KK)

#Conferindo se o maior ORF é múltiplo de três:
#Inserindo o maior ORF encontrado no arquivo "ORF.fna", se o ORF for multiplo de 3:
mult=len(len_ORF)
div=mult/3
div2=float.is_integer(div)
if div2 is True:
 print("ORF correto pois é múltiplo de três")
 MaiorORF=open("ORF.fna","w")
 MaiorORF.write(len_ORF)
else:
 print("Falha - O ORF não é múltiplo de três")

#Criando um gerador de peptídeos, através de um dicionário:
peptideo_dict={'Valina':'GTT,GTG,GTC,GTA','Fenilalanina':'TTT,TTC,TTA,TTG','Leucina':'CTT,CTC,CTA,CTG','Isoleucina':'ATA,ATC,ATA','Serina':'AGT,AGC,TCT,TCC,TCA,TCG','Prolina':'CCT,CCC,CCA,CCG','Treonina':'ACT,ACC,ACA,ACG','Alanina':'GCT,GCC,GCA,GCG','Lisina':'AAA,AAG','Aspargina':'AAU,AAC','Glutamina':'CAA,CAG','Histidina':'CAC,CAT','Tirosina':'TAT,TAC','Cisteina':'TGT,TGC','Triptofano':'TGG','Arginina':'AGA,AGG,CGT,CGC,CGA,CGG','Glicina':'GGT,GGC,GGA,GGG'}
codons = re.findall(r"(.{3})",len_ORF)
print("Bases que serão transcitas e posteriormente utilizadas no ribossomo, para criação do peptídeo:",codons)

#Criando um ribossomo virtual:
codon1=codons[0]
codon2=codons[1]
codon3=codons[2]
codon4=codons[3]

if codon1 in peptideo_dict['Alanina']:
 codon1='Alanina'
if codon2 in peptideo_dict['Alanina']:
 codon2='Alanina'
if codon3 in peptideo_dict['Alanina']:
 codon3='Alanina'
if codon4 in peptideo_dict['Alanina']:
 codon4='Alanina'
if codon1 in peptideo_dict['Leucina']:
 codon1='Leucina'
if codon2 in peptideo_dict['Leucina']:
 codon2='Leucina'
if codon3 in peptideo_dict['Leucina']:
 codon3='Leucina'
if codon4 in peptideo_dict['Leucina']:
 codon4='Leucina'
if codon1 in peptideo_dict['Isoleucina']:
 codon1='Isoleucina'
if codon2 in peptideo_dict['Isoleucina']:
 codon2='Isoleucina'
if codon3 in peptideo_dict['Isoleucina']:
 codon3='Isoleucina'
if codon4 in peptideo_dict['Isoleucina']:
 codon4='Isoleucina'
if codon1 in peptideo_dict['Serina']:
 codon1='Serina'
if codon2 in peptideo_dict['Serina']:
 codon2='Serina'
if codon3 in peptideo_dict['Serina']:
 codon3='Serina'
if codon4 in peptideo_dict['Serina']:
 codon4='Serina'
if codon1 in peptideo_dict['Fenilalanina']:
 codon1='Fenilalanina'
if codon2 in peptideo_dict['Fenilalanina']:
 codon2='Fenilalanina'
if codon3 in peptideo_dict['Fenilalanina']:
 codon3='Fenilalanina'
if codon4 in peptideo_dict['Fenilalanina']:
 codon4='Fenilalanina'
if codon1 in peptideo_dict['Prolina']:
 codon1='Prolina'
if codon2 in peptideo_dict['Prolina']:
 codon2='Prolina'
if codon3 in peptideo_dict['Prolina']:
 codon3='Prolina'
if codon4 in peptideo_dict['Prolina']:
 codon4='Prolina'
if codon1 in peptideo_dict['Treonina']:
 codon1='Treonina'
if codon2 in peptideo_dict['Treonina']:
 codon2='Treonina'
if codon3 in peptideo_dict['Treonina']:
 codon3='Treonina'
if codon4 in peptideo_dict['Treonina']:
 codon4='Treonina'
if codon1 in peptideo_dict['Lisina']:
 codon1='Lisina'
if codon2 in peptideo_dict['Lisina']:
 codon2='Lisina'
if codon3 in peptideo_dict['Lisina']:
 codon3='Lisina'
if codon4 in peptideo_dict['Lisina']:
 codon4='Lisina'
if codon1 in peptideo_dict['Aspargina']:
 codon1='Aspargina'
if codon2 in peptideo_dict['Aspargina']:
 codon2='Aspargina'
if codon3 in peptideo_dict['Aspargina']:
 codon3='Aspargina'
if codon4 in peptideo_dict['Aspargina']:
 codon4='Aspargina'
if codon1 in peptideo_dict['Glutamina']:
 codon1='Glutamina'
if codon2 in peptideo_dict['Glutamina']:
 codon2='Glutamina'
if codon3 in peptideo_dict['Glutamina']:
 codon3='Glutamina'
if codon4 in peptideo_dict['Glutamina']:
 codon4='Glutamina'
if codon1 in peptideo_dict['Histidina']:
 codon1='Histidina'
if codon2 in peptideo_dict['Histidina']:
 codon2='Histidina'
if codon3 in peptideo_dict['Histidina']:
 codon3='Histidina'
if codon4 in peptideo_dict['Histidina']:
 codon4='Histidina'
if codon1 in peptideo_dict['Tirosina']:
 codon1='Tirosina'
if codon2 in peptideo_dict['Tirosina']:
 codon2='Tirosina'
if codon3 in peptideo_dict['Tirosina']:
 codon3='Tirosina'
if codon4 in peptideo_dict['Tirosina']:
 codon4='Tirosina'
if codon1 in peptideo_dict['Cisteina']:
 codon1='Cisteina'
if codon2 in peptideo_dict['Cisteina']:
 codon2='Cisteina'
if codon3 in peptideo_dict['Cisteina']:
 codon3='Cisteina'
if codon4 in peptideo_dict['Cisteina']:
 codon4='Cisteina'
if codon1 in peptideo_dict['Triptofano']:
 codon1='Triptofano'
if codon2 in peptideo_dict['Triptofano']:
 codon2='Triptofano'
if codon3 in peptideo_dict['Triptofano']:
 codon3='Triptofano'
if codon4 in peptideo_dict['Triptofano']:
 codon4='Triptofano'
if codon1 in peptideo_dict['Arginina']:
 codon1='Arginina'
if codon2 in peptideo_dict['Arginina']:
 codon2='Arginina'
if codon3 in peptideo_dict['Arginina']:
 codon3='Arginina'
if codon4 in peptideo_dict['Arginina']:
 codon4='Arginina'
if codon1 in peptideo_dict['Glicina']:
 codon1='Glicina'
if codon2 in peptideo_dict['Glicina']:
 codon2='Glicina'
if codon3 in peptideo_dict['Glicina']:
 codon3='Glicina'
if codon4 in peptideo_dict['Glicina']:
 codon4='Glicina'
if codon1 in peptideo_dict['Valina']:
 codon1='Valina'
if codon2 in peptideo_dict['Valina']:
 codon2='Valina'
if codon3 in peptideo_dict['Valina']:
 codon3='Valina'
if codon4 in peptideo_dict['Valina']:
 codon4='Valina'

print("Cadeia peptidica formada:","Metionina-",codon1,"-",codon2,"-",codon3,"-",codon4)


