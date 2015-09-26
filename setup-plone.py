
import transaction
import pkg_resources
from Products.CMFPlone.factory import addPloneSite
from AccessControl.SecurityManagement import newSecurityManager
from plone import namedfile
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


uf = app.acl_users
user = uf.getUser('admin')
newSecurityManager(None, user.__of__(uf))
addPloneSite(app, 'plone', extension_ids=['plonetheme.barceloneta:default', 'zopyx.ipsumplone:default'])

site = app['plone']
site.restrictedTraverse('@@demo-content')()
print 'commited'
transaction.commit()

