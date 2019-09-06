
1. Have a local Python(3.7) environment
	
	- [Anaconda](https://www.anaconda.com/distribution/) is an easy way to do this, although somewhat bloated with packages
	
	- If you are short on space, consider installing [*Miniconda*](https://docs.conda.io/en/latest/miniconda.html) as we will be working in a virtualenv anyways
2. Set up your environment.
	
	1. Clone this repo

	```
	git clone https://github.com/lucasdurand/visualization-seminar.git
	cd visualization-seminar
	```

	2. Create a virtualenv and install our packages:

	```
	pip install pipenv
	pipenv install
	```

	3. Once everything is installed you can *activate* the environment with `pipenv shell`. Now you're inside and things should work as expected: try running `jupyter notebook` to launch a Jupyter instance and confirm everything is happy.

3. Install `git`, a version control tool:

	- Windows: https://git-scm.com/download/win
	- Mac: https://git-scm.com/download/mac
	- Linux: ... this should already be here

3. [Install the **Heroku CLI**](https://devcenter.heroku.com/articles/getting-started-with-python#set-up). Go ahead and create yourself a free account while you're at it. We are going to use this later to deploy an app to *the Cloud*. 
