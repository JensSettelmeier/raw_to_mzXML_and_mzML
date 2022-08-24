# raw_to_mzXML_and_mzML
Python code to convert RAW MS files to mzXML or mzML and mzXML to mzML or the other way around.  
In case you are struggling to convert raw MS files to mzXML or mzML or mzXML to mzML and the other way around using python I hope
you will find this code helpful. If you do, I would appreciate your upvote :)

### How to use convertRawMP.py:
Most simplest approach: Clone the repo. Put your raw files into the folder.
Open a terminal in the folder. Execute: "python convertRawMP.py --f mzXML" or "python convertRawMP.py --f mzML" to convert all raw files in the folder to mzXML or mzML. 
If you use --c 1 parameter, which means you execute "python convertRawMP.py --f mzXML --c 1", then no raw file moving will happen and only one cpu core used. 



### How to use MS_format_convert.py:
Most simplest approach: Clone the repo. Put your mzML or mzXML files into the folder which should be converted to the other file format.
Open a terminal in the folder. Execute: "python MS_format_convert.py --i mzXML --o mzML" or "python MS_format_convert.py --i mzML --o mzXML" to convert all mzML/mzXML files in the folder to mzXML or mzML.
--i determines the input format, --o the output format.  
Only use this method, if you don't have the raw file. If you have the raw file, convertRawMP.py is recommanded. 
