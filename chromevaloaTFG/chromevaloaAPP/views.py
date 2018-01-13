# -*- encoding: utf-8 -*-

#Django stuff
from django.shortcuts import get_object_or_404, render
from chromevaloaAPP.models import SelContigTable,Fulllengther2,SelUnigeneTable,Read2,Cluster2

from chromevaloaAPP.tables import SelUnigeneTableTable, SelContigTableTable
from django.http import HttpResponse
from django_tables2 import RequestConfig
#For I18N
from django.utils.translation import ugettext as _
#For calling Blast from python
from Bio.Blast import NCBIWWW
#For parsing Blast output
from Bio.Blast import NCBIXML
#The 3 different types of blast
from Bio.Blast.Applications import NcbitblastxCommandline
from Bio.Blast.Applications import NcbitblastnCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
#For file handling
import sys
import os
#For exporting data to csv
import djqscsv
#For checking if blast query is correct
from ast import literal_eval
from django.views.static import serve
#For clustal and jalview
from Bio.Align.Applications import ClustalOmegaCommandline

from django.core.servers.basehttp import FileWrapper

#Obtain the client ip adress to save the data
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:   
        ip = request.META.get('REMOTE_ADDR')
    return ip

    
def blast(request):
    path = os.path.dirname(os.path.abspath(__file__))
    #If sequence exist in request.POST, the user has clicked the submit button
    if 'sequence' in request.POST or 'file' in request.FILES:
        #If the sequence is not empty, we can continue
        sequence = request.POST["sequence"].replace(" ","").replace("\r","").replace("\n","").replace("\t","")
        isThereAFile = ('file' in request.FILES)

        if sequence != "" or isThereAFile:
            sequence = request.POST["sequence"].upper()
            formatP = request.POST["formatP"]
            blast = request.POST["blast"]
            evalueI = request.POST["evalue"]
            db = request.POST["db"]
            hits = request.POST["hits"]
            ip = get_client_ip(request)

            #We check with sets if the query is formed by correct chars
            sequence = sequence.replace(" ","").replace("\r","").replace("\n","").replace("\t","")
            querySet = set(literal_eval(str(list(sequence))))
            tblastnSet = set(['A','C','G','T','U','W','S','M','K','R','Y','B','D','H','V','n','-','.'])
            blastSet = set(['A','C','G','T','U','R','Y','S','W','K','M','B','D','H','V','N','-','.'])
            if (blast == "tblastn"):
                if (not querySet.issubset(tblastnSet)):
                    return render(request, 'chromevaloaAPP/blastOutput.html',{'blast_record': "ERROR WRONG"})
            else:
                if (not querySet.issubset(blastSet)):
                    return render(request, 'chromevaloaAPP/blastOutput.html',{'blast_record': "ERROR WRONG"})

            #We check the hits and evalue fields
            try:
                float(evalueI)
            except ValueError:
                return render(request, 'chromevaloaAPP/blastOutput.html',{'blast_record': "ERROR EVALUE"})

            if not hits.isdigit():
                return render(request, 'chromevaloaAPP/blastOutput.html',{'blast_record': "ERROR HITS"})

            #We try to make the folder for the files
            try:
                os.makedirs(path + "/blastOutput/"+ip)
            except:
                #The folder already exists
                pass 

            #If there is a file, I read the file

            try:
                f = request.FILES['file'];
                fName = f.name
                if formatP == "genbank":
                    content = f.read()
                    prueba =  content.split("ORIGIN")[1].split("\n")
                    acum = ""
                    for line in prueba:
                        acum += str(line.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").
                            replace("6","").replace("7","").replace("8","").replace("9","").replace(" ",""))
                    acum = acum[0:-2]
                    with open(path + "/blastOutput/"+ip+'/' +fName, 'wb+') as destination:
                        destination.write(acum)
                elif formatP =="embl":
                    content = f.read()
                    prueba =  content.split("SQ")[1].split("\n")
                    acum = ""
                    for line in prueba[1:len(prueba)]:
                        acum += str(line.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").
                            replace("6","").replace("7","").replace("8","").replace("9","").replace(" ",""))
                    acum = acum[0:-2]
                    with open(path + "/blastOutput/"+ip+'/' +fName, 'wb+') as destination:
                        destination.write(acum)
                else:
                    with open(path + "/blastOutput/"+ip+'/' +fName, 'wb+') as destination:
                        for chunk in f.chunks():
                            destination.write(chunk)
            #If not, the sequenece of the text gap
            except:
                fName = "query.txt"
                print "exceptioneee"
                with open(path + "/blastOutput/"+ip+'/' + fName, 'wb+') as destination:
                	destination.write(sequence)

            #Inicialice the params of blast
            query_param = path + "/blastOutput/"+ip+"/"+fName
            db_param = path + "/db/"+db
            evalue_param = evalueI
            outfmt_param = 5 #xml
            out_param = path + "/blastOutput/"+ip+"/blastOutput.xml"

            if (blast == "tblastx"):
            	blastn_cline = NcbitblastxCommandline(query=query_param, db=db_param,\
            		evalue=evalue_param, max_target_seqs= hits, outfmt=outfmt_param,out=out_param)
            elif(blast == "tblastn"):
            	blastn_cline = NcbitblastnCommandline(query=query_param, db=db_param,\
            		evalue=evalue_param, max_target_seqs= hits, outfmt=outfmt_param,out=out_param)
            elif(blast == "blastn"):
           		blastn_cline = NcbiblastnCommandline(query=query_param, db=db_param,\
           			evalue=evalue_param, max_target_seqs= hits, outfmt=outfmt_param,out=out_param)

            os.system(str(blastn_cline))
            result_handle = open(path + "/blastOutput/"+ip+"/blastOutput.xml")
            try:
                blast_record = NCBIXML.read(result_handle)
            except:
                return render(request, 'chromevaloaAPP/blastOutput.html',{'blast_record': "ERROR BLAST"})

            #If all was ok
            return render(request, 'chromevaloaAPP/blastOutput.html',\
                {'blast_record': blast_record, 'db':db})
        #If the query was empty
        return render(request, 'chromevaloaAPP/blastOutput.html',{'blast_record': "ERROR EMPTY"})
    #If the user didn't press the submit button (Initial page)
    return render(request, 'chromevaloaAPP/blast.html')

