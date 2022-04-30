# OCR
Hindi and Gujarati text recognition from images

----------------------------------------------------------------------------------------------------------

-Download Tesseract using the below link: 
For Windows X64: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.1.20220118.exe
For Windows X32: https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w32-setup-v5.0.1.20220118.exe


Select Additional Script Data, expand it, and select Devanagari script.

Under Additional Language Data, select Hindi and Gujarati.
(Recommended : Download all the scripts and language data)
----------------------------------------------------------------------------------------------------------

Once the installation is done, you need to install the basic requirements for the program to run. For that just type the command 'pip install -r requirements.txt' (I have included the requirement.txt file).
Note: If 'pip install -r requirements.txt' is not working, then execute this command 'pip freeze > requirements.txt' and then execute 'pip install -r requirements.txt'.

After successful installation, you can recognize text from images by saving the images in the 'get' folder inside of 'Gujarati' and 'Hindi' directory.

Now simply run 'main.py' 

If the program runs successfully, then you can find the text extracted from the images inside the 'post' folder which is in output 'directory'.






