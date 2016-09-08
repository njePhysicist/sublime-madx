#/bin/python
#A python script to automate generating the rules for elements and attributes

#Sample of a command...
# madxCommand:
#   patterns:
#   - begin: (?i)\b(QUADRUPOLE)\b
#     beginCaptures:
#       '1': {name: keyword.operator.madx}
#     end: (?=\;)
#     patterns:
#     - include: '#attributes'

def repositoryName(key):
	"""
	Creates the name used in the repository for a particular key.
	This is a separate function so that all relevant parties can call
	this function and changes will propagate.
	"""
	return 'att'+key

def createRegexString(atts):
	"""Creates the regex string for the list of attributes."""
	rs = "\t\t\tmatch: (?i)\\b("
	for v in atts:
		rs += v+"|"
	rs = rs[:-1]
	rs += ")(\s*)((\=)|\:\=)"
	return rs

def attributesRepositoryEntry(key,atts):
	print '\t'+repositoryName(key)+':'
	print '\t\tpatterns:'
	print '\t\t- comment: Attributes'
	rs = createRegexString(atts)
	print rs
	print '\t\t\tcaptures:'
	print '\t\t\t\t\'1\': {name: keyword.attribute.cattribute}'


def commandRepositoryEntry(command):
	print '\t\t- begin: (?i)\\b('+command+')(\\s*)\\b'
	print '\t\t\tbeginCaptures:'
	print '\t\t\t\t\'1\': {name: keyword.operator.madx}'
	print '\t\t\tend: (?=\;)'
	print '\t\t\tpatterns:'
	#Add the attributes
	print '\t\t\t- include: \'#'+repositoryName(command)+'\''

def commandRepositoryEntryWithAtts(command,atts):
	print '\t\t- begin: (?i)\\b('+command+')(\\s*)\\b'
	print '\t\t\tbeginCaptures:'
	print '\t\t\t\t\'1\': {name: keyword.operator.madx}'
	print '\t\t\tend: (?=\;)'
	print '\t\t\tpatterns:'
	#Add the attributes
	print '\t\t\t- comment: Attributes'
	rs = createRegexString(atts)
	print '\t'+rs
	print '\t\t\t\tcaptures:'
	print '\t\t\t\t\t\'1\': {name: keyword.attribute.cattribute}'
	print '\t\t\t- include: \'#madxComments\''
	print '\t\t\t- include: \'#madxOperators\''
	


d = {
	'OPTION'     :['FLAG'],
	'SET'        :['FORMAT','SEQUENCE'],
	'USE'        :['SEQUENCE','PERIOD','RANGE','SURVEY'],
	'SELECT'     :['FLAG','RANGE','CLASS','PATTERN','SEQUENCE','FULL','CLEAR','COLUMN','SLICE','THICK'],
	'BEAM'       :['PARTICLE','MASS','CHARGE','ENERGY','PARTICLEGAMMA','BETA','BRHO','EX','EXN','EY','EYN','EY','SIGT','SIGE','KBUNCH','NPART','BCURRENT','BUNCHED','RADIATE','BV','SEQUENCE'],
	'RESBEAM'    :['SEQUENCE'],
	'DRIFT'      :['L'], #FIRST ELEMENT TYPE
	'SBEND'      :['L','ANGLE','TILT' ,'K0'   ,'K1'   ,'K2'   ,'E1'   ,'E2'   ,'FINT','FINTX','HGAP','H1','H2','THICK'],
	'RBEND'      :['L','ANGLE','TILT' ,'K0'   ,'K1'   ,'K2'   ,'E1'   ,'E2'   ,'FINT','FINTX','HGAP','H1','H2','THICK'],
	'DIPEDGE'    :['H','E1','FINT','HGAP','TILT'],
	'QUADRUPOLE' :['L','K1','K1S','TILT','THICK'],
	'SEXTUPOLE'  :['L','K2','K2S','TILT'],
	'OCTUPOLE'   :['L','K3','K3S','TILT'],
	'MULTIPOLE'  :['LRAD','TILT','KNL','KSL'],
	'SOLENOID'   :['L','KS','KSI'],
	'NLLENS'     :['KNLL','CNLL'],
	'KICKER'     :['L','KICK','TILT','HKICK','VKICK'],
	'TKICKER'    :['L','KICK','TILT','HKICK','VKICK'],
	'HKICKER'    :['L','KICK','TILT'],
	'VKICKER'    :['L','KICK','TILT',],
	'RFCAVITY'   :['L','VOLT','LAG','FREQ','HARMON','N_BESSEL','NO_CAVITY_TOTALPATH'],
	'RFMULTIPOLE':['L','VOLT','LAG','FREQ','HARMON','LRAD','TILT','KNL','KSL','PNL','PSL'],
	'CRABCAVITY' :['L','VOLT','LAG','FREQ','HARMON','RV1','RV2','RV3','RV4','RPH1','RPH2','LAGF'],
	'ELSEPARATOR':['L','EX','EY','TILT'],
	'MONITOR'    :['L'],
	'VMONITOR'   :['L'],
	'HMONITOR'   :['L'],
	'INSTRUMENT' :['L'],
	'PLACEHOLDER':['L'],
	'COLLIMATOR' :['L','APERTYPE','APERTURE','APER_OFFSET','APER_TOL'],
	'ECOLLIMATOR':['L','XSIZE','YSIZE'],
	'RCOLLIMATOR':['L','XSIZE','YSIZE'],
	'BEAMBEAM'   :['CHARGE','XMA','YMA','SIGX','SIGY','WIDTH','BBSHAPE','BBDIR'],
	'MATRIX'     :['TYPE','L','KICK1','KICK6','RM11','RM66','TM111','TM666'],
	'YROTATION'  :['ANGLE'],
	'SROTATION'  :['ANGLE'],
	'TRANSLATION':['X','Y','T','PX','PY','PT'],
	'CHANGEREF'  :['PATCH_ANG','PATCH_TRANS'] #LAST ELEMENT TYPE
	}

#dOdd is odd commands that have no attributes or behave differently. 
dOdd = {
	'MARKER',
	'RANGE' ,
	'LINE'  
	# 'SEQUENCE'   :['L','REFER','REFPOS','ADD_PASS','NEXT_SEQU'] # ENDS WITH ENDSEQUENCE; NEED A BEGIN/END MATCH FOR THIS ONE.
	}

for k in d.keys():
	# commandRepositoryEntry(k)
	commandRepositoryEntryWithAtts(k,d[k])
print '\t\t- include: \'#madxComments\''
print '\t\t- include: \'#madxOperators\''
# for k in d.keys():
# 	attributesRepositoryEntry(k,d[k])

