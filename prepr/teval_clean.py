"""Clean freshly imported teaching evaluation collections."""

from pymongo import MongoClient

from mymodules import cleanings

scheme = MongoClient().exams
teval = scheme.create_collection("teachEval")

cln = cleanings.Cleaner(teval)
cln.set_qset(cleanings.QSET_OLD)
cln.clean(scheme.rawTeachingsEv1011, 2010, True)

cln.set_qset(cleanings.QSET_GEN)
cln.clean(scheme.rawTeachingsEv1112, 2011, True)
cln.clean(scheme.rawTeachingsEv1213, 2012, True)
cln.clean(scheme.rawTeachingsEv1314, 2013, True)
cln.clean(scheme.rawTeachingsEv1415, 2014, True)
cln.clean(scheme.rawTeachingsEv1516, 2015, True)
cln.clean(scheme.rawTeachingsEv1617, 2016, True)

cln.drop()

