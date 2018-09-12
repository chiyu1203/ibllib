## Init
from oneibl.one import ONE
from ibllib.misc import pprint
one = ONE(base_url='https://test.alyx.internationalbrainlab.org', username='test_user',
          password='TapetesBloc18')

## Find an experiment
eid = one.search(users='olivier', date_range=['2018-08-24', '2018-08-24'])
pprint(eid)
one.search_terms()

## List dataset types for a session
eid = '86e27228-8708-48d8-96ed-9aa61ab951db'
one.list(eid)
## More Info about a session
d = one.list(eid, 'All')

## Get More Info about datasets
d = one.list(eid, details=True)
print(d)

print(d)
## List #1
one.list(None, 'dataset-types')
one.list(None, 'users')
one.list(None, 'subjects')

## Load #1
dataset_types = ['clusters.templateWaveforms', 'clusters.probes', 'clusters.depths']
eid = '86e27228-8708-48d8-96ed-9aa61ab951db'
wf, pr, d = one.load(eid, dataset_types=dataset_types)

## Load #2
my_data = one.load(eid, dataset_types=dataset_types, dclass_output=True)
from ibllib.misc import pprint
pprint(my_data.local_path)
pprint(my_data.dataset_type)

## Load everything
eid = one.search(subjects='flowers')
my_data = one.load(eid[0])
pprint(my_data.dataset_type)

## Load
eid = '86e27228-8708-48d8-96ed-9aa61ab951db'
dataset_types = ['clusters.probes', 'thisDataset.IveJustMadeUp', 'clusters.depths']
t, empty, cl = one.load(eid, dataset_types=dataset_types)



## Search users
eid = one.search(users=['olivier'])

eid = one.search(users=['nbonacchi', 'olivier'])
# with details
eid, session_details = one.search(users=['nbonacchi', 'olivier'], details=True)
pprint(session_details)

## Search by date
eid = one.search(users='olivier', date_range=['2018-08-24', '2018-08-24'])

