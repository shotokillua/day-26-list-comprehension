student_dict = {
    "student": ['Angela', 'James', 'Lily'],
    "score": [56, 76, 98]
}
import pandas

student_dict_df = pandas.DataFrame(student_dict)
print(student_dict_df)