def index(request):
    return render(request, 'chromevaloaAPP/index.html')

def getBrowseCSV(request):
    data = SelContigTable.objects.values('idcontig','descrip','numreads','accession','evalue','identity','selected')
    filename = djqscsv.generate_filename(data, append_datestamp=True) 
    return djqscsv.render_to_csv_response(data,filename)    

def getExpressionCSV(request):
    data = SelUnigeneTable.objects.all().select_related('Expression').values('accession','descrip')
    filename = djqscsv.generate_filename(data, append_datestamp=True) 
    return djqscsv.render_to_csv_response(data,filename)



def getAlnFile(request):
    path = os.path.dirname(os.path.abspath(__file__))
    ip = get_client_ip(request)
    file = open( path + "/jalview/"+ip+'/clustalOUT.aln')
    response = HttpResponse(file, content_type='text/txt')
    response['Content-Disposition'] = 'attachment; filename=myfile.aln'
    return response
    
def browse(request):
    table = SelContigTableTable(SelContigTable.objects.values \
        ('idcontig','descrip','numreads','accession','evalue','identity','selected','result')\
        .filter(selected = 'Y'))
    
    RequestConfig(request,paginate={"per_page": 20}).configure(table)
    return render(request, 'chromevaloaAPP/browse.html', {'SelContigTableTable': table})


def expression(request):
    table = SelUnigeneTableTable(SelUnigeneTable.objects.values('idcontig','accession','descrip','expr')) #tambien expr

    RequestConfig(request,paginate={"per_page": 20}).configure(table)
    return render(request, 'chromevaloaAPP/expression.html', {'SelUnigeneTableTable': table})

def details(request,accession):
    table = SelContigTable.objects.values('idcontig','contigseq').filter(idcontig__icontains=accession)
    #$sql = "SELECT contigSEQ FROM contigseq WHERE IDcontig = '$IDcontig'"
    #contig = get_object_or_404(Contigseq, contigseq=accession)
    return render(request, 'chromevaloaAPP/details.html',{'idcontig': table[0].get("idcontig"), "contigseq" : table[0].get("contigseq").upper()})

