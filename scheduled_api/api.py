# Copyright (c) 2022, Totrox & Aakvatech and contributors
# For license information, please see license.txt

import frappe, json
from scheduled_api.process import enqueue_execute


@frappe.whitelist()
def add_request(
    method,
    data,
    callback_url=None,
    callback_profile=None,
    tag=None,
    reference_id=None,
    ref_doctype=None,
    ref_docname=None,
):
    if isinstance(data, dict):
        data = json.dumps(data)
    elif isinstance(data, object):
        data = json.dumps(frappe._dict(data))
    doc = frappe.new_doc("Schedule Request")
    doc.method = method
    doc.data = data
    doc.callback_url = callback_url
    doc.callback_profile = callback_profile
    doc.tag = tag
    doc.reference_id = reference_id
    doc.insert(ignore_mandatory=True, ignore_permissions=True)
    frappe.response["data"] = doc.as_dict()
    frappe.db.commit()
    enqueue_execute(doc.name)
