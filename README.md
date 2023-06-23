## Summary

## Project Members
- [Ang Jon Ming](https://github.com/jon3r4de)
- [Low Weisheng Giovanni](https://github.com/giovannilow)
- [Loh Yu Tong](https://github.com/youdonnnn)


## Motivation

Tedious and time-consuming tasks are not just widespread in legal practice, but wholly needless and with real consequences on the livelihoods of lawyers and the business of law firms. Furthermore, with the Rules of Court 2021 requiring expeditious proceedings, many smaller firms are placed in a much weaker position compared to larger firms that may have superior, but often costly, legal technology. 

Thus, at present, legal technology in fact drastically widens the competitive disadvantage faced by smaller firms, with serious questions about procedural fairness and equal access to justice.

The legal profession therefore needs a scalable and highly cost-efficient solution to time-consuming tasks. With this in mind, the Algorithm for Litigation Documents (ALD) streamlines the process of compiling a Bundle of Documents (BOD) into a single program executable with one click, without the need to rely on costly services that smaller firms may not be able to afford. ALD’s strength lies in its economy – it is simply a .py file – which in turn makes it supremely scalable and re-usable, cutting out significant time costs and opportunity costs for smaller firms.

Furthermore, ALD leverages artificial intelligence (AI) to extrapolate the contents of each document, such as date, time, title, names and so on, saving huge time costs. ALD is also able to parse through piles of voluminous documents to provide a summary of all or each, and thus easily scalable to provide an instant and cost-effective solution to other time-consuming processes with respect to all standard-form legal documents. This would reduce time costs not just in the compiling of BODs but across the entire profession. 

ALD is a step towards significant and expensive pain points in litigation in an accessible and scalable way, ensuring that the entire profession benefits from increased efficiency and productivity.



## TechStack

We decided to use Python for our script for documenting the types of documents in a file due to several reasons. First, Python is a versatile and powerful programming language known for its simplicity and readability. It allows me to express the logic of the script in a clear and concise manner. Second, Python has a rich ecosystem of libraries and modules that provide extensive functionality for various tasks. In this script, I utilized collections, os, calendar, docx, tkinter, and PIL (Python Imaging Library) to handle file operations, document processing, graphical user interface (GUI) development, and image manipulation. Third, Python is platform-independent, which means the script can run on different operating systems without major modifications. 

Lastly, the solution we’re suggesting requires the application to take in a large amount of information while looking through files and hence creating a Python script would allow us to efficiently and quickly make up a GUI 

## Instructions to run the program

Prerequisite: 

Make sure to have python installed :)

Depending on your version of pip, you can use “pip install” or “pip3 install”

These are the commands which would help you install the relevant packages required :)

pip install dateparser==1.1.8 

pip installTransformers==4.30.2

pip install torch==2.0.1

pip install torchaudio==2.0.2

pip install torchvision==0.15.2

pip install python-docx==0.8.11

pip install pypdf==3.10.0

pip install protobuf==3.20.2


Instructions to make the fileDocumentation.py file an executable:

For mac users: 

1.Open Terminal


2. Find the which file its in and key in the file path in the command line 


- [link for help](https://support.apple.com/en-sg/guide/terminal/apddfb31307-3e90-432f-8aa7-7cbc05db27f7/mac#:~:text=In%20the%20Terminal%20app%20on,it%20in%20the%20new%20location.)

3. Once you’re in the file key in the below commands:
	
	pip install pyinstaller (if you have python3 installed key in [pip3 install pyinstaller] 

	pyinstaller name_of_python_script.py --name name_of_what_you_want_the_app_to_be_called --windowed --onefile

	pyinstaller name_of_what_you_want_the_app_to_be_called.spec 

4. This would create an executable file which would open the gui and script on click 


## For detailed usage instructions with photos

- [Click me](https://docs.google.com/document/d/1sCcNOIv9fNf_n9Z4UowgdfXjKE5VcrCdsmLcb_UrdcA/edit?usp=sharing)




