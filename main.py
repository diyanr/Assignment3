import re
from textblob import TextBlob
import pandas as pd


def get_company_data(filepath):
    name = []
    purpose = []
    sentiment = []

    with open(filepath, "r") as file:
        line_num = 0
        for line in file:
            line_num += 1
            if line_num == 1:
                continue
            match = re.match(r"(.+),([^,]+)", line)
            name.append(match[1].strip('"').strip())
            purpose.append(match[2].strip('"').strip())
            sentiment.append(TextBlob(match[2].strip('"').strip()).sentiment.polarity)

    return pd.DataFrame({"Name": name,
                         "Purpose": purpose,
                         "Sentiment": sentiment})


if __name__ == "__main__":
    file1 = "Data/mydata.csv"
    file2 = "Data/results.txt"
    result = pd.concat([get_company_data(file1), get_company_data(file2)])
    print("Top 10 companies with highest sentiments")
    print("========================================")
    print(result.nlargest(10, "Sentiment")[["Name", "Sentiment"]])
    print("\n\n")
    print("Top 10 companies with lowest sentiments")
    print("========================================")
    print(result.nsmallest(10, "Sentiment")[["Name", "Sentiment"]])
