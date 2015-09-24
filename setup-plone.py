
import transaction
import pkg_resources
from Products.CMFPlone.factory import addPloneSite
from AccessControl.SecurityManagement import newSecurityManager
from plone import namedfile
from plone.registry.interfaces import IRegistry
from zope.component import getUtility


uf = app.acl_users
user = uf.getUser('admin')
#uf._doChangeUser('admin', admin_pw, ('Manager',), ())
newSecurityManager(None, user.__of__(uf))
addPloneSite(app, 'plone', extension_ids=['plonetheme.barceloneta:default'])

site = app['plone']
print 'commited'
transaction.commit()

