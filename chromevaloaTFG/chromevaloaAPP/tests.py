from django.test import TestCase,RequestFactory
from chromevaloaAPP.models import DefContig
from views import searchBrowse




class defContigTest(TestCase):
	def setUp(self):
		# Every test needs access to the request factory.
		print "setup"
		self.factory = RequestFactory()

		#DefContig.objects.create(idcontig="",descrip="",accession="",length="",evalue="",identity="",goprocess="",gofunction="",ec="",ips="",numreads="",selected="")
		DefContig.objects.create(idcontig="",descrip="",accession="",length=1,evalue=1.0,identity=1.0,goprocess="",gofunction="",ec="",ips="",numreads=1,selected="")
	def test_search_browse(self):
		print "test"
		# Create an instance of a GET request.
		request = self.factory.get('/browse/search/?field=descrip&q=chromatin')

		# Test my_view() as if it were deployed at /customer/details
		response = searchBrowse(request)
		self.assertEqual(response.status_code, 200)
		self.assertEqual(request.GET["q"],"chromatin")
		self.assertEqual(request.GET["field"],"descrip")