# Activity Log

This is my EPQ Activity Log and a small Python project to make writing that Activity Log a bit easier.

If you're downloading this repo for your personal use, there is a proper release available here.

If you insist on downloading the source code for some reason, change the learner name, learner number, etc. in a file called `.env`. The format should be: <pre>LEARNER_NAME=&lt;your learner name&gt;
LEARNER_NUMBER=&lt;your learner number&gt;
CENTRE_NAME=&lt;your centre name&gt;
CENTRE_NUMBER=&lt;your centre number&gt;
UNIT_NAME=&lt;your unit name&gt;
UNIT_NUMBER=&lt;your unit number&gt;
TEACHER_ASSESSOR=&lt;your teacher assessor&gt;
PROPOSED_PROJECT_TITLE=&lt;your proposed project title&gt;
<br># This is "Activity Log" if not set
FILENAME=
<br># I'd recommend keeping these both True, but if you
\# don't care about the markdown version, you can
\# set that to False
\# If you set the HTML version to False, then the
\# "Open HTML file" button on the GUI won't work
CREATE_HTML=True
CREATE_MARKDOWN=True</pre>

If any of the values have spaces, they should be in double quotes like `"John Doe"`.
