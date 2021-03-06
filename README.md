Senior Project Chromevol Web 
============

<p align="center">
<img src="https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/chromevaloa.png" width="500">
<img src="https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/tools.PNG" width="300">
</p>

This was part of the senior project of my undergrad in computer science at UDC (Spain), carried out in collaboration with the group CHROMEVOL from Florida International University and RNASA from University of La Coruña. My thesis directors were Vanessa Aguiar-Pulido (@vaguiarpulido) and Daniel Rivero Cebrián. The 165 pages report (Spanish) can be viewed [here](https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/Report.pdf) for further explanations. All the use-cases, architecture, design, testing, UML and other diagrams can be seen there.
The webpage is currently in use by the group CHROMEVOL and available here http://chromevol.fiu.edu. It was developed in Django.



## Functionalities

- View and Query the Contigs and Unigenes Database in a biology-oriented way, fully linked content and to be able to order it by any field.
- Download the database.
- Online call the tool BLAST (BLASTN, TBLASTN or TBLASTX) given as input sequences in different formats (FAST, EMBL, GENBANK or RAW) with different configuration options.
- Call Clustal Omega to align and visualize a Contig or Unigene with all Reads of the formating Clusters.
- Internationalization in Spanish and English.
- User management with groups and privileges (Search, Create, Read, Update, Remove).
- Cluster and Contig, Read management (Search, Create, Read, Update, Remove).

## Methodology

Scrum was used throughout all the project, with 3-week Sprints and constantly changing requirements. Trello with the plugin Scrum for Trello was used to manage the backlogs. 3 Sprints were necessary, without taking into account the previous phases. The Gantt diagram can be seen here:
<p align="center">
<img src="https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/gantt.png" width="700">
</p>


## Database
The Entity-Relationship model for the database can be seen here, first for the biological part and second for the user, group and privileges management:

<p align="center">
<img src="https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/ERBIO.png" width="400"><img src="https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/ERUSERS.png" width="400">
</p>



## Tools
- Django
- Python
- MySQL
- BLAST
- Clustal Omega
- HTML
- CSS
- Django-tables2
- Trello
- Scrum for Trello
- Jalview
- yEd


## Installation

- Install Python 2.7.x
```
http://heliumhq.com/docs/installing_python_2.7.5_on_ubuntu
```
- Install MySQL Server
```
https://help.ubuntu.com/12.04/serverguide/mysql.html
```
- Install pip
```
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv
```
- Install MySQL Python
```
 pip install MySQL-python 
 sudo apt-get install python-mysqldb 
```
-Install Django
```
pip install -U Django
pip install django --upgrade
```
- Install Django Extensions
```
pip install django-queryset-csv
pip install django-tables2
```
- Install BLAST
```
apt-get install ncbi-blast+
```
- Install Clustal Omega
```
sudo apt-get install clustalo
```

## Execution
```
python manage.py runserver --insecure
```
Which will execute the server in the port 8000 of localhost


## Contact

Contact [Daniel Ruiz Perez](mailto:druiz072@fiu.edu) for requests, bug reports and good jokes.


## License

The software in this repository is available under the GNU General Public License, version 3. See the [LICENSE](https://github.com/DaniRuizPerez/SeniorProjectChromevol/blob/master/LICENSE) file for more information.
