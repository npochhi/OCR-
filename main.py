import subprocessimport globimport sysimport xml.etree.ElementTree as ETimport footnotesimport citationpdfDirectory = "PDFDirectory/"pdfToXMLDirectory = "PDFtoXML/"def runScript():	pdfFiles = glob.glob(pdfDirectory + "*.pdf")	for file in pdfFiles:		pdfFileName = file.split('/')[1].split('.')[0].split('/')[-1]		subprocess.call("./pdftoxml.exe -noImage -noImageInline " + pdfDirectory + pdfFileName + \			".pdf " + pdfToXMLDirectory + pdfFileName + ".xml", shell = True)		XMLFile = pdfToXMLDirectory + pdfFileName + ".xml"		XMLTree = ET.parse(XMLFile)		XMLRoot = XMLTree.getroot()		if '-f' in sys.argv or '-a' in sys.argv:			try:				footnotes.footnoteMain(XMLRoot, pdfFileName)			except Exception: 				print "Excepion occurred while processing Footnotes!"		if '-c' in sys.argv or '-a' in sys.argv:			citation.mainf(XMLRoot, pdfFileName)runScript()		