Emotion Recognition:
/*******************************************Running on normal windows system*************************************/

These steps need to be followed for making the emoiton recognition model 
the primary needs for this to be successful is that a laptop 
should have running python 3 compiler in it along with pip or pip3 library for windows OS. 
1.First installing the libraries
	a. First check the version of python and pip you have in the laptop
		python3 --version
		pip3 --version
	b. Its better if you can create a virtual environment to isolate 
	   package installation from system.
		python -m venv --system-site-packages .\venv
		.\venv\Scripts\activate(Activating the virtual env)
		pip install --upgrade pip(install packages afterwards if you are to work on a virtual environment)
		deactivate(to get out of the environment)
	c.Now install the tensorflow package (if its already installed it will get upgraded)
		pip install --upgrade tensorflow
	d.Check if tensorflow is installed by typing following commands
		$ python
		>> import tensorflow(it should not throw any error if its installed)
	e.Now we need to install the opencv for the model
		pip install opencv-python
	f.Now install the cmake library to use the dlib library
		pip install cmake
	g.Now installing the dlib
		pip install https://pypi.python.org/packages/da/06/bd3e241c4eb0a662914b3b4875fc52dd176a9db0d4a2c915ac2ad8800e9e/dlib-19.7.0-cp36-cp36m-win_amd64.whl#md5=b7330a5b2d46420343fbed5df69e6a3f
		If the above step does not work follow these steps:
		1.Download the CMake installer and install it: https://cmake.org/download/
		2.Add CMake executable path to the Enviroment Variables:
		  set PATH="%PATH%;C:\Program Files\CMake\bin"
		  note: The path of the executable could be different from C:\Program Files\CMake\bin, just set the PATH accordingly.
		  note: The path will be set temporarily, to make the change permanent you have to set it in the “Advanced system settings” → “Environment Variables” tab.
		3.Restart The Cmd or PowerShell window for changes to take effect.
		4.Download the Dlib source(.tar.gz) from the Python Package Index : https://pypi.org/project/dlib/#files extract it and enter into the folder.
		5.Check the Python version: python -V. This is my output: Python 3.7.2 so I'm installing it for Python3.x and not for Python2.x
		  note: You can install it for both Python 2 and Python 3, if you have set different variables for different binaries i.e: python2 -V, python3 -V
		6.Run the installation: python setup.py install
	h. This issue probably wont be there but still if it comes up try installing pillow package.Pillow is a fork of PIL that adds some user-friendly features.
		python -m pip install --upgrade Pillow
2. Now that the libraries are installed for the windows OS the next steps can be done with ease.Download the code given and make changes for path at the following files:
	a.mainRunner.py
	  line number 33: change the path for the haar_cascade_classifier it is already downloaded and is in this folder MajorProject-main\EmotionRecognition named frontalface.xml
	  line number 34: change the path for the emotion recognition model which is also mentioned in the folder mentioned same folder mentioned above with name face.hdf5
	  line number 38: change the path for the workbook for writing data in the files.
	  line number 97: change the path for saving the photos generated in the folder 
	  line number 98: change the path for saving the data in the files in the workbook
	b.report_generator.py
	  line number 44: change the path to read from files created by mainRunner.py which is data.xlsx
3.Now that the changes are made in the paths the code should run perfectly on a system but look that you have an installed camera rather than using an external camera as it also throws errors in the open-cv

/*********************************************************Running on Nvidia Jetson Nano*********************************************/
For running the same code on the nvidia jetson nano use the following steps:
1.Before you install TensorFlow for Jetson, ensure you:
	a.Install JetPack on your Jetson device.
	b.Install system packages required by TensorFlow:
	  $ sudo apt-get update
	  $ sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran
	Install and upgrade pip3.
	  $ sudo apt-get install python3-pip
	  $ sudo pip3 install -U pip testresources setuptools==49.6.0 
	Install the Python package dependencies.
	  $ sudo pip3 install -U numpy==1.19.4 future==0.18.2 mock==3.0.5 h5py==2.10.0 keras_preprocessing==1.1.1 keras_applications==1.0.8 gast==0.2.2 futures protobuf pybind11
2.Installing tensorflow
	Install TensorFlow using the pip3 command. This command will install the latest version of TensorFlow compatible with JetPack 4.5.
	  $ sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow
	Note: TensorFlow version 2 was recently released and is not fully backward compatible with TensorFlow 1.x. If you would prefer to use a TensorFlow 1.x package, it can be installed by specifying the TensorFlow version to be less than 2, as in the following command:
	  $ sudo pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 ‘tensorflow<2’
	If you want to install the latest version of TensorFlow supported by a particular version of JetPack, issue the following command:
	  $ sudo pip3 install --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v$JP_VERSION tensorflow
3.Similalry as in windows opencv can be installed using the line
	pip install opencv-python
4.Now install the packages for the camke library using line
	pip install cmake
5.Now install the dlib library with the line
	pip install dlib

/*****************************************Running code on the AI DL Server**********************************************************/ 
Steps to install and run the emotion recognition code in the AI Deep Learning Server:
The following code has been uploaded in the url http://dlserver.vce.ac.in:60010/   {Token id :e2113ab9cc5b166e97607b5593729dab6deab252443fd76f )
Docker path:sudo nvidia-docker run -d -v /home/admin123/test_dir/IT_USER03:/tf/ -p 60010:8888 it/speechproject:latest
1.Take the folder in which you have saved the project.
2.Convert it into a zip file.
3.upload the zip file onto the server
4.Use the following code to extract the folder and its contents (make sure to change the path):
	import zipfile as zf
	files = zf.ZipFile("ZippedFolder.zip", 'r')
	files.extractall()
	files.close() 
5.After extracting go to the emotion recognition code
6.Install the following libraries using following lines and before that check the tensorflow version using command
	import tensorflow as tf
	print(tf.__version__)
It is good if it has tensorflow version>2.0
Next installing dependencies
	pip install wheel
	pip install pillow
	pip install --upgrade tensorflow
	pip install keras
	pip install opencv-python

/********************************************Source Code for Emotion Recognition model making***************************************/
Emotion Recognition code for making the model: 
	path:MajorProject-main\Emotion training code\Model_creation.ipynb
	This model needs to be executed on a jupyter notebook or google collab to train the model.
Emotion Testing code for the model:
	path:MajorProject-main\Emotion training code\Model_tester.ipynb
	This model tests the above emotion model.
The dataset for this model can be attained from the path: MajorProject-main\Data\Emotion_dataset

/*********************************************Source Code for Gaze tracking *******************************************************/
The code for gaze tracking :
	path:MajorProject-main\GazeTracking\gaze_tracking\gaze_tracking.py
	This model tracks the eye movement

/**********************************************Source Code for Both Emotion Recognition and Gaze tracking combined*****************/
The code for both Emotion Recognition and Gaze tracking combined:
	path:MajorProject-main\mainRunner.py
	This code combines both the emotion recognition and eye tracking and stores its data in the file in the path:MajorProject-main\Data\sheets\Data.xlsx
	The later part uses the report generator to generate the result of the attained data in data.xlsx file
	path:MajorProject-main\report_generator.py
