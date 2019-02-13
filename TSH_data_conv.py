import json


def main():
      patient_info = read_data()
      find_name()
      find_age()
      find_gender()
      TSH = TSH_values()
      TSH_diagnosis(TSH)


def read_data():
    test_data = open("test_data.txt", "r")
    patient_info = test_data.readlines()
    # patient_info is a list where each line is a string
    test_data.close()
    patient_info.pop(-1)
    return patient_info


def find_name():
    name = 'Anne Boynton'
    first_last = name.split()
    # print(first_last)
    firstName = first_last[0]
    lastName = first_last[1]
    print(firstName)
    print(lastName)
    return firstName, lastName


def find_age():
    age_str = '45'
    age = int(age_str)
    print(age)
    return age

def find_gender():
    gender = 'Female'
    print(gender)
    return gender

def TSH_values():
    TSHfromtext = 'TSH,3.5,3.6,1.8,2.8,1.9,3.4,3,3.6,3,4'
    TSH_list = TSHfromtext.split(',')
    TSH_list.pop(0)
    TSH = [float(i) for i in TSH_list]
    print(TSH)
    return TSH

def TSH_diagnosis(TSH):
    hyper_TSH = []
    hypo_TSH = []
    for i in TSH:
        if i < 1:
            hyper_TSH.append(i)

        elif i > 4:
            hypo_TSH.append(i)

    if len(hyper_TSH)>0:
        diagnosis = 'hyperthyroidism'
    elif len(hypo_TSH)>0:
        diagnosis = 'hypothyroidism'
    elif len(hyper_TSH)==0 and len(hypo_TSH)==0:
        diagnosis = 'normal thyroid function'
    print(diagnosis)
    return diagnosis


if __name__ == "__main__":
    main()
