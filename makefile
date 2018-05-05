DB = exams
SCHEME= MongoClient().exams
PRDIR= cd prepr &&

all: export

reset_db:
	mongo $(DB) --eval "db.dropDatabase()"

import: reset_db
	$(PRDIR) sh import.sh

#
# teaching evaluation recipes
#
teval: teval_prune

teval_clean: import
	$(PRDIR) python3 teval_clean.py

teval_aggr: teval_clean
	$(PRDIR) python3 teval_aggr.py	

teval_merge: teval_aggr
	$(PRDIR) python3 teval_merge.py	

teval_prune: teval_merge
	$(PRDIR) python3 teval_prune.py	

#
# students productivity recipes
#
stud: stud_aggr

stud_aggr: import 
	$(PRDIR) python3 stud_aggr.py	

#
# merge and final stuff
#
merged: stud teval
	$(PRDIR) python3 datasets_merge.py


export: merged
	$(PRDIR) sh export.sh

