import cx_Freeze

#ONLY RUN FROM COMMAND LINE
#in cmd
# navigate to the dir that contains this file
#type:
#	python setup.py build
# or
#	python setup.py bdist_msi

executables = [cx_Freeze.Executable("B3.py")]
includeFiles = ["Data\\chromedriver.exe", "Data\\credentials.xml", "Data\\words.txt", "README.txt"]

cx_Freeze.setup(
      name="B3",
	  version="1.0",
	  description="BingBucksBot - opens a CHROME browser and searches BING.com using an account and password supplied by the user.",
	  executables = executables,
	  author="Eric Monteforte",
      options = {
        'build_exe': {"include_files":includeFiles,
                        "packages":"selenium"}}
	  )
