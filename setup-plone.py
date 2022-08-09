import transaction

import plone.api
from plone import namedfile
from plone.registry.interfaces import IRegistry
from plone.app.textfield.value import RichTextValue
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from Products.CMFPlone.factory import addPloneSite
from AccessControl.SecurityManagement import newSecurityManager

uf = app.acl_users
user = uf.getUser('admin')
newSecurityManager(None, user.__of__(uf))

if 'plone' in app.objectIds():
    app.manage_delObjects(['plone'])
addPloneSite(
    app,
    'plone',
    extension_ids=[
        'plonetheme.barceloneta:default', 
#        'zopyx.ipsumplone:default',
#'Products.PloneFormGen:default', 
#'plone.restapi:default',
#'plone.app.multilingual:default', 
#'Products.PloneFormGen:default',
#'zopyx.plone.smashdocs:default', 
#'pp.client.plone:default',
'collective.easyform:default',
'xmldirector.connector:default'
    ])

plone.api.user.create(
    username='editor',
    password='editor',
    roles=('Member', 'Editor'),
    email="test@test.de")
plone.api.user.create(
    username='reader',
    password='reader',
    roles=('Member', 'Reader'),
    email="test@test.de")
plone.api.user.create(
    username='admin2',
    password='admin2',
    roles=('Member', 'Manager'),
    email="test@test.de")
plone.api.user.create(
    username='siteadmin',
    password='siteadmin',
    roles=('Member', 'Site Administrator'),
    email="test@test.de")

site = app['plone']
#site.restrictedTraverse('@@demo-content')()

fp = plone.api.content.create(container=site, type="Document", id="front-page", title="Front page")
plone.api.content.transition(fp, "publish")
fp.setTitle(u'Plone 6 demo site')
fp.setDescription(
    u'Welcome to the Plone 6 demo website - provided by ZOPYX. Feel free to play around with Plone 5!'
)
with open('data/frontpage.html', 'rb') as handle:
    fp.text = RichTextValue(
        str(handle.read(), 'utf8'), 'text/html', 'text/html')
fp.reindexObject()

print('commited')
transaction.commit()
