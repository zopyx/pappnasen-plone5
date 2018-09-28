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

plone.api.user.create(
    username='sd-editor',
    password='sd-editor',
    roles=('Contributor', 'SD Editor'),
    email="test@test.de")
plone.api.user.create(
    username='sd-commentator',
    password='sd-commentator',
    roles=('Reader', 'SD Commentator'),
    email="test@test.de")
plone.api.user.create(
    username='sd-reader',
    password='sd-reader',
    roles=('Reader', 'SD Reader'),
    email="test@test.de")
plone.api.user.create(
    username='sd-approver',
    password='sd-approver',
    roles=('Contributor', 'SD Approver'),
    email="test@test.de")

sd = plone.api.content.create(
    type='SmashFolder',
    container=site,
    id='sd-workspace',
    title=u'Smashdocs Workgroup Folder')
sd.group_id = str(uuid.uuid4())

registry = getUtility(IRegistry)
settings = registry.forInterface(ISmashdocsSettings)
settings.client_id = u'369bc312a9def6860435049c342f0b3df940cee0565e1c7386dc360d084bdfb7'
settings.client_key = u'0e66de1966d9d9217fca0b70010fab0dd12b741a229eb6beea5807bb7c29700c'
settings.partner_url = u'https://zopyx.smashdocs.net/api'

registry = getUtility(IRegistry)
settings = registry.forInterface(IPPClientPloneSettings)
settings.server_username = u'demo'
settings.server_password = u'demo'

print 'commited'
transaction.commit()
