# ld-example

Pretty simple Python3 SDK "hello-python" based on the LaunchDarkly Quick Start guide.

* The first few lines import the LaunchDarkly modules for the Python script to have access to it.
* We then set the script to use my account's Production environment's unique SDK key.
* We define some user parameters, and then evaluate whether that user (Bob Loblaw) should have access to my feature, "hello-feature"
* The user gets added to user list in the LD dashboard, and for me it was evaluating as Bob should __not__ be getting the feature initially, so turned on Targeting and did an override to have him see it and he was able to see it.
* The code prints out an affirmative if they are going to see the feature, or a negative if they are not.
