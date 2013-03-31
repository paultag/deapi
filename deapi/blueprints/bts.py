from flask import Blueprint, render_template, abort, request
from deapi.emitters import emit
from deapi.services.bts import query


bts = Blueprint(
    'bts',
    __name__,
    template_folder='templates'
)


# TODO: Support multiple bugnumbers
@bts.route("/get-status/<int:bugnumber>", methods=['GET'])
def get_status(bugnumber):
	ret = query("get_status", bugnumber)
	serialize = dict()
	for key in ret._asdict()['item']._asdict()['value']._asdict():
		value = ret._asdict()['item']._asdict()['value']._asdict()[key]
		if isinstance(value, basestring) or isinstance(value, int) or type(value) is list:
			serialize[key] = value
		else:
			serialize[key] = value._asdict()
	return emit(serialize, True)


@bts.route("/get-bugs/<conditions>", methods=['GET'])
def get_bugs(conditions):
	conditions = conditions.split(',')
	return emit(query("get_bugs", conditions)._aslist(), True)

@bts.route("/get-usertag/<email>", methods=['GET'])
def get_usertag(email):
	ret = query("get_usertag", email)
	serialize = dict()
	if isinstance(ret._aslist()[0][0], int):
		for pair in ret._asdict():
			serialize[pair] = ret._asdict()[pair]._aslist()
	else:
		for pair in ret._aslist()[0]:
			serialize[pair['key']] = pair['value']._aslist()
	return emit(serialize, True)

@bts.route("/get-bug-log/<int:bugnumber>", methods=['GET'])
def get_bug_log(bugnumber):
	ret = query("get_bug_log", bugnumber)
	serialize = []
	for message in ret:
		messagedict = dict()
		for key in message._asdict():
			if isinstance(message[key], basestring) or isinstance(message[key], int):
				messagedict[key]=message[key]
			else:
				messagedict[key]=message[key]._aslist()
		serialize.append(messagedict)
	return emit(serialize, True)

@bts.route("/newest-bugs/<int:amount>", methods=['GET'])
def newest_bugs(amount):
	return emit(query("newest_bugs", amount)._aslist(), True)

@bts.route("/get-versions/<package>/<dist>/<arch>", methods=['GET'])
def get_versions(package, dist, arch):
	return emit(query("get_versions", {"package":package, "dist":dist, "arch":arch})._aslist(), True)


#@bts.route("//<source_name>", methods=['GET'])
#def (source_name):
#    return emit(query("", source_name), True)
