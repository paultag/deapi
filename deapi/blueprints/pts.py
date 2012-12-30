from flask import Blueprint, render_template, abort, request
from deapi.emitters import emit
from deapi.services.pts import query


pts = Blueprint(
    'pts',
    __name__,
    template_folder='templates'
)


@pts.route("/versions/<source_name>", methods=['GET'])
def versions(source_name):
    ret = query("versions", source_name)
    if isinstance(ret, basestring):
        ret = {"unstable": ret}  # This is a dirty, dirty lie.
    return emit(ret, True)


@pts.route("/latest-version/<source_name>", methods=['GET'])
def latest_version(source_name):
    return emit(query("latest_version", source_name), True)


@pts.route("/maintainer/<source_name>", methods=['GET'])
def maintainer(source_name):
    return emit(query("maintainer", source_name), True)


@pts.route("/uploaders/<source_name>", methods=['GET'])
def uploaders(source_name):
    return emit(query("uploaders", source_name)._aslist(), True)


@pts.route("/standards-version/<source_name>", methods=['GET'])
def standards_version(source_name):
    return emit(query("standards_version", source_name), True)


@pts.route("/priority/<source_name>", methods=['GET'])
def priority(source_name):
    return emit(query("priority", source_name), True)


@pts.route("/section/<source_name>", methods=['GET'])
def section(source_name):
    return emit(query("section", source_name), True)


@pts.route("/binary-names/<source_name>", methods=['GET'])
def binary_names(source_name):
    return emit(query("binary_names", source_name)._aslist(), True)


@pts.route("/lintian/<source_name>", methods=['GET'])
def lintian(source_name):
    return emit(query("lintian", source_name), True)


@pts.route("/bugs/<source_name>", methods=['GET'])
def bugs(source_name):
    return emit(query("bug_counts", source_name), True)


#@pts.route("//<source_name>", methods=['GET'])
#def (source_name):
#    return emit(query("", source_name), True)
