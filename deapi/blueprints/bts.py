from flask import Blueprint, render_template, abort, request
from deapi.emitters import emit
from deapi.services.bts import query, query_get_versions


bts = Blueprint(
    'bts',
    __name__,
    template_folder='templates'
)


@bts.route("/get-status/<bugnumbers>", methods=['GET'])
def get_status(bugnumbers):
    return emit(query("get_status", bugnumbers), True)


@bts.route("/get-bugs/<conditions>", methods=['GET'])
def get_bugs(conditions):
	return emit(query("get_bugs", conditions), True)


@bts.route("/get-usertag/<email>", methods=['GET'])
def get_usertag(email):
	return emit(query("get_usertag", email), True)


@bts.route("/get-bug-log/<int:bugnumber>", methods=['GET'])
def get_bug_log(bugnumber):
	return emit(query("get_bug_log", bugnumber), True)


@bts.route("/newest-bugs/<int:amount>", methods=['GET'])
def newest_bugs(amount):
	return emit(query("newest_bugs", amount), True)


@bts.route("/get-versions/<package>/<dist>/<arch>", methods=['GET'])
def get_versions(package, dist, arch):
	return emit(query_get_versions(package, dist, arch), True)


#@bts.route("//<source_name>", methods=['GET'])
#def (source_name):
#    return emit(query("", source_name), True)
