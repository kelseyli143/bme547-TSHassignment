import json


def main():
      patient_info = read_data()
      create_jsons(patient_info)


def read_data():
    test_data = open("test_data.txt", "r")
    patient_info = test_data.readlines()
    # patient_info is a list where each line is a string
    test_data.close()
    patient_info.pop(-1)
    return patient_info


def create_jsons(patient_info):
    index = 0
    for line in patient_info:
        if index == 0:
            firstName, lastName = find_name(line, patient_info)
        if index == 1:
            age = find_age(line, patient_info)
        if index == 2:
            gender = find_gender(line, patient_info)
        if index == 3:
            TSH = TSH_values(line, patient_info)
            diagnosis = TSH_diagnosis(line, patient_info, TSH)
            outDictionary = {
                             "First Name": firstName,
                             "Last Name": lastName,
                             "age": age,
                             "gender": gender,
                             "diagnosis": diagnosis,
                             "TSH": TSH
                             }
            out_file = open(firstName+"-"+lastName+".json", "w")
            json.dump(outDictionary, out_file)
            out_file.close()

        index = index + 1

        if index == 4:
            index = 0

    return patient_info


def find_name(line, patient_info):
    index = patient_info.index(line)
    name = patient_info[index]
    first_last = name.split()
    # print(first_last)
    firstName = first_last[0]
    lastName = first_last[1]
    # print(firstName)
    # print(lastName)
    return firstName, lastName


def find_age(line, patient_info):
    index = patient_info.index(line)
    age_str = patient_info[index]
    age = int(age_str)
    # print(age)
    return age


def find_gender(line, patient_info):
    index = patient_info.index(line)
    gender = patient_info[index]
    gender = gender.strip()
    # print(gender)
    return gender


def TSH_values(line, patient_info):
    TSH_list = line.split(',')
    TSH_list.pop(0)
    TSH = [float(i) for i in TSH_list]
    TSH.sort()
    # print(TSH)
    return TSH


def TSH_diagnosis(line, patient_info, TSH):
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
    # print(diagnosis)
    return diagnosis


if __name__ == "__main__":
    main()
