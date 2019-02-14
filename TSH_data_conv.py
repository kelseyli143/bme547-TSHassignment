

import json


def main():
    patient_info = read_data()
    create_jsons(patient_info)


def read_data():
    """Reads data in from the text file

    This function reads in the data line by line from the text file that
    contains all of the patient info. It pops out the last line, which is
    not part of the patient data but rather says 'END'.

    Returns:
        list: the patient info from the text file with each line as an item
        in a list
    """
    test_data = open("test_data.txt", "r")
    patient_info = test_data.readlines()
    # patient_info is a list where each line is a string
    test_data.close()
    patient_info.pop(-1)
    return patient_info


def create_jsons(patient_info):
    """Outputs json file for each patient with their information and diagnosis

    This code starts with an index of 0. It increments the index value by 1
    each time it runs through the loop, and resets back to 0 once the index
    value hits 4. This index keeps track of the type of information in the
    patient information text file. This function calls functions to find the
    name, age, gender, TSH values,and diagnosis based on the TSH values in
    the file. It then creates a dictionary and outputs a json file for each
    individual patient.

    Args:
        patient_info (list): the patient info from the text file with each
        line as an item in a list
    """
    index = 0
    for line in patient_info:
        if index == 0:
            firstname, lastname = find_name(line)
        if index == 1:
            age = find_age(line)
        if index == 2:
            gender = find_gender(line)
        if index == 3:
            TSH = TSH_values(line)
            diagnosis = TSH_diagnosis(TSH)
            outDictionary = {
                             "First Name": firstname,
                             "Last Name": lastname,
                             "Age": age,
                             "Gender": gender,
                             "Diagnosis": diagnosis,
                             "TSH": TSH
                             }
            out_file = open(firstname+"-"+lastname+".json", "w")
            json.dump(outDictionary, out_file)
            out_file.close()

        index = index + 1

        if index == 4:
            index = 0

    return patient_info


def find_name(line):
    """Extracts the patient's first and last name from the patient information
    text file

    Args:
        line (string): the line corresponding to the patient's name, from
        the loop in the create_jsons function

    Returns:
        string: patient's first name
        string: patient's last name
    """
    name = line
    first_last = name.split()
    # print(first_last)
    firstname = first_last[0]
    lastname = first_last[1]
    # print(firstname)
    # print(lastname)
    return firstname, lastname


def find_age(line):
    """Extracts the patient's age from the patient information text file

     Args:
         line (string): the line corresponding to the patient's age, from
         the loop in the create_jsons function

     Returns:
         int: patient's age
     """
    age_str = line
    age = int(age_str)
    # print(age)
    return age


def find_gender(line):
    """Extracts the patient's gender from the patient information text file

     Args:
         line (string): the line corresponding to the patient's gender, from
         the loop in the create_jsons function

     Returns:
         string: the patient's gender
     """
    gender = line.strip()
    # print(gender)
    return gender


def TSH_values(line):
    """Extracts the patient's TSH values from the patient information text file

     Args:
         line (string): the line corresponding to the patient's TSH values,
         from the loop in the create_jsons function

     Returns:
         list: the patient's TSH values, is a list of floats
     """
    TSH_list = line.split(',')
    TSH_list.pop(0)
    TSH = [float(i) for i in TSH_list]
    TSH.sort()
    # print(TSH)
    return TSH


def TSH_diagnosis(TSH):
    """Determines the patient's diagnosis based on their TSH levels

     Args:
         TSH (list): the patient's TSH values, is a list of floats

     Returns:
         string: patient's diagnosis, will return either hyperthyroidism,
         hypothyroidism, or normal thyroid function
     """
    hyper_TSH = []
    hypo_TSH = []
    for i in TSH:
        if i < 1:
            hyper_TSH.append(i)

        elif i > 4:
            hypo_TSH.append(i)

    if len(hyper_TSH) > 0:
        diagnosis = 'hyperthyroidism'
    elif len(hypo_TSH) > 0:
        diagnosis = 'hypothyroidism'
    elif len(hyper_TSH) == 0 and len(hypo_TSH) == 0:
        diagnosis = 'normal thyroid function'
    print(diagnosis)
    return diagnosis


if __name__ == "__main__":
    main()
