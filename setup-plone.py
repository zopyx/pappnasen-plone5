import transaction

import plone.api
from plone import namedfile
from plone.registry.interfaces import IRegistry
from plone.app.textfield.value import RichTextValue
from Testing.makerequest import makerequest
from zope.component import getUtility
from plone.app.theming.browser.controlpanel import ThemingControlpanel
from plone.registry.interfaces import IRegistry
from zope.component.hooks import setSite

from Products.CMFPlone.factory import addPloneSite
from AccessControl.SecurityManagement import newSecurityManager


class MyThemingControlpanel(ThemingControlpanel):
    def authorize(self):
        return True


uf = app.acl_users
user = uf.getUser("admin")
newSecurityManager(None, user.__of__(uf))

if "plone" in app.objectIds():
    app.manage_delObjects(["plone"])

addPloneSite(
    app,
    "plone",
    extension_ids=[
        "zopyx.ipsumplone:default",
        "collective.easyform:default",
        "plone.restapi:default",
        "plone.app.multilingual:default",
    ],
)


site = app.plone
site = makerequest(site)

site.REQUEST.form["form.button.Enable"] = "DONE"
site.REQUEST.form["themeName"] = "barceloneta"
view = MyThemingControlpanel(site, site.REQUEST)
view.update()

setSite(site)

plone.api.user.create(
    username="editor",
    password="editor",
    roles=("Member", "Editor"),
    email="test@test.de",
)
plone.api.user.create(
    username="reader",
    password="reader",
    roles=("Member", "Reader"),
    email="test@test.de",
)
plone.api.user.create(
    username="admin2",
    password="admin2",
    roles=("Member", "Manager"),
    email="test@test.de",
)
plone.api.user.create(
    username="siteadmin",
    password="siteadmin",
    roles=("Member", "Site Administrator"),
    email="test@test.de",
)

site = app["plone"]
site.restrictedTraverse("@@demo-content")()
print(site.objectIds())

fp = plone.api.content.create(
    container=site, type="Document", id="front-page", title="front-page"
)
plone.api.content.transition(fp, "publish")
fp.setTitle("Plone 6 demo site")
fp.setDescription(
    "Welcome to the Plone 6 demo website - provided by ZOPYX. Feel free to play around with Plone 5!"
)


with open("data/frontpage.html", "r") as handle:
    fp.text = RichTextValue(handle.read(), "text/html", "text/html")
fp.reindexObject()

site.default_page = "front-page"

print("commited")
transaction.commit()
