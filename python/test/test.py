import pandas as pd
import csv

# Step 1: Start with an empty DataFrame
df = pd.DataFrame(columns=["Name", "Age", "City"])

# Step 2: Add rows dynamically
df.loc[len(df)] = ["Alice", 25, "New York"]
df.loc[len(df)] = ["Bob", 30, "Los Angeles"]
df.loc[len(df)] = ["Charlie", 35, "Chicago"]

# Print the updated DataFrame
print(df)

# Optional: Export to a CSV file
df.to_csv("output.csv", index=False)


data = [['book', 'chapters', 'verses', 'sentences', 'words', 'letters', 'pages'], 
        ['Genesis', 50, 1533, 2116, 38766, 163742, 54], 
        ['Exodus', 40, 1213, 1610, 31831, 133989, 43], 
        ['Leviticus', 27, 859, 1164, 23797, 100203, 33], 
        ['Numbers', 36, 1288, 1647, 31167, 138153, 44], 
        ['Deuteronomy', 34, 959, 1236, 27492, 116017, 38], 
        ['Joshua', 24, 658, 866, 17660, 79934, 25], 
        ['Judges', 21, 618, 917, 17859, 78689, 25], 
        ['Ruth', 4, 85, 142, 2538, 10909, 4], 
        ['1_Samuel', 31, 810, 1206, 24669, 104801, 34], 
        ['2_Samuel', 24, 695, 1009, 20162, 87254, 28], 
        ['1_Kings', 22, 816, 1090, 24175, 104103, 33], 
        ['2_Kings', 25, 719, 1046, 23443, 101629, 33], 
        ['1_Chronicles', 29, 941, 1156, 19447, 94344, 30], 
        ['2_Chronicles', 36, 822, 1068, 25433, 115083, 37], 
        ['Ezra', 10, 280, 313, 7066, 32141, 11], 
        ['Nehemiah', 13, 406, 493, 10373, 46865, 15], 
        ['Esther', 10, 167, 233, 5519, 24511, 8], 
        ['Job', 42, 1070, 1277, 18074, 74058, 24], 
        ['Psalms', 150, 2461, 3245, 42286, 176210, 58], 
        ['Proverbs', 31, 915, 1009, 15142, 64690, 21], 
        ['Ecclesiastes', 12, 222, 300, 5701, 22900, 7], 
        ['Song_of_Solomon', 8, 117, 206, 2754, 11519, 4], 
        ['Isaiah', 66, 1292, 2228, 37132, 156987, 51], 
        ['Jeremiah', 52, 1364, 2228, 42323, 183839, 59], 
        ['Lamentations', 5, 154, 266, 3467, 14538, 5], 
        ['Ezekiel', 48, 1273, 1883, 38703, 166014, 53], 
        ['Daniel', 12, 357, 517, 11832, 50500, 17], 
        ['Hosea', 14, 197, 326, 5242, 22392, 7], 
        ['Joel', 3, 73, 115, 1973, 8465, 3], 
        ['Amos', 9, 146, 208, 4255, 18104, 5], 
        ['Obadiah', 1, 21, 33, 671, 2930, 1], 
        ['Jonah', 4, 48, 72, 1344, 5424, 2], 
        ['Micah', 7, 105, 177, 3092, 13028, 4], 
        ['Nahum', 3, 47, 102, 1261, 5550, 2], 
        ['Habakkuk', 3, 56, 117, 1501, 6354, 2], 
        ['Zephaniah', 3, 53, 93, 1617, 7085, 2], 
        ['Haggai', 2, 38, 52, 1130, 4967, 2], 
        ['Zechariah', 14, 211, 293, 6299, 26758, 8], 
        ['Malachi', 4, 55, 102, 1876, 8060, 3], 
        ['Matthew', 28, 1071, 1346, 24224, 101747, 33], ['Mark', 16, 666, 834, 15064, 62679, 21], ['Luke', 24, 1151, 1432, 26249, 109644, 36], ['John', 21, 867, 1105, 20137, 80701, 26], ['Acts', 28, 1007, 1197, 25130, 109462, 35], ['Romans', 16, 433, 563, 10399, 43964, 15], ['1_Corinthians', 16, 437, 578, 10206, 41432, 13], ['2_Corinthians', 13, 257, 327, 6659, 27751, 9], ['Galatians', 6, 149, 178, 3477, 14597, 5], ['Ephesians', 6, 155, 167, 3429, 14740, 5], ['Philippians', 4, 104, 119, 2519, 10559, 3], ['Colossians', 4, 95, 113, 2294, 10032, 4], ['1_Thessalonians', 5, 89, 100, 2022, 8410, 2], ['2_Thessalonians', 3, 47, 50, 1170, 4989, 2], ['1_Timothy', 6, 113, 132, 2588, 11687, 4], ['2_Timothy', 4, 83, 97, 1812, 8136, 2], ['Titus', 3, 46, 52, 1045, 4743, 2], ['Philemon', 1, 25, 25, 512, 2056, 1], ['Hebrews', 13, 303, 339, 7573, 32699, 10], ['James', 5, 108, 152, 2496, 10479, 3], ['1_Peter', 5, 105, 128, 2661, 11675, 4], ['2_Peter', 3, 61, 76, 1681, 7657, 3], ['1_John', 5, 105, 142, 2802, 11293, 3], ['2_John', 1, 13, 17, 342, 1352, 1], ['3_John', 1, 14, 22, 354, 1465, 0], ['Jude', 1, 25, 29, 719, 3290, 1], ['Revelation', 22, 404, 551, 12435, 50768, 17]]

with open("output2.csv", "w") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(data)

data3 = pd.DataFrame(data[1:], columns=data[0])
data3.to_csv("output3.csv", index=False)    # export the dataframe to a csv file