def jalview(request,contig):
    print "\n\nJALVIEW! \n\n"
    
    path = os.path.dirname(os.path.abspath(__file__))
    ip = get_client_ip(request)
    idcluster = Cluster2.objects.values('idcluster').filter(idcontig=contig)
    sequences = Read2.objects.values('idread','readseq').filter(idcluster__in=idcluster)
    #print "idcluster -> " + str(idcluster)
    #print "sequences -> " + str(sequences)

 
    try:
        os.makedirs(path + "/jalview/"+ip)
    except:
        #The folder already exists
        pass 


    with open(path + "/jalview/"+ip+'/clustalIN.fasta', 'wb+') as destination:
        print "REAAAAAAAAAAAAAD"+destination.read()
        for sequence in sequences:
            destination.write(">" + str(sequence["idread"]) + "\n")
            destination.write(sequence["readseq"] + "\n")

    in_file = path + "/jalview/"+ip+'/clustalIN.fasta'
    out_file = path + "/jalview/"+ip+'/clustalOUT.aln'
    clustalomega_cline = ClustalOmegaCommandline(infile=in_file, outfile=out_file, verbose=True, auto=False)
    print clustalomega_cline
    os.system(str(clustalomega_cline) +  '  --force ')
    return render(request, 'chromevaloaAPP/jalview.html',{'idcontig':contig})

def programHelp(request):
    return render(request, 'chromevaloaAPP/programHelp.html')

def dbHelp(request):
    return render(request, 'chromevaloaAPP/dbHelp.html')

def searchBrowse(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET["q"]
        field = request.GET["field"]
        if not q:
            errors.append(_('Enter a search term.'))
        elif len(q) > 30:
            errors.append(_('Please enter at most 30 characters.'))
        else:
            if field=="idcontig":
                table = SelContigTableTable(SelContigTable.objects.filter(idcontig__icontains=q))
            elif field == "descrip":
                table = SelContigTableTable(SelContigTable.objects.filter(descrip__icontains=q))
            elif field == "numreads":
                table = SelContigTableTable(SelContigTable.objects.filter(numreads__icontains=q))
            elif field == "accession":
                table = SelContigTableTable(SelContigTable.objects.filter(accession__icontains=q))
            elif field == "evalue":
                table = SelContigTableTable(SelContigTable.objects.filter(evalue__icontains=q))
            elif field == "identity":
                table = SelContigTableTable(SelContigTable.objects.filter(identity__icontains=q))
            elif field == "orf":
                table = SelContigTableTable(SelContigTable.objects.filter(result__icontains=q))
           #elif field == "result":
            #    table = DefContigTable(SelContigTable.objects.filter(result__icontains=q))

            RequestConfig(request,paginate={"per_page": 20}).configure(table)
            return render(request, 'chromevaloaAPP/browse.html', {'SelContigTableTable': table})

    table = SelContigTableTable(SelContigTable.objects.values \
        ('idcontig','descrip','numreads','accession','evalue','identity','selected'))
    RequestConfig(request,paginate={"per_page": 20}).configure(table)
    return render(request, 'chromevaloaAPP/browse.html', {'SelContigTableTable': table, 'errors': errors})


def searchExpression(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        field = request.GET["field"]

        if not q:
            errors.append(_('Enter a search term.'))
        elif len(q) > 30:
            errors.append(_('Please enter at most 30 characters.'))
        else:
            if field=="accession":
                table = SelUnigeneTableTable(SelUnigeneTable.objects.filter(accession__icontains=q))
            elif field == "descrip":
                table = SelUnigeneTableTable(SelUnigeneTable.objects.filter(descrip__icontains=q))
            RequestConfig(request,paginate={"per_page": 20}).configure(table)
            return render(request, 'chromevaloaAPP/expression.html', {'SelUnigeneTableTable': table})

    table = SelUnigeneTableTable(SelUnigeneTable.objects.all()\
        .select_related('Expression').values('accession','descrip')) #tambien expr
    RequestConfig(request,paginate={"per_page": 20}).configure(table)
    return render(request, 'chromevaloaAPP/expression.html', {'SelUnigeneTableTable': table, 'errors': errors})


def handler404(request):
    return render(request, 'chromevaloaAPP/404.html')

def handler500(request):
    return render(request, 'chromevaloaAPP/500.html')
