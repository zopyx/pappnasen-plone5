
import transaction

import plone.api
from plone import namedfile
from plone.registry.interfaces import IRegistry
from plone.app.textfield.value import RichTextValue
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

from zopyx.plone.smashdocs.interfaces import ISmashdocsSettings


from Products.CMFPlone.factory import addPloneSite
from AccessControl.SecurityManagement import newSecurityManager

uf = app.acl_users
user = uf.getUser('admin')
newSecurityManager(None, user.__of__(uf))

if 'plone' in app.objectIds():
    app.manage_delObjects(['plone'])
addPloneSite(app, 'plone', extension_ids=['plonetheme.barceloneta:default', 'zopyx.ipsumplone:default', 'Products.PloneFormGen:default', 'plone.app.multilingual:default', 'plone.app.multilingual:default', 'Products.PloneFormGen:default', 'zopyx.plone.smashdocs:default'])

plone.api.user.create(username='editor', password='editor', roles=('Member', 'Editor'), email="test@test.de")
plone.api.user.create(username='reader', password='reader', roles=('Member', 'Reader'), email="test@test.de")
plone.api.user.create(username='admin2', password='admin2', roles=('Member', 'Manager'), email="test@test.de")
plone.api.user.create(username='siteadmin', password='siteadmin', roles=('Member', 'Site Administrator'), email="test@test.de")

site = app['plone']
site.restrictedTraverse('@@demo-content')()


registry = getUtility(IRegistry)
settings = registry.forInterface(ISmashdocsSettings)
settings.client_id = u'd674ed8c5aa073f12fc73b94a232b9eb3cfe8da5de703ad6c0a40e998395ddda'
settings.client_key = u'c35cb21efd1acc1771c92fe7a43ab8a78287b5ca5c07f01c4a462f75464e8dfe' 

fp = site['front-page']
fp.setTitle(u'Plone 5 demo site')
fp.setDescription(u'Welcome to the Plone 5 demo website - provided by ZOPYX. Feel free to play around with Plone 5!')
with open('data/frontpage.html', 'rb') as handle:
    fp.text = RichTextValue(unicode(handle.read(), 'utf8'), 'text/html', 'text/html')
fp.reindexObject()

print 'commited'
transaction.commit()

