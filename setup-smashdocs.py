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
settings.client_id = u'154458bcd97c5a7f1c6e08407409b12918d89962d3ea58613eeafba5e2286902'
settings.client_key = u'ae4287bafc5666f45b0d32c4e0e39fba3515f4c0007e2dbf5b212f2658d5891e'
settings.partner_url = u'https://zopyx.smashdocs.net/api'

registry = getUtility(IRegistry)
settings = registry.forInterface(IPPClientPloneSettings)
settings.server_username = u'demo'
settings.server_password = u'demo'

print('commited')
transaction.commit()
