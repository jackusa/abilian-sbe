Changelog for Abilian SBE
=========================

0.1.1 (2015-05-27)
------------------

Improvements
~~~~~~~~~~~~

*  community views: support graceful csrf failure
*  added attachment to forum post by email
*  added attachments views in forum
*  forum post: show 'send by mail' only if enabled for community or current user
*  i18n on roles

Fixes
~~~~~

* fix css rule for 'recent users' box
*  communities settings forms:  fix imagefield arguments
*  NavAction Communities is now only showed when authenticated
*  added regex clean forum posts from email

Refactoring
~~~~~~~~~~~

*  folder security: use Permission/Role objects
*  * views/social.py: remove before_request
*  forum views: use CBV
*  forum: form factorisation
*  @login_required on community index and social.wall, has_access() stops anonymous users
*  pep8 cleanup
*  tests/functional  port is now dynamic to avoid runtime errors
*  replaced csrf_field -> csrf.field() in thread.html to have proper csrf and allow action to go on (#16)
*  unescaped activity entry body_html
*  fix test: better mock of celery task
*  abilian-core removed extensions.celery; use periodic_task from abilian.core.celery
*  forum: in-mail tasks: set app default config values; conditionnaly register check_maildir
*  celery: use 'shared_task' decorator

0.1 (2015-03-31)
----------------

Initial release
