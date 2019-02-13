import json

def main():
      patient_info = read_data()

def read_data():
    test_data = open("test_data.txt", "r")
    patient_info = test_data.readlines()
    # patient_info is a list where each line is a string
    test_data.close()
    patient_info.pop(-1)
    return patient_info

if __name__ == "__main__":
    main()
