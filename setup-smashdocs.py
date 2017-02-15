import uuid
import transaction

from zope.component import getUtility
from plone.registry.interfaces import IRegistry
from zopyx.plone.smashdocs.interfaces import ISmashdocsSettings
from pp.client.plone.interfaces import IPPClientPloneSettings
from zope.component.hooks import setSite

import plone.api

uf = app.acl_users
user = uf.getUser('admin')
newSecurityManager(None, user.__of__(uf))

site = app['plone']
setSite(site)

plone.api.user.create(username='sd-editor', password='sd-editor', roles=('Contributor', 'SD Editor'), email="test@test.de")
plone.api.user.create(username='sd-commentator', password='sd-commentator', roles=('Reader', 'SD Commentator'), email="test@test.de")
plone.api.user.create(username='sd-reader', password='sd-reader', roles=('Reader', 'SD Reader'), email="test@test.de")
plone.api.user.create(username='sd-approver', password='sd-approver', roles=('Contributor', 'SD Approver'), email="test@test.de")

sd = plone.api.content.create(type='SmashFolder', container=site, id='sd-workspace', title=u'Smashdocs Workgroup Folder')
sd.group_id = str(uuid.uuid4())

registry = getUtility(IRegistry)
settings = registry.forInterface(ISmashdocsSettings)
settings.client_id = u'd674ed8c5aa073f12fc73b94a232b9eb3cfe8da5de703ad6c0a40e998395ddda'
settings.client_key = u'c35cb21efd1acc1771c92fe7a43ab8a78287b5ca5c07f01c4a462f75464e8dfe' 


registry = getUtility(IRegistry)
settings = registry.forInterface(IPPClientPloneSettings)
settings.server_username = u'demo'
settings.server_password = u'demo'

print 'commited'
transaction.commit()

