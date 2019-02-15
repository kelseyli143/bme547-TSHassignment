**Instructions on how to use the TSH_data_conv.py module:**<br/>
Enter the repository with the TSH_data_conv.py code, and run ‘python3 TSH_data_conv.py’ from the command line. There must be a test_data.txt file with patient information in the same directory. The module will output a json file with first name, last name, age, gender, diagnosis, and TSH values for each patient. 

**Instructions on how to use the test_TSH_data_conv.py module:**<br/>
To run unit testing on the TSH_data_conv.py module, the user should execute ‘pytest -v’ from the terminal. This will return PASSED or FAILED corresponding to each unit test. 

**Notes on how the TSH_data_conv.py module works:**<br/>
The main() function itself calls two functions. The first is called read_data(), which reads in patient data line by line from the patient information text file. The second function called is the create_jsons() function.<br/>

This create_jsons() function starts with index of 0. There is a loop that runs through each line of the text file. The function increments the index value by 1 each time it runs through the loop, and resets back to 0 once the index value hits 4. This index keeps track of the type of information in each line of the text file. Create_jsons() calls the find_name, find_gender, find_age, TSH_diagnosis, and TSH_values functions to extract the respective patient information from the text file. It then creates a dictionary and outputs a json file for each individual patient.<br/> 

For the TSH_diagnosis() function, for each patient, the code loops through the TSH values and creates one list of values that are above 4 and one list of values that are below 1. If there are any values in either list, the diagnosis will be either ‘hypothyroidism’ or ‘hyperthyroidism’, respectively. If neither list has any values, that means that all of the TSH values are between 1 and 4 and the diagnosis is thus ‘normal thyroid function’.<br/>

**Notes on how the test_TSH_data_conv.py module works:**<br/>
The test_TSH_data_conv.py script uses the parametrize decorator from pytest in order to perform unit testing on the TSH_data_conv.py function. It consists of a parametrized test with 12 test cases. The testing script uses test cases of lists of TSH values with varying numbers of test results and a mix of 'hypo/hyperthyroidism’ and ‘normal thyroid function’ expected diagnoses. 

**Notes about the assignment:**
* I pushed all of the docs/_build/html folder from the Sphinx documentation to GitHub. The TSH_data_conv.html and test_TSH_data_conv.html files have the documentation for the main diagnosing script and the testing script, respectively. 
* I enabled travis CI and ensured that my scripts passed the travis CI testing, including following pep8 standards
