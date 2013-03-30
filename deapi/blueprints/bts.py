from flask import Blueprint, render_template, abort, request
from deapi.emitters import emit
from deapi.services.pts import query


bts = Blueprint(
    'bts',
    __name__,
    template_folder='templates'
)


@bts.route("/get-status/<bugnumbers>", methods=['GET'])
def get_status(bugnumbers):
    return emit(query_get_status(bugnumbers), True)


@bts.route("/get-bugs/<conditions>", methods=['GET'])
def get_bugs(conditions):
	return emit(query_get_bugs(conditions), True)

@bts.route("/get-usertag/<email>", methods=['GET'])
def get_usertag(email):
	return emit(query_get_usertag(email), True)


@bts.route("/get-bug-log/<int:bugnumber>", methods=['GET'])
def get_bug_log(bugnumber):
	return emit(query_get_bug_log(bugnumber), True)


@bts.route("/newest-bugs/<int:amount>", methods=['GET'])
def newest_bugs(amount):
	return emit(query_newest_bugs(amount), True)


@bts.route("/get-versions/<package>/<dist>/<arch>", methods=['GET'])
def get_versions(package, dist, arch):
	return emit(query_get_versions(package, dist, arch), True)


#@bts.route("//<source_name>", methods=['GET'])
#def (source_name):
#    return emit(query("", source_name), True)
